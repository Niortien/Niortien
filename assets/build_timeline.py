"""Génère assets/timeline-fr.svg et assets/timeline-en.svg : la frise animée de toute la carrière.

Lancer depuis le dossier assets :  python build_timeline.py
Pour ajouter une étape, ajoutez une ligne dans ITEMS (ordre chronologique) puis relancez.
"""
from html import escape

# catégorie : formation | poste | client | perso ; en_cours : le point pulse
# (année, date FR, date EN, titre FR, titre EN, détail FR, détail EN, catégorie, en_cours, vedette)
ITEMS = [
    (2021, "juil. 2021", "Jul 2021", "Baccalauréat série D", "Baccalaureate, science track",
     "Lycée Moderne 1 Abobo", "Lycée Moderne 1 Abobo", "formation", False, False),
    (2021, "2021 → 2024", "2021 → 2024", "Licence MIAGE", "Bachelor's degree, MIAGE",
     "Université Polytechnique de Bingerville", "Polytechnic University of Bingerville", "formation", False, False),
    (2022, "août → déc. 2022", "Aug → Dec 2022", "Python pour l'analyse de données", "Python for data analysis",
     "GOMYCODE · pandas, NumPy, Matplotlib", "GOMYCODE · pandas, NumPy, Matplotlib", "formation", False, False),
    (2023, "juin 2023 → mars 2024", "Jun 2023 → Mar 2024", "Bootcamp Full-Stack JS (MERN)", "Full-Stack JS bootcamp (MERN)",
     "GOMYCODE · React, Node.js, Express, MongoDB", "GOMYCODE · React, Node.js, Express, MongoDB", "formation", False, False),
    (2024, "août → nov. 2024", "Aug → Nov 2024", "Stage développeur web · SOTRA", "Web developer intern · SOTRA",
     "Application de gestion interne (WinDev, MERISE, SQL)", "Internal management app (WinDev, MERISE, SQL)", "poste", False, False),
    (2025, "janv. → juil. 2025", "Jan → Jul 2025", "Formation et stage Next.js / NestJS", "Next.js / NestJS training and internship",
     "LUNION-LAB · TypeScript, PostgreSQL, Prisma", "LUNION-LAB · TypeScript, PostgreSQL, Prisma", "formation", False, False),
    (2025, "juil. 2025", "Jul 2025", "Lunion Educ App", "Lunion Educ App",
     "Application mobile éducative en Flutter", "Educational mobile app in Flutter", "client", False, False),
    (2025, "août 2025 →", "Aug 2025 →", "Développeur Full-Stack · LUNION-LAB", "Full-Stack Developer · LUNION-LAB",
     "Poste actuel · plus de 9 applications livrées en production", "Current role · 9+ applications shipped to production", "poste", True, False),
    (2025, "août → oct. 2025", "Aug → Oct 2025", "Turbo ERP", "Turbo ERP",
     "Turbo Delivery · RH, logistique et reporting", "Turbo Delivery · HR, logistics and reporting", "client", False, False),
    (2025, "sept. → nov. 2025", "Sep → Nov 2025", "Turbo Finance", "Turbo Finance",
     "Turbo Delivery · trésorerie, facturation, tableaux de bord", "Turbo Delivery · cash flow, invoicing, dashboards", "client", False, False),
    (2025, "sept. → oct. 2025", "Sep → Oct 2025", "Chicken-Nation", "Chicken-Nation",
     "Site et commande en ligne d'une chaîne de fast-food", "Website and online ordering for a fast-food chain", "client", False, False),
    (2025, "sept. 2025 → juin 2026", "Sep 2025 → Jun 2026", "Lunion Secu", "Lunion Secu",
     "API de sécurité en temps réel (NestJS, Socket.io)", "Real-time security API (NestJS, Socket.io)", "client", False, False),
    (2025, "oct. → nov. 2025", "Oct → Nov 2025", "Sidi Immobilier", "Sidi Immobilier",
     "Annonces immobilières et back-office agents", "Property listings and agent back office", "client", False, False),
    (2025, "oct. → déc. 2025", "Oct → Dec 2025", "Luxury Home Abidjan", "Luxury Home Abidjan",
     "Immobilier haut de gamme", "High-end real estate", "client", False, False),
    (2025, "nov. → déc. 2025", "Nov → Dec 2025", "Site de LUNION-LAB", "LUNION-LAB website",
     "Site officiel de l'agence", "The agency's official website", "client", False, False),
    (2025, "nov. 2025", "Nov 2025", "Site de l'UPB", "UPB website",
     "Site universitaire (Next.js, GSAP)", "University website (Next.js, GSAP)", "client", False, False),
    (2025, "nov. 2025 → janv. 2026", "Nov 2025 → Jan 2026", "Catholikia", "Catholikia",
     "Plateforme paroissiale, rôles membres, prêtres, admins", "Parish platform with member, priest and admin roles", "client", False, False),
    (2025, "déc. 2025 → janv. 2026", "Dec 2025 → Jan 2026", "OSA FC", "OSA FC",
     "Site officiel d'un club de football", "Official website of a football club", "client", False, False),
    (2026, "janv. → mars 2026", "Jan → Mar 2026", "Paroisse Saint-Sauveur", "Saint-Sauveur Parish",
     "Back-office : sacrements, membres, documents", "Back office: sacraments, members, documents", "client", False, False),
    (2026, "févr. → mars 2026", "Feb → Mar 2026", "Stock Pro", "Stock Pro",
     "Gestion de stock avec alertes de seuil", "Inventory management with threshold alerts", "perso", False, False),
    (2026, "mars → avr. 2026", "Mar → Apr 2026", "H2C Africa", "H2C Africa",
     "Site institutionnel (React, TipTap)", "Institutional website (React, TipTap)", "client", False, False),
    (2026, "mars → mai 2026", "Mar → May 2026", "Biblio UPB", "Biblio UPB",
     "Bibliothèque universitaire, 10 modules, 3 rôles", "University library, 10 modules, 3 roles", "perso", False, False),
    (2026, "avr. 2026 →", "Apr 2026 →", "Maintenance Pro · SATE", "Maintenance Pro · SATE",
     "Gestion de flotte et des interventions, en production", "Fleet and service management, in production", "client", True, False),
    (2026, "avr. 2026", "Apr 2026", "Djene Shop · Gestion École · Basit Ticket · Ephrata", "Djene Shop · School ERP · Basit Ticket · Ephrata",
     "E-commerce, ERP scolaire, tickets, site vitrine", "E-commerce, school ERP, ticketing, showcase site", "perso", False, False),
    (2026, "juin 2026", "Jun 2026", "Gestion hôtelière", "Hotel management",
     "API de gestion d'hôtel et site d'un hôtel à Korhogo", "Hotel management API and a hotel website in Korhogo", "perso", False, False),
    (2026, "juin 2026 →", "Jun 2026 →", "Dri Valé", "Dri Valé",
     "Boutique streetwear : site vitrine, stock et caisse", "Streetwear store: storefront, stock and point of sale", "perso", True, True),
    (2026, "août 2026 →", "Aug 2026 →", "Mon Djossi", "Mon Djossi",
     "Caisse et stock pour toutes les boutiques ivoiriennes", "Point of sale and inventory for every Ivorian shop", "perso", True, True),
]

COLORS = {"formation": "#58a6ff", "poste": "#3fb950", "client": "#a78bfa", "perso": "#f2b632"}
LEGEND = {
    "fr": [("formation", "Formation"), ("poste", "Poste et stage"), ("client", "Projet client"), ("perso", "Projet personnel")],
    "en": [("formation", "Education"), ("poste", "Job and internship"), ("client", "Client project"), ("perso", "Personal project")],
}
TITLE = {"fr": "Toute ma carrière, étape par étape", "en": "My whole career, step by step"}
ONGOING = {"fr": "en cours", "en": "ongoing"}

W = 840
SPINE_X = 186
TOP = 92
ROW = 46
YEAR_H = 40
STAGGER = 0.11


def build(lang: str) -> str:
    i_date, i_title, i_detail = (1, 3, 5) if lang == "fr" else (2, 4, 6)
    parts, y, prev_year, n = [], TOP, None, 0
    for item in ITEMS:
        year, cat, ongoing, star = item[0], item[7], item[8], item[9]
        if year != prev_year:
            delay = n * STAGGER
            parts.append(
                f'<g class="it" style="animation-delay:{delay:.2f}s">'
                f'<rect x="{SPINE_X - 34}" y="{y + 6}" width="68" height="26" rx="13" fill="#161b22" stroke="#30363d"/>'
                f'<text class="year" x="{SPINE_X}" y="{y + 24}" text-anchor="middle">{year}</text></g>'
            )
            y += YEAR_H
            prev_year = year
            n += 1
        color = COLORS[cat]
        delay = n * STAGGER
        cy = y + 16
        halo = f'<circle class="ping" cx="{SPINE_X}" cy="{cy}" r="7" fill="{color}" style="transform-origin:{SPINE_X}px {cy}px"/>' if ongoing else ""
        badge = ""
        if ongoing:
            badge = f'<text class="live" x="{W - 24}" y="{cy + 5}" text-anchor="end" fill="{color}">● {ONGOING[lang]}</text>'
        title_cls = "title star" if star else "title"
        prefix = "★ " if star else ""
        parts.append(
            f'<g class="it" style="animation-delay:{delay:.2f}s">'
            f'<text class="date" x="{SPINE_X - 22}" y="{cy + 5}" text-anchor="end">{escape(item[i_date])}</text>'
            f'{halo}<circle cx="{SPINE_X}" cy="{cy}" r="7" fill="{color}" stroke="#0d1117" stroke-width="3"/>'
            f'<text class="{title_cls}" x="{SPINE_X + 22}" y="{cy}" fill="{color if star else "#e6edf3"}">{prefix}{escape(item[i_title])}</text>'
            f'<text class="detail" x="{SPINE_X + 22}" y="{cy + 19}">{escape(item[i_detail])}</text>'
            f'{badge}</g>'
        )
        y += ROW
        n += 1
    height = y + 24
    spine_len = height - TOP - 20
    total = n * STAGGER + 0.6
    legend, lx = [], 24
    for cat, label in LEGEND[lang]:
        legend.append(f'<circle cx="{lx + 6}" cy="58" r="6" fill="{COLORS[cat]}"/><text class="leg" x="{lx + 18}" y="63">{escape(label)}</text>')
        lx += 18 + len(label) * 8 + 34
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" role="img" aria-label="{escape(TITLE[lang])}">
  <defs>
    <linearGradient id="spine" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#58a6ff"/><stop offset=".45" stop-color="#3fb950"/><stop offset=".75" stop-color="#a78bfa"/><stop offset="1" stop-color="#f2b632"/>
    </linearGradient>
  </defs>
  <style>
    .h {{ font: 700 22px 'Segoe UI', Ubuntu, Arial, sans-serif; fill: #e6edf3; }}
    .leg {{ font: 500 13px 'Segoe UI', Ubuntu, Arial, sans-serif; fill: #8b949e; }}
    .year {{ font: 700 14px 'Segoe UI', Ubuntu, Arial, sans-serif; fill: #e6edf3; }}
    .date {{ font: 500 12.5px 'Segoe UI', Ubuntu, Arial, sans-serif; fill: #8b949e; }}
    .title {{ font: 700 15px 'Segoe UI', Ubuntu, Arial, sans-serif; }}
    .star {{ font-size: 16px; }}
    .detail {{ font: 400 12.5px 'Segoe UI', Ubuntu, Arial, sans-serif; fill: #8b949e; }}
    .live {{ font: 700 12px 'Segoe UI', Ubuntu, Arial, sans-serif; }}
    .it {{ opacity: 0; animation: rise .55s cubic-bezier(.2, .8, .2, 1) both; }}
    .spine {{ stroke-dasharray: {spine_len}; stroke-dashoffset: {spine_len}; animation: draw {total:.1f}s linear forwards; }}
    .ping {{ animation: ping 1.8s cubic-bezier(0, 0, .2, 1) infinite; }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateX(-14px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes ping {{ 0% {{ transform: scale(1); opacity: .7; }} 80%, 100% {{ transform: scale(2.6); opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .it {{ opacity: 1; animation: none; }} .spine {{ stroke-dashoffset: 0; animation: none; }} .ping {{ animation: none; }} }}
  </style>
  <rect x="1" y="1" width="{W - 2}" height="{height - 2}" rx="18" fill="#0d1117" stroke="#30363d"/>
  <text class="h" x="24" y="38">{escape(TITLE[lang])}</text>
  {"".join(legend)}
  <line class="spine" x1="{SPINE_X}" y1="{TOP + 8}" x2="{SPINE_X}" y2="{height - 12}" stroke="url(#spine)" stroke-width="3" stroke-linecap="round"/>
  {"".join(parts)}
</svg>
'''


if __name__ == "__main__":
    for lang in ("fr", "en"):
        with open(f"timeline-{lang}.svg", "w", encoding="utf8") as f:
            f.write(build(lang))
    print(f"{len(ITEMS)} étapes, frises écrites")
