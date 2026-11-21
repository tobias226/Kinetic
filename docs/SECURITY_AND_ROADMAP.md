# Security, confidentiality and sensible production roadmap

## Status

**Proof of concept only.** No sign-in, external connections, shared user database, investor access or real-time API integration. Streamlit session state is designed to demonstrate interactions with bundled fictional data, not safeguard institution-level information. Public links are ordinary research citations.

## Why a co-management portal is not turned on by default

An independent sponsor typically manages sensitive investment, LP and counterparty information. A real cross-organisation portal must impose **least privilege** at the *platform, investor, asset, document and transaction* level. A single public Streamlit app with a generic password, anonymous file upload, a link-based dashboard or a common CSV would not meet that standard. A “partner preview” is therefore local and redacted; downloading text does not upload it anywhere or grant a third party access.

## Production-first architecture

**Phase 1 — Operational integration.** Respect the current firm workflow. Sync into an approved existing CRM (e.g. whichever the firm already uses) and create stable IDs, ownership, action dates, relationship history and citation/verification fields. Add record-level review and duplicate detection.

**Phase 2 — Identity and permissions.** Approved SSO/OIDC, encrypted secrets, centrally governed account provisioning, platform-by-platform RBAC/ABAC, tenant isolation, logging, approvals, retention and deletion schedules; do not build custom password handling. Third-party privacy/security review before launch.

**Phase 3 — Research and sources.** Licensed commercial data feeds, timestamped market/asset datasets, firm-approved verified introductions, clear provenance, contradiction handling and required human approval gates. No covert LinkedIn scraping or invented capital availability.

**Phase 4 — Partner room.** Permissioned workspaces, per-deal redacted materials, expiring access links only after verification, secure document storage, watermarking where appropriate, audit trail, communication consent and a segregation-of-duties review. The partner should see only the exact authorized opportunity and the explicitly approved data.

**Phase 5 — Analytical assurance.** Weight calibration using outcomes and expert review, model-monitoring dashboards, scenario validation against actual asset data and governance around investment-decision usage.

## Operational boundaries of this build

- **Persistence:** edits survive only during the active Streamlit session; export and import datasets to preserve them outside the app.
- **Security:** there is no role-based access, login, audit-grade history, encryption of hypothetical records or data sharing.
- **External data:** no live finance, market, property, mapping or news API.
- **Source freshness:** public signals are snapshots as of November 2026.
- **Financial completeness:** the carbon lab compares simple lifecycle emissions and undiscounted costs but not IRR, discounted cash flow, asset valuation or project feasibility.
- **Privacy:** do not upload private financial information or business contacts to any public deployment.
- **Impersonation:** do not add the firm's logo or present the demo as their internal system without express permission.

## Minimum requirements before use with real data

1. Consent and authority to process private relationships and counterparties.
2. Approved internal hosting, authentication, network controls, secrets and vulnerability testing.
3. Proper data governance, source/licensing controls, retention and GDPR assessment.
4. Audit logs, recoverable database and backup/recovery procedures.
5. Independent model validation for any real underwriting or allocation decisions.
6. Explicit written approvals governing what can be shared with each institutional partner.
