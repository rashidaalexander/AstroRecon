# AstroRecon

<p align="center">
  <img src="assets/banner.png" alt="AstroRecon banner" width="100%" />
</p>

<p align="center">
  <img src="assets/starfield.gif" alt="AstroRecon starfield" width="100%" />
</p>

```text
ASTRORECON
```

**Open-source orbital infrastructure reconnaissance engine**

![License](https://img.shields.io/badge/license-MIT-1ecbe1) ![Python](https://img.shields.io/badge/python-3.11+-1ecbe1) ![Docker](https://img.shields.io/badge/docker-ready-1ecbe1) ![Tests](https://img.shields.io/badge/tests-passing-1ecbe1)

**Related:** [SignalNebula](../SignalNebula) • [OrbitalGraph](../OrbitalGraph)

## Overview

Builds searchable datasets of satellites, operators, ground stations, and mission metadata from sample catalogs.

## Why this repo exists

AstroRecon is part of a space-AI-security ecosystem designed to look and behave like a small open research lab. It ships with runnable code, sample data, a CLI, tests, Docker support, architecture notes, and ADR-style design records so the repository feels serious the second someone lands on it.

## Architecture

<p align="center">
  <img src="assets/architecture.svg" alt="AstroRecon architecture" width="100%" />
</p>

**Pipeline**

Catalog ingest → normalization → metadata enrichment → exportable intelligence set

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m astrorecon.cli catalog data/sample_catalog.json
python -m astrorecon.cli operators data/sample_catalog.json
```

## Docker

```bash
docker build -t astrorecon .
docker run --rm astrorecon
```

## Repository layout

```text
astrorecon/
├── astrorecon/
│   ├── cli.py
│   ├── engine.py
│   ├── models.py
│   └── utils.py
├── data/
├── docs/
│   ├── architecture.md
│   └── adr/
├── tests/
├── assets/
├── README.md
├── requirements.txt
├── Dockerfile
└── LICENSE
```

## Documentation

- `docs/architecture.md` for end-to-end system design
- `docs/adr/ADR-001.md` for processing choices
- `docs/adr/ADR-002.md` for report strategy
- `docs/adr/ADR-003.md` for ecosystem links

## Tests

```bash
pytest
```

## Notes

This project is a **research-style prototype** with sample datasets and operator-friendly outputs. It is intentionally presentation-heavy, but it still runs and produces real output from bundled data.

## License

MIT
