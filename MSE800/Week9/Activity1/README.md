# Crewbridge — Development Methodology

Crewbridge is a managed workforce platform for the NZ hospitality sector. It
connects short-staffed venues with work-ready staff, and handles the sourcing,
vetting, compliance, and paid peer-training on the employer's behalf. The roles in
the system are Employer, Worker, Trainer, and Admin.

---

## Waterfall

### What it is

Waterfall is a sequential approach. You finish one phase, sign it off, then move to
the next. You don't start design until requirements are agreed, and you don't start
coding until design is done. It works well when the requirements are clear and
unlikely to change much, because there isn't a lot of going back.

### Phases

**1. Requirements Analysis**
Gather and document what the system needs to do. For Crewbridge this means defining
the four roles (Employer, Worker, Trainer, Admin), the functional requirements (post
a job, match a worker, run a placement, assign training, calculate trainer payment,
rate a worker), and the non-functional requirements (security, performance, and the
compliance rules around work-hour limits). Output is a requirements document that
everyone agrees on.

**2. System Design**
Decide how the system will be built. This is where we produce the architecture, the
database design (ER diagram), the UML diagrams (use-case, class, sequence), the API
contracts, and the UI wireframes in Figma. The work-hour-cap compliance engine is
designed here too. Output is a design specification.

**3. Implementation**
Write the code based on the design. Backend in Django + Django REST Framework,
frontend in React, database in PostgreSQL. This includes the matching, placement,
paid-training, and compliance modules. Output is the working application.

**4. Testing**
Verify the system against the requirements. Unit and integration tests using Jest
and React Testing Library on the frontend, and Pytest-django / DRF test classes on
the backend. Particular focus on the compliance engine and the trainer-payment
calculation, since those are the parts most likely to cause real problems if wrong.
Output is a tested, working build with bugs fixed.

**5. Deployment**
Release the application to a test environment through the CI/CD pipeline (GitHub
Actions), deployed to Azure or Render. Run smoke tests to confirm it works in the
deployed environment.

**6. Maintenance**
Keep the system running. Fix bugs, monitor it, respond to user feedback, and plan
the future roadmap (real payments, background checks, expansion into other
verticals).

### When Waterfall makes sense

- The requirements are well understood and stable.
- The project is documentation-heavy (which suits coursework, where the design
  documents and diagrams are graded deliverables).
- You need a clear, predictable plan from start to finish.

### Downsides

- Hard to change direction once you're partway through.
- You don't see working software until late in the process.
- If a requirement was misunderstood early, you often don't find out until testing.
