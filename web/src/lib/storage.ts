import type { StoryRequest, StoryResponse } from "./api";

export type StoredStory = {
  ts: number;
  req: StoryRequest;
  res: StoryResponse;
};

const STORAGE_KEY = "stories";

function parseStories(raw: string | null): StoredStory[] {
  if (!raw) {
    return [];
  }
  try {
    const parsed = JSON.parse(raw) as StoredStory[];
    if (Array.isArray(parsed)) {
      return parsed.filter(item => typeof item?.ts === "number");
    }
  } catch (error) {
    console.warn("Failed to parse stories from storage", error);
  }
  return [];
}

export function loadHistory(): StoredStory[] {
  if (typeof localStorage === "undefined") {
    return [];
  }
  return parseStories(localStorage.getItem(STORAGE_KEY));
}

export function pushHistory(entry: StoredStory): StoredStory[] {
  const history = [entry, ...loadHistory()].slice(0, 50);
  if (typeof localStorage !== "undefined") {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
  }
  return history;
}
