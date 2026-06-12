"""Content for Home, About, Program Leadership, and Experience pages."""
from templates import rel

# Minimal inline icons (decorative, aria-hidden).
ICONS = {
    "plan": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true" focusable="false"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
    "compass": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2.2 5-5 2.2 2.2-5z"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/></svg>',
    "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true" focusable="false"><circle cx="8.5" cy="9" r="3"/><circle cx="16" cy="10.5" r="2.4"/><path d="M3.5 19c.6-3 2.7-4.5 5-4.5s4.4 1.5 5 4.5M13.5 18.6c.5-2.2 1.9-3.4 3.8-3.4 1.6 0 2.9.9 3.5 2.7"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true" focusable="false"><path d="M4 5.5A2.5 2.5 0 016.5 3H20v15.5H6.5A2.5 2.5 0 004 21z"/><path d="M4 18.5A2.5 2.5 0 016.5 16H20"/></svg>',
    "speak": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true" focusable="false"><path d="M4 9h3l8-5v16l-8-5H4z"/><path d="M18 9.5a4 4 0 010 5"/></svg>',
}


def home(depth):
    r = lambda p: rel(p, depth)
    leadership_cards = [
        ("plan", "Program and Project Management",
         "Fayana plans, coordinates, and monitors complex initiatives from intake through delivery. She develops scopes of work, builds work plans, tracks milestones, and keeps concurrent workstreams organized.",
         "/program-leadership/", "Explore program leadership"),
        ("compass", "Public Health Program Strategy and Operations",
         "She helps organizations connect public health priorities to clear goals, responsibilities, and operational decisions. Her strategy work stays grounded in implementation realities.",
         "/about/", "Learn about her approach"),
        ("search", "Research and Evaluation",
         "Fayana brings doctoral-level training in qualitative and mixed-methods research to program questions. She uses evidence and stakeholder feedback to support assessment and improvement.",
         "/research-writing/", "Review research areas"),
        ("people", "Stakeholder and Community Engagement",
         "She builds and maintains accountable partnerships with clients, organizational leaders, cross-functional teams, and community organizations, including on sensitive topics.",
         "/program-leadership/", "See partnership work"),
        ("book", "Curriculum and Facilitation",
         "Fayana designs curricula, develops workshops, and facilitates virtual and in-person learning for university students, professionals, and community audiences.",
         "/teaching-facilitation/", "View teaching and facilitation"),
        ("speak", "Research Translation and Communication",
         "She translates complex research and technical material into clear written products, presentations, and digital content for varied audiences.",
         "/speaking/", "View speaking"),
    ]
    cards_html = "\n".join(
        f"""        <article class="card">
          <div class="card-icon">{ICONS[icon]}</div>
          <h3>{title}</h3>
          <p>{body}</p>
          <p><a class="card-link" href="{r(link)}">{label}</a></p>
        </article>""" for icon, title, body, link, label in leadership_cards
    )

    timeline = [
        ("June 2021 – 2025", "Senior Public Health Consultant", "Michigan Public Health Institute"),
        ("August 2019 – May 2021", "Assistant Professor of Medical Anthropology", "University of Memphis"),
        ("2019", "Visiting Assistant Professor of Public Health", "Hampshire College"),
        ("January 2018 – January 2019", "Post-Doctoral Research Associate", "University of Massachusetts Amherst"),
        ("August 2010 – December 2017", "Doctoral Researcher, Graduate Scholar, and Graduate Teaching Assistant", "Michigan State University"),
        ("2009 – 2010", "Project Coordinator", "University of Arizona"),
        ("Dates in review", "Editorial Intern", "Science Magazine"),
    ]
    timeline_html = "\n".join(
        f"""        <li>
          <span class="timeline-period">{period}</span>
          <h3>{title}</h3>
          <p class="timeline-org">{org}</p>
        </li>""" for period, title, org in timeline
    )

    # Category keys give the six Featured Work cards visual rhythm without photos:
    # program=bronze, research=plum-mid, education=slate, communication=aubergine.
    featured_cats = [
        ("work-cat-program", "Consulting"),
        ("work-cat-research", "Research"),
        ("work-cat-program", "Program Design"),
        ("work-cat-education", "Education"),
        ("work-cat-program", "Project Coordination"),
        ("work-cat-communication", "Communication"),
    ]
    featured = [
        ("Public Health Consulting and Program Coordination", "Michigan Public Health Institute",
         "Senior Public Health Consultant",
         "Led and coordinated multiple concurrent public health projects, advised clients on social justice programming, and supported partnerships, facilitation, and implementation.",
         ["Program Management", "Public Health", "Facilitation"], "/work/public-health-consulting/"),
        ("Community-Engaged Research on Aging and Chronic Illness", "Michigan State University",
         "Doctoral Researcher",
         "Conducted approximately 18 months of field research on aging, caregiving, chronic illness, and health disparities among older Black women in Detroit.",
         ["Research", "Community Engagement", "Public Health"], "/work/aging-caregiving-research/"),
        ("Research and Professional Development Program Design", "University of Massachusetts Amherst",
         "Post-Doctoral Research Associate",
         "Helped develop a research and professional development program for students from underrepresented backgrounds and supported an NIH R01 grant application.",
         ["Program Management", "Grant Support", "Education"], "/work/research-development-program/"),
        ("Public Health Curriculum and Program Assessment", "University of Memphis",
         "Assistant Professor of Medical Anthropology",
         "Designed courses on race, health disparities, and applied medical anthropology, and supported curriculum review and program assessment.",
         ["Education", "Evaluation", "Public Health"], "/work/curriculum-development/"),
        ("Federally Funded Research Project Coordination", "University of Arizona",
         "Project Coordinator",
         "Coordinated research activities, monitored expenditures, managed data, and supervised undergraduate researchers on a federally funded project.",
         ["Project Management", "Research", "Grant Support"], "/work/research-project-coordination/"),
        ("Science Journalism and Research Translation", "Science Magazine",
         "Editorial Intern",
         "Interviewed researchers, fact-checked scientific information, wrote digital articles, and produced a podcast episode for broad audiences.",
         ["Science Communication", "Research"], "/work/science-communication/"),
    ]
    featured_html = "\n".join(
        f"""        <article class="card {cat_class}">
          <span class="work-cat-label">{cat_label}</span>
          <h3><a href="{r(link)}">{title}</a></h3>
          <p class="entry-meta">{org} &middot; {role}</p>
          <p>{summary}</p>
          <ul class="tag-list">{''.join(f'<li>{t}</li>' for t in tags)}</ul>
        </article>""" for (title, org, role, summary, tags, link), (cat_class, cat_label) in zip(featured, featured_cats)
    )

    return f"""  <section class="hero">
    <div class="container hero-grid">
      <div>
        <span class="eyebrow">Dr. Fayana Richards, MPH, PMP</span>
        <h1>Public Health Program Strategy, Operations, and Leadership</h1>
        <p class="lede">Fayana Richards is a public health strategist, medical anthropologist, and program leader with more than 18 years of experience across consulting, research, higher education, community engagement, and professional learning.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{r('/work/')}">View Selected Work</a>
          <a class="btn btn-secondary" href="{r('/program-leadership/')}">Review Program Leadership</a>
          <a class="text-link" href="{r('/resume/')}">Download Résumé</a>
        </div>
      </div>
      <div class="hero-figure">
        <!-- PLACEHOLDER: headshot — drop the approved photo at /assets/img/headshot.jpg.
             The FR monogram below is a fallback that displays only while the image is missing. -->
        <div class="portrait-frame">
          <img src="{r('/assets/img/headshot.jpg')}" alt="Dr. Fayana Richards" width="280" height="350" fetchpriority="high" decoding="async" onerror="this.classList.add('img-missing')">
          <span class="portrait-fallback" aria-hidden="true">FR</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="value-heading">
    <div class="container">
      <h2 id="value-heading">Turning Complex Priorities Into Organized Action</h2>
      <div class="section-intro">
        <p>Fayana supports organizations as they plan, implement, assess, and strengthen public health and social impact programs. Her work combines project planning, stakeholder engagement, research, facilitation, and clear communication. She brings structure to complex initiatives while remaining attentive to the people and communities affected by program decisions.</p>
      </div>
    </div>
  </section>

  <section class="section section-neutral" aria-labelledby="credentials-heading">
    <div class="container">
      <h2 id="credentials-heading" class="visually-hidden">Credential Summary</h2>
      <div class="card-grid card-grid-4">
        <article class="card stat-card">
          <span class="stat-value">18+ Years</span>
          <p>Public health, research, education, consulting, and program leadership</p>
        </article>
        <article class="card stat-card">
          <span class="stat-value">PhD and MPH</span>
          <p>Advanced preparation in medical anthropology and public health</p>
        </article>
        <article class="card stat-card">
          <span class="stat-value">Cross-Sector Experience</span>
          <p>Consulting, higher education, research, nonprofit, and community settings</p>
        </article>
        <article class="card stat-card">
          <span class="stat-value">Community-Centered Practice</span>
          <p>Health disparities, aging, caregiving, chronic illness, and community health</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="leadership-heading">
    <div class="container">
      <h2 id="leadership-heading">Core Leadership Areas</h2>
      <div class="card-grid card-grid-3">
{cards_html}
      </div>
    </div>
  </section>

  <section class="section section-neutral" aria-labelledby="method-heading">
    <div class="container">
      <h2 id="method-heading">A Working Method Built for Complex Programs</h2>
      <div class="process-grid">
        <div class="process-step">
          <h3>Clarify</h3>
          <p>Define the need, goals, stakeholders, scope, constraints, and indicators of progress.</p>
        </div>
        <div class="process-step">
          <h3>Plan</h3>
          <p>Translate the need into a work plan, timeline, responsibilities, and deliverables.</p>
        </div>
        <div class="process-step">
          <h3>Coordinate</h3>
          <p>Support communication, partnership activity, meeting follow-up, and cross-functional work.</p>
        </div>
        <div class="process-step">
          <h3>Assess</h3>
          <p>Review project information, stakeholder feedback, implementation progress, and performance concerns.</p>
        </div>
        <div class="process-step">
          <h3>Communicate</h3>
          <p>Provide clear updates, recommendations, presentations, learning materials, and written products.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="featured-heading">
    <div class="container">
      <h2 id="featured-heading">Featured Work</h2>
      <div class="card-grid card-grid-3">
{featured_html}
      </div>
      <p style="margin-top: var(--space-6);"><a class="btn btn-secondary" href="{r('/work/')}">View All Selected Work</a></p>
    </div>
  </section>

  <section class="section section-neutral" aria-labelledby="career-heading">
    <div class="container">
      <h2 id="career-heading">Career Overview</h2>
      <ol class="timeline">
{timeline_html}
      </ol>
      <p style="margin-top: var(--space-6);"><a class="btn btn-primary" href="{r('/experience/')}">Review Full Experience</a></p>
    </div>
  </section>

  <section class="section" aria-labelledby="research-heading">
    <div class="container">
      <h2 id="research-heading">Research, Writing, and Public Communication</h2>
      <div class="section-intro">
        <p>Fayana&rsquo;s research and writing address aging, caregiving, chronic illness, race and health, and the conditions that shape health outcomes. Her experience includes community-based field research, academic publication, public health instruction, conference presentation, science writing, and research translation.</p>
      </div>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{r('/research-writing/')}">Review Research Areas</a>
        <a class="btn btn-secondary" href="{r('/research-writing/#publications')}">View Publications</a>
        <a class="btn btn-secondary" href="{r('/speaking/')}">View Speaking</a>
      </div>
    </div>
  </section>

  <section class="section section-neutral" aria-labelledby="focus-heading">
    <div class="container">
      <h2 id="focus-heading">Professional Focus</h2>
      <div class="section-intro">
        <p>Fayana is open to consulting, speaking, and employment opportunities in the following areas:</p>
      </div>
      <ul class="tag-list" style="margin-top: var(--space-5);">
        <li>Senior program leadership</li>
        <li>Strategic initiatives</li>
        <li>Public health consulting</li>
        <li>Research program management</li>
        <li>Aging and caregiving initiatives</li>
        <li>Workforce development</li>
        <li>Academic programming</li>
        <li>Learning and facilitation</li>
        <li>Responsible AI applications in public health and program operations</li>
      </ul>
    </div>
  </section>

  <section class="cta-band" aria-labelledby="contact-cta-heading">
    <div class="container">
      <div>
        <h2 id="contact-cta-heading">Connect With Fayana</h2>
        <p>For program leadership, strategic initiatives, research collaboration, academic programming, facilitation, or speaking opportunities, use the contact form or an approved professional channel.</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-light" href="{r('/contact/')}">Contact Fayana</a>
        <a class="btn btn-outline-light" href="{r('/resume/')}">Download Résumé</a>
      </div>
    </div>
  </section>
"""


def about(depth):
    r = lambda p: rel(p, depth)
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">About</span>
      <h1>About Dr. Fayana Richards</h1>
      <p class="lede section-intro">Public health strategist, medical anthropologist, program leader, researcher, and educator.</p>
    </div>
  </section>

  <section class="section" aria-labelledby="bio-heading">
    <div class="container split">
      <div>
        <h2 id="bio-heading">Professional Biography</h2>
        <p>Dr. Fayana Richards is a public health strategist, medical anthropologist, program leader, researcher, and educator with more than 18 years of experience across public health consulting, higher education, research, community engagement, and professional learning.</p>
        <p>Her work focuses on social and structural determinants of health, aging, caregiving, chronic illness, workforce development, and culturally responsive program design. Across her professional roles, she has planned and monitored projects, developed scopes of work, coordinated cross-functional teams, supported organizational partnerships, facilitated workshops, advised clients and leaders, supervised staff, and translated research findings into practical program decisions.</p>
        <p>From June 2021 to 2025, Fayana served as a Senior Public Health Consultant at the Michigan Public Health Institute. Her work included leading or coordinating multiple public health initiatives, advising on social justice programming, supporting strong partnerships, facilitating virtual learning, developing project plans, monitoring progress, and addressing sensitive implementation concerns.</p>
        <p>Fayana previously served as an Assistant Professor of Medical Anthropology at the University of Memphis and as a Visiting Assistant Professor of Public Health at Hampshire College. Her teaching addressed race, health disparities, applied medical anthropology, and public health. She developed curricula, supported program assessment, contributed to administrative planning, and mentored students in research and community engagement.</p>
        <p>Her research preparation includes postdoctoral work at the University of Massachusetts Amherst and doctoral research at Michigan State University. Her doctoral fieldwork examined aging, caregiving, chronic illness, and health disparities among older Black women in Detroit. She conducted approximately 18 months of field research and received multi-year support from Michigan State University and the National Science Foundation.</p>
        <p>Earlier in her career, Fayana coordinated a federally funded research project at the University of Arizona. Her responsibilities included research coordination, expenditure monitoring, expense reporting, data management, and supervision of undergraduate researchers. She also completed editorial work with Science Magazine, where she interviewed researchers, conducted background research, fact-checked scientific information, wrote digital articles, and produced a podcast episode.</p>
        <p>Fayana holds a Doctor of Philosophy in Medical Anthropology, a Master of Public Health, and a Master of Arts in Medical Anthropology from Michigan State University. She earned a Bachelor of Arts in Medical Anthropology and Journalism from the University of Arizona. She also holds the Project Management Professional (PMP) credential from the Project Management Institute.</p>
        <p>Her work reflects a consistent commitment to sound analysis, clear communication, meaningful partnership, and public health programs that account for the social conditions affecting people and communities.</p>
      </div>
      <aside aria-labelledby="education-aside-heading">
        <div class="case-aside">
          <h2 id="education-aside-heading">Education and Credentials</h2>
          <dl>
            <dt>Michigan State University</dt>
            <dd>Doctor of Philosophy in Medical Anthropology, 2018</dd>
            <dd>Master of Public Health, 2015</dd>
            <dd>Master of Arts in Medical Anthropology, 2012</dd>
            <dt>University of Arizona</dt>
            <dd>Bachelor of Arts in Medical Anthropology and Journalism, 2008</dd>
            <dt>Certifications and Training</dt>
            <dd>Project Management Professional (PMP), Project Management Institute, 2026</dd>
            <dd>Technology of Participation Strategic Planning and Facilitation Methods, Institute of Cultural Affairs, 2021</dd>
            <dd>NSF Summer Institute for Research Design in Cultural Anthropology, University of Florida, 2012</dd>
            <dt>Funding and Awards</dt>
            <dd>National Science Foundation (NSF) Graduate Research Fellowship, 2011&ndash;2014</dd>
            <dd>NSF Alliances for Graduate Education and the Professoriate (AGEP) Award, 2011&ndash;2013</dd>
            <dd>National Cancer Institute Diversity Research Supplement, National Institutes of Health, 2009</dd>
            <dt>Current Affiliation</dt>
            <dd>Affiliate Faculty, Center for Community Health Research, University of Massachusetts Amherst, 2019&ndash;present</dd>
          </dl>
        </div>
      </aside>
    </div>
  </section>

  <section class="section section-neutral" aria-labelledby="philosophy-heading">
    <div class="container split">
      <div>
        <h2 id="philosophy-heading">Professional Philosophy</h2>
        <blockquote class="note-box" style="margin: 0;">
          <p>&ldquo;I approach public health work with the understanding that strong programs require both reliable evidence and attention to lived experience. I help teams clarify their goals, organize complex work, communicate across roles, and use research and feedback to support practical decisions. I also believe that fairness and community needs should be reflected in how programs are planned, implemented, assessed, and communicated.&rdquo;</p>
        </blockquote>
      </div>
      <div>
        <h2>Working Principles</h2>
        <ul>
          <li>Start with a clearly defined need.</li>
          <li>Include the people affected by the work.</li>
          <li>Connect strategy with practical responsibilities.</li>
          <li>Use evidence to support decisions.</li>
          <li>Communicate progress and concerns clearly.</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="approach-heading">
    <div class="container">
      <h2 id="approach-heading">Leadership Approach and Research Perspective</h2>
      <div class="split">
        <div>
          <h3>Leadership approach</h3>
          <p>Fayana leads by bringing structure and clarity to complex work. She defines scopes, builds practical work plans, keeps concurrent workstreams visible, and makes sure responsibilities, milestones, and risks are understood across teams. She communicates directly with executives, clients, staff, and community partners, and she addresses sensitive issues early rather than letting them grow.</p>
          <p>Her supervision and mentoring reflect the same approach: clear expectations, regular feedback, and support for professional growth.</p>
        </div>
        <div>
          <h3>Research perspective</h3>
          <p>As a medical anthropologist trained in public health, Fayana treats evidence and lived experience as complementary. Her research and evaluation work draws on ethnographic methods, qualitative interviews, and quantitative information, and she focuses on translating findings into decisions that programs can act on.</p>
          <p>She is attentive to how social and structural conditions shape health, and she designs research and engagement activities that respect the communities involved.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-neutral" aria-labelledby="focus-areas-heading">
    <div class="container">
      <h2 id="focus-areas-heading">Areas of Focus</h2>
      <ul class="tag-list" style="margin-top: var(--space-5);">
        <li>Public health</li>
        <li>Health disparities</li>
        <li>Social and structural determinants of health</li>
        <li>Race and health</li>
        <li>Aging</li>
        <li>Caregiving</li>
        <li>Chronic illness</li>
        <li>Community health</li>
        <li>Health promotion</li>
        <li>Population health</li>
        <li>Workforce development</li>
        <li>Community engagement</li>
        <li>Culturally responsive program design</li>
        <li>Research translation</li>
        <li>Program implementation and evaluation</li>
        <li>Strategic planning</li>
        <li>Organizational learning</li>
        <li>Partnership development</li>
      </ul>
    </div>
  </section>

  <section class="cta-band">
    <div class="container">
      <div>
        <h2>Work With Fayana</h2>
        <p>Review her résumé or get in touch about program leadership, research, teaching, facilitation, or speaking.</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-light" href="{r('/resume/')}">View Résumé</a>
        <a class="btn btn-outline-light" href="{r('/contact/')}">Contact Fayana</a>
      </div>
    </div>
  </section>
"""


def leadership(depth):
    r = lambda p: rel(p, depth)
    sections = [
        ("Planning and Scoping",
         ["Client intake", "Needs clarification", "Scope development", "Scope of work preparation",
          "Work plan development", "Timeline development", "Deliverable definition",
          "Staffing considerations", "Budget considerations", "Project documentation"],
         "Applied in consulting engagements at the Michigan Public Health Institute and in grant development at the University of Massachusetts Amherst.",
         "/work/public-health-consulting/", "Public health consulting case study"),
        ("Project Coordination",
         ["Cross-functional coordination", "Team communication", "Meeting facilitation",
          "Action-item follow-up", "Milestone tracking", "Deliverable monitoring", "Dashboard use",
          "Resource coordination", "Dependency tracking", "Project reporting"],
         "Practiced across concurrent consulting projects and in federally funded research coordination at the University of Arizona.",
         "/work/research-project-coordination/", "Research project coordination case study"),
        ("Risk and Issue Management",
         ["Risk identification", "Implementation concern tracking", "Sensitive issue management",
          "Escalation support", "Stakeholder communication", "Adjustment planning", "Decision documentation"],
         "Central to senior consulting work involving sensitive public health topics and organizational partnerships.",
         "/work/public-health-consulting/", "Public health consulting case study"),
        ("Partnerships and Stakeholders",
         ["Client advising", "Leadership communication", "Community engagement", "Partnership development",
          "Contract discussion support", "Agreement support", "Collaborative planning", "Relationship management"],
         "Developed through client advising, community partnership work, and support for contract and agreement discussions.",
         "/work/public-health-consulting/", "Public health consulting case study"),
        ("Performance and Learning",
         ["Qualitative feedback", "Quantitative information", "Program assessment", "Curriculum assessment",
          "Project review", "Performance monitoring", "Lessons applied to later work", "Research translation"],
         "Reflected in program and curriculum assessment at the University of Memphis and evidence-informed consulting practice.",
         "/work/curriculum-development/", "Curriculum development case study"),
        ("Team Development",
         ["Staff supervision", "Consultant team leadership", "Student mentoring",
          "Undergraduate research supervision", "Professional development", "Feedback and work review",
          "Role clarification"],
         "Includes leading a team of public health consultants, supervising staff, and mentoring students and undergraduate researchers.",
         "/work/research-development-program/", "Research and professional development program case study"),
    ]
    sections_html = "\n".join(
        f"""      <article class="card">
        <h3>{title}</h3>
        <ul>
{''.join(f'          <li>{item}</li>' + chr(10) for item in items)}        </ul>
        <p>{context}</p>
        <p><a class="card-link" href="{r(link)}">{label}</a></p>
      </article>""" for title, items, context, link, label in sections
    )
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Program and Project Leadership</span>
      <h1>Program and Project Leadership</h1>
      <p class="lede section-intro">Fayana&rsquo;s project leadership experience spans public health consulting, research programs, higher education, grant development, curriculum design, and community partnerships. She brings structure to complex work through clear planning, coordinated communication, progress monitoring, and evidence-informed decision-making.</p>
      <p class="section-intro">She holds the Project Management Professional (PMP) credential from the Project Management Institute (2026).</p>
    </div>
  </section>

  <section class="section" aria-labelledby="leadership-areas-heading">
    <div class="container">
      <h2 id="leadership-areas-heading" class="visually-hidden">Leadership capability areas</h2>
      <div class="card-grid card-grid-2">
{sections_html}
      </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="container">
      <div>
        <h2>See This Leadership in Practice</h2>
        <p>Case studies show how Fayana applies planning, coordination, and evidence across real engagements.</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-light" href="{r('/work/')}">View Selected Work</a>
        <a class="btn btn-outline-light" href="{r('/experience/')}">Review Experience</a>
      </div>
    </div>
  </section>
"""


def experience(depth):
    r = lambda p: rel(p, depth)
    entries = [
        {
            "type": "Employment", "title": "Senior Public Health Consultant",
            "org": "Michigan Public Health Institute", "dates": "June 2021 &ndash; 2025",
            "summary": "Senior consulting role spanning multiple concurrent public health projects. Combined project leadership, client advising, facilitation, partnership support, and evidence-informed decision-making, with a focus on social justice programming and health equity topics.",
            "bullets": [
                "Led or coordinated multiple concurrent public health projects and led a team of public health consultants.",
                "Conducted client intake meetings, developed scopes of work, and built project plans and work plans.",
                "Established and monitored timelines and milestones, tracked deliverables, and maintained dashboards and project-tracking tools.",
                "Advised clients and organizational leaders on social justice programming and managed sensitive issues and escalations.",
                "Designed and facilitated workshops, including virtual sessions addressing racism, oppression, health disparities, and related public health issues.",
                "Supported contract negotiations, partnership agreements, and joint-venture agreement work.",
                "Supervised staff and used qualitative and quantitative information to support program decisions.",
            ],
            "tags": ["Program Management", "Public Health", "Facilitation", "Partnerships"],
            "link": ("/work/public-health-consulting/", "Read the consulting case study"),
        },
        {
            "type": "Academic appointment", "title": "Assistant Professor of Medical Anthropology",
            "org": "University of Memphis", "dates": "August 2019 &ndash; May 2021",
            "summary": "Faculty appointment combining teaching, curriculum development, program assessment, and student mentoring, with a focus on race, health disparities, and applied medical anthropology.",
            "bullets": [
                "Designed and taught courses related to race, health disparities, and applied medical anthropology.",
                "Developed curricula and instructional materials connected to measurable learning objectives.",
                "Supported curriculum review, program assessment, and administrative planning.",
                "Mentored students in research and community engagement.",
                "Used interactive teaching and discussion-based methods.",
            ],
            "tags": ["Education", "Curriculum Development", "Evaluation", "Mentoring"],
            "link": ("/work/curriculum-development/", "Read the curriculum case study"),
        },
        {
            "type": "Academic appointment", "title": "Visiting Assistant Professor of Public Health",
            "org": "Hampshire College", "dates": "2019",
            "summary": "Visiting faculty appointment teaching public health content within an interdisciplinary liberal arts setting.",
            "bullets": [
                "Taught public health content and supported interdisciplinary education.",
                "Applied expertise in medical anthropology and population health.",
                "Developed and delivered instructional content and supported student learning.",
            ],
            "tags": ["Education", "Public Health"],
            "link": None,
        },
        {
            "type": "Research appointment", "title": "Post-Doctoral Research Associate",
            "org": "University of Massachusetts Amherst &middot; Center for Community Health Research", "dates": "January 2018 &ndash; January 2019",
            "summary": "Postdoctoral appointment supporting community-engaged research on chronic disease prevention and transnational health, with substantial program development and grant support responsibilities.",
            "bullets": [
                "Helped develop a research and professional development program for students from underrepresented backgrounds.",
                "Assisted with staffing requirements and budget development for a National Institutes of Health (NIH) R01 grant application, and supported grant compliance planning.",
                "Coordinated research and professional development activities with faculty, staff, students, and community partners.",
                "Supported community-engaged research on chronic disease prevention and transnational health.",
            ],
            "tags": ["Research", "Program Management", "Grant Support", "Community Engagement"],
            "link": ("/work/research-development-program/", "Read the program design case study"),
        },
        {
            "type": "Graduate roles", "title": "Doctoral Researcher, Graduate Scholar, and Graduate Teaching Assistant",
            "org": "Michigan State University", "dates": "August 2010 &ndash; December 2017 (teaching 2011&ndash;2017)",
            "summary": "Doctoral training in medical anthropology with extended community-based field research and sustained teaching support roles.",
            "bullets": [
                "Conducted approximately 18 months of field research on aging, caregiving, chronic illness, and health disparities among older Black women in Detroit.",
                "Examined social and structural determinants of health using qualitative and quantitative information, including interviews and field-based research.",
                "Received multi-year support from Michigan State University and the National Science Foundation.",
                "Supported college-level teaching, assisted with grading, delivered guest lectures, and supported assessment development.",
                "Developed experience in research design, data collection, analysis, and research communication.",
            ],
            "tags": ["Research", "Community Engagement", "Education"],
            "link": ("/work/aging-caregiving-research/", "Read the research case study"),
        },
        {
            "type": "Employment", "title": "Project Coordinator",
            "org": "University of Arizona", "dates": "2009 &ndash; 2010",
            "summary": "Coordination role on a federally funded research project, combining research operations, financial monitoring, and supervision of undergraduate researchers.",
            "bullets": [
                "Coordinated activities for a federally funded research project.",
                "Prepared monthly expense reports and monitored project expenditures.",
                "Supported project documentation, reporting, and data management.",
                "Supervised undergraduate research activities.",
                "Used Atlas.ti and SPSS to support research tasks.",
            ],
            "tags": ["Project Management", "Research", "Grant Support"],
            "link": ("/work/research-project-coordination/", "Read the coordination case study"),
        },
        {
            "type": "Internship", "title": "Editorial Intern",
            "org": "Science Magazine", "dates": "Dates in review",
            "summary": "Editorial internship focused on translating scientific research for broad audiences across digital formats. Details of this role are being confirmed against approved records.",
            "bullets": [
                "Interviewed researchers and conducted background research.",
                "Fact-checked scientific information.",
                "Wrote articles for the Science website and produced a podcast episode.",
                "Supported digital science communication.",
            ],
            "tags": ["Science Communication", "Research"],
            "link": ("/work/science-communication/", "Read the science communication case study"),
        },
    ]
    entries_html = ""
    for e in entries:
        bullets = "".join(f"          <li>{b}</li>\n" for b in e["bullets"])
        tags = "".join(f"<li>{t}</li>" for t in e["tags"])
        link_html = f'\n        <p><a class="card-link" href="{r(e["link"][0])}">{e["link"][1]}</a></p>' if e["link"] else ""
        entries_html += f"""      <article class="entry">
        <p class="entry-meta"><span class="entry-type">{e['type']}</span> <span>{e['dates']}</span></p>
        <h3>{e['title']}</h3>
        <p class="entry-org">{e['org']}</p>
        <p>{e['summary']}</p>
        <ul>
{bullets}        </ul>
        <ul class="tag-list">{tags}</ul>{link_html}
      </article>
"""
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Experience</span>
      <h1>Professional Experience</h1>
      <p class="lede section-intro">More than 18 years of experience across public health consulting, higher education, research, community engagement, and science communication, presented in reverse-chronological order.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{r('/resume/')}">Download Résumé</a>
        <a class="btn btn-secondary" href="{r('/work/')}">View Selected Work</a>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="entries-heading">
    <div class="container">
      <h2 id="entries-heading" class="visually-hidden">Experience entries</h2>
{entries_html}    </div>
  </section>

  <section class="cta-band">
    <div class="container">
      <div>
        <h2>Looking for a Concise Summary?</h2>
        <p>The résumé page provides a downloadable overview of Fayana&rsquo;s experience and credentials.</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-light" href="{r('/resume/')}">Go to Résumé</a>
        <a class="btn btn-outline-light" href="{r('/contact/')}">Contact Fayana</a>
      </div>
    </div>
  </section>
"""
