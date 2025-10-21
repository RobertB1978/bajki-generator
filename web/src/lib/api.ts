import axios from "axios";

export const api = axios.create({
  baseURL: "",
  headers: { "Content-Type": "application/json" }
});

export async function createStory(hero: string, mood: string) {
  const res = await api.post("/api/stories", { hero, mood });
  return res.data as {
    title: string;
    hero: string;
    mood: string;
    story: { title: string; text: string }[];
  };
}
