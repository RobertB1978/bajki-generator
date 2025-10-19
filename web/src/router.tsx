import { createBrowserRouter } from "react-router-dom";
import Generate from "./pages/Generate";
import History from "./pages/History";
import NotFound from "./pages/NotFound";

export const router = createBrowserRouter([
  { path: "/", element: <Generate /> },
  { path: "/history", element: <History /> },
  { path: "*", element: <NotFound /> }
]);
