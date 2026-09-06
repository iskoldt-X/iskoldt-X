#!/usr/bin/env python3
"""Generate every image the profile README uses.

This is the assembled version: the layouts picked out of prototypes 8 and 9
after seeing all of them rendered on GitHub.

  header     unchanged, and NOT generated here -- assets/header.svg is a
             hand-authored file carried over from prototype 7.
  flagship   two panes side by side, split by a vertical rule (from 9)
  evidence   `tree` output (the layout from 9's flagship-tree, applied to the
             evidence content)
  sideline   three-across tile grid (from 9), now six tiles

Invariants kept from prototype 8, all of them measured rather than assumed:

  * ONE set of images. No #gh-light-mode-only / #gh-dark-mode-only. That
    switch follows the viewer's own environment, which the author cannot
    control, so a viewer whose GitHub theme is pinned opposite to their OS saw
    dark cards on a white page. Every block is a self-contained terminal
    window instead, which reads as a deliberate object on any background.
  * No <foreignObject>. Native <rect>/<circle>/<text> only.
  * Heights are COMPUTED from the wrapped line count, so text cannot overflow.
  * ASCII tree charset (`|--`), not box-drawing, so a missing glyph on someone
    else's machine cannot render as a tofu box.

CJK text is measured at full width and gets its own font fallback chain. It is
never load-bearing: every Chinese phrase here restates something the English
beside it already says.
"""

import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"

BODY_BG = "#010409"
BAR_BG = "#161b22"
BORDER = "#30363d"
GREEN = "#3fb950"
FG = "#e6edf3"
MUTED = "#8b949e"
DIM = "#6e7681"
BLUE = "#58a6ff"
YELLOW = "#d29922"
TAG_BG = "#161b22"
RULE = "#21262d"

MONO = ("ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,"
        "'Liberation Mono',monospace")
# The monospace faces above carry no CJK glyphs; the browser falls back for
# those runs, so name the fallbacks explicitly rather than leaving it to luck.
MONO_CJK = (MONO + ",'PingFang SC','Hiragino Sans GB','Microsoft YaHei',"
            "'Noto Sans CJK SC','Source Han Sans SC',sans-serif")

WIDTH = 900
PAD_X = 30
BAR_H = 40
RATIO = 0.60


def is_cjk(ch):
    o = ord(ch)
    return (0x2E80 <= o <= 0x9FFF or 0x3000 <= o <= 0x303F
            or 0xFF00 <= o <= 0xFFEF)


def has_cjk(text):
    return any(is_cjk(ch) for ch in text)


def w(text, size):
    """Advance width in px. CJK glyphs are full width, Latin ones are not."""
    return sum(1.0 if is_cjk(ch) else RATIO for ch in text) * size


def wrap(text, size, max_px):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if w(trial, size) <= max_px or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Canvas:
    def __init__(self):
        self.parts = []

    def text(self, x, y, size, fill, text, weight=None):
        extra = f' font-weight="{weight}"' if weight else ""
        family = MONO_CJK if has_cjk(text) else MONO
        self.parts.append(
            f'<text x="{round(x, 1)}" y="{round(y, 1)}" '
            f'font-family="{family}" font-size="{size}" '
            f'fill="{fill}"{extra}>{esc(text)}</text>')

    def rect(self, x, y, width, height, fill, rx=None, stroke=None):
        r = f' rx="{rx}"' if rx else ""
        s = f' stroke="{stroke}" stroke-width="1"' if stroke else ""
        self.parts.append(
            f'<rect x="{round(x, 1)}" y="{round(y, 1)}" '
            f'width="{round(width, 1)}" height="{round(height, 1)}"'
            f'{r} fill="{fill}"{s}/>')

    def tag(self, x, y, label, size=11):
        box = w(label, size) + 16
        self.rect(x, y, box, 19, TAG_BG, rx=3, stroke=BORDER)
        self.text(x + 8, y + 13.5, size, MUTED, label)
        return box


def window(name, bar_title, height, canvas, aria):
    head = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" '
        f'height="{height}" viewBox="0 0 {WIDTH} {height}" role="img" '
        f'aria-label="{esc(aria)}">',
        f'<title>{esc(bar_title)}</title>',
        f'<rect x="0" y="0" width="{WIDTH}" height="{height}" rx="10" '
        f'fill="{BODY_BG}"/>',
        f'<rect x="0" y="0" width="{WIDTH}" height="{BAR_H}" rx="10" '
        f'fill="{BAR_BG}"/>',
        f'<rect x="0" y="30" width="{WIDTH}" height="10" fill="{BAR_BG}"/>',
        '<circle cx="28" cy="20" r="6" fill="#ff5f56"/>',
        '<circle cx="50" cy="20" r="6" fill="#ffbd2e"/>',
        '<circle cx="72" cy="20" r="6" fill="#27c93f"/>',
        f'<text x="450" y="24.5" font-family="{MONO}" font-size="13" '
        f'fill="{MUTED}" text-anchor="middle">{esc(bar_title)}</text>',
    ]
    tail = [
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" '
        f'rx="10" fill="none" stroke="{BORDER}" stroke-width="1.5"/>',
        '</svg>',
    ]
    (OUT / f"{name}.svg").write_text(
        "\n".join(head + canvas.parts + tail) + "\n", encoding="utf-8")
    print(f"{name}.svg  {WIDTH}x{height}")


# --------------------------------------------------------------------------
# Flagship -- two panes side by side
# --------------------------------------------------------------------------

PANES = [
    dict(
        cwd="~/GPCR-annotation-tools",
        name="GPCR Annotation Tools",
        tags=["214 commits", "solo-authored"],
        body=("A Gemini model proposes each structural-annotation field; a "
              "chain of deterministic validators holds veto power over every "
              "one of them, and every override is written to an append-only "
              "audit trail."),
        note=("Started as a fork of the GPCRdb team's repo -- being "
              "deployed, NAR manuscript submitted (first author)."),
        links=["github.com/iskoldt-X/GPCR-annotation-tools"],
    ),
    dict(
        cwd="~/protwis",
        name="The container platform GPCRdb runs on",
        tags=["10 PRs merged", "43 stars / 75 forks"],
        body=("Django + RDKit-PostgreSQL, health-check-gated startup, "
              "multi-architecture images, and a 36-cell Python x Django x "
              "RDKit compatibility matrix that runs automatically in CI on "
              "every push."),
        note="Official GPCRdb infrastructure, merged upstream.",
        links=["protwis/protwis  (10 PRs merged upstream)",
               "protwis/protwis_django_docker",
               "protwis/postgres_rdkit_docker"],
    ),
]


def flagship():
    c = Canvas()
    gutter = 26
    pane_w = (WIDTH - 2 * PAD_X - gutter) / 2
    heights = []
    for i, pane in enumerate(PANES):
        x = PAD_X + i * (pane_w + gutter)
        y = BAR_H + 30
        c.text(x, y, 13, GREEN, f"{pane['cwd']} $")
        y += 30
        for line in wrap(pane["name"], 15, pane_w):
            c.text(x, y, 15, FG, line, weight="600")
            y += 21
        y += 4
        tx = x
        for tag in pane["tags"]:
            tx += c.tag(tx, y, tag) + 7
        y += 32
        for line in wrap(pane["body"], 12.5, pane_w):
            c.text(x, y, 12.5, MUTED, line)
            y += 18
        y += 8
        for line in wrap(pane["note"], 12.5, pane_w):
            c.text(x, y, 12.5, DIM, line)
            y += 18
        y += 8
        for link in pane["links"]:
            c.text(x, y, 12, BLUE, link)
            y += 17
        heights.append(y)

    height = round(max(heights) + 26)
    c.parts.insert(0, f'<rect x="{PAD_X + pane_w + gutter / 2}" y="{BAR_H + 16}"'
                      f' width="1" height="{height - BAR_H - 34}" '
                      f'fill="{RULE}"/>')
    window("flagship", "bash -- flagship  (2 panes)", height, c,
           "Two side-by-side terminal panes. Left: GPCR Annotation Tools, 214 "
           "commits, solo-authored -- a Gemini model proposes each "
           "structural-annotation field, deterministic validators hold veto "
           "power over every one, every override written to an append-only "
           "audit trail; being deployed, NAR manuscript submitted, first "
           "author. Right: the container platform GPCRdb runs on, 10 PRs "
           "merged, 43 stars and 75 forks -- Django plus RDKit-PostgreSQL, "
           "health-check-gated startup, multi-architecture images, and a "
           "36-cell Python by Django by RDKit compatibility matrix automated "
           "in CI, across two container repositories of his own plus 10 "
           "PRs merged into the upstream GPCRdb codebase.")


# --------------------------------------------------------------------------
# Evidence -- `tree` output
# --------------------------------------------------------------------------

TREE = [
    ("cmd", "binghan@github:~$ tree more/"),
    ("root", "more/"),
    ("branch", "|-- pre-computation-pipeline/", "private codebase, no public repo"),
    ("leaf", "|   |-- slurm/", "staged jobs, explicit contracts, resumable"),
    ("leaf", "|   |-- tests/", "~250 automated + golden-fixture regression suite"),
    ("leaf", "|   `-- STATUS", "licensed Schrodinger Suite"),
    ("blank",),
    ("branch", "|-- viral-genomes-LSTM/", "MSc research"),
    ("leaf", "|   |-- pytorch/", "sequence models trained on HPC"),
    ("leaf", "|   |-- corpus/", "15.6M GISAID SARS-CoV-2 genomes"),
    ("leaf", "|   `-- PAPER", "Gene 2024; 916:148426 (first author)"),
    ("blank",),
    ("branch", "`-- Plasmer/", "co-developed, third author"),
    ("leaf", "    |-- model/", "Random Forest, plasmid host-range prediction"),
    ("leaf", "    |-- uptake/", "56 citations, 1.1k Docker pulls"),
    ("leaf", "    `-- SOURCE", "github.com/nekokoe/Plasmer"),
]


def evidence():
    c = Canvas()
    size = 13.5
    col = PAD_X + 34 * size * RATIO
    y = BAR_H + 34
    for row in TREE:
        kind = row[0]
        if kind == "blank":
            y += 12
            continue
        if kind == "cmd":
            c.text(PAD_X, y, 15, GREEN, row[1])
            y += 32
            continue
        colour = {"root": FG, "branch": FG, "leaf": MUTED}[kind]
        weight = "600" if kind in ("root", "branch") else None
        c.text(PAD_X, y, size, colour, row[1], weight=weight)
        if len(row) > 2:
            c.text(col, y, size, YELLOW if kind == "branch" else DIM, row[2])
        y += 24
    window("evidence", "bash -- tree more/", round(y + 18), c,
           "A tree listing of three kinds of evidence. pre-computation-"
           "pipeline: a private codebase with no public repo, staged SLURM "
           "jobs with explicit contracts, resumable, about 250 automated "
           "tests plus a golden-fixture regression suite, built on the "
           "licensed Schrodinger Suite. viral-genomes-LSTM: MSc research, "
           "PyTorch sequence models trained on HPC over 15.6 million GISAID "
           "SARS-CoV-2 genomes, Gene 2024 volume 916:148426, first author. "
           "Plasmer: co-developed as third author, a Random Forest classifier "
           "for plasmid host-range prediction, 56 citations, 1.1 thousand "
           "Docker pulls.")


# --------------------------------------------------------------------------
# Sideline -- three-across tile grid
# --------------------------------------------------------------------------

TILES = [
    ("ankidkdeck", "11 stars",
     "3,000-word Danish core-vocabulary Anki deck, with IPA and audio.", None),
    ("DR-LRC", None,
     "Local Whisper transcription of Danish public-radio audio.", None),
    ("BifrostLingua", None,
     "A smaller Danish-learning helper tool.", None),
    ("savebot", "5 stars",
     "A Telegram bot, containerized with Docker.", None),
    ("iskoldtbark", None,
     "A push-notification CLI for my own automation pipelines.", None),
    ("SRUN-authenticator", "78 stars",
     "Auto-login for a campus network gateway.", "我写代码的起点。"),
]


def sideline():
    c = Canvas()
    gutter = 18
    per_row = 3
    tile_w = (WIDTH - 2 * PAD_X - gutter * (per_row - 1)) / per_row
    y0 = BAR_H + 34
    c.text(PAD_X, y0, 15, GREEN, "binghan@github:~$ ls play/")
    top = y0 + 22
    tile_h = 112
    for i, (name, tag, desc, zh) in enumerate(TILES):
        col, row = i % per_row, i // per_row
        x = PAD_X + col * (tile_w + gutter)
        y = top + row * (tile_h + gutter)
        c.rect(x, y, tile_w, tile_h, BAR_BG, rx=6, stroke=BORDER)
        c.text(x + 14, y + 26, 13, FG, name, weight="600")
        if tag:
            c.tag(x + tile_w - w(tag, 11) - 30, y + 12, tag)
        ty = y + 48
        for line in wrap(desc, 11.5, tile_w - 28):
            c.text(x + 14, ty, 11.5, MUTED, line)
            ty += 16
        if zh:
            c.text(x + 14, ty + 4, 11.5, DIM, zh)
    rows = (len(TILES) + per_row - 1) // per_row
    height = round(top + rows * tile_h + (rows - 1) * gutter + 24)
    window("sideline", "bash -- ls play/", height, c,
           "A grid of six side projects. ankidkdeck, 11 stars, a 3,000-word "
           "Danish core-vocabulary Anki deck with IPA and audio. DR-LRC, "
           "local Whisper transcription of Danish public-radio audio. "
           "BifrostLingua, a smaller Danish-learning helper tool. savebot, 5 "
           "stars, a Telegram bot containerized with Docker. iskoldtbark, a "
           "push-notification CLI for my own automation pipelines. "
           "SRUN-authenticator, 78 stars, auto-login for a campus network "
           "gateway, and where my coding started.")


if __name__ == "__main__":
    flagship()
    evidence()
    sideline()
