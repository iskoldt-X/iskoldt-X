<!--
  Maintenance notes.

  The four pictures are generated: python3 scripts/gen_profile.py
  Their text lives in that script (PANES, TREE, TILES), not in this file.
  assets/header.svg is the exception -- hand-authored, no script touches it.
  Hand edits to the other three are lost the next time the generator runs.

  Design constraints behind the pictures, so they do not get undone by accident:
  - ONE set of images, no #gh-light-mode-only / #gh-dark-mode-only. That switch
    follows each viewer's own environment, which cannot be controlled from here,
    so a viewer whose GitHub theme is pinned opposite to their OS would see a
    dark card on a white page. Every block is a self-contained terminal window
    instead, and reads the same on either background.
  - Native <rect>/<circle>/<text> only, no <foreignObject>.
  - Heights are computed from the wrapped line count, so text cannot overflow.
  - ASCII tree characters, so a missing glyph cannot render as a tofu box.
-->

<div align="center">

<img src="assets/header.svg" alt="Terminal window. Prompt: whoami. Output: Binghan Xiao, AI / Agentic Engineer, PhD KU/SUND, GPCRdb developer, Copenhagen DK." width="100%">

**I build software for bioinformatics, computational drug discovery and structural
biology. Most recently an AI-driven annotation pipeline where I designed a voting system, and deterministic
validators that overrule the AI. Open to AI / agentic engineering, data engineering,
data science and scientific software roles in the Copenhagen area.**

[![based in](https://img.shields.io/badge/based_in-Copenhagen%2C_DK-58a6ff?style=flat-square&labelColor=0d1117)](#)
[![focus](https://img.shields.io/badge/focus-agentic_AI_for_health_%2F_bioinformatics_%2F_drug_discovery-8b949e?style=flat-square&labelColor=0d1117)](#)

</div>

---

## `$` whoami

I'm a PhD researcher (Drug Design & Pharmacology, University of
Copenhagen / SUND) and a GPCRdb developer. GPCRdb is the reference database
for a receptor family that's the target of roughly a third of approved
drugs, and I build the software behind it. Lately that includes an AI
layer that has to earn a scientist's trust field by field, not just look
good in a demo -- deterministic validators, audit trails, human-in-the-loop
review.

---

## Flagship work

<div align="center">

<img src="assets/flagship.svg" alt="Two side-by-side terminal panes. Left: GPCR Annotation Tools, 214 commits, solo-authored -- a Gemini model proposes each structural-annotation field, deterministic validators hold veto power over every one, every override written to an append-only audit trail; being deployed, NAR manuscript submitted, first author. Right: the container platform GPCRdb runs on, 10 PRs merged, 43 stars and 75 forks -- Django plus RDKit-PostgreSQL, health-check-gated startup, multi-architecture images, and a 36-cell Python by Django by RDKit compatibility matrix automated in CI, across two container repositories of his own plus 10 PRs merged into the upstream GPCRdb codebase." width="100%">

</div>

**GPCR Annotation Tools** is an AI-driven annotation pipeline for GPCR structural
data. Gemini proposes each field; a chain of deterministic validators can
overrule any of them against an external database or a computed value, and
every override is logged for human review. Started as a fork of the GPCRdb
team's repository, all 214 commits are mine, 8 PRs merged upstream. Being
deployed into GPCRdb; NAR manuscript submitted (first author).
[repository](https://github.com/iskoldt-X/GPCR-annotation-tools) &nbsp;&middot;&nbsp;
[merged PRs](https://github.com/protwis/GPCR-annotation-tools/pulls?q=is%3Apr+author%3Aiskoldt-X)

The container platform GPCRdb runs on. Django + RDKit-PostgreSQL,
health-check-gated startup, multi-architecture images, and a
**36-cell Python x Django x RDKit compatibility matrix** that runs
automatically in CI on every push. Ten of my PRs are merged into
`protwis/protwis` (43 stars, 75 forks).
[merged PRs](https://github.com/protwis/protwis/pulls?q=is%3Apr+author%3Aiskoldt-X+is%3Amerged) &nbsp;&middot;&nbsp;
[protwis_django_docker](https://github.com/protwis/protwis_django_docker) &nbsp;&middot;&nbsp;
[postgres_rdkit_docker](https://github.com/protwis/postgres_rdkit_docker)

---

## More



<div align="center">

<img src="assets/evidence.svg" alt="A tree listing of three kinds of evidence. pre-computation-pipeline: a private codebase with no public repo, staged SLURM jobs with explicit contracts, resumable, about 250 automated tests plus a golden-fixture regression suite, built on the licensed Schrodinger Suite. viral-genomes-LSTM: MSc research, PyTorch sequence models trained on HPC over 15.6 million GISAID SARS-CoV-2 genomes, Gene 2024 volume 916:148426, first author. Plasmer: co-developed as third author, a Random Forest classifier for plasmid host-range prediction, 56 citations, 1.1 thousand Docker pulls." width="100%">

</div>

**A pre-computation pipeline for molecular modeling** runs as a private
codebase, with staged jobs on an HPC cluster under SLURM for the licensed
Schrodinger Suite, explicit contracts between stages, idempotent and
resumable, and about 250 automated tests plus a golden-fixture regression
suite that catches drift after a vendor upgrade. No public repository to
link.

**LSTM models over 15.6 million viral genomes**, from my MSc research --
sequence models in PyTorch, trained on HPC, tracking SARS-CoV-2
evolutionary dynamics across the full GISAID corpus.
[paper (DOI)](https://doi.org/10.1016/j.gene.2024.148426) &nbsp;&middot;&nbsp;
[code snapshot](https://github.com/iskoldt-X/SARS-CoV-2-dynamic-evolution)
(*Gene*, 2024, 916:148426, first author)

I co-developed **Plasmer** as third author, a Random Forest classifier for
plasmid host-range prediction that other labs now run in production
(*Microbiology Spectrum*, 56 citations, 1,100+ Docker pulls).
[repository](https://github.com/nekokoe/Plasmer)

---

## AI at work, AI at play


<div align="center">

<img src="assets/sideline.svg" alt="A grid of six side projects. ankidkdeck, 11 stars, a 3,000-word Danish core-vocabulary Anki deck with IPA and audio. DR-LRC, local Whisper transcription of Danish public-radio audio. BifrostLingua, a smaller Danish-learning helper tool. savebot, 5 stars, a Telegram bot containerized with Docker. iskoldtbark, a push-notification CLI for my own automation pipelines. SRUN-authenticator, 78 stars, auto-login for a campus network gateway, and where my coding started." width="100%">

</div>

[ankidkdeck](https://github.com/iskoldt-X/ankidkdeck)
![stars](https://img.shields.io/github/stars/iskoldt-X/ankidkdeck?style=flat-square&color=3fb950&labelColor=0d1117)

A 3,000-word Danish core-vocabulary Anki deck generated with IPA and audio.

[DR-LRC](https://github.com/iskoldt-X/DR-LRC)

Local Whisper transcription of Danish public-radio audio into subtitles.

[BifrostLingua](https://github.com/iskoldt-X/BifrostLingua)

A smaller Danish-learning helper tool.

[savebot](https://github.com/iskoldt-X/savebot)
![stars](https://img.shields.io/github/stars/iskoldt-X/savebot?style=flat-square&color=3fb950&labelColor=0d1117)

[iskoldtbark](https://github.com/iskoldt-X/iskoldtbark)

A
push-notification CLI for my own automation pipelines.

[SRUN-authenticator](https://github.com/iskoldt-X/SRUN-authenticator)
![stars](https://img.shields.io/github/stars/iskoldt-X/SRUN-authenticator?style=flat-square&color=3fb950&labelColor=0d1117)

Auto-login for a campus network gateway, and where my coding
started.

---

## Stack

**Core**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![SLURM/HPC](https://img.shields.io/badge/SLURM%2FHPC-333333?style=flat-square)

**AI / ML**

![Gemini API](https://img.shields.io/badge/Gemini_API-333333?style=flat-square)
![Tool Calling](https://img.shields.io/badge/Tool_Calling-333333?style=flat-square)
![Structured Output](https://img.shields.io/badge/Structured_Output-333333?style=flat-square)
![Evaluation & Audit Design](https://img.shields.io/badge/Evaluation_%26_Audit_Design-333333?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-333333?style=flat-square)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-333333?style=flat-square)

**Cloud (used, not deep)**

![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-F80000?style=flat-square&logo=oracle&logoColor=white)

---

<div align="center">

If you're building AI that has to earn trust in a regulated or scientific
setting, I'd like to hear about it -- reach out here on GitHub.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-binghanxiao-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=0d1117)](https://www.linkedin.com/in/binghanxiao)


</div>
