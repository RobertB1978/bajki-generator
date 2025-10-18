import axios from 'axios'

export type StoryLength = 'short' | 'medium' | 'long'

export interface StorySegment {
  title: string
  text: string
}

export interface StoryResponse {
  title: string
  hero: string
  mood: string
  topic: string
  length: StoryLength
  language: string
  summary: string
  created_at: string
  estimated_read_time: number
  story: StorySegment[]
}

export interface StoryPayload {
  hero: string
  age: number
  topic: string
  mood: string
  length: StoryLength
}

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? '/api'

const api = axios.create({
  baseURL: apiBaseUrl
})

export async function createStory(payload: StoryPayload): Promise<StoryResponse> {
  const { data } = await api.post<StoryResponse>('/stories', payload)
  return data
}
