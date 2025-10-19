import axios from "axios";
import { z } from "zod";

const BASE = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

export const StoryLength = z.enum(["short", "medium", "long"]);
export type StoryLengthValue = z.infer<typeof StoryLength>;

export const StoryRequest = z.object({
  hero: z.string().min(1),
  age: z.number().int().min(1).max(12),
  topic: z.string().min(1),
  mood: z.string().min(1),
  length: StoryLength
});
export type StoryRequest = z.infer<typeof StoryRequest>;

export const StorySegment = z.object({
  title: z.string().optional(),
  text: z.string()
});
export const StoryResponse = z.object({
  title: z.string(),
  hero: z.string(),
  topic: z.string(),
  length: StoryLength,
  summary: z.string().optional(),
  story: z.array(StorySegment)
});
export type StoryResponse = z.infer<typeof StoryResponse>;

export async function createStory(req: StoryRequest) {
  const payload = StoryRequest.parse(req);
  const { data } = await axios.post(`${BASE}/api/stories`, payload, {
    headers: { "Content-Type": "application/json" }
  });
  return StoryResponse.parse(data);
}
