import type { AxiosResponse } from "axios";
import { describe, expect, it } from "vitest";
import { api, createStory } from "../lib/api";

describe("createStory", () => {
  it("posts payload and returns story data", async () => {
    const mockData: Awaited<ReturnType<typeof createStory>> = {
      title: "Przygoda Ala",
      hero: "Ala",
      mood: "pogodny",
      story: [{ title: "Rozdział 1", text: "Ala..." }]
    };

    const originalPost = api.post;
    api.post = (async (path, payload) => {
      expect(path).toBe("/api/stories");
      expect(payload).toEqual({ hero: "Ala", mood: "pogodny" });
      return Promise.resolve({ data: mockData } as AxiosResponse<typeof mockData>);
    }) as typeof api.post;

    try {
      const result = await createStory("Ala", "pogodny");
      expect(result).toEqual(mockData);
    } finally {
      api.post = originalPost;
    }
  });
});
