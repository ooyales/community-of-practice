import { ArrowRight, Presentation, Monitor, SlidersHorizontal, FileText, Users, Target, TrendingUp, Shield } from 'lucide-react';

const tools = [
  {
    title: 'Strategy Pitch',
    desc: 'Full interactive presentation — the challenge, phased approach, team, CLINs, milestones, staffing timeline, and differentiators.',
    icon: Presentation,
    href: '/cop-pitch-interactive.html',
    accent: 'var(--accent)',
    tag: 'Presentation',
  },
  {
    title: 'CoP Portal Demo',
    desc: 'Live mockup of the Analytics CoP portal — migration tracker, community activity, leaderboard, and events calendar.',
    icon: Monitor,
    href: '/cop-in-a-box-demo.html',
    accent: 'var(--success)',
    tag: 'Portal Prototype',
  },
  {
    title: 'Scenario Planner',
    desc: 'Model different migration scenarios — adjust portfolio disposition, migration methods, and see real-time cost & effort comparisons.',
    icon: SlidersHorizontal,
    href: '/portfolio-scenario-planner.html',
    accent: 'var(--highlight)',
    tag: 'Interactive Tool',
  },
];

const pillars = [
  {
    icon: Users,
    title: 'Community-Led Adoption',
    desc: 'Peers teach peers. Office hours, showcases, and paired development build organic capability that outlasts any contract.',
  },
  {
    icon: Target,
    title: 'Milestone-Gated Payments',
    desc: 'T&M flexibility with FFP accountability. Hours accrue, but invoicing is gated by inspectable milestone acceptance.',
  },
  {
    icon: TrendingUp,
    title: 'Built-In Demand Signal',
    desc: 'Optional CLINs activate on real evidence — not guesswork. The CoP reveals where teams need hands-on execution.',
  },
  {
    icon: Shield,
    title: 'Zero Lock-In',
    desc: 'Every deliverable transfers to the agency. The CoP is designed to outlive the contract. We succeed when you don\'t need us.',
  },
];

export default function Home() {
  return (
    <div className="min-h-screen" style={{ background: 'var(--paper)', color: 'var(--ink)' }}>
      {/* ─── HERO ─── */}
      <header className="relative overflow-hidden text-white" style={{
        background: 'linear-gradient(165deg, #1a1a2e 0%, #2d5a7b 55%, #3a7ca5 100%)',
        minHeight: '520px',
      }}>
        {/* Decorative orb */}
        <div className="absolute -top-48 -right-48 w-[600px] h-[600px] rounded-full pointer-events-none"
          style={{ background: 'radial-gradient(circle, rgba(212,168,67,0.15) 0%, transparent 70%)' }} />

        <div className="relative z-10 max-w-5xl mx-auto px-8 py-20 md:py-28">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-semibold tracking-wider uppercase mb-8"
            style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.15)' }}>
            <span className="w-1.5 h-1.5 rounded-full" style={{ background: 'var(--highlight)' }} />
            Summit Materials
          </div>

          <h1 className="text-4xl md:text-5xl lg:text-6xl font-light leading-tight max-w-3xl"
            style={{ fontFamily: "'DM Serif Display', serif" }}>
            Migrate Smarter, Not Harder — A{' '}
            <em style={{ color: 'var(--highlight)' }}>Community of Practice</em> Approach
          </h1>

          <p className="mt-6 text-base md:text-lg font-light max-w-2xl leading-relaxed" style={{ opacity: 0.85 }}>
            Accelerate MicroStrategy disinvestment through structured enablement, organic adoption,
            and on-demand professional services — all under a single flexible T&M engagement.
          </p>

          <div className="flex flex-wrap gap-10 mt-12">
            {[
              { value: '3×', label: 'Faster Adoption' },
              { value: '40–60%', label: 'Cost Reduction' },
              { value: '3 Platforms', label: 'One Team' },
              { value: '7', label: 'Milestone Gates' },
            ].map((s) => (
              <div key={s.label} className="flex flex-col">
                <span className="text-3xl" style={{ fontFamily: "'DM Serif Display', serif", color: 'var(--highlight)' }}>
                  {s.value}
                </span>
                <span className="text-xs uppercase tracking-wider mt-1" style={{ opacity: 0.6 }}>
                  {s.label}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Bottom fade line */}
        <div className="absolute bottom-0 left-0 right-0 h-px"
          style={{ background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent)' }} />
      </header>

      {/* ─── TOOL CARDS ─── */}
      <section className="max-w-5xl mx-auto px-8 -mt-10 relative z-20">
        <div className="grid md:grid-cols-3 gap-5">
          {tools.map((t) => (
            <a
              key={t.title}
              href={t.href}
              className="group block rounded-lg p-7 transition-all duration-300 hover:-translate-y-1"
              style={{
                background: 'var(--card-bg, #fff)',
                border: '1px solid var(--border)',
                boxShadow: '0 4px 24px rgba(0,0,0,0.06)',
              }}
              onMouseEnter={(e) => e.currentTarget.style.borderColor = t.accent}
              onMouseLeave={(e) => e.currentTarget.style.borderColor = 'var(--border)'}
            >
              <div className="flex items-center gap-3 mb-4">
                <div className="w-10 h-10 rounded-lg flex items-center justify-center"
                  style={{ background: t.accent, opacity: 0.9 }}>
                  <t.icon size={20} color="#fff" />
                </div>
                <span className="text-xs font-semibold tracking-wider uppercase"
                  style={{ fontFamily: "'JetBrains Mono', monospace", color: t.accent }}>
                  {t.tag}
                </span>
              </div>
              <h3 className="text-lg font-medium mb-2" style={{ fontFamily: "'DM Serif Display', serif" }}>
                {t.title}
              </h3>
              <p className="text-sm leading-relaxed mb-4" style={{ color: 'var(--muted)' }}>
                {t.desc}
              </p>
              <span className="inline-flex items-center gap-1.5 text-sm font-medium transition-all group-hover:gap-3"
                style={{ color: t.accent }}>
                Open <ArrowRight size={14} />
              </span>
            </a>
          ))}
        </div>
      </section>

      {/* ─── ONE-PAGER DOWNLOAD ─── */}
      <section className="max-w-5xl mx-auto px-8 mt-6">
        <a
          href="/cop-one-pager.pdf"
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center gap-4 rounded-lg p-5 transition-all duration-200 hover:-translate-y-0.5"
          style={{
            background: 'var(--card-bg, #fff)',
            border: '1px solid var(--border)',
            boxShadow: '0 2px 12px rgba(0,0,0,0.04)',
          }}
        >
          <div className="w-10 h-10 rounded-lg flex items-center justify-center"
            style={{ background: 'var(--ink)' }}>
            <FileText size={20} color="var(--highlight)" />
          </div>
          <div className="flex-1">
            <h3 className="text-sm font-semibold" style={{ fontFamily: "'DM Serif Display', serif" }}>
              One-Pager — Strategic Capability Brief
            </h3>
            <p className="text-xs mt-0.5" style={{ color: 'var(--muted)' }}>
              PDF leave-behind with milestones, CLINs, team, and phased approach. Print-ready.
            </p>
          </div>
          <span className="text-xs font-medium uppercase tracking-wider" style={{ color: 'var(--accent)' }}>
            Download PDF
          </span>
        </a>
      </section>

      {/* ─── WHY A COP ─── */}
      <section className="max-w-5xl mx-auto px-8 py-20">
        <div className="text-xs font-semibold tracking-widest uppercase mb-3" style={{ color: 'var(--accent)' }}>
          The Approach
        </div>
        <h2 className="text-2xl md:text-3xl max-w-lg mb-3" style={{ fontFamily: "'DM Serif Display', serif" }}>
          Why a Community of Practice?
        </h2>
        <p className="max-w-xl mb-12 leading-relaxed" style={{ color: 'var(--muted)' }}>
          The traditional model — award a contract, throw bodies at the problem, hope for the best — leaves
          agencies dependent on contractors and wondering where the money went. The CoP model flips that script.
        </p>

        <div className="grid md:grid-cols-2 gap-5">
          {pillars.map((p) => (
            <div key={p.title} className="rounded-lg p-6 transition-all duration-200 hover:-translate-y-0.5"
              style={{ background: 'var(--card-bg, #fff)', border: '1px solid var(--border)' }}>
              <div className="flex items-start gap-4">
                <div className="w-9 h-9 rounded-lg flex items-center justify-center flex-shrink-0 mt-0.5"
                  style={{ background: 'rgba(45,90,123,0.08)' }}>
                  <p.icon size={18} style={{ color: 'var(--accent)' }} />
                </div>
                <div>
                  <h3 className="text-sm font-semibold mb-1.5">{p.title}</h3>
                  <p className="text-sm leading-relaxed" style={{ color: 'var(--muted)' }}>{p.desc}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ─── PHASED SUMMARY ─── */}
      <section className="text-white py-20" style={{ background: 'var(--ink)' }}>
        <div className="max-w-5xl mx-auto px-8">
          <div className="text-xs font-semibold tracking-widest uppercase mb-3" style={{ color: 'var(--highlight)' }}>
            Phased Approach
          </div>
          <h2 className="text-2xl md:text-3xl max-w-lg mb-12" style={{ fontFamily: "'DM Serif Display', serif" }}>
            Three Phases, One Continuous Engagement
          </h2>

          <div className="grid md:grid-cols-3 gap-6">
            {[
              {
                phase: 'Phase 1',
                months: 'Mo 1–4',
                title: 'AoA Support & CoP Standup',
                items: ['Platform evaluation (Tableau, Qlik, Power BI)', 'Portfolio assessment & classification', 'CoP infrastructure & governance'],
                color: 'var(--accent)',
              },
              {
                phase: 'Phase 2',
                months: 'Mo 5–9',
                title: 'Pilot Migration & Enablement',
                items: ['Office hours, showcases, paired development', 'First 150+ dashboards migrated', 'Self-service ratio target: ≥40%'],
                color: 'var(--accent-light)',
              },
              {
                phase: 'Phase 3',
                months: 'Mo 10+',
                title: 'Scaled Migration & Execution',
                items: ['Optional CLINs activate on demand', 'Full-scale migration to completion', 'CoP transitions to agency-sustained'],
                color: 'var(--highlight)',
              },
            ].map((p) => (
              <div key={p.phase} className="rounded-lg p-6" style={{
                background: 'rgba(255,255,255,0.04)',
                border: '1px solid rgba(255,255,255,0.08)',
              }}>
                <div className="flex items-center gap-2 mb-4">
                  <div className="w-2.5 h-2.5 rounded-full" style={{ background: p.color }} />
                  <span className="text-xs font-semibold tracking-wider uppercase"
                    style={{ fontFamily: "'JetBrains Mono', monospace", opacity: 0.6 }}>
                    {p.phase} · {p.months}
                  </span>
                </div>
                <h3 className="text-base font-medium mb-3" style={{ fontFamily: "'DM Serif Display', serif", color: p.color }}>
                  {p.title}
                </h3>
                <ul className="space-y-2">
                  {p.items.map((item) => (
                    <li key={item} className="text-sm flex items-start gap-2" style={{ opacity: 0.6 }}>
                      <span style={{ color: p.color }}>→</span> {item}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ─── CTA FOOTER ─── */}
      <section className="text-center py-16 px-8" style={{
        background: 'linear-gradient(180deg, var(--paper) 0%, #eeebe4 100%)',
      }}>
        <h2 className="text-2xl md:text-3xl mb-4 mx-auto max-w-md" style={{ fontFamily: "'DM Serif Display', serif" }}>
          Sell Outcomes, Not Hours
        </h2>
        <p className="max-w-md mx-auto mb-8 text-sm leading-relaxed" style={{ color: 'var(--muted)' }}>
          Enablement first. Execution when you need it. T&M flexibility with milestone accountability.
        </p>
        <div className="flex justify-center gap-3 text-xs font-semibold tracking-wider uppercase"
          style={{ fontFamily: "'JetBrains Mono', monospace", color: 'var(--accent)' }}>
          <span>T&M</span>
          <span style={{ opacity: 0.3 }}>·</span>
          <span>Milestone Invoicing</span>
          <span style={{ opacity: 0.3 }}>·</span>
          <span>Optional CLINs</span>
        </div>
      </section>
    </div>
  );
}
