import { useState } from "react";
import { createStory, StoryLength } from "../lib/api";
import type { StoryRequest } from "../lib/api";
import { pushHistory } from "../lib/storage";

export default function Generate() {
  const [form, setForm] = useState<StoryRequest>({
    hero: "Ala",
    age: 5,
    topic: "przygoda z kotem",
    mood: "pogodny",
    length: "short"
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [output, setOutput] = useState<string>("");

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setOutput("");
    try {
      const res = await createStory(form);
      const md = [
        `# ${res.title}`,
        res.summary ? `**Streszczenie:** ${res.summary}` : "",
        ...res.story.map(seg => `${seg.title ? "## " + seg.title + "\n" : ""}${seg.text}`)
      ].filter(Boolean).join("\n\n");
      setOutput(md);
      pushHistory({ ts: Date.now(), req: form, res });
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Błąd");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-3xl mx-auto p-6 space-y-6">
      <header className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">Generator bajek</h1>
        <a className="underline" href="/history">Historia</a>
      </header>

      <form className="grid gap-4" onSubmit={onSubmit}>
        <div className="grid grid-cols-2 gap-4">
          <label className="grid gap-1">
            <span>Bohater</span>
            <input className="border p-2 rounded" value={form.hero}
              onChange={e => setForm({ ...form, hero: e.target.value })}/>
          </label>
          <label className="grid gap-1">
            <span>Wiek</span>
            <input type="number" min={1} max={12} className="border p-2 rounded" value={form.age}
              onChange={e => setForm({ ...form, age: Number(e.target.value) })}/>
          </label>
        </div>

        <label className="grid gap-1">
          <span>Temat</span>
          <input className="border p-2 rounded" value={form.topic}
            onChange={e => setForm({ ...form, topic: e.target.value })}/>
        </label>

        <div className="grid grid-cols-2 gap-4">
          <label className="grid gap-1">
            <span>Nastrój</span>
            <input className="border p-2 rounded" value={form.mood}
              onChange={e => setForm({ ...form, mood: e.target.value })}/>
          </label>
          <label className="grid gap-1">
            <span>Długość</span>
            <select
              className="border p-2 rounded"
              value={form.length}
              onChange={e =>
                setForm({ ...form, length: StoryLength.parse(e.target.value) })
              }
            >
              {StoryLength.options.map(option => (
                <option key={option} value={option}>
                  {option}
                </option>
              ))}
            </select>
          </label>
        </div>

        <button className="bg-black text-white rounded px-4 py-2" disabled={loading}>
          {loading ? "Generuję…" : "Generuj bajkę"}
        </button>
        {error && <p className="text-red-600">{error}</p>}
      </form>

      <section>
        <h2 className="text-xl font-semibold mb-2">Wynik</h2>
        <pre className="bg-gray-900 text-green-300 p-4 rounded whitespace-pre-wrap">{output || "—"}</pre>
      </section>
    </div>
  );
}
