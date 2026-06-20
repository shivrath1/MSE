# Crewbridge — Functional Requirements

**Project:** Crewbridge — AI-assisted managed workforce platform for NZ hospitality
**Document type:** Functional Requirements Specification
**Scope:** MVP1
**Version:** 1.0

---

## 1. Introduction

### 1.1 Purpose
This document lists the functional requirements for Crewbridge MVP1 — what the system
must *do*. Each requirement has an ID, a statement, a priority, and notes where needed.
It is the agreed reference for what we build and test against.

### 1.2 Scope
Crewbridge connects short-staffed hospitality venues with work-ready staff and handles
screening, eligibility verification, onboarding, and matching using AI assistance, so
that operating cost stays low and the service fee can sit below the market rate. The
MVP also includes a training-materials marketplace. Real payments, payroll, and
government identity checks are out of scope for MVP1 and are simulated or deferred.

### 1.3 Priority key
- **M** — Must have for the MVP demo.
- **S** — Should have.
- **C** — Could have (first to be cut if time is short).

### 1.4 User roles
- **Employer** — a venue that posts staffing needs and accepts workers.
- **Worker** — a person seeking hospitality work.
- **Trainer** — an experienced worker who runs paid inductions and/or sells training
  materials.
- **Admin** — the Crewbridge operator.

---

## 2. Functional Requirements

### 2.1 Authentication & user management

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-1 | The system shall allow a user to register with email and password. | M |
| FR-2 | The system shall authenticate users at login and issue an access token. | M |
| FR-3 | The system shall assign every user one role: Employer, Worker, Trainer, or Admin. | M |
| FR-4 | The system shall restrict features and data access based on the user's role. | M |
| FR-5 | The system shall allow a user to view and update their own profile. | M |
| FR-6 | The system shall allow a user to log out and invalidate their session/token. | S |

### 2.2 Worker

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-7 | The system shall allow a worker to create and edit a profile (experience, skills, availability). | M |
| FR-8 | The system shall allow a worker to upload identity/eligibility documents. | M |
| FR-9 | The system shall display the worker's current eligibility status (verified / pending / flagged). | M |
| FR-10 | The system shall show a worker the jobs they are eligible for. | M |
| FR-11 | The system shall allow a worker to accept an eligible job, creating a placement. | M |
| FR-12 | The system shall prevent a worker from accepting a job that would breach their work-hour conditions. | M |
| FR-13 | The system shall show a worker their placement history and rating. | S |

### 2.3 Employer

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-14 | The system shall allow an employer to create and edit a venue profile. | M |
| FR-15 | The system shall allow an employer to post a staffing need (role, date/time, hours, pay rate). | M |
| FR-16 | The system shall allow an employer to view, edit, and close their own job posts. | M |
| FR-17 | The system shall present an AI-ranked shortlist of eligible workers for a post. | M |
| FR-18 | The system shall allow an employer to accept a worker from the shortlist. | M |
| FR-19 | The system shall allow an employer to rate a worker after a placement. | S |
| FR-20 | The system shall allow an employer to re-book a previously used worker. | S |
| FR-21 | The system shall show an employer their free-placement allowance used and any (simulated) fee. | S |

### 2.4 AI-assisted processing

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-22 | The system shall route all AI requests through a single service with timeout and fallback handling. | M |
| FR-23 | The eligibility agent shall extract key fields (name, document type, expiry, work-hour conditions) from uploaded documents and set an eligibility status. | M |
| FR-24 | The matching agent shall produce a ranked shortlist of eligible workers for a job post, each with a short reason. | M |
| FR-25 | The screening agent shall produce a structured skills summary and suitability score for a candidate. | S |
| FR-26 | The onboarding agent shall generate an editable onboarding checklist when a placement is confirmed. | C |
| FR-27 | The system shall flag any low-confidence or failed AI result to Admin instead of auto-approving it. | M |

### 2.5 Compliance

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-28 | The system shall record each worker's work-hour conditions where applicable. | M |
| FR-29 | The system shall block any placement that would exceed a worker's work-hour conditions. | M |
| FR-30 | The system shall store document expiry dates and flag expired documents, downgrading eligibility. | S |

### 2.6 Placement & training

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-31 | The system shall create a placement record when an employer accepts a worker. | M |
| FR-32 | The system shall track a placement through a status lifecycle (matched → confirmed → completed). | M |
| FR-33 | The system shall allow a trainer to be assigned to a placement for a paid induction. | S |
| FR-34 | The system shall calculate the trainer payment for an induction (payment simulated). | S |

### 2.7 Training-materials marketplace

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-35 | The system shall allow a trainer to create a material listing (title, description, price, file or link). | S |
| FR-36 | The system shall allow a worker to browse and search material listings. | S |
| FR-37 | The system shall allow a worker to purchase a material (payment simulated) and then access it. | S |
| FR-38 | The system shall record purchases and track trainer earnings. | S |
| FR-39 | The system shall allow Admin to review and remove listings. | C |

### 2.8 Admin

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-40 | The system shall allow Admin to view all user accounts and approve, suspend, or remove them. | M |
| FR-41 | The system shall provide Admin a review queue of AI-flagged items with approve/reject actions. | M |
| FR-42 | The system shall provide Admin platform-level figures (users, placements, flagged items, sales). | S |

### 2.9 Pricing (represented, simulated)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-43 | The system shall track each employer's free-placement allowance and apply a simulated service fee beyond it. | S |
| FR-44 | The system shall display fees, worker pay, and content sales without processing real money in MVP1. | S |

### 2.10 Platform / supporting

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-45 | The system shall expose an API contract (OpenAPI/Swagger) for the frontend to build against. | M |
| FR-46 | The system shall provide a way to load synthetic/demo data for development and demos. | M |

---

## 3. Traceability note

These functional requirements map to the backend and frontend user stories
(BE-xx / FE-xx) in the user-story documents, and to the at-a-glance list (R1–R29) in
the MVP1 requirements document. Each user story implements one or more of the
requirements above.
