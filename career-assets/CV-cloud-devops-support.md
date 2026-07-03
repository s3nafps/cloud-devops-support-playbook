# Cloud/DevOps Support CV Positioning Draft

Use this as the new CV direction. Replace bracketed fields and keep only claims you can prove with GitHub commits, screenshots, deployments, or written references.

## Target CV Header

**Mohamed Senator**  
Algeria | Remote / EMEA | [Email] | [Phone] | [LinkedIn] | [GitHub] | [Portfolio]

**Cloud / DevOps Support Engineer**  
Linux, Docker, VPS deployments, monitoring, backup automation, troubleshooting, and customer-facing technical support.

## Professional Summary

Cloud/DevOps support-focused engineer with hands-on experience deploying and troubleshooting Linux VPS applications, Docker Compose stacks, DNS/Cloudflare routing, production logs, and backup/restore workflows. Strong at turning unclear infrastructure problems into repeatable runbooks, scripts, monitoring checks, and documented fixes. Looking for Cloud Support, DevOps Support, Linux Support, or Junior DevOps roles where practical debugging, clear communication, and operational reliability matter.

## Core Skills

- Linux support: Ubuntu server basics, SSH workflows, services, logs, permissions, firewall checks.
- Containers: Docker, Docker Compose, container logs, health checks, volumes, restart policies.
- Web operations: DNS, reverse proxy concepts, HTTPS/SSL, Cloudflare routing, deployment checks.
- Monitoring: endpoint health checks, uptime monitoring, incident notes, status evidence.
- Backup and recovery: Docker volume backups, restore testing, checksum verification, cron-ready scripts.
- Automation: Bash scripts, PowerShell on Windows, GitHub CLI, repeatable runbooks.
- Troubleshooting: 502/5xx errors, failed builds, missing dependencies, misconfigured start commands, database/schema startup issues.
- Communication: support notes, customer updates, handover docs, case-study writing.

## Selected Projects

### CloudOps Rescue Kit
GitHub: https://github.com/s3nafps/cloudops-rescue-kit

Built a practical VPS/Docker operations toolkit for small teams and solo founders who need deployment diagnostics, monitoring, backups, and incident handover without a heavy platform.

- Created Bash scripts for diagnostics, endpoint checks, Docker Compose volume backups, restore testing, and preflight checks.
- Wrote runbooks for VPS rescue, backup/restore, monitoring, screenshots, and customer incident reporting.
- Designed the project around publishable evidence: before/after screenshots, backup checksums, restore test proof, and case-study structure.
- Focused on low-cost tools: Docker, Bash, cron, Uptime Kuma, GitHub, and a small VPS or local VM.

### Production VPS/Docker Deployment And Troubleshooting
Use only if you can show proof from the deployed project.

- Deployed and stabilized a production web application using Docker Compose, Dokploy/Traefik-style routing, Cloudflare, and container logs.
- Fixed production build/startup issues by tracing missing frontend dependencies, start commands, schema bootstrap steps, and runtime logs.
- Improved admin-facing scraper/run visibility by surfacing run status, error summaries, and operational logs.
- Repaired ingestion by tracing the real backing API instead of relying on a stale client-rendered HTML page.

### Secure VPS Dashboard Access
Use only if you can show proof from the VPS work.

- Routed a self-hosted dashboard through Cloudflare Tunnel/Access and verified that public access worked through the protected hostname.
- Blocked direct-origin access to a Docker-published dashboard port using firewall/Docker chain controls after confirming UFW alone was not sufficient.
- Documented the final operational state and service checks for future maintenance.

### Windows Developer Environment Bootstrap
Use only if relevant to the role.

- Set up Git, Node.js, Python, GitHub CLI, npm, and package-manager workflows on Windows PowerShell.
- Fixed PowerShell execution policy issues affecting npm/npx and verified the machine with `gh auth status`, package-manager checks, and build commands.
- Documented repeatable setup steps for future developer onboarding.

## Experience Section Rewrite Pattern

Use this for each previous job or project:

**[Role / Project Name]** - [Company or Personal Project]  
[Dates] | [Location / Remote]

- Supported [system/application] by troubleshooting [Linux/Docker/network/build/database] issues using logs, command-line checks, and documented runbooks.
- Reduced repeated manual work by creating [script/runbook/checklist] for [deployment/backup/monitoring/support].
- Communicated technical findings clearly to [client/team/user], including risk, next steps, and verification evidence.
- Improved reliability by adding [health check/backup/restore test/monitoring/alerting].

## ATS Keyword Bank

Use naturally across the CV and LinkedIn profile:

Cloud Support, DevOps Support, Linux Support, Technical Support Engineer, Application Support, Docker, Docker Compose, VPS, Ubuntu, Nginx, Traefik, Cloudflare, DNS, SSL, HTTPS, Bash, PowerShell, GitHub Actions, CI/CD, Monitoring, Uptime, Grafana, Prometheus, Uptime Kuma, Backup, Restore, Incident Response, Troubleshooting, Logs, Scripting, Automation, Customer Support, Runbooks.

## CV Proof Checklist

Before sending the CV:

- Add public GitHub link to CloudOps Rescue Kit.
- Add one case-study link or portfolio page.
- Add screenshots or a short demo video link if possible.
- Remove any bullet that sounds impressive but cannot be proven.
- Keep the CV to 1 page if applying junior/support roles; 2 pages only if you have enough relevant evidence.
