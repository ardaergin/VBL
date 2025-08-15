<section class="faq">
  <h1>Frequently Asked Questions</h1>

<details class="faq-item">
    <summary>
      <span class="q">My question is not mentioned here?</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      If you have a different question than what is discussed in this FAQ, please feel free to reach out the the VU Behavioral Lab team via <a href="mailto:vbl@vu.nl">vbl@vu.nl</a>. They will try to respond as soon as possible to your question and make sure that it will be listed on this page as well. 
    </div>
  </details>

  <details class="faq-item">
    <summary>
      <span class="q">How long does the participant payment usually take?</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      We aim for <strong>2 weeks</strong>, but during holidays or summer it might take longer.
    </div>
  </details>

  <details class="faq-item">
    <summary>
      <span class="q">Acknowledgements in paper</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      Please add the following statement in the Acknowledgments section of your manuscript: <strong>We thank the Research Participation Project of the School of Business and Economics and the Applied Behavioral Science lab (Vrije Universiteit Amsterdam) for data collection support.</strong>.
    </div>
  </details>

<style>
  /* Container */
  .faq{
    --bg: #ffffff;
    --card: #f9fafb;
    --muted: #4b5563;
    --text: #000000;
    --accent: #0ea5e9;
    --border: #d1d5db;

    max-width: 760px;
    margin: 3rem auto;
    padding: 0 1rem;
    color: var(--text);
    font: 16px/1.5 ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
  }

  .faq h1{
    font-size: clamp(1.6rem, 3vw, 2.2rem);
    font-weight: 800;
    margin: 0 0 1.25rem;
    letter-spacing: -0.02em;
    color: var(--text);
  }

  /* Card-like details */
  .faq-item{
    border: 1px solid var(--border);
    border-radius: 16px;
    background: var(--card);
    margin: 0 0 0.75rem;
    overflow: clip;
  }

  /* Remove default marker */
  .faq-item summary { list-style: none; }
  .faq-item summary::-webkit-details-marker { display: none; }

  /* Summary (question) */
  .faq-item summary{
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: .75rem;
    padding: 1rem 1.1rem 1rem 1rem;
    cursor: pointer;
    position: relative;
  }

  .faq-item summary .q{
    font-weight: 700;
    letter-spacing: -0.01em;
    display: inline-flex;
    align-items: center;
    gap: .5rem;
  }

  /* Chevron */
  .faq-item .chev{
    width: 1.1rem; height: 1.1rem;
    border-right: 2px solid var(--muted);
    border-bottom: 2px solid var(--muted);
    transform: rotate(-45deg);
    transition: transform .25s ease, border-color .25s ease;
    opacity: .9;
  }
  .faq-item[open] .chev{
    transform: rotate(45deg);
    border-color: var(--accent);
  }

  /* Answer */
  .faq-item .a{
    padding: 0 1rem 1rem;
    color: var(--muted);
    border-top: 1px solid var(--border);
    background: #fff;
    animation: fadeDown .25s ease;
  }

  /* Hover / focus styles for better affordance */
  .faq-item summary:hover .q{ text-shadow: 0 0 0.5px currentColor; }
  .faq-item summary:focus-visible{
    outline: 3px solid color-mix(in oklab, var(--accent) 50%, transparent);
    outline-offset: 2px;
    border-radius: 14px;
  }

  /* Subtle open/close animation */
  @keyframes fadeDown{
    from{ opacity: 0; translate: 0 -4px; }
    to{ opacity: 1; translate: 0 0; }
  }

  /* Respect reduced motion */
  @media (prefers-reduced-motion: reduce){
    .faq-item .chev{ transition: none; }
    .faq-item .a{ animation: none; }
  }
</style>
