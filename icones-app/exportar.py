#!/usr/bin/env python3
"""Exporta os SVG do pacote para PNG 64/128/256 e gera o preview."""

from pathlib import Path

import cairosvg

ROOT = Path(__file__).parent
SVG_DIR = ROOT / "svg"
SIZES = (64, 128, 256)

ICONS = [
    ("tab-inicio", "Início", "Aba"),
    ("tab-estudar", "Estudar", "Aba"),
    ("tab-resultados", "Resultados", "Aba"),
    ("foguete", "Foguete / dias seguidos", "Início"),
    ("ranking", "Medalha / ranking", "Início e Resultados"),
    ("questoes", "Questões", "Estudar e Início"),
    ("flashcards", "Flashcards", "Estudar e Início"),
    ("provas", "Provas", "Estudar"),
    ("simulados", "Simulados", "Estudar"),
    ("revisao", "Revisão", "Estudar e Início"),
    ("desempenho", "Desempenho", "Resultados"),
    ("raio-x-banca", "Raio X da Banca", "Resultados"),
    ("check-meta", "Meta cumprida", "Início"),
    ("chevron", "Seta", "Cards"),
]


def export_pngs() -> None:
    for size in SIZES:
        out_dir = ROOT / "png" / str(size)
        out_dir.mkdir(parents=True, exist_ok=True)
        for name, _, _ in ICONS:
            svg = SVG_DIR / f"{name}.svg"
            cairosvg.svg2png(
                url=str(svg),
                write_to=str(out_dir / f"{name}.png"),
                output_width=size,
                output_height=size,
            )


def write_preview() -> None:
    cards = []
    for name, title, where in ICONS:
        cards.append(
            f"""
            <article class="card">
              <div class="icon-well">
                <img src="png/256/{name}.png" alt="{title}">
              </div>
              <h2>{title}</h2>
              <p>{where}</p>
              <code>{name}.svg</code>
            </article>
            """
        )
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ícones do aplicativo</title>
  <style>
    :root {{
      --bg: #1c1c1e;
      --card: #2c2c2e;
      --well: #3a3a3c;
      --text: #f2f2f7;
      --muted: #aeaeb2;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      padding: 32px 20px 64px;
    }}
    h1 {{ font-size: 28px; font-weight: 650; margin: 0 0 8px; }}
    .lead {{ color: var(--muted); margin: 0 0 28px; max-width: 640px; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 16px;
    }}
    .card {{
      background: var(--card);
      border-radius: 20px;
      padding: 18px 16px 16px;
    }}
    .icon-well {{
      width: 72px;
      height: 72px;
      border-radius: 18px;
      background: var(--well);
      display: grid;
      place-items: center;
      margin-bottom: 14px;
    }}
    .icon-well img {{ width: 36px; height: 36px; }}
    h2 {{ font-size: 15px; margin: 0 0 4px; font-weight: 600; }}
    p {{ margin: 0 0 10px; color: var(--muted); font-size: 13px; }}
    code {{ color: #c4b5e0; font-size: 12px; }}
  </style>
</head>
<body>
  <h1>Ícones do aplicativo</h1>
  <p class="lead">Pacote das telas Início, Estudar e Resultados, com cores saturadas. SVG vetorial e PNG 64/128/256 com fundo transparente.</p>
  <div class="grid">
    {''.join(cards)}
  </div>
</body>
</html>
"""
    (ROOT / "preview.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    export_pngs()
    write_preview()
    print(f"Exportados {len(ICONS)} ícones em {SIZES}")
