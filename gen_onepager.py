#!/usr/bin/env python3
"""
MigrateIQ — One-Pager PDF Generator
Usage:
    python gen_onepager.py                          # defaults to microstrategy
    python gen_onepager.py --platform cognos         # IBM Cognos version
    python gen_onepager.py --platform bobj            # SAP BusinessObjects version
    python gen_onepager.py --platform obiee           # Oracle OBIEE version
    python gen_onepager.py --platform all             # generates all four
"""

import argparse
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

PLATFORMS = {
    "microstrategy": {
        "legacy": "MicroStrategy", "legacyFull": "MicroStrategy Analytics",
        "assets": "dashboards", "asset": "dashboard", "portfolio": "3,000",
        "reason": "platform disinvestment and license cost reduction",
        "complex": "dossiers, Visual Insight dashboards, distribution services, Intelligent Cube dependencies",
        "targets": "Tableau, Qlik Sense, Power BI/Fabric",
        "targetTags": ["Tableau", "Qlik Sense", "Power BI/Fabric"],
    },
    "cognos": {
        "legacy": "Cognos", "legacyFull": "IBM Cognos Analytics",
        "assets": "reports", "asset": "report", "portfolio": "2,500",
        "reason": "IBM license consolidation and platform modernization",
        "complex": "Framework Manager models, Report Studio burst reports, Analysis Studio cubes, TM1 integrations",
        "targets": "Tableau, Power BI/Fabric, Qlik Sense",
        "targetTags": ["Tableau", "Power BI/Fabric", "Qlik Sense"],
    },
    "bobj": {
        "legacy": "BusinessObjects", "legacyFull": "SAP BusinessObjects BI",
        "assets": "reports", "asset": "report", "portfolio": "4,000",
        "reason": "SAP BI platform sunset and enterprise modernization",
        "complex": "Web Intelligence documents, Crystal Reports, universe semantic layers, scheduled publication jobs",
        "targets": "Power BI/Fabric, Tableau, Qlik Sense",
        "targetTags": ["Power BI/Fabric", "Tableau", "Qlik Sense"],
    },
    "obiee": {
        "legacy": "OBIEE", "legacyFull": "Oracle BI Enterprise Edition",
        "assets": "analyses", "asset": "analysis", "portfolio": "1,800",
        "reason": "Oracle license rationalization and cloud migration",
        "complex": "RPD metadata models, BI Publisher templates, Essbase cube dependencies, Data Visualization projects",
        "targets": "Power BI/Fabric, Tableau, Qlik Sense",
        "targetTags": ["Power BI/Fabric", "Tableau", "Qlik Sense"],
    },
}

INK = HexColor('#1a1a2e'); ACCENT = HexColor('#2d5a7b'); ACCENT_LIGHT = HexColor('#3a7ca5')
HIGHLIGHT = HexColor('#d4a843'); MUTED = HexColor('#6b7280'); PAPER = HexColor('#f7f5f0')
BORDER = HexColor('#d1cdc4'); WHITE = HexColor('#ffffff'); SUCCESS = HexColor('#2d6a4f')
OPTIONAL = HexColor('#7c3aed'); ALT_ROW = HexColor('#f0ede8')

def draw(filename, p):
    c = canvas.Canvas(filename, pagesize=letter)
    w, h = letter
    Assets = p["assets"].capitalize(); Asset = p["asset"].capitalize()

    c.setFillColor(PAPER); c.rect(0,0,w,h,fill=1,stroke=0)
    # Top bar
    c.setFillColor(INK); c.rect(0,h-110,w,110,fill=1,stroke=0)
    c.setFillColor(HIGHLIGHT); c.rect(0,h-113,w,3,fill=1,stroke=0)
    c.setFillColor(HIGHLIGHT); c.circle(52,h-35,3,fill=1,stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold",7); c.drawString(60,h-39,"MIGRATEIQ  \u00b7  STRATEGIC CAPABILITY BRIEF")
    c.setFont("Helvetica-Bold",21); c.drawString(40,h-70,"Migrate Smarter, Not Harder")
    c.setFillColor(HIGHLIGHT); c.setFont("Helvetica-Oblique",12)
    c.drawString(40,h-88,f"{p['legacyFull']} \u2192 {p['targets']}")

    # Stats bar
    sy = h-140
    c.setFillColor(WHITE); c.rect(40,sy,w-80,28,fill=1,stroke=0)
    c.setStrokeColor(BORDER); c.setLineWidth(0.5); c.rect(40,sy,w-80,28,fill=0,stroke=1)
    stats = [(p["portfolio"],f"{Assets} Portfolio"),("40\u201360%","Cost Reduction"),("3 Platforms","One Team"),("7 Milestones","Payment Gates")]
    sw = (w-80)/4
    for i,(val,lab) in enumerate(stats):
        x = 40+i*sw+sw/2
        c.setFillColor(ACCENT); c.setFont("Helvetica-Bold",10); c.drawCentredString(x,sy+14,val)
        c.setFillColor(MUTED); c.setFont("Helvetica",5.5); c.drawCentredString(x,sy+4,lab.upper())
        if i<3: c.setStrokeColor(BORDER); c.line(40+(i+1)*sw,sy+4,40+(i+1)*sw,sy+22)

    col_y=sy-20; cl=40; cr=w/2+10; cw=w/2-50

    # LEFT: Milestones
    c.setFillColor(HIGHLIGHT); c.setFont("Helvetica-Bold",6.5); c.drawString(cl,col_y,"MILESTONE PAYMENT SCHEDULE")
    ms=[("M1","Mo 2","CoP Infrastructure Established","Portal, governance charter, community cadence"),
        ("M2","Mo 3","AoA Evaluation Delivered","Platform comparison, TCO analysis, briefing"),
        ("M3","Mo 4","Portfolio Assessment & Roadmap",f"{p['legacy']} inventory classified, roadmap approved"),
        ("M4","Mo 6","CoP Adoption Threshold","\u226530 members, \u226575% attendance, first showcase"),
        ("M5","Mo 9","Pilot Migration Complete",f"\u2265150 {p['assets']} accepted, self-service \u226540%"),
        ("M6","Mo 14","Full-Scale Migration Checkpoint","\u226575% portfolio migrated, complex complete"),
        ("M7","Mo 18","Decommission & Transition","100% resolved, CoP agency-sustained")]
    ty=col_y-14
    c.setFillColor(INK); c.rect(cl,ty,cw,13,fill=1,stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold",5)
    c.drawString(cl+4,ty+4,"ID"); c.drawString(cl+24,ty+4,"TIMING"); c.drawString(cl+62,ty+4,"MILESTONE"); c.drawString(cl+170,ty+4,"KEY DELIVERABLES")
    ty-=2; pc={"M1":ACCENT,"M2":ACCENT,"M3":ACCENT,"M4":ACCENT_LIGHT,"M5":ACCENT_LIGHT,"M6":HIGHLIGHT,"M7":HIGHLIGHT}
    for i,(mid,timing,title,desc) in enumerate(ms):
        ty-=15
        if i%2==0: c.setFillColor(ALT_ROW); c.rect(cl,ty-2,cw,15,fill=1,stroke=0)
        c.setFillColor(pc[mid]); c.circle(cl+7,ty+4,3,fill=1,stroke=0)
        c.setFillColor(HIGHLIGHT); c.setFont("Courier-Bold",6.5); c.drawString(cl+14,ty+1,mid)
        c.setFillColor(MUTED); c.setFont("Courier",5.5); c.drawString(cl+30,ty+1,timing)
        c.setFillColor(INK); c.setFont("Helvetica-Bold",6.5); c.drawString(cl+62,ty+1,title)
        c.setFillColor(MUTED); c.setFont("Helvetica",5.5); c.drawString(cl+170,ty+1,desc)

    # Phase legend
    ty-=18; px=cl
    for lab,color,mo in [("Phase 1",ACCENT,"Mo 1\u20134"),("Phase 2",ACCENT_LIGHT,"Mo 5\u20139"),("Phase 3",HIGHLIGHT,"Mo 10+")]:
        c.setFillColor(color); c.circle(px+3,ty+3,3,fill=1,stroke=0)
        c.setFillColor(INK); c.setFont("Helvetica-Bold",5.5); c.drawString(px+10,ty,lab)
        c.setFillColor(MUTED); c.setFont("Helvetica",5.5); c.drawString(px+42,ty,mo); px+=78

    # Staffing mini-Gantt
    ty-=20; c.setFillColor(HIGHLIGHT); c.setFont("Helvetica-Bold",6.5); c.drawString(cl,ty,"STAFFING TIMELINE")
    gy=ty-12; gl=cl+120; gw=cw-120; mw=gw/18
    c.setFillColor(INK); c.rect(cl,gy,cw,10,fill=1,stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold",4.5); c.drawString(cl+4,gy+3,"LABOR CATEGORY")
    c.setFont("Courier",4)
    for m in range(1,19): c.drawCentredString(gl+(m-1)*mw+mw/2,gy+3,str(m))
    gy-=5
    c.setFillColor(ACCENT); c.rect(gl,gy,mw*4,4,fill=1,stroke=0)
    c.setFillColor(ACCENT_LIGHT); c.rect(gl+mw*4,gy,mw*5,4,fill=1,stroke=0)
    c.setFillColor(HIGHLIGHT); c.rect(gl+mw*9,gy,mw*9,4,fill=1,stroke=0)
    gy-=3; bc={"base":ACCENT,"scale":HIGHLIGHT,"opt":OPTIONAL}
    for role,s,e,bt,note in [("Solutions Architect",1,18,"base","Fractional"),("Community Manager",1,16,"base","1 FTE"),
        ("Migration Architect",1,12,"base","1 FTE\u2192taper"),("Viz Champions (1\u21923)",1,18,"scale","1\u21922\u21923"),
        ("Training Specialist",3,18,"base","1 FTE"),("Sr. BI Developer",8,18,"opt","CLIN 1002"),("Data Gov Analyst",10,18,"opt","CLIN 1003")]:
        gy-=10; c.setFillColor(INK); c.setFont("Helvetica",5.5); c.drawString(cl+4,gy+2,role)
        bx=gl+(s-1)*mw; bw2=(e-s+1)*mw; c.setFillColor(bc[bt]); c.rect(bx,gy,bw2,7,fill=1,stroke=0)
        c.setFillColor(WHITE); c.setFont("Courier",3.5); c.drawString(bx+2,gy+2,note)
    gy-=10; c.setFillColor(MUTED); c.setFont("Helvetica",5); c.drawString(cl+4,gy+2,"Payment Gates")
    for mid2,mo2 in [("M1",2),("M2",3),("M3",4),("M4",6),("M5",9),("M6",14),("M7",18)]:
        mx=gl+(mo2-1)*mw+mw/2; c.setFillColor(HIGHLIGHT)
        c.saveState(); c.translate(mx,gy+3); c.rotate(45); c.rect(-2.5,-2.5,5,5,fill=1,stroke=0); c.restoreState()
        c.setFont("Courier-Bold",3.5); c.drawCentredString(mx,gy-4,mid2)

    # Note
    gy-=14; c.setFillColor(HIGHLIGHT); c.rect(cl,gy-18,2,18,fill=1,stroke=0)
    ns=ParagraphStyle('n',fontName='Helvetica',fontSize=6.5,leading=9,textColor=INK)
    np=Paragraph(f"<b>Outcome-Based Invoicing:</b> T&amp;M flexibility + milestone accountability. Reusable across any agency facing {p['reason']}.",ns)
    npw,nph=np.wrap(cw-10,100); np.drawOn(c,cl+8,gy-nph)

    # CLIN table
    cy2=gy-nph-14; c.setFillColor(ACCENT); c.setFont("Helvetica-Bold",6.5); c.drawString(cl,cy2,"CLIN STRUCTURE")
    clins=[("0001","Base","CoP Enablement & Mgmt","M1, M4",SUCCESS),("0002","Base","AoA & Migration Arch","M2, M3",SUCCESS),
        ("0003","Base","Training & Enablement","M3, M5",SUCCESS),("1001","Opt","Viz Dev \u2014 Standard","M5, M6",OPTIONAL),
        ("1002","Opt","Viz Dev \u2014 Advanced","M6, M7",OPTIONAL),("1003","Opt","Data Governance","M7",OPTIONAL)]
    cy2-=12; c.setFillColor(INK); c.rect(cl,cy2,cw,12,fill=1,stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold",5)
    c.drawString(cl+4,cy2+3,"CLIN"); c.drawString(cl+35,cy2+3,"TYPE"); c.drawString(cl+65,cy2+3,"DESCRIPTION")
    c.drawString(cl+195,cy2+3,"GATES"); c.drawString(cl+cw-42,cy2+3,"STRUCTURE")
    cy2-=1
    for i,(cid,ct,desc,gates,bc2) in enumerate(clins):
        cy2-=13
        if i%2==0: c.setFillColor(ALT_ROW); c.rect(cl,cy2-1,cw,13,fill=1,stroke=0)
        c.setFillColor(INK); c.setFont("Courier-Bold",6.5); c.drawString(cl+4,cy2+2,cid)
        c.setFillColor(bc2); c.setFont("Helvetica-Bold",5.5); c.drawString(cl+35,cy2+2,ct.upper())
        c.setFillColor(INK); c.setFont("Helvetica",6.5); c.drawString(cl+65,cy2+2,desc)
        c.setFillColor(HIGHLIGHT); c.setFont("Courier-Bold",5.5); c.drawString(cl+195,cy2+2,gates)
        c.setFillColor(MUTED); c.setFont("Courier",5); c.drawString(cl+cw-42,cy2+2,"T&M" if ct=="Base" else "T&M+Ceil")

    # RIGHT COLUMN
    c.setFillColor(ACCENT); c.setFont("Helvetica-Bold",6.5); c.drawString(cr,col_y,"THE TEAM")
    ry=col_y-14
    for role,labor,fte in [("Solutions Architect","Sr. Data Analytics Architect","Fractional"),("Community Manager","Knowledge Mgmt Specialist","1 FTE"),
        ("Visualization Champions","BI Developer / Data Viz Eng","2\u20133 FTE"),("Migration Architect","Sr. Enterprise BI Architect","1 FTE"),("Training Specialist","Technical Training Developer","1 FTE")]:
        c.setFillColor(INK); c.setFont("Helvetica-Bold",7); c.drawString(cr,ry,role)
        c.setFillColor(MUTED); c.setFont("Courier",5.5); c.drawString(cr+140,ry+1,labor)
        c.setFillColor(ACCENT); c.setFont("Helvetica-Bold",5.5); c.drawString(cr+cw-c.stringWidth(fte,"Helvetica-Bold",5.5),ry+1,fte); ry-=14

    ry-=10; c.setFillColor(ACCENT); c.setFont("Helvetica-Bold",6.5); c.drawString(cr,ry,"PHASED APPROACH"); ry-=4
    for num,months,title,desc,color in [("Phase 1","Mo 1\u20134","AoA Support & CoP Standup",f"Platform evaluation, {p['legacy']} assessment, CoP infrastructure.",ACCENT),
        ("Phase 2","Mo 5\u20139","Pilot Migration & Enablement","Office hours, showcases, paired development.",ACCENT_LIGHT),
        ("Phase 3","Mo 10+","Scaled Migration & Execution","Optional CLINs activate. Self-sufficient + contractor-led.",HIGHLIGHT)]:
        ry-=12; c.setFillColor(color); c.circle(cr+4,ry+3,3.5,fill=1,stroke=0)
        c.setFillColor(MUTED); c.setFont("Courier",5.5); c.drawString(cr+14,ry+4,f"{num}  \u00b7  {months}")
        c.setFillColor(INK); c.setFont("Helvetica-Bold",7.5); c.drawString(cr+14,ry-7,title)
        ds=ParagraphStyle('d',fontName='Helvetica',fontSize=6.5,leading=8.5,textColor=MUTED)
        dp=Paragraph(desc,ds); dpw,dph=dp.wrap(cw-18,100); dp.drawOn(c,cr+14,ry-10-dph); ry-=10+dph+6

    ry-=8; c.setFillColor(ACCENT); c.setFont("Helvetica-Bold",6.5); c.drawString(cr,ry,"SUCCESS METRICS"); my=ry-13
    for mt,md in [("CoP Participation","Members, office hours, KB articles"),("Self-Service Ratio","Agency-led vs. contractor-led"),
        (f"Cost per {Asset}","Benchmarked vs. traditional migration"),("Decommission Timeline",f"Tracking to full {p['legacy']} exit")]:
        c.setFillColor(INK); c.setFont("Helvetica-Bold",7); c.drawString(cr,my,mt)
        c.setFillColor(MUTED); c.setFont("Helvetica",6); c.drawString(cr,my-9,md); my-=22

    my-=4; c.setFillColor(HIGHLIGHT); c.setFont("Helvetica-Bold",6.5); c.drawString(cr,my,"WHY MIGRATEIQ"); dy=my-13
    for dt,dd in [("Tri-Platform Fluency",f"{p['targets']} \u2014 no vendor bias."),("CoP Model is Proven","Peers teach peers; self-sustaining."),
        ("Built-In Demand Signal","Optional CLINs on evidence, not guesswork."),("Zero Lock-In","All deliverables transfer to the agency.")]:
        c.setFillColor(HIGHLIGHT); c.setFont("Helvetica-Bold",7); c.drawString(cr,dy,dt)
        c.setFillColor(MUTED); c.setFont("Helvetica",6); c.drawString(cr,dy-9,dd); dy-=22

    # Footer
    c.setFillColor(INK); c.rect(0,0,w,32,fill=1,stroke=0); c.setFillColor(HIGHLIGHT); c.rect(0,32,w,2,fill=1,stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica",6.5); c.drawString(40,12,"MigrateIQ  \u00b7  Sell Outcomes, Not Hours.  \u00b7  Enablement First. Execution When You Need It.")
    c.setFillColor(HexColor('#ffffff60')); c.setFont("Courier",5.5)
    c.drawString(w-260,12,f"{p['legacy']} (Legacy)  \u00b7  "+"  \u00b7  ".join(p["targetTags"]))
    c.save(); print(f"\u2713 {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate MigrateIQ one-pager PDF")
    parser.add_argument("--platform",default="microstrategy",choices=list(PLATFORMS.keys())+["all"])
    args = parser.parse_args()
    if args.platform == "all":
        for key,preset in PLATFORMS.items(): draw(f"/home/claude/migrateiq-onepager-{key}.pdf",preset)
    else:
        draw(f"/home/claude/migrateiq-onepager-{args.platform}.pdf",PLATFORMS[args.platform])
