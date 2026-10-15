"""Gera os SVGs do README (PT e EN) com a identidade visual do lado Tech de leonardomartins.dev.

Uso: python scripts/generate_assets.py
Edite os dicionários de conteúdo abaixo e rode de novo para atualizar as imagens em assets/.
"""

from pathlib import Path
import sys
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

# Tokens do tema Tech do site
BG = "#050508"
BG2 = "#0c0b12"
BG3 = "#17151f"
INK = "#eeeaf6"
MUTED = "#a39db3"
ACCENT = "#a855f7"
ACCENT_DEEP = "#7e22ce"
PINK = "#ec4899"

DISPLAY = "'Archivo','Archivo Black','Arial Black','Segoe UI',Helvetica,Arial,sans-serif"
BODY = "'Archivo','Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'Cascadia Code',Menlo,Consolas,monospace"

BASE_CSS = f"""
.d{{font-family:{DISPLAY};font-weight:800;text-transform:uppercase;letter-spacing:-.02em}}
.b{{font-family:{BODY}}}
.m{{font-family:{MONO};letter-spacing:.08em}}
@keyframes up{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:none}}}}
@keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
@keyframes glow{{0%,100%{{opacity:.55}}50%{{opacity:.9}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes grow{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""


def svg(w, h, body, css="", label=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{escape(label)}" fill="none">'
        f"<title>{escape(label)}</title><style>{BASE_CSS}{css}</style>{body}</svg>"
    )


def wrap(text, size, width, ratio=0.52):
    max_chars = max(8, int(width / (size * ratio)))
    lines, cur = [], ""
    for word in text.split():
        if len(cur) + len(word) + (1 if cur else 0) > max_chars:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}" if cur else word
    if cur:
        lines.append(cur)
    return lines


def tspans(lines, x, size, lh=1.45):
    return "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else size * lh:.1f}">{escape(l)}</tspan>' for i, l in enumerate(lines)
    )


def defs_glow(id_, cx, cy, r, color=ACCENT, op=0.45):
    return (
        f'<radialGradient id="{id_}" cx="{cx}" cy="{cy}" r="{r}" gradientUnits="userSpaceOnUse">'
        f'<stop offset="0" stop-color="{color}" stop-opacity="{op}"/>'
        f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>'
    )


# ---------------------------------------------------------------- conteúdo

CONTENT = {
    "pt": {
        "path": "~/le0nardomartins/tech",
        "place": "SÃO PAULO — BR",
        "role": "Desenvolvedor Full Stack  ·  Engenharia Mecatrônica @ FIAP",
        "status": "DISPONÍVEL PARA O TIME",
        "stats": [
            ("4+", "Anos de dedicação", "Estudo intensivo e projetos complexos"),
            ("11+", "Anos aprendendo", "Jornada iniciada aos 10 anos"),
            ("30+", "Projetos entregues", "Projetos reais em produção para clientes"),
        ],
        "sections": {
            "about": ("01", "Quem eu sou", "Engenharia, código e negócio na mesma cabeça"),
            "projects": ("02", "Missões concluídas", "Engenharia, tecnologia e criatividade"),
            "journey": ("03", "Fases da jornada", "Trajetória profissional"),
            "stack": ("04", "Inventário", "Ferramentas que uso para construir"),
            "badges": ("05", "Conquistas desbloqueadas", "Reconhecimentos e certificações"),
            "activity": ("06", "Registro de atividade", "Commits, PRs e experimentos"),
            "contact": ("07", "Convidar para o time", "Vamos conversar"),
        },
        "mission": "MISSÃO",
        "done": "CONCLUÍDA",
        "demo": "VER DEMO",
        "open": "VER PROJETO",
        "now": "ATUAL",
        "next": "PRÓXIMO",
        "footer": "Obrigado pela visita. Se meu perfil combina com o seu time, vamos conversar.",
        "projects": [
            ("magic-mirror", "Magic Mirror",
             "Espelho inteligente que envelhece a pessoa com base nos hábitos dela e projeta como ela estará em 30 anos. Apresentado no Future Fest FIAP para centenas de visitantes.",
             ["IA", "React", "Visão computacional", "Future Fest"], None),
            ("lumina", "Assistente Lumina",
             "Assistente de IA para RH com foco em NR1 e segurança do trabalho. Sistema completo para análise e prevenção de acidentes, com insights e recomendações.",
             ["IA", "Full Stack", "Banco de dados", "NR1"], None),
            ("bluesystems", "Blue Systems",
             "Monitoramento da vida marinha para identificar perigos, manchas de óleo e animais que precisam de ajuda.",
             ["IA", "Monitoramento", "Vida marinha", "Conservação"], "demo"),
            ("greenwave", "Green Wave",
             "Hidroponia modular, sustentável e automática que planta, rega, colhe e ajusta temperatura e nutrientes sozinha.",
             ["IoT", "Automação", "Hidroponia", "Sustentabilidade"], "demo"),
            ("monitoramento", "Monitor de Desastres",
             "Aplicação para monitoramento e alerta de desastres naturais, com interface moderna e notificações em tempo real.",
             ["React", "TypeScript", "Vite", "Tempo real"], "demo"),
            ("ysmbank", "ysmBANK",
             "Sistema bancário acadêmico completo: interface moderna, contas, transferências e gestão financeira.",
             ["Java", "Banking", "Sistema", "Academia"], None),
        ],
        "journey": [
            ("2024 — 2026", "Estagiário de Operações", "Brainvest Wealth Management", "Automação interna e Comitê de Inovação", False),
            ("2025 — ATUAL", "Co-Founder & Tech Lead", "Snow Dive Group", "Arquitetura, clientes e entrega de produto", True),
            ("2026", "Mentor de Projetos", "FIAP School", "Mentoria, execução e inovação aplicada", False),
            ("PRÓXIMO", "Crescimento exponencial", "Impacto técnico e estratégico", "Projetos de maior escala", None),
        ],
    },
    "en": {
        "path": "~/le0nardomartins/tech",
        "place": "SÃO PAULO — BR",
        "role": "Full Stack Developer  ·  Mechatronics Engineering @ FIAP",
        "status": "OPEN TO JOIN YOUR TEAM",
        "stats": [
            ("4+", "Years of dedication", "Intensive study and complex projects"),
            ("11+", "Years learning", "Journey started at age 10"),
            ("30+", "Projects delivered", "Real projects in production for clients"),
        ],
        "sections": {
            "about": ("01", "Who I am", "Engineering, code and business in one head"),
            "projects": ("02", "Missions completed", "Engineering, technology and creativity"),
            "journey": ("03", "Journey phases", "Professional path"),
            "stack": ("04", "Inventory", "Tools I build with"),
            "badges": ("05", "Achievements unlocked", "Recognition and certifications"),
            "activity": ("06", "Activity log", "Commits, PRs and experiments"),
            "contact": ("07", "Invite to the team", "Let's talk"),
        },
        "mission": "MISSION",
        "done": "COMPLETED",
        "demo": "WATCH DEMO",
        "open": "VIEW PROJECT",
        "now": "NOW",
        "next": "NEXT",
        "footer": "Thanks for stopping by. If my profile fits your team, let's talk.",
        "projects": [
            ("magic-mirror", "Magic Mirror",
             "A smart mirror that ages people based on their habits and shows how they may look in 30 years. Showcased at FIAP Future Fest to hundreds of visitors.",
             ["AI", "React", "Computer vision", "Future Fest"], None),
            ("lumina", "Lumina Assistant",
             "AI assistant for HR focused on NR1 and workplace safety. A complete system for accident analysis and prevention, with insights and recommendations.",
             ["AI", "Full Stack", "Databases", "NR1"], None),
            ("bluesystems", "Blue Systems",
             "Marine life monitoring to spot hazards, oil spills and animals that need help.",
             ["AI", "Monitoring", "Marine life", "Conservation"], "demo"),
            ("greenwave", "Green Wave",
             "Modular, sustainable and automatic hydroponics that plants, waters, harvests and tunes temperature and nutrients on its own.",
             ["IoT", "Automation", "Hydroponics", "Sustainability"], "demo"),
            ("monitoramento", "Disaster Monitor",
             "An app for monitoring and alerting on natural disasters, with a modern interface and real-time notifications.",
             ["React", "TypeScript", "Vite", "Real-time"], "demo"),
            ("ysmbank", "ysmBANK",
             "A complete academic banking system: modern interface, accounts, transfers and financial management.",
             ["Java", "Banking", "System", "Academic"], None),
        ],
        "journey": [
            ("2024 — 2026", "Operations Intern", "Brainvest Wealth Management", "Internal automation and Innovation Committee", False),
            ("2025 — NOW", "Co-Founder & Tech Lead", "Snow Dive Group", "Architecture, clients and product delivery", True),
            ("2026", "Project Mentor", "FIAP School", "Mentoring, execution and applied innovation", False),
            ("NEXT", "Exponential growth", "Technical and strategic impact", "Larger-scale projects", None),
        ],
    },
}


# ---------------------------------------------------------------- peças

def header(c):
    w, h = 1200, 440
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>' for x in range(0, w + 1, 60))
    grid += "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>' for y in range(0, h + 1, 60))
    words = [("Think.", INK), ("Build.", INK), ("Evolve.", ACCENT)]
    motto = "".join(
        f'<text class="d mo" x="1136" y="{150 + i * 62}" text-anchor="end" font-size="54" fill="{col}" '
        f'style="animation-delay:{0.6 + i * 0.25:.2f}s">{word}</text>'
        for i, (word, col) in enumerate(words)
    )
    css = """
.t{animation:up .9s cubic-bezier(.2,.7,.2,1) both}
.mo{animation:up .8s cubic-bezier(.2,.7,.2,1) both}
.f{animation:fade 1.2s ease both}
.g{animation:glow 6s ease-in-out infinite}
.p{animation:pulse 2s ease-in-out infinite}
.c{animation:blink 1.1s steps(1) infinite}
.r{transform-origin:64px 0;animation:grow 1.4s .4s cubic-bezier(.2,.7,.2,1) both}
"""
    body = f"""
<defs>
{defs_glow("g1", 980, 120, 520)}
{defs_glow("g2", 140, 470, 420, PINK, .22)}
<linearGradient id="fadeG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="gm"><rect width="{w}" height="{h}" fill="url(#fadeG)"/></mask>
<clipPath id="clip"><rect width="{w}" height="{h}" rx="22"/></clipPath>
</defs>
<g clip-path="url(#clip)">
<rect width="{w}" height="{h}" fill="{BG}"/>
<g stroke="{INK}" stroke-opacity=".05" mask="url(#gm)">{grid}</g>
<rect class="g" width="{w}" height="{h}" fill="url(#g1)"/>
<rect class="g" width="{w}" height="{h}" fill="url(#g2)" style="animation-delay:-3s"/>
<text class="m f" x="64" y="62" font-size="15" fill="{MUTED}">{escape(c["path"])}<tspan class="c" fill="{ACCENT}"> ▍</tspan></text>
<text class="m f" x="1136" y="62" font-size="15" fill="{MUTED}" text-anchor="end">{escape(c["place"])}</text>
<text class="d t" x="60" y="196" font-size="104" fill="{INK}">Leonardo</text>
<text class="d t" x="60" y="300" font-size="104" fill="{INK}" style="animation-delay:.15s">Martins<tspan fill="{ACCENT}">.</tspan></text>
{motto}
<rect class="r" x="64" y="342" width="1072" height="1" fill="{INK}" fill-opacity=".18"/>
<text class="b f" x="64" y="388" font-size="21" fill="{INK}" style="animation-delay:.8s">{escape(c["role"])}</text>
<g class="f" style="animation-delay:1s">
<circle class="p" cx="{1136 - len(c["status"]) * 9.6 - 22}" cy="382" r="6" fill="{ACCENT}"/>
<text class="m" x="1136" y="388" font-size="15" fill="{ACCENT}" text-anchor="end">{escape(c["status"])}</text>
</g>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="22" stroke="{INK}" stroke-opacity=".08"/>
</g>"""
    return svg(w, h, body, css, "Leonardo Martins — Think. Build. Evolve.")


def stats(c):
    w, h = 1200, 200
    col = w / 3
    parts = []
    for i, (num, label, desc) in enumerate(c["stats"]):
        x = 48 + i * col
        delay = 0.15 * i
        parts.append(
            f'<g class="s" style="animation-delay:{delay:.2f}s">'
            f'<text class="d" x="{x}" y="104" font-size="76" fill="{INK}">{num[:-1]}<tspan fill="{ACCENT}">+</tspan></text>'
            f'<text class="m" x="{x + 4}" y="142" font-size="14" fill="{INK}">{escape(label.upper())}</text>'
            f'<text class="b" x="{x + 4}" y="168" font-size="16" fill="{MUTED}">{escape(desc)}</text></g>'
        )
        if i:
            parts.append(f'<rect x="{i * col}" y="40" width="1" height="128" fill="{INK}" fill-opacity=".1"/>')
    css = ".s{animation:up .8s cubic-bezier(.2,.7,.2,1) both}"
    body = (
        f'<rect width="{w}" height="{h}" rx="20" fill="{BG2}"/>'
        f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="20" stroke="{INK}" stroke-opacity=".08"/>'
        + "".join(parts)
    )
    return svg(w, h, body, css, " · ".join(f"{n} {l}" for n, l, _ in c["stats"]))


def section(num, title, sub):
    w, h = 1200, 96
    css = ".r{transform-origin:0 0;animation:grow 1.2s cubic-bezier(.2,.7,.2,1) both}.t{animation:up .7s cubic-bezier(.2,.7,.2,1) both}"
    body = f"""
<text class="m t" x="2" y="30" font-size="15" fill="{ACCENT}">{num} /</text>
<text class="d t" x="0" y="74" font-size="44" fill="{INK}">{escape(title)}<tspan fill="{ACCENT}">.</tspan></text>
<text class="b t" x="1198" y="74" font-size="17" fill="{MUTED}" text-anchor="end">{escape(sub)}</text>
<rect class="r" x="0" y="94" width="{w}" height="1" fill="{INK}" fill-opacity=".14"/>
<rect class="r" x="0" y="93" width="72" height="3" fill="{ACCENT}"/>"""
    return svg(w, h, body, css, title)


def card(c, i, total, proj):
    _, title, desc, tags, kind = proj
    w, h = 600, 340
    lines = wrap(desc, 17, w - 96, 0.5)[:4]
    cta = c["demo"] if kind == "demo" else c["open"]
    tag_limit = 560 - (len(cta) + 2) * 8.3 - 20
    tag_svg, tx = "", 40
    for t in tags:
        tw = len(t) * 8.4 + 26
        if tx + tw > tag_limit:
            break
        tag_svg += (
            f'<rect x="{tx}" y="278" width="{tw:.0f}" height="30" rx="15" stroke="{INK}" stroke-opacity=".22"/>'
            f'<text class="m" x="{tx + tw / 2:.0f}" y="298" font-size="12.5" fill="{INK}" text-anchor="middle">{escape(t.upper())}</text>'
        )
        tx += tw + 8
    title_size = 40 if len(title) <= 18 else 34
    css = ".p{animation:pulse 2s ease-in-out infinite}.g{animation:glow 5s ease-in-out infinite}"
    body = f"""
<defs>{defs_glow("cg", 560, 0, 340, ACCENT, .32)}<clipPath id="cc"><rect width="{w}" height="{h}" rx="20"/></clipPath></defs>
<g clip-path="url(#cc)">
<rect width="{w}" height="{h}" fill="{BG2}"/>
<rect class="g" width="{w}" height="{h}" fill="url(#cg)" style="animation-delay:-{i * 0.8:.1f}s"/>
<text class="m" x="40" y="52" font-size="13" fill="{MUTED}">{c["mission"]} {i + 1:02d}/{total:02d}</text>
<circle class="p" cx="{560 - len(c["done"]) * 8.3 - 16}" cy="47" r="5" fill="{ACCENT}"/>
<text class="m" x="560" y="52" font-size="13" fill="{ACCENT}" text-anchor="end">{c["done"]}</text>
<text class="d" x="38" y="116" font-size="{title_size}" fill="{INK}">{escape(title)}</text>
<text class="b" x="40" y="156" font-size="17" fill="{MUTED}">{tspans(lines, 40, 17)}</text>
{tag_svg}
<text class="m" x="560" y="298" font-size="12.5" fill="{ACCENT}" text-anchor="end">{cta} ↗</text>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="20" stroke="{INK}" stroke-opacity=".09"/>
</g>"""
    return svg(w, h, body, css, f"{title} — {desc}")


def journey(c):
    w, h = 1200, 330
    steps = c["journey"]
    col = (w - 96) / len(steps)
    y_line = 110
    parts = [
        f'<rect x="48" y="{y_line}" width="{w - 96}" height="1" fill="{INK}" fill-opacity=".14"/>',
        f'<rect class="r" x="48" y="{y_line - 1}" width="{col * 2.5:.0f}" height="3" fill="url(#lg)"/>',
    ]
    for i, (period, title, org, tag, current) in enumerate(steps):
        x = 48 + i * col
        d = f"animation-delay:{0.2 + i * 0.18:.2f}s"
        color = ACCENT if current is not False else INK
        if current is None:
            node = f'<circle cx="{x + 8}" cy="{y_line}" r="8" fill="{BG2}" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="3 3"/>'
        elif current:
            node = (
                f'<circle class="p" cx="{x + 8}" cy="{y_line}" r="16" fill="{ACCENT}" fill-opacity=".25"/>'
                f'<circle cx="{x + 8}" cy="{y_line}" r="8" fill="{ACCENT}"/>'
            )
        else:
            node = f'<circle cx="{x + 8}" cy="{y_line}" r="7" fill="{INK}"/>'
        title_lines = wrap(title.upper(), 23, col - 24, 0.66)
        ty = 172
        parts.append(
            f'<g class="s" style="{d}">{node}'
            f'<text class="m" x="{x}" y="72" font-size="14" fill="{color}">{escape(period)}</text>'
            f'<text class="d" x="{x}" y="{ty}" font-size="23" fill="{INK}">{tspans(title_lines, x, 23, 1.15)}</text>'
            f'<text class="b" x="{x}" y="{ty + 26 * len(title_lines) + 10}" font-size="16.5" fill="{INK}" fill-opacity=".85">{escape(org)}</text>'
            f'<text class="b" x="{x}" y="{ty + 26 * len(title_lines) + 40}" font-size="15" fill="{MUTED}">'
            f'{tspans(wrap(tag, 15, col - 30, 0.5), x, 15, 1.4)}</text></g>'
        )
    css = (
        ".s{animation:up .8s cubic-bezier(.2,.7,.2,1) both}.p{animation:pulse 2s ease-in-out infinite}"
        ".r{transform-origin:48px 0;animation:grow 1.6s cubic-bezier(.2,.7,.2,1) both}"
    )
    body = (
        f'<defs><linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="{ACCENT_DEEP}"/>'
        f'<stop offset="1" stop-color="{ACCENT}"/></linearGradient></defs>'
        f'<rect width="{w}" height="{h}" rx="20" fill="{BG2}"/>'
        f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="20" stroke="{INK}" stroke-opacity=".08"/>'
        + "".join(parts)
    )
    return svg(w, h, body, css, " → ".join(f"{p}: {t} ({o})" for p, t, o, _, _ in steps))


def footer(c):
    w, h = 1200, 220
    css = ".t{animation:up .9s cubic-bezier(.2,.7,.2,1) both}.g{animation:glow 6s ease-in-out infinite}.c{animation:blink 1.1s steps(1) infinite}"
    body = f"""
<defs>{defs_glow("fg", 600, 260, 520)}<clipPath id="fc"><rect width="{w}" height="{h}" rx="22"/></clipPath></defs>
<g clip-path="url(#fc)">
<rect width="{w}" height="{h}" fill="{BG}"/>
<rect class="g" width="{w}" height="{h}" fill="url(#fg)"/>
<text class="d t" x="600" y="112" font-size="58" fill="{INK}" text-anchor="middle">Think. Build. <tspan fill="{ACCENT}">Evolve.</tspan><tspan class="c" fill="{ACCENT}">▍</tspan></text>
<text class="b t" x="600" y="160" font-size="18" fill="{MUTED}" text-anchor="middle" style="animation-delay:.2s">{escape(c["footer"])}</text>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="22" stroke="{INK}" stroke-opacity=".08"/>
</g>"""
    return svg(w, h, body, css, "Think. Build. Evolve.")


def main():
    # --static: congela as animações (útil para gerar prévias em PNG)
    global OUT, BASE_CSS
    if "--static" in sys.argv:
        BASE_CSS += "*{animation:none!important}"
    if "--out" in sys.argv:
        OUT = Path(sys.argv[sys.argv.index("--out") + 1])
    for lang, c in CONTENT.items():
        d = OUT / lang
        d.mkdir(parents=True, exist_ok=True)
        files = {
            "header.svg": header(c),
            "stats.svg": stats(c),
            "journey.svg": journey(c),
            "footer.svg": footer(c),
        }
        for key, (num, title, sub) in c["sections"].items():
            files[f"section-{key}.svg"] = section(num, title, sub)
        for i, proj in enumerate(c["projects"]):
            files[f"project-{proj[0]}.svg"] = card(c, i, len(c["projects"]), proj)
        for name, content in files.items():
            (d / name).write_text(content, encoding="utf-8")
        print(f"{lang}: {len(files)} arquivos em {d}")


if __name__ == "__main__":
    main()
