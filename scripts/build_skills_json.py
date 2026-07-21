#!/usr/bin/env python3
"""Build skills.json catalog from plugin folders.

Walks every <plugin>/skills/<skill>/SKILL.md, parses YAML frontmatter, and
emits a top-level skills.json that mirrors the Claude-Skills schema. Used by
scripts/generate_site.py to produce the static site.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT = REPO_ROOT / "skills.json"

# 48 plugin slugs in display order: 23 original + 25 new (grouped per README sections).
DOMAINS_ORDER = [
    # German legal practice (general)
    "arbeitsrecht", "datenschutzrecht", "vertragsrecht", "mietrecht", "wohnungseigentumsrecht",
    "gesellschaftsrecht", "strafrecht", "insolvenzrecht", "prozessrecht",
    "erbrecht", "familienrecht", "betreuungsrecht",
    # Fachanwaltschaften
    "it-recht", "bankrecht", "gewerblicher-rechtsschutz", "steuerrecht", "verwaltungsrecht",
    # EU / cross-cutting compliance
    "ki-vo-compliance", "nis2", "hinweisgeberschutz", "lieferkettengesetz",
    "dora", "dsa-dma", "csrd",
    # Substantive general law (expanded)
    "europarecht", "verfassungsrecht", "sozialrecht", "handelsrecht",
    "medizinrecht", "versicherungsrecht", "baurecht", "verkehrsrecht",
    "urheber-medienrecht", "sportrecht", "migrationsrecht", "agrarrecht",
    # Regulated industries (expanded)
    "vergaberecht", "umweltrecht", "energierecht",
    "aussenwirtschaft-zoll-sanktionen", "geldwaesche-aml-kyc",
    "transportrecht", "produktrecht", "ki-governance",
    # Specialty & IP (expanded)
    "wettbewerbsrecht", "kartellrecht", "kapitalmarktrecht", "patentrecht",
    "berufsrecht-anwaltschaft",
    # Cyber-Resilienz / Produkt-Cybersicherheit
    "cyber-resilience-act",
]

# Human-readable category labels for the site.
DOMAIN_META = {
    "arbeitsrecht": ("Arbeitsrecht", "KSchG, BetrVG, Aufhebungsvertrag, Abmahnung, Sozialauswahl"),
    "datenschutzrecht": ("Datenschutzrecht / GDPR", "DSGVO, BDSG, AVV, Datenpanne, DPIA, Drittlandtransfer"),
    "vertragsrecht": ("Vertragsrecht", "AGB-Kontrolle, Klauselgestaltung, Leistungsstörung, Anfechtung"),
    "mietrecht": ("Mietrecht", "Wohnraummiete, Mieterhöhung, Kündigung, Betriebskostenabrechnung, WEG"),
    "wohnungseigentumsrecht": ("Wohnungseigentumsrecht (WEG)", "Beschlussanfechtung §§ 44/45, Hausgeld/Jahresabrechnung § 28, bauliche Veränderung §§ 20/21 — post-WEMoG"),
    "gesellschaftsrecht": ("Gesellschaftsrecht", "GmbH-Recht, Geschäftsführerhaftung, AG-Grundzüge, Umwandlungen"),
    "strafrecht": ("Strafrecht", "Strafbefehl-Verteidigung, Akteneinsicht, OWi-Verkehr, Belehrungen"),
    "insolvenzrecht": ("Insolvenzrecht", "InsO § 15a, StaRUG, Liquiditätsplanung, Fortbestehensprognose"),
    "prozessrecht": ("Prozessrecht", "Klageschrift §§ 253 ff. ZPO, Beweisantritt, Zuständigkeit, Rechtsmittel"),
    "erbrecht": ("Erbrecht", "Testament, Erbvertrag, Pflichtteil §§ 2303 ff. BGB, Erbschein, Erbschaftsteuer"),
    "familienrecht": ("Familienrecht", "Scheidung, Zugewinnausgleich, Unterhalt, Sorge- und Umgangsrecht"),
    "betreuungsrecht": ("Betreuungsrecht", "Reform 2023 (§§ 1814 ff. BGB), Jahresbericht § 1863, Vermögenssorge"),
    "it-recht": ("IT-Recht", "SaaS-Verträge, Outsourcing, Softwarelizenz, Open Source, Cloud-AVV"),
    "bankrecht": ("Bank- und Kapitalmarktrecht", "Verbraucherdarlehen §§ 491 ff. BGB, MiFID II, Anlageberatung"),
    "gewerblicher-rechtsschutz": ("Gewerblicher Rechtsschutz", "Marken (MarkenG), Designs (DesignG), UWG-Abmahnung"),
    "steuerrecht": ("Steuerrecht", "AO Außenprüfung, Einspruch §§ 347 ff. AO, Selbstanzeige § 371, FGO"),
    "verwaltungsrecht": ("Verwaltungsrecht", "Widerspruch §§ 68 ff. VwGO, Anfechtungs-/Verpflichtungsklage, § 80"),
    "ki-vo-compliance": ("EU KI-VO / AI Act", "VO (EU) 2024/1689 — Hochrisiko Art. 6, Betreiber Art. 26, GPAI"),
    "nis2": ("NIS2", "RL (EU) 2022/2555 / NIS2UmsuCG — Risikomanagement, 24h-Frühwarnung"),
    "hinweisgeberschutz": ("HinSchG", "Interne Meldestelle, Vertraulichkeit, Repressalienverbot, Pflicht ab 50 EE"),
    "lieferkettengesetz": ("LkSG", "Risikoanalyse, Präventionsmaßnahmen, Beschwerde § 8, BAFA-Bericht § 10"),
    "dora": ("DORA", "VO (EU) 2022/2554 — IKT-Risiko, Vorfälle Art. 19, TLPT, Drittparteienrisiko"),
    "dsa-dma": ("DSA / DMA", "VO (EU) 2022/2065 + 2022/1925 — Notice & Action, Statement of Reasons, Gatekeeper"),
    "csrd": ("CSRD / ESRS", "RL (EU) 2022/2464 — doppelte Wesentlichkeitsanalyse, Berichtspflichten 2024–28"),
    "europarecht": ("Europarecht", "AEUV, Art. 267 Vorabentscheidung, Vertragsverletzung Art. 258–260, Richtlinien"),
    "verfassungsrecht": ("Verfassungsrecht", "GG, BVerfGG, Grundrechtsdogmatik, Organstreit Art. 93 GG"),
    "sozialrecht": ("Sozialrecht", "SGB I–XII, Bürgergeld, Renten SGB VI, Widerspruch § 84 SGG"),
    "handelsrecht": ("Handelsrecht", "HGB §§ 1–15, Handelsvertreter §§ 84 ff. + § 89b, §§ 377/378 Rügepflicht"),
    "medizinrecht": ("Medizinrecht", "Arzthaftung §§ 630a–h BGB, MBO-Ä, Akteneinsicht, § 203 StGB"),
    "versicherungsrecht": ("Versicherungsrecht", "VVG Deckungsprüfung 3-stufig, §§ 19–22, 28 ff., Maklerhaftung"),
    "baurecht": ("Baurecht", "BGB Bauvertrag §§ 650a–u, VOB/B, BauGB §§ 29–35, LBO, § 212a BauGB"),
    "verkehrsrecht": ("Verkehrsrecht", "StVG §§ 7/17/18, FeV MPU, OWi StVO + BKatV, §§ 142/315c/316 StGB"),
    "urheber-medienrecht": ("Urheber- und Medienrecht", "UrhG § 97a-Abmahnung, Lizenz §§ 32/32a, MStV § 18, Gegendarstellung"),
    "sportrecht": ("Sportrecht", "Verbands-/Vereinsrecht, CAS/DIS, AntiDopG/WADC, Athletenvertrag, Stadionverbot"),
    "migrationsrecht": ("Migrationsrecht", "AufenthG, AsylG §§ 3/4, § 60 V/VII, Dublin VO 604/2013, Abschiebung"),
    "agrarrecht": ("Agrarrecht", "GAP 2023–27, GrdstVG / RSG-Vorkauf, LPachtVG, LwAnpG"),
    "vergaberecht": ("Vergaberecht", "GWB Teil 4, VgV, UVgO, Nachprüfung §§ 155 ff. GWB, Rüge § 160 III"),
    "umweltrecht": ("Umweltrecht", "BImSchG §§ 4–7, KrWG, WHG, BNatSchG, UVPG, UmwRG"),
    "energierecht": ("Energierecht", "EnWG §§ 17/18, EEG-Förderung, EnEfG/EDL-G ab 7,5 GWh/a"),
    "aussenwirtschaft-zoll-sanktionen": ("Außenwirtschaft, Zoll, Sanktionen", "AWG/AWV, Dual-Use VO 2021/821, Sanktions-VOen, UZK Art. 33"),
    "geldwaesche-aml-kyc": ("Geldwäsche / AML-KYC", "GwG, KYC §§ 10 ff., FIU-Meldung § 43, AMLR/AMLA ab 2027"),
    "transportrecht": ("Transportrecht", "HGB §§ 407–452d, CMR, Spedition §§ 453 ff., ADSp 2017"),
    "produktrecht": ("Produktrecht", "ProdHaftG + § 823 BGB, GPSR VO 2023/988, Rückrufrecht"),
    "ki-governance": ("KI-Governance", "ISO 42001/23894, NIST AI RMF, AVV Art. 28, § 43e BRAO"),
    "wettbewerbsrecht": ("Wettbewerbsrecht (UWG)", "UWG § 13-Abmahnung, irreführende Werbung §§ 5/5a/5b, eV §§ 12 ff."),
    "kartellrecht": ("Kartellrecht (GWB/AEUV)", "§ 1 GWB / Art. 101 AEUV, §§ 18 ff. + § 19a, §§ 35 ff. Fusionskontrolle"),
    "kapitalmarktrecht": ("Kapitalmarktrecht", "WpHG/MAR, Prospekt-VO 2017/1129, WpÜG-Pflichtangebot"),
    "patentrecht": ("Patentrecht", "PatG/EPÜ, §§ 139 ff. Verletzung, Freedom-to-Operate, UPC"),
    "berufsrecht-anwaltschaft": ("Berufsrecht (Anwaltschaft)", "BRAO + § 203 StGB, FAO-Fortbildung § 15, RDG-Abgrenzung"),
    "cyber-resilience-act": ("Cyber Resilience Act", "VO (EU) 2024/2847 — Anwendungsbereich, Meldepflichten ab 11.09.2026, Anhang I, CE"),
}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    """Tiny YAML-ish parser tuned for SKILL.md frontmatter (no deps)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    meta: dict = {}
    current_key = None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        # list item under previous key
        if re.match(r"^\s+-\s+", line) and current_key:
            value = line.strip()[2:].strip().strip('"').strip("'")
            meta.setdefault(current_key, [])
            if isinstance(meta[current_key], list):
                meta[current_key].append(value)
            continue
        m2 = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if not m2:
            continue
        key, value = m2.group(1), m2.group(2).strip()
        current_key = key
        if value == "":
            meta[key] = []
        elif value.startswith('"') and value.endswith('"'):
            meta[key] = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            meta[key] = value[1:-1]
        else:
            meta[key] = value
    return meta


def derive_tags(name: str, description: str, domain: str) -> list[str]:
    """Extract simple lowercase kebab tags from skill name + key statutory anchors."""
    tags: list[str] = []
    # Name parts
    for part in re.split(r"[-_]", name):
        if len(part) >= 3:
            tags.append(part.lower())
    # Find § / Art / VO references in description
    for ref in re.findall(r"§+\s*\d+[a-z]?", description, re.I):
        tags.append(ref.replace(" ", "").lower())
    for ref in re.findall(r"Art\.\s*\d+", description, re.I):
        tags.append(ref.replace(" ", "").lower())
    # Common statute abbreviations
    for abbr in re.findall(r"\b(BGB|HGB|StGB|StPO|ZPO|GWB|UWG|UrhG|PatG|VVG|VwGO|SGG|SGB|AktG|GmbHG|KSchG|BetrVG|BImSchG|KrWG|WHG|BNatSchG|UVPG|UmwRG|EnWG|EEG|AWG|AWV|UZK|MAR|WpHG|WpÜG|MStV|GpsR|GwG|InsO|AufenthG|AsylG|FeV|StVG|StVO|GG|BVerfGG|FAO|BRAO|RDG|AEUV|EUV|GRCh|DSGVO|BDSG|TTDSG|MBO-Ä|NIS2|HinSchG|LkSG|DORA|DSA|DMA|CSRD|ESRS|KI-VO)\b", description):
        tags.append(abbr.lower())
    # Domain prefix as a tag
    tags.append(domain)
    # Dedupe, preserve order
    seen, out = set(), []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out[:8]


def count_tools(plugin_dir: Path) -> int:
    """Tool count = (scripts/*.py at plugin level) + (skill-level scripts where present)."""
    n = 0
    scripts = plugin_dir / "scripts"
    if scripts.is_dir():
        n += sum(1 for p in scripts.glob("*.py"))
    return n


def main() -> None:
    plugin_files = []  # collected (plugin, skill_dir)
    for domain in DOMAINS_ORDER:
        plug = REPO_ROOT / domain
        if not (plug / "skills").is_dir():
            continue
        for skill_dir in sorted((plug / "skills").iterdir()):
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                plugin_files.append((domain, skill_dir))

    skills_out: list[dict] = []
    domain_counts: dict[str, dict] = {}
    for domain, skill_dir in plugin_files:
        skill_md = skill_dir / "SKILL.md"
        meta = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        name = meta.get("name") or skill_dir.name
        desc = meta.get("description") or ""
        # Strip stray quotes / newlines
        desc = re.sub(r"\s+", " ", desc).strip()
        path = skill_md.relative_to(REPO_ROOT).as_posix()
        tools = count_tools(REPO_ROOT / domain)
        has_references = (REPO_ROOT / domain / "references").is_dir()
        has_assets = (REPO_ROOT / domain / "assets").is_dir()
        tags = derive_tags(name, desc, domain)
        skills_out.append({
            "name": name,
            "description": desc,
            "path": path,
            "domain": domain,
            "category": domain,
            "subdomain": "",
            "version": "0.1.0",
            "license": "Apache-2.0 OR MIT",
            "tags": tags,
            "tools": tools,
            "has_references": has_references,
            "has_assets": has_assets,
        })
        dc = domain_counts.setdefault(domain, {"count": 0, "tools": 0})
        dc["count"] += 1
        dc["tools"] += tools

    catalog = {
        "name": "ai-skills-german-law",
        "description": (
            "AI skills for German legal practice and EU compliance — 48 plugins, "
            f"{len(skills_out)} skills, multi-provider (Claude, Gemini, GPT), "
            "primary-source citations to gesetze-im-internet.de and EUR-Lex."
        ),
        "version": "0.2.0",
        "repository": "https://github.com/borghei/AI-Skills-German-Law",
        "website": "https://borghei.github.io/AI-Skills-German-Law",
        "author": "borghei",
        "license": "Apache-2.0 OR MIT",
        "total_skills": len(skills_out),
        "updated": str(date.today()),
        "domains": {
            d: {
                "count": domain_counts.get(d, {}).get("count", 0),
                "tools": domain_counts.get(d, {}).get("tools", 0),
                "label": DOMAIN_META[d][0],
                "desc": DOMAIN_META[d][1],
            }
            for d in DOMAINS_ORDER
        },
        "skills": skills_out,
    }
    OUT.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO_ROOT)} — {len(skills_out)} skills across {len(domain_counts)} domains")


if __name__ == "__main__":
    main()
