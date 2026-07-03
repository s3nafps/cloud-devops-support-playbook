from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "artifacts"
OUTPUT_PDF = OUTPUT_DIR / "Mohamed_Senator_Service_Menu_2026.pdf"


PACKAGES = [
    {
        "name": "VPS Docker Rescue Audit",
        "price": "USD 79",
        "delivery": "24-48 hours",
        "best_for": "Founders or small teams with a broken Docker app on one VPS.",
        "includes": "Logs, ports, disk, memory, DNS/HTTPS symptoms, one safe fix, incident report, next steps.",
    },
    {
        "name": "Backup and Restore Safety Net",
        "price": "USD 149",
        "delivery": "2-3 days",
        "best_for": "Working VPS apps with no tested backup or restore proof.",
        "includes": "Backup workflow, checksum, safe restore test, cron example, recovery runbook.",
    },
    {
        "name": "Monitoring and Handover Setup",
        "price": "USD 199",
        "delivery": "2-4 days",
        "best_for": "Teams that only discover downtime from customers.",
        "includes": "Uptime Kuma or endpoint checks, first-response runbook, alert test, handover notes.",
    },
]


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleMenu",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=21,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#111827"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubTitleMenu",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#b45309"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCenter",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#374151"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionText",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.1,
            textColor=colors.HexColor("#111827"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallText",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.4,
            leading=10.4,
            textColor=colors.HexColor("#374151"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="FooterText",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=10.2,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4b5563"),
        )
    )
    return styles


def package_table(styles):
    rows = [
        [
            Paragraph("<b>Package</b>", styles["SectionText"]),
            Paragraph("<b>Price</b>", styles["SectionText"]),
            Paragraph("<b>Delivery</b>", styles["SectionText"]),
            Paragraph("<b>Best fit</b>", styles["SectionText"]),
            Paragraph("<b>What is included</b>", styles["SectionText"]),
        ]
    ]
    for item in PACKAGES:
        rows.append(
            [
                Paragraph(f"<b>{item['name']}</b>", styles["SectionText"]),
                Paragraph(item["price"], styles["SectionText"]),
                Paragraph(item["delivery"], styles["SectionText"]),
                Paragraph(item["best_for"], styles["SmallText"]),
                Paragraph(item["includes"], styles["SmallText"]),
            ]
        )

    table = Table(
        rows,
        colWidths=[38 * mm, 20 * mm, 24 * mm, 44 * mm, 54 * mm],
        repeatRows=1,
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#fff7ed")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#9a3412")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("LINEBELOW", (0, 0), (-1, 0), 0.8, colors.HexColor("#fdba74")),
                ("GRID", (0, 1), (-1, -1), 0.35, colors.HexColor("#d1d5db")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
            ]
        )
    )
    return table


def build_pdf():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        leftMargin=11 * mm,
        rightMargin=11 * mm,
        title="Mohamed Senator Service Menu",
        author="Mohamed Senator",
    )

    story = [
        Paragraph("Mohamed Senator", styles["TitleMenu"]),
        Paragraph("Cloud / DevOps Support Service Menu", styles["SubTitleMenu"]),
        Paragraph(
            "Fixed-scope VPS and Docker support for founders and small teams. "
            "Focused on practical operations work, clear handover notes, and low-cost tooling.",
            styles["BodyCenter"],
        ),
        Spacer(1, 4 * mm),
        package_table(styles),
        Spacer(1, 5 * mm),
        Paragraph(
            "<b>Operating rules:</b> No passwords or private keys in chat. "
            "No open-ended retainers before a successful fixed-scope delivery. "
            "Every job should leave evidence: screenshots, notes, runbooks, or restore proof.",
            styles["SectionText"],
        ),
        Spacer(1, 3 * mm),
        Paragraph(
            "Public proof: github.com/s3nafps/cloudops-rescue-kit | "
            "Career playbook: github.com/s3nafps/cloud-devops-support-playbook | "
            "Portfolio: mohamedsenator.vercel.app",
            styles["FooterText"],
        ),
    ]

    doc.build(story)
    print(f"Wrote {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()
