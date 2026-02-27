# Check yr Priv — Demo

A self-contained demo version of [Check yr Priv](https://github.com/BardSec/check-yr-priv) pre-loaded with **realistic fictional data** from the fake tenant **Contoso Technologies Ltd**.

Designed for screenshots, documentation, and demo videos — no Microsoft account or Azure App Registration required.

---

## What's different from production

| | Production | Demo |
|---|---|---|
| Auth | Microsoft OAuth2 (MSAL) | Click to sign in instantly |
| Data | Live Microsoft Graph API | Static fictional data |
| Azure credentials | Required | Not required |
| Redis | Session storage | Session storage (unchanged) |
| Frontend | Identical | Identical + "Demo" badge |

---

## Demo data overview

**Tenant:** Contoso Technologies Ltd (`4a7f3b21-e89c-4d56-b12a-8f90c4d5e6a7`)

**18 active assignments across 14 roles:**

| Role | Principals | Protected? |
|---|---|---|
| Global Administrator | Alice Chen, Bob Martinez, IT-Admins (group) | ✅ CA + MFA |
| Privileged Role Administrator | David Kim | ✅ CA + MFA |
| Security Administrator | Carol Johnson, Jasmine Patel | ✅ CA + MFA |
| Conditional Access Administrator | Jasmine Patel | ✅ CA + MFA |
| Exchange Administrator | Eve Thompson | ❌ Unprotected |
| User Administrator | Frank Wilson | ❌ Unprotected |
| SharePoint Administrator | Henry Baker | ❌ Unprotected |
| Cloud Application Administrator | Kevin O'Brien | ❌ Unprotected |
| Application Administrator | DevOps-Automation (SP) | ❌ Unprotected |
| Intune Administrator | Grace Liu | ❌ Unprotected |
| Hybrid Identity Administrator | Liam Nguyen | ❌ Unprotected |
| Reports Reader | Maya Patel | — |
| License Administrator | Isabella Rodriguez | — |
| Groups Administrator | Liam Nguyen | — |

**6 PIM-eligible assignments:** Isabella (Global Admin), Carol (User Admin), Kevin (Security Admin), David (Hybrid Identity Admin), Alice (Priv Auth Admin), Bob (Auth Policy Admin)

**5 Conditional Access policies:**
1. Require MFA — Global Administrators *(enforced)*
2. Require MFA — Security & CA Admins *(enforced, phishing-resistant)*
3. Block Legacy Authentication *(enforced, no MFA grant)*
4. MFA for All Employees *(report-only — not enforced)*
5. Require Compliant Device — Finance Apps *(enforced, no MFA grant)*

**Dashboard result:** 7 of 14 high-privilege active assignments protected (50%) · 7 unprotected roles flagged in alert banner

---

## Quick start

```bash
docker compose up --build
```

Then open **http://localhost** and click **Sign in with Microsoft** — you'll be logged in instantly as `alice.chen@contoso.com`.

No `.env` file needed. Optionally copy `.env.example` to `.env` to override the secret key.

---

## Architecture

Identical to production — same Docker Compose, same nginx proxy, same React frontend, same FastAPI backend structure. The only differences are:

- `backend/app/config.py` — Azure credential fields removed
- `backend/app/routers/auth.py` — OAuth flow replaced with instant demo login
- `backend/app/routers/roles.py` — calls `demo_data` instead of `graph`
- `backend/app/services/demo_data.py` — static fictional Graph API responses
- `frontend/src/components/Layout.jsx` — "Demo" badge in header

To switch back to production, swap in the production versions of those four backend files and the production `config.py`.
