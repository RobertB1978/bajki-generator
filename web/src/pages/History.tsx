import { StoryRequest, StoryResponse } from "../lib/api";

type StoredStory = {
  ts: number;
  req?: StoryRequest;
  res?: StoryResponse;
};

function loadHistory(): StoredStory[] {
  try {
    const raw = localStorage.getItem("stories");
    if (!raw) {
      return [];
    }
    const parsed = JSON.parse(raw) as StoredStory[];
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

export default function History(){
  const items = loadHistory();
  return (
    <div className="max-w-3xl mx-auto p-6 space-y-4">
      <header className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">Historia</h1>
        <a className="underline" href="/">Generator</a>
      </header>
      <ul className="space-y-3">
        {items.map((x, i) => (
          <li key={i} className="border rounded p-3 bg-white">
            <div className="text-sm text-gray-500">{new Date(x.ts).toLocaleString()}</div>
            <div className="font-medium">{x.res?.title}</div>
            <div className="text-sm">Bohater: {x.req?.hero} | Temat: {x.req?.topic}</div>
          </li>
        ))}
        {items.length===0 && <p>Brak pozycji.</p>}
      </ul>
    </div>
  );
}
