import type { StoryResponse } from '../api/client'

interface StoryPlayerProps {
  story: StoryResponse
  onReset: () => void
}

function StoryPlayer({ story, onReset }: StoryPlayerProps) {
  return (
    <section className="story-result">
      <header>
        <h2>{story.title}</h2>
        <p>
          Bohater/ka: <strong>{story.hero}</strong> • Nastrój: <strong>{story.mood}</strong> • Motyw:{' '}
          <strong>{story.topic}</strong>
        </p>
        <p>Szacowany czas czytania: ok. {Math.round(story.estimated_read_time / 60)} minut</p>
        <button type="button" onClick={onReset}>
          Nowa bajka
        </button>
      </header>
      <article>
        {story.story.map((segment) => (
          <div key={segment.title} className="story-segment">
            <h3>{segment.title}</h3>
            <p>{segment.text}</p>
          </div>
        ))}
      </article>
    </section>
  )
}

export default StoryPlayer
