# GenAI-Powered Learning Management System (LMS)

Production-oriented BSCS Final Year Project based on the existing six-module SRS. The six modules are preserved and are not replaced.

## Modules
1. Curriculum Management
2. Course Management
3. Course Offering & Student Registration
4. Course Progress Monitoring
5. Personalized Feedback on Assessment & Stakeholders
6. CipherBot – AI Learning Assistant (RAG-Based)

## Architecture
React + TypeScript frontend, Node.js/Express API, PostgreSQL/Prisma, Redis, separate FastAPI AI service, Docker Compose, CI/CD foundation and k6 load-testing starter.

## Run locally
Copy `.env.example` to `.env`, then run `docker compose up --build`.
Open `http://localhost:5173`; API health is `http://localhost:4000/health`.

## Production scaling
Use managed PostgreSQL/Redis/object storage, CDN/WAF, multiple stateless API replicas behind a load balancer, background workers and centralized monitoring. Actual 2,000+ concurrent-user performance must be measured on production-like infrastructure; no benchmark numbers are fabricated.

## Security
Secrets belong in environment/secret-manager configuration. Authentication uses Argon2 password hashing and short-lived JWTs; API security includes Helmet, CORS and rate limiting.
