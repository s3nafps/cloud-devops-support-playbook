# Client Discovery and Intake

Use this before any VPS, Docker, monitoring, backup, or automation work.

Goal: qualify the lead, capture the buyer's real wording, avoid secret sharing, and decide whether the request fits a fixed package or needs a custom quote.

## Rules

- Do not ask the client to paste passwords, private keys, `.env` files, or full database dumps into chat.
- Ask for symptoms, architecture shape, timeline, and outcome first.
- Keep the first call or chat focused on diagnosis and scope, not implementation promises.
- Capture exact buyer wording in the tracker. That language is demand evidence.
- If the request is vague, sell the audit first.

## What To Ask First

1. What is currently broken or at risk?
2. Is the app down, unstable, slow, or just missing monitoring/backups?
3. What is running right now: one VPS, multiple VPSs, Docker Compose, Nginx/Caddy, database?
4. When did the issue start?
5. What changed before the issue started?
6. How urgent is it: blocked revenue, internal tool, or non-urgent cleanup?
7. Who has server access on your side?
8. Do you need a diagnosis only, a fix, or a fix plus handover notes?
9. Do you already have backups?
10. Have you ever tested a restore?

## Secret-Safe Requests

Ask for these instead of secrets:

- screenshot of the error page,
- sanitized container status output,
- domain and public endpoint behavior,
- rough stack description,
- non-sensitive log excerpts,
- current backup method, if any,
- preferred maintenance window,
- whether SSH access exists already.

If deeper access is needed later, ask the client to create a temporary user or rotate credentials after the engagement.

## Qualification Paths

### Path 1: VPS Docker Health Check

Use when:

- app is down or unstable,
- ports, proxy, container restarts, disk, or memory look suspicious,
- the client mainly needs a fast written diagnosis.

Good fit wording:

- "My app is down on a VPS."
- "Docker is running but the site does not load."
- "Containers restart and I do not know why."

### Path 2: Monitoring and Alerts Setup

Use when:

- the app usually works but downtime is discovered too late,
- no one knows what to check first,
- the client wants a lightweight operations baseline.

Good fit wording:

- "We only know when users complain."
- "We need alerts and a simple runbook."

### Path 3: Backup and Restore Proof

Use when:

- the app is running but backups are weak or untested,
- the client fears data loss,
- there is no restore evidence.

Good fit wording:

- "We have backups but never tested them."
- "I need to know we can recover if the VPS dies."

## Disqualifiers

Do not force a fixed package when:

- the client wants full platform rebuild work,
- there are multiple environments with unclear ownership,
- Kubernetes or cloud IAM work dominates the request,
- they need 24/7 support immediately,
- they refuse written scope or outcome boundaries.

In those cases:

- offer a paid audit first, or
- decline if access, urgency, or scope is unsafe.

## 15-Minute Discovery Flow

### Minute 1-3

- confirm the business problem,
- confirm urgency,
- confirm who owns access.

### Minute 4-7

- map the stack at a high level,
- identify symptoms,
- identify recent changes.

### Minute 8-11

- confirm backups, monitoring, and current operating process,
- confirm whether the client needs diagnosis only or implementation too.

### Minute 12-15

- recommend one fixed package or a paid audit,
- repeat scope boundaries,
- state deliverable and timeline,
- tell them not to send secrets in chat.

## Scope Close Script

Use this after the discovery call:

> Based on what you described, the best starting point is the [package name]. I will focus on [scope]. Deliverables are [deliverables]. I do not need passwords or private keys in chat. If access is needed, use a temporary method on your side and rotate it after the work.

## What To Record

Record every lead in:

- `trackers/freelance-lead-validation-tracker.csv`
- `trackers/client-intake-call-notes.csv`

Capture:

- the exact problem wording,
- urgency,
- stack shape,
- package fit,
- objections,
- next step,
- whether the same problem repeats across leads.

## Evidence Threshold Before Building More

Do not expand into a new offer, automation product, or SaaS unless:

- at least 5 leads describe the same problem clearly,
- at least 2 leads ask for the same outcome,
- at least 1 lead pays for a manual version,
- the delivery steps are stable enough to document.
