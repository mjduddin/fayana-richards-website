"""Research, Teaching, Speaking, Résumé, Contact, statements, and 404 pages."""
from templates import rel


def research(depth):
    r = lambda p: rel(p, depth)
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Research and Writing</span>
      <h1>Research and Writing</h1>
      <p class="lede section-intro">Fayana&rsquo;s research and writing address aging, caregiving, chronic illness, race and health, and the social and structural conditions that shape health outcomes.</p>
    </div>
  </section>

  <section class="section" aria-labelledby="overview-heading">
    <div class="container split">
      <div>
        <h2 id="overview-heading">Research Overview</h2>
        <p>Fayana is a medical anthropologist with public health training whose research centers on how social and structural conditions shape health. Her doctoral fieldwork examined aging, caregiving, chronic illness, and health disparities among older Black women in Detroit, drawing on approximately 18 months of community-based field research supported by Michigan State University and the National Science Foundation.</p>
        <p>Her postdoctoral work at the University of Massachusetts Amherst supported community-engaged research on chronic disease prevention and transnational health. Across roles, she emphasizes research translation: turning findings into language and decisions that programs, leaders, and communities can use.</p>
      </div>
      <div>
        <h2>Research Interests</h2>
        <ul class="tag-list">
          <li>Health disparities</li>
          <li>Aging</li>
          <li>Caregiving</li>
          <li>Chronic illness</li>
          <li>Race and health</li>
          <li>Social determinants of health</li>
          <li>Structural determinants of health</li>
          <li>Community health</li>
          <li>Health promotion</li>
          <li>Community-engaged research</li>
          <li>Culturally responsive programs</li>
          <li>Workforce development</li>
          <li>Health and social impact</li>
        </ul>
        <h2 style="margin-top: var(--space-6);">Research Methods</h2>
        <ul class="tag-list">
          <li>Ethnographic research</li>
          <li>Qualitative interviews</li>
          <li>Field research</li>
          <li>Qualitative analysis</li>
          <li>Quantitative analysis</li>
          <li>Mixed-methods research</li>
          <li>Community engagement</li>
          <li>Literature review</li>
          <li>Research translation</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section section-neutral" id="publications" aria-labelledby="publications-heading">
    <div class="container">
      <h2 id="publications-heading">Peer-Reviewed Publications</h2>
      <div class="empty-state">
        <p>Publication information is being prepared for the website. A complete curriculum vitae is available upon request.</p>
      </div>

      <h2 style="margin-top: var(--space-7);">Reports, Briefs, and Book Chapters</h2>
      <div class="empty-state">
        <p>Additional publication information is being prepared for this website.</p>
      </div>

      <h2 style="margin-top: var(--space-7);">Public Scholarship and Science Journalism</h2>
      <p>As an editorial intern with Science Magazine, Fayana interviewed researchers, conducted background research, fact-checked scientific information, wrote articles for the Science website, and produced a podcast episode. Specific article and podcast details will be added after review of approved records.</p>
      <p><a class="card-link" href="{r('/work/science-communication/')}">Read the science communication case study</a></p>

      <h2 style="margin-top: var(--space-7);">Works in Progress</h2>
      <div class="empty-state">
        <p>Information about current writing projects will be added after review of approved materials.</p>
      </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="container">
      <div>
        <h2>Request the Full Curriculum Vitae</h2>
        <p>A complete record of publications, presentations, and research activity is available upon request.</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-light" href="{r('/contact/')}">Contact Fayana</a>
      </div>
    </div>
  </section>
"""


def teaching(depth):
    r = lambda p: rel(p, depth)
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Teaching and Facilitation</span>
      <h1>Teaching and Facilitation</h1>
      <p class="lede section-intro">Fayana designs curricula, teaches university courses, develops workshops, and facilitates virtual and in-person learning for students, professionals, and community audiences.</p>
      <p class="section-intro"><a class="card-link" href="{r('/speaking/')}">Looking for conference presentations and invited talks? Visit the Speaking page.</a></p>
    </div>
  </section>

  <section class="section" aria-labelledby="university-heading">
    <div class="container">
      <h2 id="university-heading">University Teaching</h2>
      <div class="card-grid card-grid-3">
        <article class="card">
          <h3>University of Memphis</h3>
          <p>As Assistant Professor of Medical Anthropology (2019&ndash;2021), Fayana designed and taught courses on race, health disparities, and applied medical anthropology. She developed curricula and instructional materials tied to measurable learning objectives, supported curriculum review and program assessment, and mentored students in research and community engagement.</p>
        </article>
        <article class="card">
          <h3>Hampshire College</h3>
          <p>As Visiting Assistant Professor of Public Health (2019), Fayana taught public health content within an interdisciplinary setting, applying her expertise in medical anthropology and population health.</p>
        </article>
        <article class="card">
          <h3>Michigan State University</h3>
          <p>As a graduate teaching assistant (2011&ndash;2017), Fayana supported college-level teaching, assisted with grading, delivered guest lectures, and supported assessment development.</p>
        </article>
      </div>
      <div class="empty-state" style="margin-top: var(--space-6);">
        <p>Course descriptions, syllabi, and teaching materials will be added after review of approved records.</p>
      </div>
    </div>
  </section>

  <section class="section section-neutral" aria-labelledby="facilitation-heading">
    <div class="container split">
      <div>
        <h2 id="facilitation-heading">Workshop Facilitation and Professional Learning</h2>
        <p>At the Michigan Public Health Institute, Fayana designed and facilitated workshops for professional audiences, including virtual sessions addressing racism, oppression, health disparities, and related public health issues. Her facilitation practice is inclusive and community-centered, and she is trained in Technology of Participation strategic planning and facilitation methods (Institute of Cultural Affairs, 2021).</p>
        <p>At the University of Massachusetts Amherst, she helped develop a research and professional development program for students from underrepresented backgrounds, coordinating learning activities across faculty, staff, students, and community partners.</p>
      </div>
      <div>
        <h2>Teaching and Facilitation Strengths</h2>
        <ul class="tag-list">
          <li>Curriculum design</li>
          <li>Instructional material development</li>
          <li>Interactive teaching</li>
          <li>Group discussion facilitation</li>
          <li>Virtual facilitation</li>
          <li>Learning assessment</li>
          <li>Program assessment</li>
          <li>Student mentoring</li>
          <li>Professional development</li>
          <li>Community-engaged learning</li>
          <li>Research mentoring</li>
        </ul>
        <h2 style="margin-top: var(--space-6);">Subject Areas</h2>
        <ul class="tag-list">
          <li>Race and health</li>
          <li>Health disparities</li>
          <li>Applied medical anthropology</li>
          <li>Public health</li>
          <li>Community engagement</li>
          <li>Aging and health</li>
          <li>Social determinants of health</li>
          <li>Chronic illness</li>
          <li>Research methods</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="materials-heading">
    <div class="container">
      <h2 id="materials-heading">Workshop Agendas, Materials, and Feedback</h2>
      <div class="empty-state">
        <p>Workshop agendas, training presentations, participant feedback, and learning outcomes will be added after review of approved materials.</p>
      </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="container">
      <div>
        <h2>Invite Fayana to Teach or Facilitate</h2>
        <p>Fayana welcomes teaching, workshop, and facilitation invitations.</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-light" href="{r('/contact/')}">Contact Fayana</a>
        <a class="btn btn-outline-light" href="{r('/speaking/')}">View Speaking</a>
      </div>
    </div>
  </section>
"""


def speaking(depth):
    r = lambda p: rel(p, depth)
    categories = [
        ("Conference Presentations", "Conference presentation records are being verified against approved materials and will be listed here."),
        ("Invited Lectures and Panels", "Invited lecture and panel records are being verified against approved materials and will be listed here."),
        ("Workshops and Webinars", "Fayana has designed and facilitated workshops and virtual sessions on racism, oppression, health disparities, and related public health issues. Specific session records will be listed after review of approved materials."),
        ("Community and Professional Development Sessions", "Community presentation and professional development session records will be listed after review of approved materials."),
        ("Podcast Appearances and Production", "Fayana produced a podcast episode during her editorial internship with Science Magazine. Episode details will be added after verification."),
    ]
    cats_html = "\n".join(
        f"""        <article class="card">
          <h3>{title}</h3>
          <p>{body}</p>
        </article>""" for title, body in categories
    )
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Speaking</span>
      <h1>Speaking and Presentations</h1>
      <p class="lede section-intro">Fayana&rsquo;s speaking experience includes conference presentation, guest lectures, workshop facilitation, and audio science communication. Her topics span aging, caregiving, chronic illness, race and health, health disparities, community-engaged research, and program leadership.</p>
    </div>
  </section>

  <section class="section" aria-labelledby="categories-heading">
    <div class="container">
      <h2 id="categories-heading" class="visually-hidden">Speaking categories</h2>
      <div class="card-grid card-grid-2">
{cats_html}
      </div>
      <div class="empty-state" style="margin-top: var(--space-6);">
        <p>A verified list of presentations, with titles, events, host organizations, and dates, is being prepared for this website. A complete curriculum vitae is available upon request.</p>
      </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="container">
      <div>
        <h2>Invite Fayana to Speak</h2>
        <p>Fayana welcomes speaking and facilitation invitations.</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-light" href="{r('/contact/')}">Contact Fayana</a>
      </div>
    </div>
  </section>
"""


def resume(depth):
    r = lambda p: rel(p, depth)
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Résumé</span>
      <h1>Résumé</h1>
      <p class="lede section-intro">Dr. Fayana Richards, MPH, PMP, is a public health program strategy and operations leader and medical anthropologist with more than 18 years of experience across consulting, research, higher education, community engagement, and professional learning. She holds a PhD in Medical Anthropology and an MPH from Michigan State University and the Project Management Professional credential from the Project Management Institute.</p>
    </div>
  </section>

  <section class="section" aria-labelledby="download-heading">
    <div class="container split">
      <div>
        <h2 id="download-heading">Download</h2>
        <div class="empty-state">
          <p>The current résumé file is being prepared for download. In the meantime, a copy is available promptly upon request through the <a href="{r('/contact/')}">contact page</a>.</p>
        </div>
        <!-- When the approved PDF is available, place it at /assets/downloads/Fayana Richards Resume.pdf
             and replace the empty state above with:
        <p><a class="btn btn-primary" href="{r('/assets/downloads/Fayana Richards Resume.pdf')}" download>Download Résumé (PDF)</a></p>
        -->
        <p style="margin-top: var(--space-5);"><button type="button" class="btn btn-secondary" onclick="window.print()">Print This Page</button></p>
      </div>
      <div>
        <h2>Explore the Details</h2>
        <ul>
          <li><a href="{r('/experience/')}">Full professional experience</a></li>
          <li><a href="{r('/work/')}">Selected work and case studies</a></li>
          <li><a href="{r('/about/')}">Education, credentials, and biography</a></li>
          <li><a href="{r('/contact/')}">Contact Fayana</a></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section section-neutral" aria-labelledby="summary-heading">
    <div class="container">
      <h2 id="summary-heading">Summary of Qualifications</h2>
      <div class="card-grid card-grid-2">
        <article class="card">
          <h3>Experience</h3>
          <ul>
            <li>Senior Public Health Consultant, Michigan Public Health Institute (June 2021&ndash;2025)</li>
            <li>Assistant Professor of Medical Anthropology, University of Memphis (2019&ndash;2021)</li>
            <li>Visiting Assistant Professor of Public Health, Hampshire College (2019)</li>
            <li>Post-Doctoral Research Associate, University of Massachusetts Amherst (2018&ndash;2019)</li>
            <li>Doctoral Researcher and Graduate Teaching Assistant, Michigan State University (2010&ndash;2017)</li>
            <li>Project Coordinator, University of Arizona (2009&ndash;2010)</li>
          </ul>
        </article>
        <article class="card">
          <h3>Education and Credentials</h3>
          <ul>
            <li>PhD, Medical Anthropology, Michigan State University, 2018</li>
            <li>MPH, Michigan State University, 2015</li>
            <li>MA, Medical Anthropology, Michigan State University, 2012</li>
            <li>BA, Medical Anthropology and Journalism, University of Arizona, 2008</li>
            <li>Project Management Professional (PMP), Project Management Institute, 2026</li>
            <li>Technology of Participation Strategic Planning and Facilitation Methods, Institute of Cultural Affairs, 2021</li>
          </ul>
        </article>
      </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="container">
      <div>
        <h2>Request the Résumé or Curriculum Vitae</h2>
        <p>Both documents are available upon request while download files are finalized.</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-light" href="{r('/contact/')}">Contact Fayana</a>
      </div>
    </div>
  </section>
"""


def contact(depth):
    r = lambda p: rel(p, depth)
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Contact</span>
      <h1>Contact Fayana</h1>
      <p class="lede section-intro">For senior program leadership, strategic initiatives, public health, research administration, academic programming, facilitation, speaking, or collaborative opportunities, complete the form below.</p>
    </div>
  </section>

  <section class="section" aria-labelledby="form-heading">
    <div class="container split">
      <div>
        <h2 id="form-heading">Send a Message</h2>
        <form id="contact-form" class="form-grid" method="POST" action="/contact/?submitted=true" name="contact" data-netlify="true" netlify-honeypot="company-website" novalidate>
          <input type="hidden" name="form-name" value="contact">
          <p class="honeypot-field" aria-hidden="true">
            <label>Leave this field empty: <input type="text" name="company-website" tabindex="-1" autocomplete="off"></label>
          </p>
          <div class="form-row">
            <div class="form-field">
              <label for="name">Name <span aria-hidden="true">*</span></label>
              <input type="text" id="name" name="name" autocomplete="name" required aria-required="true" aria-describedby="name-error">
              <p class="field-error" id="name-error" aria-live="polite"></p>
            </div>
            <div class="form-field">
              <label for="organization">Organization</label>
              <input type="text" id="organization" name="organization" autocomplete="organization">
            </div>
          </div>
          <div class="form-row">
            <div class="form-field">
              <label for="email">Email <span aria-hidden="true">*</span></label>
              <input type="email" id="email" name="email" autocomplete="email" required aria-required="true" aria-describedby="email-error">
              <p class="field-error" id="email-error" aria-live="polite"></p>
            </div>
            <div class="form-field">
              <label for="inquiry-type">Inquiry type <span aria-hidden="true">*</span></label>
              <select id="inquiry-type" name="inquiry-type" required aria-required="true" aria-describedby="inquiry-type-error">
                <option value="">Select an inquiry type</option>
                <option>Employment Opportunity</option>
                <option>Program Leadership</option>
                <option>Strategic Initiative</option>
                <option>Research Collaboration</option>
                <option>Academic Opportunity</option>
                <option>Speaking or Facilitation</option>
                <option>Professional Partnership</option>
                <option>Other</option>
              </select>
              <p class="field-error" id="inquiry-type-error" aria-live="polite"></p>
            </div>
          </div>
          <div class="form-field">
            <label for="subject">Subject <span aria-hidden="true">*</span></label>
            <input type="text" id="subject" name="subject" required aria-required="true" aria-describedby="subject-error">
            <p class="field-error" id="subject-error" aria-live="polite"></p>
          </div>
          <div class="form-field">
            <label for="message">Message <span aria-hidden="true">*</span></label>
            <p class="field-hint">Please share a brief description of the opportunity or question. Do not include sensitive personal information.</p>
            <input type="hidden" name="_subject" value="Website contact form submission">
            <textarea id="message" name="message" required aria-required="true" aria-describedby="message-error"></textarea>
            <p class="field-error" id="message-error" aria-live="polite"></p>
          </div>
          <div>
            <button type="submit" class="btn btn-primary">Send Message</button>
            <p id="form-status" class="form-status" role="status" aria-live="polite" tabindex="-1"></p>
          </div>
          <p class="field-hint">Required fields are marked with an asterisk (*). Submissions are routed to Fayana&rsquo;s professional email. See the <a href="{r('/privacy/')}">privacy statement</a> for how messages are handled.</p>
        </form>
      </div>
      <aside aria-labelledby="channels-heading">
        <div class="case-aside">
          <h2 id="channels-heading">Direct Channels</h2>
          <dl>
            <dt>Email</dt>
            <dd><a href="mailto:frichard84@gmail.com">frichard84@gmail.com</a></dd>
            <dt>LinkedIn</dt>
            <dd><a href="https://www.linkedin.com/in/fayanar/" rel="me noopener" target="_blank">linkedin.com/in/fayanar<span class="visually-hidden"> (opens in a new tab)</span></a></dd>
          </dl>
          <h2 style="margin-top: var(--space-5);">Response</h2>
          <p>Fayana reviews inquiries regularly and responds as soon as possible. For time-sensitive speaking or facilitation requests, please include the event date in your message.</p>
        </div>
      </aside>
    </div>
  </section>
"""


def accessibility_page(depth):
    r = lambda p: rel(p, depth)
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Site Information</span>
      <h1>Accessibility Statement</h1>
    </div>
  </section>

  <section class="section">
    <div class="container section-intro">
      <p>This website is designed to conform to the Web Content Accessibility Guidelines (WCAG) 2.2 at Level AA. Accessibility measures on this site include semantic HTML and a logical heading structure, a skip-to-content link, keyboard-accessible navigation and controls with visible focus indicators, sufficient color contrast, descriptive link text and page titles, labeled form fields with clear validation messages and status announcements, alternative text for meaningful images, support for reduced-motion preferences, and layouts that adapt to text resizing and small screens.</p>
      <p>Accessibility is an ongoing commitment. If you encounter a barrier while using this website, or if you need information from this site in a different format, please contact Fayana at <a href="mailto:frichard84@gmail.com">frichard84@gmail.com</a> or through the <a href="{r('/contact/')}">contact form</a>. Please describe the issue and the page where it occurred, and reasonable efforts will be made to address it promptly.</p>
      <p>This statement was last reviewed in June 2026.</p>
    </div>
  </section>
"""


def privacy_page(depth):
    r = lambda p: rel(p, depth)
    return f"""  <section class="section-tight section-neutral">
    <div class="container">
      <span class="eyebrow">Site Information</span>
      <h1>Privacy Statement</h1>
    </div>
  </section>

  <section class="section">
    <div class="container section-intro">
      <h2>Information This Site Collects</h2>
      <p>This website collects only the information you choose to provide through the contact form: your name, organization (optional), email address, subject, inquiry type, and message. The form includes spam protection. Please do not include sensitive personal information in your message.</p>

      <h2>How Information Is Used</h2>
      <p>Contact form submissions are delivered to Fayana&rsquo;s professional email and used only to respond to your inquiry. Submissions are not sold, shared for marketing purposes, or used to build mailing lists.</p>

      <h2>Cookies and Analytics</h2>
      <p>This website does not set tracking cookies and does not use advertising trackers. If privacy-respecting analytics are added in the future, this statement will be updated first.</p>

      <h2>Third-Party Services</h2>
      <p>The site uses a form-handling service to deliver contact form submissions and a font service to display typefaces. These services may process technical data, such as IP addresses, as part of normal operation. Links to external sites, such as LinkedIn, are governed by those sites&rsquo; own privacy policies.</p>

      <h2>Questions</h2>
      <p>For questions about this statement or about information you have submitted, contact <a href="mailto:frichard84@gmail.com">frichard84@gmail.com</a>.</p>
      <p>This statement was last reviewed in June 2026.</p>
    </div>
  </section>
"""


def not_found(depth):
    r = lambda p: rel(p, depth)
    return f"""  <section class="section">
    <div class="container section-intro">
      <span class="eyebrow">Page Not Found</span>
      <h1>This Page Could Not Be Found</h1>
      <p class="lede">The page you requested may have moved or may no longer exist. These links can help you find what you were looking for:</p>
      <ul>
        <li><a href="{r('/')}">Home</a></li>
        <li><a href="{r('/work/')}">Selected Work</a></li>
        <li><a href="{r('/experience/')}">Experience</a></li>
        <li><a href="{r('/contact/')}">Contact Fayana</a></li>
      </ul>
    </div>
  </section>
"""
