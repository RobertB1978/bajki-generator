import { useState } from "react";
import { createStory } from "../lib/api";

type StoryResponse = {
  title: string;
  hero: string;
  mood: string;
  story: { title: string; text: string }[];
};

type ErrorPayload = {
  response?: {
    data?: {
      error?: string;
    };
  };
};

export default function App() {
  const [hero, setHero] = useState("Ala");
  const [mood, setMood] = useState("pogodny");
  const [out, setOut] = useState<StoryResponse | null>(null);
  const [err, setErr] = useState<string | null>(null);

  const go = async () => {
    setErr(null);
    setOut(null);
    try {
      const data = await createStory(hero, mood);
      setOut(data);
    } catch (error: unknown) {
      const payload = (error as ErrorPayload | null) ?? null;
      const responseError = payload?.response?.data?.error;
      if (responseError) {
        setErr(responseError);
      } else if (error instanceof Error) {
        setErr(error.message);
      } else {
        setErr("Błąd");
      }
    }
  };

  return (
    <div style={{ maxWidth: 720, margin: "40px auto", fontFamily: "system-ui" }}>
      <h1>Bajki Generator</h1>
      <label>
        Bohater: <input value={hero} onChange={(e) => setHero(e.target.value)} />
      </label>
      <label style={{ marginLeft: 12 }}>
        Nastrój:
        <select value={mood} onChange={(e) => setMood(e.target.value)}>
          <option>pogodny</option>
          <option>zabawny</option>
          <option>tajemniczy</option>
          <option>przygodowy</option>
        </select>
      </label>
      <button style={{ marginLeft: 12 }} onClick={go}>
        Generuj
      </button>

      {err && <p style={{ color: "crimson" }}>{err}</p>}
      {out && (
        <div style={{ marginTop: 20 }}>
          <h2>{out.title}</h2>
          {out.story?.map((s, i) => (
            <section key={i}>
              <h3>{s.title}</h3>
              <p>{s.text}</p>
            </section>
          ))}
        </div>
      )}
    </div>
  );
}
