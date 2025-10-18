import { useState } from 'react'
import StoryForm from './components/StoryForm'
import StoryPlayer from './components/StoryPlayer'
import type { StoryResponse } from './api/client'

function App() {
  const [story, setStory] = useState<StoryResponse | null>(null)

  return (
    <main>
      <div className="card">
        <h1>Bajki Generator</h1>
        <p className="description">
          Twórz personalizowane opowieści dla najmłodszych. Wprowadź kilka informacji, a
          aplikacja przygotuje wyjątkową bajkę wraz z podziałem na rozdziały.
        </p>
        <StoryForm onStoryReady={setStory} />
        {story && <StoryPlayer story={story} onReset={() => setStory(null)} />}
      </div>
    </main>
  )
}

export default App
