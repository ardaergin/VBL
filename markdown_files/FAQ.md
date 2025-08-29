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
      <span class="q">How will payments be allocated to researchers?</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      <p>
      Participant payment information is securely stored within the system and is only accessible to the lab administrator. 
      To ensure timely payments, researchers are asked to:
    </p>
    <ul>
      <li>Update the participation status for the completed timeslots.</li>
      <li>Send the SONA IDs and corresponding payout amounts to the VBL team at the end of each week.</li>
    </ul>
    <p>
      Once received, the budget holder will be contacted for approval, after which the payment is processed.  
      If researchers fail to provide this information, the budget holders will be contacted directly using the details stored in the system, without the possibility for researchers to intervene further.
    </p>
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
      Please add the following statement in the Acknowledgments section of your manuscript: <strong>We thank the VU Behavioral Lab (Vrije Universiteit Amsterdam) for participant recruitment, lab usage, and data collection support</strong>.
    </div>
  </details>

  <details class="faq-item">
    <summary>
      <span class="q">Who is the VU Student Pool and when are they available?</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      The VU Student Pool consists of students from various academic backgrounds who participate in behavioural and cognitive research studies. They are available throughout the entire academic year. As of August 2025, the pool includes 550 students, and the number is steadily increasing as more students join.
    </div>
  </details>

  <details class="faq-item">
    <summary>
      <span class="q">How long in advance should I request a study?</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      Due to planning and registering, we require you to request physical lab studies at least 3 weeks / online studies at least 2 weeks before the session takes place, but preferably even earlier. 
    </div>
  </details>

 <details class="faq-item">
    <summary>
      <span class="q">I would like to invite an external researcher to the study.</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      Unfortunately, no external researchers are allowed to access the system. You can manage as a collaborator on their behalf.
    </div>
  </details>

   <details class="faq-item">
    <summary>
      <span class="q">I would like to invite an external participant to the study.</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      Unfortunately, at the moment, external participants cannot sign up or receive payments through the system.
    </div>
  </details>

  <details class="faq-item">
    <summary>
      <span class="q">Can I Use Prescreeners to Select Participants for My Study?</span>
      <span class="chev" aria-hidden="true"></span>
    </summary>
    <div class="a">
      Prescreeners are standard questionnaires (e.g., demographic or personality surveys) that participants fill out once a year. These are stored outside of SONA and used to help researchers access important participant information without having to collect it repeatedly for every study. <strong> Due to VU's data privacy and storage policies, prescreening data is not stored in SONA and cannot be used to automatically filter or preselect participants for your study.</strong> While you can specify eligibility criteria (e.g., gender, age) in your SONA study description, students may overlook these and still register. As a researcher, you retain the right to reject ineligible participants or exclude their data. Please note that applying eligibility restrictions may significantly reduce your participant pool.
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
