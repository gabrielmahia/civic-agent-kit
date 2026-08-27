"""
civic-agent-kit MCP server — Kenya civic data as AI agent tools

Tools:
  kenya_county_drought    — NDMA drought phase for any county
  kenya_budget_summary    — County budget allocation and spending data
  kenya_parliament_bills  — Bills and motions from Kenya Parliament
  kenya_sacco_lookup      — SACCO registry and financial data
  kenya_rights_query      — Constitutional rights Q&A (English/Swahili)
  kenya_counties_list     — All 47 Kenya counties with metadata
"""
from __future__ import annotations

from typing import Annotated

from fastmcp import FastMCP

mcp = FastMCP(
    name="civic-agent-kit",
    instructions=(
        "Kenya civic data tools. Access county drought data, budget allocations, "
        "parliament bills, SACCO registry, and constitutional rights. "
        "All tools support English and Kiswahili output."
    ),
)

# ── Embedded data — no file dependencies ─────────────────────────────────────

DROUGHT_DATA = {
    "Turkana": {"phase": 4, "label": "Emergency", "population_affected": 580000},
    "Marsabit": {"phase": 4, "label": "Emergency", "population_affected": 320000},
    "Mandera": {"phase": 4, "label": "Emergency", "population_affected": 490000},
    "Wajir": {"phase": 4, "label": "Emergency", "population_affected": 410000},
    "Garissa": {"phase": 3, "label": "Crisis", "population_affected": 270000},
    "Isiolo": {"phase": 3, "label": "Crisis", "population_affected": 120000},
    "Tana River": {"phase": 3, "label": "Crisis", "population_affected": 180000},
    "Samburu": {"phase": 3, "label": "Crisis", "population_affected": 150000},
    "Kajiado": {"phase": 2, "label": "Stressed", "population_affected": 95000},
    "Laikipia": {"phase": 2, "label": "Stressed", "population_affected": 80000},
    "Baringo": {"phase": 2, "label": "Stressed", "population_affected": 110000},
    "Nairobi": {"phase": 1, "label": "Minimal", "population_affected": 0},
    "Kiambu": {"phase": 1, "label": "Minimal", "population_affected": 0},
    "Mombasa": {"phase": 1, "label": "Minimal", "population_affected": 0},
    "Kisumu": {"phase": 1, "label": "Minimal", "population_affected": 0},
    "Nakuru": {"phase": 1, "label": "Minimal", "population_affected": 0},
}
PHASE_LABELS = {1: "Minimal", 2: "Stressed", 3: "Crisis", 4: "Emergency", 5: "Famine"}

BUDGET_DATA = {
    "Nairobi":  {"fy": "2022/23", "allocation_kes_b": 37.2, "development_pct": 28.1, "recurrent_pct": 71.9, "absorption_rate_pct": 89.2},
    "Kiambu":   {"fy": "2022/23", "allocation_kes_b": 9.8,  "development_pct": 31.4, "recurrent_pct": 68.6, "absorption_rate_pct": 92.1},
    "Mombasa":  {"fy": "2022/23", "allocation_kes_b": 6.1,  "development_pct": 24.8, "recurrent_pct": 75.2, "absorption_rate_pct": 78.3},
    "Kisumu":   {"fy": "2022/23", "allocation_kes_b": 4.9,  "development_pct": 29.3, "recurrent_pct": 70.7, "absorption_rate_pct": 83.6},
    "Nakuru":   {"fy": "2022/23", "allocation_kes_b": 8.4,  "development_pct": 30.1, "recurrent_pct": 69.9, "absorption_rate_pct": 87.5},
    "Mandera":  {"fy": "2022/23", "allocation_kes_b": 3.1,  "development_pct": 38.2, "recurrent_pct": 61.8, "absorption_rate_pct": 61.4},
    "Turkana":  {"fy": "2022/23", "allocation_kes_b": 4.2,  "development_pct": 41.3, "recurrent_pct": 58.7, "absorption_rate_pct": 59.8},
}

PARLIAMENT_BILLS = [
    {"id": "B001/2024", "title": "Affordable Housing Act 2024", "status": "Assented", "type": "Government", "date": "2024-03-19", "summary": "Establishes housing levy and affordable housing fund for low-income Kenyans"},
    {"id": "B012/2024", "title": "Digital Markets Act 2024",   "status": "Second Reading", "type": "Government", "date": "2024-08-14", "summary": "Regulation of digital platforms and e-commerce in Kenya"},
    {"id": "B007/2024", "title": "Water Amendment Act 2024",   "status": "Committee Stage", "type": "Government", "date": "2024-06-05", "summary": "Amendments to Water Act 2016 on borehole licensing and WRUA"},
    {"id": "B022/2023", "title": "Data Protection Amendment Bill 2023", "status": "Assented", "type": "Government", "date": "2023-09-30", "summary": "Updates to Kenya Data Protection Act 2019 on cross-border data flows"},
    {"id": "B031/2024", "title": "AI and Emerging Technologies Bill 2024", "status": "First Reading", "type": "Government", "date": "2024-10-01", "summary": "Regulatory framework for artificial intelligence in Kenya"},
]

SACCO_DATA = [
    {"name": "Stima SACCO",      "type": "Deposit-Taking", "members": 112000, "assets_kes_b": 42.1, "county": "Nairobi",  "focus": "Energy sector workers"},
    {"name": "Mwalimu SACCO",    "type": "Deposit-Taking", "members": 92000,  "assets_kes_b": 38.6, "county": "Nairobi",  "focus": "Teachers"},
    {"name": "Kenya Police SACCO","type": "Deposit-Taking", "members": 78000, "assets_kes_b": 31.2, "county": "Nairobi",  "focus": "Police service"},
    {"name": "Unaitas SACCO",    "type": "Deposit-Taking", "members": 65000,  "assets_kes_b": 22.4, "county": "Murang\'a", "focus": "Central region"},
    {"name": "Imarisha SACCO",   "type": "Deposit-Taking", "members": 48000,  "assets_kes_b": 18.9, "county": "Mombasa",  "focus": "Coast region"},
]

RIGHTS_DB = {
    ("land", "en"):      "Article 40: Every person has the right to acquire and own property. The State shall not deprive a person of property unless justified and full compensation paid promptly.",
    ("ardhi", "sw"):     "Kifungu 40: Kila mtu ana haki ya kupata na kumiliki mali. Serikali haiwezi kunyakua mali bila sababu na kulipa fidia kamili haraka.",
    ("water", "en"):     "Article 43(d): Every person has the right to clean and safe water in adequate quantities.",
    ("maji", "sw"):      "Kifungu 43(d): Kila mtu ana haki ya maji safi na salama kwa wingi wa kutosha.",
    ("health", "en"):    "Article 43(a): Every person has the right to the highest attainable standard of health, including reproductive health care.",
    ("afya", "sw"):      "Kifungu 43(a): Kila mtu ana haki ya kiwango cha juu zaidi cha afya kinachoweza kufikiwa, ikiwemo huduma za afya ya uzazi.",
    ("education", "en"): "Article 43(f): Every person has the right to education. Article 53: Every child has the right to free and compulsory basic education.",
    ("elimu", "sw"):     "Kifungu 43(f): Kila mtu ana haki ya elimu. Kifungu 53: Kila mtoto ana haki ya elimu ya msingi bure na ya lazima.",
    ("labour", "en"):    "Article 41: Every person has the right to fair labour practices and to form, join, or participate in trade union activities.",
    ("kazi", "sw"):      "Kifungu 41: Kila mtu ana haki ya mazoea ya haki ya kazi na kuunda, kujiunga, au kushiriki katika shughuli za muungano wa wafanyakazi.",
    ("housing", "en"):   "Article 43(b): Every person has the right to accessible and adequate housing.",
    ("nyumba", "sw"):    "Kifungu 43(b): Kila mtu ana haki ya nyumba inayopatikana na ya kutosha.",
    ("food", "en"):      "Article 43(c): Every person has the right to be free from hunger and to have adequate food of acceptable quality.",
    ("chakula", "sw"):   "Kifungu 43(c): Kila mtu ana haki ya kuepuka njaa na kupata chakula cha kutosha cha ubora unaokubalika.",
}

KENYA_COUNTIES = [
    "Baringo","Bomet","Bungoma","Busia","Elgeyo-Marakwet","Embu","Garissa","Homa Bay",
    "Isiolo","Kajiado","Kakamega","Kericho","Kiambu","Kilifi","Kirinyaga","Kisii","Kisumu",
    "Kitui","Kwale","Laikipia","Lamu","Machakos","Makueni","Mandera","Marsabit","Meru",
    "Migori","Mombasa","Murang\'a","Nairobi","Nakuru","Nandi","Narok","Nyamira","Nyandarua",
    "Nyeri","Samburu","Siaya","Taita-Taveta","Tana River","Tharaka-Nithi","Trans Nzoia",
    "Turkana","Uasin Gishu","Vihiga","Wajir","West Pokot"
]


# ── Tools ─────────────────────────────────────────────────────────────────────

@mcp.tool(annotations={"title": "Kenya County Drought Status", "readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
def kenya_county_drought(
    county: Annotated[str, "Kenya county name e.g. Turkana, Garissa, Nairobi"],
    language: Annotated[str, "Response language: en (English) or sw (Swahili)"] = "en",
) -> dict:
    """
    Get current NDMA drought phase for any of Kenya\'s 47 counties.
    Phase 1=Minimal, 2=Stressed, 3=Crisis, 4=Emergency, 5=Famine.
    Data source: Kenya National Drought Management Authority (NDMA).
    DEMO data — for real-time data see ndma.go.ke.
    """
    county_title = county.strip().title()
    data = DROUGHT_DATA.get(county_title)
    if not data:
        # Default for counties not in our sample
        data = {"phase": 1, "label": "Minimal", "population_affected": 0}

    phase = data["phase"]
    if language == "sw":
        phase_sw = {1: "Kidogo", 2: "Msongo", 3: "Mgawanyiko", 4: "Dharura", 5: "Njaa"}.get(phase, "Haijulikani")
        return {
            "kaunti": county_title, "awamu": phase, "hali": phase_sw,
            "idadi_watu_walioathiriwa": data["population_affected"],
            "chanzo": "DEMO — data ya mfano. Kwa data halisi: ndma.go.ke",
        }
    return {
        "county": county_title, "phase": phase, "status": PHASE_LABELS.get(phase, "Unknown"),
        "population_affected": data["population_affected"],
        "risk": "HIGH" if phase >= 4 else "MEDIUM" if phase >= 2 else "LOW",
        "source": "DEMO — synthetic data for illustration. Real data: ndma.go.ke",
    }


@mcp.tool(annotations={"title": "Kenya County Budget Summary", "readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
def kenya_budget_summary(
    county: Annotated[str, "County name, or ALL for all counties"],
    language: Annotated[str, "en or sw"] = "en",
) -> dict:
    """
    Get county budget allocation, development vs recurrent split, and absorption rate.
    FY 2022/23 data from Kenya Controller of Budget.
    DEMO data — real data: opendata.go.ke and cob.go.ke.
    """
    if county.strip().upper() == "ALL":
        return {
            "counties": list(BUDGET_DATA.keys()),
            "data": BUDGET_DATA,
            "source": "DEMO — FY2022/23 synthetic data. Real data: cob.go.ke",
        }
    county_title = county.strip().title()
    data = BUDGET_DATA.get(county_title)
    if not data:
        return {"error": f"Budget data not available for {county_title}. Available: {list(BUDGET_DATA.keys())}"}
    if language == "sw":
        return {
            "kaunti": county_title, "mwaka": data["fy"],
            "mgao_bilioni_kes": data["allocation_kes_b"],
            "asilimia_maendeleo": data["development_pct"],
            "asilimia_matumizi_ya_kawaida": data["recurrent_pct"],
            "kiwango_cha_matumizi": data["absorption_rate_pct"],
            "chanzo": "DEMO — data ya mfano",
        }
    return {
        "county": county_title,
        "fiscal_year": data["fy"],
        "total_allocation_kes_billion": data["allocation_kes_b"],
        "development_spending_pct": data["development_pct"],
        "recurrent_spending_pct": data["recurrent_pct"],
        "absorption_rate_pct": data["absorption_rate_pct"],
        "analysis": "ABOVE_AVERAGE" if data["absorption_rate_pct"] > 85 else "BELOW_AVERAGE",
        "source": "DEMO — FY2022/23 synthetic. Real: cob.go.ke",
    }


@mcp.tool(annotations={"title": "Kenya Parliament Bills", "readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
def kenya_parliament_bills(
    status: Annotated[str, "Filter: All, Assented, Second Reading, Committee Stage, First Reading"] = "All",
    keyword: Annotated[str, "Search keyword in bill title or summary"] = "",
) -> dict:
    """
    Query Kenya Parliament bills and their legislative status.
    Returns bills with title, status, type, date and summary.
    DEMO data — real data: parliament.go.ke.
    """
    bills = PARLIAMENT_BILLS
    if status.lower() != "all":
        bills = [b for b in bills if b["status"].lower() == status.lower()]
    if keyword:
        kw = keyword.lower()
        bills = [b for b in bills if kw in b["title"].lower() or kw in b["summary"].lower()]
    return {
        "count": len(bills),
        "bills": bills,
        "source": "DEMO — synthetic data. Real: parliament.go.ke/bills",
    }


@mcp.tool(annotations={"title": "Kenya SACCO Lookup", "readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
def kenya_sacco_lookup(
    name: Annotated[str, "SACCO name or partial name to search, or ALL"] = "ALL",
    county: Annotated[str, "Filter by county"] = "",
) -> dict:
    """
    Look up Kenya SACCOs from the SASRA registry.
    Returns name, type, membership, assets, county and focus sector.
    DEMO data — real registry: sasra.go.ke.
    """
    saccos = SACCO_DATA
    if name.upper() != "ALL":
        saccos = [s for s in saccos if name.lower() in s["name"].lower()]
    if county:
        saccos = [s for s in saccos if county.lower() in s["county"].lower()]
    return {
        "count": len(saccos),
        "saccos": saccos,
        "source": "DEMO — sample data. Real registry: sasra.go.ke",
    }


@mcp.tool(annotations={"title": "Kenya Constitutional Rights Q&A", "readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
def kenya_rights_query(
    right: Annotated[str, "Right to query: land/ardhi, water/maji, health/afya, education/elimu, labour/kazi, housing/nyumba, food/chakula"],
    language: Annotated[str, "en (English) or sw (Swahili)"] = "en",
) -> dict:
    """
    Query Kenya constitutional rights from Chapter 4 of the Constitution of Kenya 2010.
    Returns the specific constitutional article and its provisions.
    Works in English and Kiswahili.
    """
    key = (right.lower().strip(), language[:2].lower())
    answer = RIGHTS_DB.get(key)
    # Try other language if not found
    if not answer:
        alt_lang = "sw" if language[:2] == "en" else "en"
        alt_key = (right.lower().strip(), alt_lang)
        answer = RIGHTS_DB.get(alt_key)

    if answer:
        return {"right": right, "language": language, "provision": answer, "source": "Constitution of Kenya 2010"}

    # List available rights
    available = list(set(k for k, _ in RIGHTS_DB))
    return {
        "error": f"Right \'{right}\' not found.",
        "available_rights": available,
        "hint": "Try: land, water, health, education, labour, housing, food (English) or ardhi, maji, afya, elimu, kazi, nyumba, chakula (Swahili)",
    }


@mcp.tool(annotations={"title": "Kenya Counties List", "readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
def kenya_counties_list() -> dict:
    """List all 47 Kenya counties. Returns names suitable for use with other tools."""
    return {"count": len(KENYA_COUNTIES), "counties": KENYA_COUNTIES}


if __name__ == "__main__":
    mcp.run()
