import { useEffect, useState } from 'react'

const resumePath = '/assets/Ritik_Dandir_Resume.pdf'
const photoPath = '/assets/ritik-resume-photo.png'

const navItems = [
  ['home', 'Home'], ['about', 'About'], ['experience', 'Experience'],
  ['expertise', 'Expertise'], ['tools', 'Tools'], ['education', 'Education'], ['contact', 'Contact'],
]

const responsibilities = [
  'Prepare techno-commercial offers and engineering cost estimates based on project requirements, technical specifications, and defined scope.',
  'Support BIW welding process-related engineering activities and evaluation of manufacturing requirements.',
  'Perform engineering and manufacturing process analysis to identify opportunities for process optimization and improved manufacturing efficiency.',
  'Support cycle-time analysis and optimization activities for manufacturing processes.',
  'Perform fixture costing and estimation activities, including evaluation of engineering requirements and associated costs.',
  'Prepare and maintain engineering and business documentation for project and management requirements.',
  'Develop business dashboards and analytical reports using MS Excel and available tools.',
  'Coordinate technical information from relevant stakeholders for preparation of commercial and engineering proposals.',
  'Analyse engineering requirements and associated cost elements to support commercial decision-making and project estimation.',
  'Prepare technical information and presentations for communication of engineering and commercial requirements.',
]

const expertise = [
  ['⌘', 'BIW Welding Process', 'Manufacturing process knowledge for body-in-white welding environments.'],
  ['◈', 'Fixture Costing & Estimation', 'Engineering requirement evaluation and associated cost estimation.'],
  ['∑', 'Techno-Commercial Estimation', 'Structured offers aligned with scope, specifications and requirements.'],
  ['⌁', 'Manufacturing Process Analysis', 'Practical analysis focused on efficient manufacturing.'],
  ['↗', 'Process Optimization', 'Identifying opportunities to improve manufacturing efficiency.'],
  ['◫', 'Cycle-Time Optimization', 'Supporting cycle-time analysis across manufacturing processes.'],
  ['₹', 'Engineering Cost Analysis', 'Breaking down engineering cost elements for decisions.'],
  ['▤', 'Engineering Documentation', 'Clear project, management and proposal documentation.'],
  ['◌', 'Technical Proposal Preparation', 'Communicating technical and commercial requirements.'],
  ['▥', 'Business & Engineering Reporting', 'Dashboards and analytical reports for stakeholders.'],
  ['▦', 'Excel-Based Analysis', 'Advanced Excel, pivots, XLOOKUP and Power Query.'],
  ['⌗', 'Dashboard Development', 'Business dashboards built from available tools and data.'],
]

const tools = [
  ['MS Excel', 'Advanced', 'Pivot Tables  ·  XLOOKUP  ·  Power Query'],
  ['MS PowerPoint', '', 'Technical information and presentations'],
  ['Power BI', 'Basic / Intermediate', 'Business dashboards and analytical reports'],
  ['AutoCAD', 'Basic', 'Engineering drawing support'],
  ['ERP / SAP', 'Basic', 'Enterprise resource planning exposure'],
]

const professionalSkills = ['Analytical Thinking', 'Problem Solving', 'Technical Communication', 'Team Collaboration', 'Documentation Management', 'Time Management', 'Engineering Coordination', 'Business Communication']

const education = [
  ['2024', 'Precision Engineering Certificate Course', 'SSR Global Skill Park, Bhopal'],
  ['2023', 'Bachelor of Technology (B.Tech) – Mechanical Engineering', 'Chameli Devi Group of Institutions'],
  ['2019', 'Class XII – PCM', 'Shree Vaishnav Vidya Mandir, Khargone'],
  ['2016', 'Class X', 'Shree Vaishnav Vidya Mandir, Khargone'],
]

function Icon({ children }) { return <span className="icon" aria-hidden="true">{children}</span> }
function SectionLabel({ number, children }) { return <div className="section-label"><span>{number}</span>{children}</div> }
function DownloadButton({ className = '' }) { return <a className={`button button-primary ${className}`} href={resumePath} download="Ritik_Dandir_Resume.pdf"><span>↓</span> Download Resume</a> }

function Navbar({ menuOpen, setMenuOpen, active }) {
  return <header className="navbar">
    <a href="#home" className="brand" onClick={() => setMenuOpen(false)}><span className="brand-mark">RD</span><span>RITIK <b>DANDIR</b></span></a>
    <button className="menu-toggle" aria-label="Toggle navigation" aria-expanded={menuOpen} onClick={() => setMenuOpen(!menuOpen)}><span></span><span></span><span></span></button>
    <nav className={menuOpen ? 'nav-links open' : 'nav-links'}>
      {navItems.map(([id, label]) => <a key={id} className={active === id ? 'active' : ''} href={`#${id}`} onClick={() => setMenuOpen(false)}>{label}</a>)}
      <DownloadButton />
    </nav>
  </header>
}

function Hero() {
  return <section id="home" className="hero section-shell">
    <div className="hero-photo-wrap"><div className="photo-frame"><img src={photoPath} alt="Ritik Dandir, Mechanical Engineer" /></div><div className="photo-caption"><span className="status-dot"></span> Engineering · Automotive · Precision</div></div>
    <div className="hero-copy">
      <div className="eyebrow">EXECUTIVE ENGINEER <span>•</span> JBM GROUP</div>
      <h1>RITIK <span>DANDIR</span></h1>
      <p className="hero-role">Mechanical Engineer</p>
      <p className="hero-specialty">Manufacturing Engineering <i>/</i> BIW <i>/</i> Fixture Costing <i>/</i> Techno-Commercial Estimation</p>
      <p className="hero-summary">Mechanical Engineering professional with experience in automotive manufacturing engineering, BIW welding processes, fixture costing, techno-commercial estimation, process analysis, cycle-time optimization, and engineering documentation.</p>
      <div className="hero-actions"><DownloadButton /><a className="button button-outline" href="#contact">Contact Me <span>↗</span></a></div>
      <div className="hero-tags"><span>BIW</span><span>FIXTURE COSTING</span><span>PROCESS OPTIMIZATION</span></div>
    </div>
    <div className="hero-code" aria-hidden="true">ME / 01<br/><span>06.25°N · 75.82°E</span></div>
  </section>
}

function About() {
  return <section id="about" className="section section-light"><div className="section-shell">
    <SectionLabel number="01 /">About Me</SectionLabel>
    <div className="about-grid"><div><h2>Engineering clarity.<br /><em>Manufacturing focus.</em></h2></div><div className="about-copy"><p>Mechanical Engineering professional with experience in automotive manufacturing engineering, BIW welding processes, fixture costing, techno-commercial estimation, process analysis, cycle-time optimization, and engineering documentation.</p><p>Currently working as an Executive Engineer at JBM Group, with progression from Graduate Engineer Trainee to Executive Engineer within one year.</p><p>Experienced in preparing engineering cost estimates and techno-commercial offers, supporting fixture costing activities, analysing manufacturing processes, developing business dashboards, and coordinating technical information for engineering and commercial proposals.</p></div></div>
    <div className="stat-strip"><div><strong>2023</strong><span>CAREER START</span></div><div><strong>1 YEAR</strong><span>ROLE PROGRESSION</span></div><div><strong>BIW</strong><span>ENGINEERING FOCUS</span></div><div><strong>FIXTURE</strong><span>CORE AREA</span></div></div>
  </div></section>
}

function Experience() {
  return <section id="experience" className="section section-navy"><div className="section-shell"><SectionLabel number="02 /">Professional Experience</SectionLabel><div className="experience-layout"><div className="experience-aside"><div className="timeline-marker">01</div><div><p className="company">JBM GROUP</p><p className="location">Gurugram</p></div></div><div className="experience-main"><div className="role-row"><div><h3>Executive Engineer <span>– Engineering</span></h3><p className="date">2023 – Present</p></div><span className="role-tag">CURRENT ROLE</span></div><ul className="responsibilities">{responsibilities.map((item, i) => <li key={i}>{item}</li>)}</ul></div></div>
    <div className="progression"><div className="progression-label">CAREER PROGRESSION <span>WITHIN 1 YEAR</span></div><div className="progression-flow"><strong>Graduate Engineer Trainee</strong><span className="arrow">→</span><strong>Executive Engineer</strong></div><p>Progressed to the position of Executive Engineer, reflecting increased responsibility in engineering, costing, process analysis, documentation and commercial estimation.</p></div>
  </div></section>
}

function Expertise() {
  return <section id="expertise" className="section section-light blueprint"><div className="section-shell"><SectionLabel number="03 /">Engineering Expertise</SectionLabel><div className="section-intro"><h2>Precision in every<br /><em>engineering detail.</em></h2><p>Core capabilities spanning automotive manufacturing, estimation, analysis and technical communication.</p></div><div className="expertise-grid">{expertise.map(([icon, title, desc], index) => <article className="expertise-card" key={title}><Icon>{icon}</Icon><div><h3>{title}</h3><p>{desc}</p></div><span className="card-index">{String(index + 1).padStart(2, '0')}</span></article>)}</div></div></section>
}

function Tools() {
  return <section id="tools" className="section section-blue"><div className="section-shell"><SectionLabel number="04 /">Tools & Technologies</SectionLabel><div className="tools-layout"><div><h2>Tools that turn<br /><em>data into decisions.</em></h2><p className="muted-light">A practical working toolkit for engineering analysis, documentation, reporting and commercial proposals.</p></div><div className="tools-grid">{tools.map(([name, level, detail]) => <div className="tool-card" key={name}><div className="tool-top"><h3>{name}</h3>{level && <span>{level}</span>}</div><p>{detail}</p></div>)}</div></div><div className="skills-row"><div><p className="mini-heading">PROFESSIONAL SKILLS</p><div className="skill-pills">{professionalSkills.map(skill => <span key={skill}>{skill}</span>)}</div></div><div className="language-box"><p className="mini-heading">LANGUAGES</p><strong>English</strong><strong>Hindi</strong></div></div></div></section>
}

function Education() {
  return <section id="education" className="section section-light"><div className="section-shell"><SectionLabel number="05 /">Education</SectionLabel><div className="education-intro"><h2>Built on a foundation<br /><em>of precision.</em></h2><p>Education and continuous technical development supporting a career in manufacturing engineering.</p></div><div className="education-timeline">{education.map(([year, title, school]) => <article key={year}><span className="edu-year">{year}</span><span className="edu-node"></span><div><h3>{title}</h3><p>{school}</p></div></article>)}</div></div></section>
}

function Contact() {
  return <section id="contact" className="contact-section"><div className="section-shell"><SectionLabel number="06 /">Contact</SectionLabel><div className="contact-grid"><div><h2>Let's connect.</h2><p>Interested in discussing engineering opportunities, manufacturing projects, fixture engineering, costing, or technical collaboration?</p><div className="contact-actions"><a className="button button-light" href="mailto:ritikdandir@gmail.com">Email Me <span>↗</span></a><a className="button button-ghost" href="https://www.linkedin.com/in/ritikdandir" target="_blank" rel="noreferrer">LinkedIn <span>↗</span></a><DownloadButton className="button-ghost" /></div></div><div className="contact-details"><a href="tel:+917972684544"><Icon>☎</Icon><span>+91 797-426-8544</span></a><a href="mailto:ritikdandir@gmail.com"><Icon>✉</Icon><span>ritikdandir@gmail.com</span></a><span><Icon>⌖</Icon><span>Khargone, Madhya Pradesh, India</span></span></div></div></div></section>
}

function Footer() { return <footer><div className="section-shell footer-inner"><div><strong>RITIK <span>DANDIR</span></strong><p>Mechanical Engineer · Manufacturing Engineering · BIW · Fixture Costing</p></div><p>© 2026 Ritik Dandir. All rights reserved.</p></div></footer> }

export default function App() {
  const [menuOpen, setMenuOpen] = useState(false)
  const [active, setActive] = useState('home')
  useEffect(() => {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) setActive(entry.target.id) }), { rootMargin: '-30% 0px -60% 0px' })
    navItems.forEach(([id]) => { const el = document.getElementById(id); if (el) observer.observe(el) })
    return () => observer.disconnect()
  }, [])
  return <><Navbar menuOpen={menuOpen} setMenuOpen={setMenuOpen} active={active} /><main><Hero /><About /><Experience /><Expertise /><Tools /><Education /><Contact /></main><Footer /><button className="to-top" aria-label="Scroll to top" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>↑</button></>
}
