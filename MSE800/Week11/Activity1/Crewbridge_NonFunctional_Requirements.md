# Crewbridge — Non-Functional Requirements

**Project:** Crewbridge — AI-assisted managed workforce platform for NZ hospitality
**Document type:** Non-Functional Requirements Specification
**Scope:** MVP1
**Version:** 1.0

---

## 1. Introduction

This document lists the non-functional requirements for Crewbridge MVP1 — the quality
attributes and constraints that describe *how* the system should behave, rather than
what it does. Each requirement has an ID, a statement, and where possible a measurable
target and how it is verified. Targets are set at a level realistic for an MVP built by
two people in four weeks, not a production system.

Priority key: **M** must have, **S** should have, **C** could have.

---

## 2. Non-Functional Requirements

### 2.1 Performance

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-1 | Core actions (load a page, post a job, view a shortlist) shall respond quickly under normal use. | Under ~3 seconds for non-AI actions, excluding cold starts. Verified by manual timing. | M |
| NFR-2 | AI processing shall not block the user interface. | AI calls run asynchronously or show a loading state; the UI stays responsive. | M |
| NFR-3 | AI calls shall have a timeout and fall back gracefully. | Timeout set (e.g. 15–30s); on timeout the item is flagged to Admin rather than hanging. | M |

### 2.2 Security

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-4 | Passwords shall be stored hashed, never in plain text. | Django's default password hashing. Verified by inspection. | M |
| NFR-5 | API endpoints shall require authentication except those intended to be public. | Token-based auth enforced; verified by tests. | M |
| NFR-6 | The system shall enforce role-based access so users only access data appropriate to their role. | Permission checks on endpoints; verified by tests. | M |
| NFR-7 | Uploaded documents and purchased materials shall only be accessible to authorised users (owner and Admin). | Access controlled by ownership/role; verified by tests. | M |
| NFR-8 | Secrets (keys, DB credentials, LLM key) shall not be committed to source control. | Stored in environment variables; `.env` git-ignored. Verified by inspection. | M |
| NFR-9 | All traffic in the deployed environment shall use HTTPS. | Provided by the hosting platform. | S |

### 2.3 Privacy & data handling

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-10 | MVP1 shall use synthetic/test data and not require real personal data. | No real worker/venue data needed to build or demo. | M |
| NFR-11 | Personal documents shall be collected and shown only where needed for eligibility, and only to authorised users. | Access scoping as in NFR-7. | M |
| NFR-12 | The design shall be mindful of NZ privacy expectations (e.g. the Health/Privacy principles around personal information). | Documented as a design consideration; full compliance is future work. | S |

### 2.4 Usability

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-13 | The application shall be mobile-friendly. | Key flows usable at mobile widths. Verified by manual testing. | M |
| NFR-14 | The system shall give clear feedback for loading, empty, and error states. | Spinners, empty states, and error messages present on async actions. | M |
| NFR-15 | Error messages shall be understandable to a non-technical user. | Plain-language messages; no raw stack traces shown. | S |
| NFR-16 | Common tasks (post a job, accept a worker) shall be achievable in a few clear steps. | Verified by walkthrough. | S |

### 2.5 Reliability & availability

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-17 | A failure in the AI service shall not crash the application. | Fallback path flags to Admin; verified by simulating a failure. | M |
| NFR-18 | The system shall validate inputs and handle bad input without crashing. | Validation on forms and API; verified by tests. | M |
| NFR-19 | The test environment shall be available on demand for demos. | Hosted on a free tier; cold-start delay acceptable (woken before a demo). | S |

### 2.6 Maintainability

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-20 | The codebase shall be organised into clear modules (auth, core, AI, marketplace) per repo. | Verified by inspection. | M |
| NFR-21 | The backend and frontend shall be in separate repositories with their own README. | Verified by inspection. | M |
| NFR-22 | The system shall have automated unit/integration tests run in CI on every push and PR. | GitHub Actions green check required to merge. | M |
| NFR-23 | The API contract shall be documented and kept current. | OpenAPI/Swagger page available. | M |
| NFR-24 | Code shall be merged via reviewed pull requests, not direct commits to main. | Branch protection on `main`. | S |

### 2.7 Scalability (design intent, not load-tested in MVP)

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-25 | The architecture (API backend + separate frontend + managed DB) shall allow scaling later without a rewrite. | Verified by design review. | S |
| NFR-26 | AI usage shall be designed to control cost (only call when needed, cache where sensible). | Documented in the AI service design. | S |

### 2.8 Compatibility

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-27 | The web app shall work on current versions of major browsers (Chrome, Edge, Safari, Firefox). | Manual check. | S |
| NFR-28 | The frontend shall communicate with the backend over a documented REST API only. | No direct DB access from the frontend. | M |

### 2.9 Legal & compliance (acknowledged, mostly future work)

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-29 | The system shall represent work-hour compliance as a core feature. | Compliance check enforced (see functional FR-29). | M |
| NFR-30 | The MVP shall clearly mark simulated areas (payments, identity checks) as not production-ready. | Documented and labelled in the UI where relevant. | M |
| NFR-31 | Real employment-law obligations (payroll, ACC, holiday pay), real KYC, and real payment compliance are out of scope for MVP1 and recorded as future work. | Stated in scope documents. | M |

### 2.10 AI-specific quality

| ID | Requirement | Target / Verification | Priority |
|----|-------------|-----------------------|----------|
| NFR-32 | AI outputs that affect a person (eligibility, screening) shall be reviewable and overridable by Admin. | Human-in-the-loop review queue. | M |
| NFR-33 | AI shall assist, not autonomously decide, on eligibility and matching in MVP1. | Final actions confirmed by a human (Admin/employer). | M |
| NFR-34 | AI document handling shall be described honestly as field extraction plus rule checks, not government identity verification. | Stated in documentation and UI. | M |

---

## 3. Notes

These targets are deliberately MVP-level and measured simply (manual timing,
inspection, and tests) rather than with formal load or security testing, which are
future work. They are written so each can be checked during the demo and assessment.
