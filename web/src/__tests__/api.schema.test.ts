import { describe, it, expect } from "vitest";
import { StoryRequest, StoryResponse } from "../lib/api";

describe("API schemas", () => {
  it("validates request", () => {
    const parsed = StoryRequest.parse({
      hero: "Ala", age: 5, topic: "las", mood: "pogodny", length: "short"
    });
    expect(parsed.hero).toBe("Ala");
  });

  it("validates response shape", () => {
    const sample = {
      title: "Tytuł",
      hero: "Ala",
      topic: "las",
      length: "short",
      summary: "…",
      story: [{ title: "Start", text: "Dawno dawno…" }]
    };
    const parsed = StoryResponse.parse(sample);
    expect(parsed.story[0].text.length).toBeGreaterThan(0);
  });
});
