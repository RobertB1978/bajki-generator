import { loadHistory } from "../lib/storage";

export default function History() {
  const items = loadHistory();
  return (
    <div className="max-w-3xl mx-auto p-6 space-y-4">
      <header className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">Historia</h1>
        <a className="underline" href="/">Generator</a>
      </header>
      <ul className="space-y-3">
        {items.map(item => (
          <li key={item.ts} className="border rounded p-3 bg-white">
            <div className="text-sm text-gray-500">
              {new Date(item.ts).toLocaleString()}
            </div>
            <div className="font-medium">{item.res.title}</div>
            <div className="text-sm">
              Bohater: {item.req.hero} | Temat: {item.req.topic}
            </div>
          </li>
        ))}
        {items.length === 0 && <p>Brak pozycji.</p>}
      </ul>
    </div>
  );
}
