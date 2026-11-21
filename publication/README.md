# Polybrutus D19 — Controlled archival workflow

An **unreviewed mathematical preprint** with substantial AI assistance disclosed. No novel general theorem or new physical extra dimension is claimed.

1. Confirm both symbolic and independently coded rational exact metric and graph checks pass on the same certificate.
2. Create a **private GitHub repository**; enable independent checks in GitHub Actions and require success.
3. Freeze the successfully tested commit as scientific Git tag `v0.1.0`.
4. Create ZIP using `git archive v0.1.0`; SHA-256 check ZIP, PDF preprint and exact 276-pair JSON certificate.
5. Stage/reuse **only one** Zenodo REST draft. Verify metadata, original author, CC BY 4.0 license, parent DOI, source tag, AI disclosure and remote attachment checksums.
6. Make GitHub public, check tagged commit via **public** GitHub API, publish the same Zenodo draft and verify public DOI and three attachments.
7. Register DOI in README, CITATION.cff, release manifest and central Memoria. Never alter the frozen science tag.

Avoid automated GitHub-to-Zenodo harvesting that creates a second record. Never put passwords, private files or API keys in public Git.
