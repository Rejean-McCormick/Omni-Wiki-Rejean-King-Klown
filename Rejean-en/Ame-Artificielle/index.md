# Konnaxion – Civic Workflows & Module Interactions

Konnaxion is a socio‑technical framework for coordinating people, knowledge, and action through an ethical, modular civic architecture built on the KOA model: **KonnectED, Ethikos, Kreative, keenKonnect, EkoH, Smart Vote**.

This page is the **hub** for the wiki. It summarizes how modules relate to each other, and it links to detailed pages for each sub‑module. For implementation details (models, services, parameters), use the dedicated technical page linked at the end.

 [Visit the Dashboard](https://konnaxion.com/ekoh/dashboard)

[For an illustrated presentation of the purpose of Konnaxion, the "Knowledge Plateform".](https://kingklown.wiki/)

---

## Wiki structure

Overall structure:

* **Konnaxion – Civic Workflows & Module Interactions** *(this page)*

### KonnectED

* [Knowledge](Knowledge.md) — Collaborative Learning Library: catalog, recommendations, co‑creation, forums, progress tracking.
* [CertifiKation](CertifiKation.md) — Skills & Certification: paths, evaluations, peer validation, portfolios, credentials.

### Ethikos

* [Korum](Korum.md) — Structured Debates: topics, −3…+3 stances, threaded arguments, expert cohorts, summaries.
* [Konsultations](Konsultations.md) — Public Consultations & Feedback: time‑boxed consultations, citizen suggestions, weighted ballots, impact tracking.

### Kreative

* [Konservation](Konservation.md) — Creative Content & Cultural Preservation: digital archives, virtual exhibitions, AI‑enriched catalog, partner collections.
* [Kontact](Kontact.md) — Collaboration & Networking: profiles, intelligent matching, collaboration rooms, opportunities, endorsements.

### keenKonnect

* [Konstruct](Konstruct.md) — Project Collaboration Spaces: project workspaces, tasks, chat, AI insights, project ratings.
* [Stockage](Stockage.md) — Secure Repository & Versioned Storage: document/blueprint storage, versioning, indexing, real‑time sync.

### Kollective Intelligence

* [EkoH](EkoH.md) — Reputation & Expertise: multidimensional scoring, ethical multipliers, privacy controls, audit trails.
* [Smart Vote](Smart-Vote.md) — Weighted Voting System: EkoH‑weighted voting, multiple modalities, emerging‑expert detection, analytics.

Use this section as the navigation menu for the wiki: start from the KOA area you care about, then dive into its sub‑module page for details.

---

## Civic workflow at a glance

The README outlines a civic workflow “proposal → deliberation → decision → action.”
The KOA modules map onto that pipeline as follows:

1. **Learn & build competence – KonnectED**
   People explore resources and courses in **[Knowledge](Knowledge.md)**, then earn certifications through **[CertifiKation](CertifiKation.md)**, building skills and portfolios.

2. **Deliberate & consult – Ethikos**
   Complex issues are debated in **[Korum](Korum.md)** with nuanced stances and arguments, while broader participation is organized via **[Konsultations](Konsultations.md)** for structured public input.

3. **Weigh & decide – Kollective Intelligence**
   **[EkoH](EkoH.md)** computes domain‑specific reputation and ethics scores; **[Smart Vote](Smart-Vote.md)** uses them to weight ballots and stances, exposing both raw and weighted outcomes.

4. **Execute & coordinate – keenKonnect**
   Adopted proposals become projects in **[Konstruct](Konstruct.md)**, with tasks, chat, and AI summaries, while **[Stockage](Stockage.md)** manages all related documents and blueprints.

5. **Preserve & connect – Kreative**
   Outputs are archived and exhibited through **[Konservation](Konservation.md)**, and relationships and opportunities are managed via **[Kontact](Kontact.md)**, feeding back into future cycles of work.

---

## Technical architecture and services

For details about:

* service code‑names and how they map to Django modules
* core models and configuration parameters (thresholds, limits, routes)
* real‑time infrastructure (Channels/Redis), ETL jobs, and analytics flows

see the dedicated technical page:

* [Konnaxion – Technical Architecture & Services](Konnaxion-Technical-Architecture-And-Services.md)

That page consolidates the “technicalities” from the module specifications and the original system‑overview draft, so this hub can stay focused on workflows and navigation.