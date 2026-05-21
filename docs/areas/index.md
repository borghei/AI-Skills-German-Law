# Areas

23 installable areas organized into three groups by buyer persona.

<div class="grid" markdown>

<div class="card" markdown>
### German legal practice (11)
Everyday Kanzlei work for Anwält:innen, Syndikus, and in-house counsel.
<div class="anchor">arbeitsrecht · datenschutzrecht · vertragsrecht · mietrecht · gesellschaftsrecht · strafrecht · insolvenzrecht · prozessrecht · erbrecht · familienrecht · betreuungsrecht</div>

[Browse →](german-law.md)
</div>

<div class="card" markdown>
### Fachanwaltschaften (5)
Specialty practice areas mapped to the bar's Fachanwalt qualifications.
<div class="anchor">it-recht · bankrecht · gewerblicher-rechtsschutz · steuerrecht · verwaltungsrecht</div>

[Browse →](fachanwaltschaften.md)
</div>

<div class="card" markdown>
### EU / cross-cutting compliance (7)
Frameworks every European company touches, regardless of industry.
<div class="anchor">ki-vo-compliance · nis2 · hinweisgeberschutz · lieferkettengesetz · dora · dsa-dma · csrd</div>

[Browse →](eu-compliance.md)
</div>

</div>

## How each area is structured

```
<area>/
├── .claude-plugin/plugin.json     # marketplace manifest
├── README.md                      # area overview, skills table
├── agents/                        # researcher → drafter → reviewer (where present)
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md               # canonical, provider-agnostic
│       ├── providers/             # rendered Claude / Gemini / OpenAI adapters
│       └── test.md                # fact pattern + structural assertions
└── tests/                         # area-level test bench (when needed)
```

Each skill has a researcher (Quellensuche), drafter (Gutachtenstil-Entwurf), and reviewer (Risiko-, Frist- und Berufsrechts-Check) sub-agent. Conventions are in [CONVENTIONS.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/CONVENTIONS.md).
