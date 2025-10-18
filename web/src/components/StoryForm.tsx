import { FormEvent, useState } from 'react'
import { createStory, type StoryLength, type StoryResponse } from '../api/client'

type FormState = {
  hero: string
  age: number
  topic: string
  mood: string
  length: StoryLength
}

const defaultState: FormState = {
  hero: 'Mila',
  age: 6,
  topic: 'zaczarowany las',
  mood: 'pogodny',
  length: 'short'
}

interface StoryFormProps {
  onStoryReady: (story: StoryResponse) => void
}

function StoryForm({ onStoryReady }: StoryFormProps) {
  const [state, setState] = useState<FormState>(defaultState)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setIsLoading(true)
    setError(null)

    try {
      const story = await createStory(state)
      onStoryReady(story)
    } catch (err) {
      console.error(err)
      setError('Nie udało się wygenerować bajki. Spróbuj ponownie później.')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Bohater/ka
        <input
          required
          value={state.hero}
          onChange={(event) => setState({ ...state, hero: event.target.value })}
        />
      </label>
      <label>
        Wiek słuchacza
        <input
          type="number"
          min={1}
          max={12}
          required
          value={state.age}
          onChange={(event) => setState({ ...state, age: Number(event.target.value) })}
        />
      </label>
      <label>
        Motyw przewodni
        <input
          required
          value={state.topic}
          onChange={(event) => setState({ ...state, topic: event.target.value })}
        />
      </label>
      <label>
        Nastrój historii
        <input
          required
          value={state.mood}
          onChange={(event) => setState({ ...state, mood: event.target.value })}
        />
      </label>
      <label>
        Długość bajki
        <select
          value={state.length}
          onChange={(event) => setState({ ...state, length: event.target.value as StoryLength })}
        >
          <option value="short">Krótka</option>
          <option value="medium">Średnia</option>
          <option value="long">Długa</option>
        </select>
      </label>

      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Generowanie…' : 'Generuj bajkę'}
      </button>

      {error && <p role="alert">{error}</p>}
    </form>
  )
}

export default StoryForm
