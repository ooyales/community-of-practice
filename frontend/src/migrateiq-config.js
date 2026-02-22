// ═══════════════════════════════════════════════════════════════
//  MigrateIQ — ES Module Config for React
//  Keep in sync with public/migrateiq-config.js
// ═══════════════════════════════════════════════════════════════

export const PLATFORM_PRESETS = {
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
    targetTags: ["Tableau", "Qlik Sense", "Power BI / Fabric"],
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
    targetTags: ["Tableau", "Power BI / Fabric", "Qlik Sense"],
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
    targetTags: ["Power BI / Fabric", "Tableau", "Qlik Sense"],
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
    targetTags: ["Power BI / Fabric", "Tableau", "Qlik Sense"],
  },
};

export const ACTIVE_PLATFORM = "microstrategy";
export const P = PLATFORM_PRESETS[ACTIVE_PLATFORM];
