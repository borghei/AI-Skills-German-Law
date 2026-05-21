# Contributing

The highest-leverage thing you can do is **verify one case-law citation**. It takes 30 seconds in Beck-Online or juris, and the resulting PR helps every future user.

Full workflow on GitHub: [CONTRIBUTING.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/CONTRIBUTING.md). Code of Conduct: [CODE_OF_CONDUCT.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/CODE_OF_CONDUCT.md). What follows is the short version.

## Most valuable contributions

<div class="grid" markdown>

<div class="card" markdown>
### Verify a citation
Replace `[unverifiziert, prüfen]` with a sourced URL.
<div class="anchor">label: type:verify-citation · 30 seconds per citation</div>
</div>

<div class="card" markdown>
### Add a new area
Agrar-, Bau-, Familienrecht (we have substantive), Migrations-, Sport-, Verkehrsrecht, etc.
<div class="anchor">label: type:new-area · use arbeitsrecht/ as template</div>
</div>

<div class="card" markdown>
### Add a test case
Real (anonymized) fact patterns are the most valuable contribution.
<div class="anchor">label: type:new-skill or type:new-area</div>
</div>

<div class="card" markdown>
### Add a provider adapter
Mistral, DeepSeek, Llama. Add `providers/<name>.md` and extend `scripts/route_provider.py`.
<div class="anchor">no label yet, just open an issue</div>
</div>

<div class="card" markdown>
### Compliance correction
§ 203, § 43e BRAO, KI-VO, Drittlandtransfer, DSGVO. Citation required.
<div class="anchor">label: type:compliance</div>
</div>

</div>

## Branch naming

| Prefix | Purpose |
|---|---|
| `feature/` | New skill, new area, new provider adapter |
| `fix/` | Bug fix or citation correction |
| `verify/` | Replacing `[unverifiziert]` with sourced citation |
| `docs/` | Documentation only |

## Skill quality bar

1. YAML frontmatter with `name`, `description`, `language: de`, `provider_variants`, `test`
2. Trigger clause in `description` — "Use when ..."
3. Numbered Ablauf with statute-anchored steps
4. Sub-agent split (Researcher → Drafter → Reviewer) where applicable
5. Every case citation marked: `(URL, verified)`, `[unverifiziert, prüfen]`, or — forbidden in client-facing — `[generiert]`
6. Risiken / typische Fehler section with at least three items
7. Length under 500 lines and 5,000 words
8. Concrete examples with anonymized parties, never real Mandatsdaten

## Run validation locally

```bash
python scripts/validate.py
python scripts/eval.py
```

Both should pass before opening a PR.

## License

Contributions are accepted under the same dual license as the project: **Apache-2.0** OR **MIT**, at the user's option.
