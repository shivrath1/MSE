## Agile (Scrum)

### What it is

Agile is an iterative approach. Instead of doing all the requirements, then all the
design, then all the code, you build the product in small chunks called sprints.
Each sprint produces a working piece of the product. After each sprint you review
what you built, get feedback, and adjust the plan for the next one. This suits a
product like Crewbridge where the idea is still evolving and we expect to learn
things as we go.

We are running **2 sprints of 2 weeks each (4 weeks total)**.

### Key terms

- **Product Backlog** — the full list of features and user stories we want to build,
  in priority order.
- **Sprint Backlog** — the subset of stories we commit to for a single sprint.
- **Sprint** — a fixed two-week block where we build the committed stories.
- **Increment** — the working software produced at the end of a sprint.
- **Ceremonies** — the meetings that structure a sprint:
  - *Sprint Planning* — pick what we'll build this sprint.
  - *Daily Stand-up* — short daily sync on progress and blockers.
  - *Sprint Review* — show the working increment and get feedback.
  - *Retrospective* — discuss what went well and what to improve next sprint.

### Sprint 1 — Weeks 1 and 2

**Goal:** Stand up the core platform — accounts, roles, and the basic
employer-to-worker loop.

Sprint backlog:
- User authentication and role-based access
- Employer posts a staffing need
- Worker profile creation
- Basic matching (rule-based)
- Work-hour-cap compliance check
- Database schema and API foundation
- CI/CD pipeline set up

At the end of Sprint 1 we should have a working app where an employer can post a job
and the system can match an eligible worker.

### Sprint 2 — Weeks 3 and 4

**Goal:** Complete the value loop — training, reputation, admin, and deployment.

Sprint backlog:
- Paid peer-training workflow
- Trainer-payment calculation
- Placement lifecycle and booking
- Ratings and worker reputation
- Admin console and analytics
- Integration testing and bug fixes
- Deploy MVP1 to the test environment

We put the foundational features in Sprint 1 so we have something working to demo
early, and the features that make Crewbridge different (the paid peer-training and
trainer-payment logic) in Sprint 2, built on top of that foundation.

### When Agile makes sense

- The product is still evolving and requirements may change.
- You want working software early and often.
- Feedback matters and you want to adjust as you learn.

### Downsides

- Less predictable up front — scope can shift between sprints.
- Lighter on formal documentation, which has to be managed deliberately.
- Needs discipline with the ceremonies to work well.

---

## 3. Which approach we use and why

The two methods are not mutually exclusive for our purposes.

Waterfall fits the **coursework deliverables**. The assignment expects fixed,
documented artefacts — requirements, UML diagrams, ER design, and a clear plan. A
Waterfall view gives us that clean, phase-by-phase structure.

Agile fits the **actual build**. Crewbridge is still being shaped, the tutor is
helping refine the idea, and we expect to learn things while building. Working in two
two-week sprints lets us produce working software early, demo it, and adjust.

In practice we plan the project with the Waterfall phases for the documentation, and
execute the implementation in Agile sprints. This is a common and realistic way to
run a student project that is also meant to become a real product.

---

## 4. Tools

| Area | Tool |
|------|------|
| Backend | Python, Django, Django REST Framework |
| Frontend | React (Vite), Tailwind CSS |
| Database | PostgreSQL |
| Documentation | Confluence |
| Diagrams (UML, ER) | Visual Paradigm Online |
| Wireframes | Figma |
| Project management | Jira / Kanban board |
| Version control | Git / GitHub |
| CI/CD | GitHub Actions |
| Hosting (MVP) | Azure (student credits) or Render / Railway |
| Testing | Jest, React Testing Library, Mocha + Chai, Pytest-django |