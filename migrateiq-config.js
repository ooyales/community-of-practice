// ═══════════════════════════════════════════════════════════════
//  MigrateIQ — Shared Platform Configuration
//  
//  Change the active preset below to generate all materials
//  for a different legacy platform. All HTML files that include
//  this script will adapt automatically on page load.
//
//  USAGE: Uncomment ONE preset block, save, refresh any material.
// ═══════════════════════════════════════════════════════════════

const PLATFORM_PRESETS = {

  microstrategy: {
    legacy: "MicroStrategy",
    legacyFull: "MicroStrategy Analytics",
    legacyShort: "MicroStrategy",
    reason: "platform disinvestment and license cost reduction",
    portfolio: "3,000",
    assets: "dashboards",
    asset: "dashboard",
    complex: "MicroStrategy dossiers, Visual Insight dashboards, distribution services, and Intelligent Cube dependencies",
    targets: "Tableau, Qlik Sense, Power BI/Fabric",
    agency: "federal agencies",
  },

  cognos: {
    legacy: "Cognos",
    legacyFull: "IBM Cognos Analytics",
    legacyShort: "Cognos",
    reason: "IBM license consolidation and platform modernization",
    portfolio: "2,500",
    assets: "reports",
    asset: "report",
    complex: "Cognos Framework Manager models, Report Studio burst reports, Analysis Studio cubes, and TM1 integrations",
    targets: "Tableau, Power BI/Fabric, Qlik Sense",
    agency: "federal agencies",
  },

  bobj: {
    legacy: "BusinessObjects",
    legacyFull: "SAP BusinessObjects BI",
    legacyShort: "BOBJ",
    reason: "SAP BI platform sunset and enterprise modernization",
    portfolio: "4,000",
    assets: "reports",
    asset: "report",
    complex: "Web Intelligence documents, Crystal Reports, universe semantic layers, and scheduled publication jobs",
    targets: "Power BI/Fabric, Tableau, Qlik Sense",
    agency: "federal agencies and defense organizations",
  },

  obiee: {
    legacy: "OBIEE",
    legacyFull: "Oracle BI Enterprise Edition",
    legacyShort: "OBIEE",
    reason: "Oracle license rationalization and cloud migration",
    portfolio: "1,800",
    assets: "analyses",
    asset: "analysis",
    complex: "OBIEE RPD metadata models, BI Publisher templates, Essbase cube dependencies, and Oracle Data Visualization projects",
    targets: "Power BI/Fabric, Tableau, Qlik Sense",
    agency: "federal agencies",
  },

};

// ═══════════ ACTIVE PRESET ═══════════
// Change this line to switch platforms across ALL materials:
const ACTIVE_PLATFORM = "microstrategy";
// ═══════════════════════════════════════

const P = PLATFORM_PRESETS[ACTIVE_PLATFORM];

// Template rendering utility — call after DOM is ready
function migrateIQ_renderTemplates() {
  document.querySelectorAll('[data-tpl]').forEach(el => {
    const template = el.getAttribute('data-tpl');
    el.innerHTML = template
      .replace(/\{legacy\}/g, P.legacy)
      .replace(/\{legacyFull\}/g, P.legacyFull)
      .replace(/\{legacyShort\}/g, P.legacyShort)
      .replace(/\{reason\}/g, P.reason)
      .replace(/\{portfolio\}/g, P.portfolio)
      .replace(/\{assets\}/g, P.assets)
      .replace(/\{asset\}/g, P.asset)
      .replace(/\{complex\}/g, P.complex)
      .replace(/\{targets\}/g, P.targets)
      .replace(/\{agency\}/g, P.agency);
  });
  // Also update <title>
  if (document.title.includes('{legacy}') || document.title.includes('MicroStrategy')) {
    document.title = document.title.replace(/MicroStrategy|Cognos|BusinessObjects|OBIEE|\{legacy\}/g, P.legacy);
  }
}
