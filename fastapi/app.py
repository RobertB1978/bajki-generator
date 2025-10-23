"""Minimal subset of FastAPI used for unit tests.

The goal of this shim is to provide just enough of FastAPI's surface so the
application can run in environments where installing third party packages is
not possible.  Only the features exercised by the tests are implemented.
"""

from __future__ import annotations

from dataclasses import dataclass, field, is_dataclass, replace
from typing import Any, Callable, Dict, Iterable, List, Optional
import inspect


class Depends:
    """Sentinel used to declare callable dependencies for route parameters."""

    def __init__(self, dependency: Callable[..., Any]):
        self.dependency = dependency


@dataclass
class _Route:
    """Internal representation of an HTTP route."""

    method: str
    segments: List[str]
    endpoint: Callable[..., Any]
    response_model: Any = None
    tags: Optional[List[str]] = None
    dependencies: Dict[str, Callable[..., Any]] = field(default_factory=dict)

    @property
    def path(self) -> str:
        if not self.segments:
            return "/"
        return "/" + "/".join(self.segments)


def _split_path(path: str) -> List[str]:
    """Turn a URL path into a list of normalized segments."""

    if not path or path == "/":
        return []
    return [segment for segment in path.strip("/").split("/") if segment]


def _extract_dependencies(func: Callable[..., Any]) -> Dict[str, Callable[..., Any]]:
    """Collect dependencies declared via :class:`Depends`."""

    dependencies: Dict[str, Callable[..., Any]] = {}
    signature = inspect.signature(func)
    for name, parameter in signature.parameters.items():
        default = parameter.default
        if isinstance(default, Depends):
            dependencies[name] = default.dependency
    return dependencies


def _coerce_value(value: Any, annotation: Any) -> Any:
    """Best effort conversion of request data to the declared annotation."""

    if annotation is inspect.Signature.empty or annotation is Any:
        return value

    if inspect.isclass(annotation) and is_dataclass(annotation):
        if isinstance(value, annotation):
            return value
        if isinstance(value, dict):
            return annotation(**value)

    return value


def _prepare_response(result: Any) -> tuple[int, Any]:
    """Normalise endpoint return values to ``(status_code, payload)`` tuples."""

    status = 200
    payload = result

    if isinstance(result, tuple):
        if len(result) == 0:
            payload = None
        elif len(result) == 1:
            payload = result[0]
        else:
            payload = result[0]
            status = result[1]

    return status, payload


class APIRouter:
    """Container mirroring FastAPI's :class:`APIRouter`."""

    def __init__(self, prefix: str = "", tags: Optional[Iterable[str]] = None):
        self._routes: List[_Route] = []
        self._prefix_segments = _split_path(prefix)
        self._default_tags = list(tags or []) or None

    @property
    def routes(self) -> List[_Route]:
        return list(self._routes)

    @property
    def prefix(self) -> List[str]:
        return list(self._prefix_segments)

    def get(self, path: str, response_model: Any = None, tags: Optional[Iterable[str]] = None):
        return self._register("GET", path, response_model, tags)

    def post(self, path: str, response_model: Any = None, tags: Optional[Iterable[str]] = None):
        return self._register("POST", path, response_model, tags)

    def _register(
        self,
        method: str,
        path: str,
        response_model: Any,
        tags: Optional[Iterable[str]],
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            route = _Route(
                method=method.upper(),
                segments=_split_path(path),
                endpoint=func,
                response_model=response_model,
                tags=list(tags or self._default_tags or []),
                dependencies=_extract_dependencies(func),
            )
            self._routes.append(route)
            return func

        return decorator


class FastAPI:
    """Extremely small drop-in replacement for FastAPI used in tests."""

    def __init__(self, title: str, version: str = "0.1.0"):
        self.title = title
        self.version = version
        self._routes: List[_Route] = []
        self._middleware: List[tuple[type[Any], Dict[str, Any]]] = []

    @property
    def routes(self) -> List[_Route]:
        return list(self._routes)

    def add_middleware(self, middleware_class: type[Any], **options: Any) -> None:
        """Store middleware declarations for completeness."""

        self._middleware.append((middleware_class, dict(options)))

    def include_router(self, router: APIRouter, prefix: str = "") -> None:
        """Attach routes from another router with an optional prefix."""

        prefix_segments = _split_path(prefix)
        for route in router.routes:
            combined_segments = prefix_segments + router.prefix + route.segments
            self._routes.append(replace(route, segments=combined_segments))

    def get(self, path: str, response_model: Any = None, tags: Optional[Iterable[str]] = None):
        return self._register("GET", path, response_model, tags)

    def post(self, path: str, response_model: Any = None, tags: Optional[Iterable[str]] = None):
        return self._register("POST", path, response_model, tags)

    def _register(
        self,
        method: str,
        path: str,
        response_model: Any,
        tags: Optional[Iterable[str]],
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            route = _Route(
                method=method.upper(),
                segments=_split_path(path),
                endpoint=func,
                response_model=response_model,
                tags=list(tags or []),
                dependencies=_extract_dependencies(func),
            )
            self._routes.append(route)
            return func

        return decorator

    # ------------------------------------------------------------------
    # Request handling helpers used by :class:`fastapi.testclient.TestClient`
    # ------------------------------------------------------------------
    def handle_request(self, method: str, path: str, body: Any = None) -> tuple[int, Any]:
        """Dispatch a request to the registered route."""

        method = method.upper()
        segments = _split_path(path)
        for route in self._routes:
            if route.method == method and route.segments == segments:
                return self._execute_route(route, body)
        raise LookupError(f"No route registered for {method} {path}")

    def _execute_route(self, route: _Route, body: Any) -> tuple[int, Any]:
        signature = inspect.signature(route.endpoint)
        kwargs: Dict[str, Any] = {}
        body_consumed = False

        for name, parameter in signature.parameters.items():
            if name in route.dependencies:
                kwargs[name] = route.dependencies[name]()
                continue

            if not body_consumed and body is not None:
                kwargs[name] = _coerce_value(body, parameter.annotation)
                body_consumed = True
                continue

            if parameter.default is not inspect.Signature.empty:
                kwargs[name] = parameter.default
                continue

            raise TypeError(f"Unable to satisfy parameter '{name}' for route {route.path}")

        result = route.endpoint(**kwargs)
        return _prepare_response(result)
