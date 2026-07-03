# Fixed-Price Freelance Service Packages

The packages are intentionally narrow. They solve real pain quickly and create portfolio evidence. Quote global clients in USD/EUR when possible; convert to DA only at payment time because exchange rates move.

## Package 1: VPS Docker Rescue Audit

**Price:** USD 79 starter price  
**Delivery:** 24-48 hours  
**Best buyer:** founder, indie hacker, small agency, or developer with a Docker app failing on a VPS.

### Customer Problem

"My app is down, Docker is confusing, SSL/DNS may be broken, and I need someone to tell me what is wrong and fix the obvious issue."

### Included

- Inspect one Linux VPS and one Docker/Docker Compose app.
- Check containers, logs, ports, disk, memory, DNS/HTTPS symptoms, and startup commands.
- Fix one clearly scoped deployment/runtime issue if it is safe and within access.
- Deliver a short incident report with before/after evidence and next steps.
- Provide a simple health-check command for the client.

### Not Included

- Rewriting the application.
- Fixing unknown application bugs.
- Database recovery after corruption.
- Kubernetes.
- Ongoing maintenance.

### Deliverables

- `incident-report.md`
- screenshots of before/after state
- command summary
- recommended next actions

### Upsell

Offer Package 2 if the client has no backup/restore proof.

## Package 2: Backup And Restore Safety Net

**Price:** USD 149 starter price  
**Delivery:** 2-3 days  
**Best buyer:** small business or solo founder with a working VPS app but no tested backup.

### Customer Problem

"If this server dies or someone deletes data, I do not know how to recover."

### Included

- Identify app data locations: Docker volumes, bind mounts, database dumps where applicable.
- Add a backup script for one Docker Compose project.
- Create local backup archive with checksum.
- Run one restore test into a separate test volume or documented safe target.
- Add a cron example for scheduled backups.
- Deliver a backup/restore runbook.

### Not Included

- Paid storage fees.
- Full disaster recovery architecture.
- Legal/compliance backup guarantees.
- Unlimited databases or multiple apps.

### Deliverables

- backup script or configured command
- restore test evidence
- checksum file
- runbook
- screenshots

### Upsell

Offer monitoring if the client also lacks uptime checks.

## Package 3: Monitoring And Handover Setup

**Price:** USD 199 starter price  
**Delivery:** 2-4 days  
**Best buyer:** small team with a VPS app that only discovers downtime from customers.

### Customer Problem

"I need to know when my app is down and I need simple notes for what to check first."

### Included

- Set up Uptime Kuma or lightweight endpoint checks for up to 5 URLs.
- Add basic Docker container health visibility where possible.
- Add CPU/disk/memory check commands.
- Create a first-response runbook for common issues.
- Create a handover document for the client or developer.

### Not Included

- 24/7 on-call.
- Complex observability stack.
- Prometheus/Grafana architecture unless separately scoped.
- Application code changes.

### Deliverables

- monitoring dashboard screenshot
- endpoint list
- first-response runbook
- alert test screenshot
- handover note

### Optional Add-On

Monthly light maintenance can be offered only after at least one fixed-price delivery succeeds. Start simple: one monthly check, backup verification, and short status report.

## Pricing Rule

Do not compete only on price. Compete on clarity:

- fixed scope,
- fast delivery,
- screenshots,
- written handover,
- no secret leakage,
- restore proof,
- clear exclusions.
