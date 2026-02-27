"""
Static demo data — mimics Microsoft Graph API responses.

This module replaces services/graph.py for the demo version of the app.
All data is fictional and intended for screenshots, documentation, and demo videos.
The fake tenant "Contoso Technologies Ltd" has a realistic mix of:
  - Protected high-privilege roles (Global Admin, Security Admin)
  - Several UNPROTECTED high-privilege roles (triggering the alert banner)
  - PIM-eligible assignments for key roles
  - Multiple CA policies (some enforcing MFA, some not)
"""

# ---------------------------------------------------------------------------
# Demo tenant
# ---------------------------------------------------------------------------
_TENANT_ID = "4a7f3b21-e89c-4d56-b12a-8f90c4d5e6a7"
_TENANT_NAME = "Contoso Technologies Ltd"

# ---------------------------------------------------------------------------
# Role definition IDs (real Entra built-in role GUIDs)
# ---------------------------------------------------------------------------
_GLOBAL_ADMIN      = "62e90394-69f5-4237-9190-012177145e10"
_PRIV_ROLE_ADMIN   = "e8611ab8-c189-46e8-94e1-60213ab1f814"
_SEC_ADMIN         = "194ae4cb-b126-40b2-bd5b-6091b380977d"
_EXCHANGE_ADMIN    = "29232cdf-9323-42fd-ade2-1d097af3e4de"
_SHAREPOINT_ADMIN  = "f28a1f50-f6e7-4571-818b-6a12f2af6b6c"
_USER_ADMIN        = "fe930be7-5e62-47db-91af-98c3a49a38b1"
_PRIV_AUTH_ADMIN   = "7be44c8a-adaf-4e2a-84d6-ab2649e08a13"
_HYBRID_ID_ADMIN   = "8ac3fc64-6eca-42ea-9e69-59f4c7b60eb2"
_CLOUD_APP_ADMIN   = "158c047a-c907-4556-b7ef-446551a6b5f7"
_APP_ADMIN         = "9b895d92-2cd3-44c7-9d02-a6ac2d5ea5c3"
_CA_ADMIN          = "b1be1c3e-b65d-4f19-8427-f6fa0d97feb9"
_AUTH_POLICY_ADMIN = "0526716b-113d-4c15-b2c8-68e3c22b9f80"
_INTUNE_ADMIN      = "3a2c62db-5318-420d-8d74-23affee5d9d5"

# Non-high-privilege roles
_REPORTS_READER    = "88d8e3e3-8f55-4a1e-953a-9b9898b8876b"
_LICENSE_ADMIN     = "4d6ac14f-3453-41d0-bef9-a3e0c569773a"
_GROUPS_ADMIN      = "fdd7a751-b60b-444a-984c-02652fe8fa1c"
_USAGE_REPORTS     = "75934031-6c7e-415a-99d7-48dbd49e875e"

# ---------------------------------------------------------------------------
# Principals (users, groups, service principals)
# ---------------------------------------------------------------------------
_PRINCIPALS: dict[str, dict] = {
    "u-alice": {
        "id": "u-alice",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Alice Chen",
        "userPrincipalName": "alice.chen@contoso.com",
    },
    "u-bob": {
        "id": "u-bob",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Bob Martinez",
        "userPrincipalName": "bob.martinez@contoso.com",
    },
    "u-carol": {
        "id": "u-carol",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Carol Johnson",
        "userPrincipalName": "carol.johnson@contoso.com",
    },
    "u-david": {
        "id": "u-david",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "David Kim",
        "userPrincipalName": "david.kim@contoso.com",
    },
    "u-eve": {
        "id": "u-eve",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Eve Thompson",
        "userPrincipalName": "eve.thompson@contoso.com",
    },
    "u-frank": {
        "id": "u-frank",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Frank Wilson",
        "userPrincipalName": "frank.wilson@contoso.com",
    },
    "u-grace": {
        "id": "u-grace",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Grace Liu",
        "userPrincipalName": "grace.liu@contoso.com",
    },
    "u-henry": {
        "id": "u-henry",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Henry Baker",
        "userPrincipalName": "henry.baker@contoso.com",
    },
    "u-isabella": {
        "id": "u-isabella",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Isabella Rodriguez",
        "userPrincipalName": "isabella.rodriguez@contoso.com",
    },
    "u-jasmine": {
        "id": "u-jasmine",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Jasmine Patel",
        "userPrincipalName": "jasmine.patel@contoso.com",
    },
    "u-kevin": {
        "id": "u-kevin",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Kevin O'Brien",
        "userPrincipalName": "kevin.obrien@contoso.com",
    },
    "u-liam": {
        "id": "u-liam",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Liam Nguyen",
        "userPrincipalName": "liam.nguyen@contoso.com",
    },
    "u-maya": {
        "id": "u-maya",
        "@odata.type": "#microsoft.graph.user",
        "displayName": "Maya Patel",
        "userPrincipalName": "maya.patel@contoso.com",
    },
    "g-itadmins": {
        "id": "g-itadmins",
        "@odata.type": "#microsoft.graph.group",
        "displayName": "IT-Admins",
    },
    "sp-devops": {
        "id": "sp-devops",
        "@odata.type": "#microsoft.graph.servicePrincipal",
        "displayName": "DevOps-Automation",
    },
}

# ---------------------------------------------------------------------------
# Helper builders
# ---------------------------------------------------------------------------

def _role(role_id: str, name: str) -> dict:
    return {"id": role_id, "displayName": name}


def _active(
    uid: str,
    role_id: str,
    role_name: str,
    member_type: str = "Direct",
    start: str = "2024-01-15T00:00:00Z",
    end: str | None = None,
) -> dict:
    return {
        "id": f"asgn-active-{uid}-{role_id[:8]}",
        "principalId": uid,
        "roleDefinitionId": role_id,
        "principal": _PRINCIPALS[uid],
        "roleDefinition": _role(role_id, role_name),
        "memberType": member_type,
        "startDateTime": start,
        "endDateTime": end,
    }


def _eligible(
    uid: str,
    role_id: str,
    role_name: str,
    start: str = "2024-06-01T00:00:00Z",
    end: str = "2026-12-31T23:59:59Z",
) -> dict:
    return {
        "id": f"asgn-elig-{uid}-{role_id[:8]}",
        "principalId": uid,
        "roleDefinitionId": role_id,
        "principal": _PRINCIPALS[uid],
        "roleDefinition": _role(role_id, role_name),
        "memberType": "Direct",
        "startDateTime": start,
        "endDateTime": end,
    }


# ---------------------------------------------------------------------------
# Public API — same signatures as services/graph.py (minus the token arg)
# ---------------------------------------------------------------------------

def get_organization() -> dict:
    return {
        "id": _TENANT_ID,
        "displayName": _TENANT_NAME,
        "verifiedDomains": [{"name": "contoso.com", "isDefault": True}],
    }


def get_active_role_assignments() -> list[dict]:
    """
    Returns 18 active assignments across 14 roles.
    Protected (via CA policies): Global Admin, Priv Role Admin,
                                  Security Admin, CA Admin  → 7 assignments
    Unprotected:                  Exchange, User, SharePoint, Cloud App,
                                  App, Intune, Hybrid Identity Admin     → 7 assignments
    Non-high-privilege:           Reports Reader, License Admin,
                                  Groups Admin, Usage Reports Reader      → 4 assignments
    """
    return [
        # ── Global Administrator (CA + MFA — Policy 1) ───────────────────────
        _active("u-alice",    _GLOBAL_ADMIN, "Global Administrator",
                start="2023-09-12T00:00:00Z"),
        _active("u-bob",      _GLOBAL_ADMIN, "Global Administrator",
                start="2022-04-03T00:00:00Z"),
        _active("g-itadmins", _GLOBAL_ADMIN, "Global Administrator",
                member_type="Group", start="2024-01-08T00:00:00Z"),

        # ── Privileged Role Administrator (CA + MFA — Policy 1) ─────────────
        _active("u-david", _PRIV_ROLE_ADMIN, "Privileged Role Administrator",
                start="2024-02-20T00:00:00Z", end="2026-06-30T23:59:59Z"),

        # ── Security Administrator (CA + auth-strength — Policy 2) ──────────
        _active("u-carol",   _SEC_ADMIN, "Security Administrator",
                start="2023-11-20T00:00:00Z"),
        _active("u-jasmine", _SEC_ADMIN, "Security Administrator",
                start="2024-03-15T00:00:00Z"),

        # ── Conditional Access Administrator (CA — Policy 2) ─────────────────
        _active("u-jasmine", _CA_ADMIN, "Conditional Access Administrator",
                start="2024-03-15T00:00:00Z"),

        # ── Exchange Administrator (NOT protected) ────────────────────────────
        _active("u-eve", _EXCHANGE_ADMIN, "Exchange Administrator",
                start="2023-07-01T00:00:00Z"),

        # ── User Administrator (NOT protected) ────────────────────────────────
        _active("u-frank", _USER_ADMIN, "User Administrator",
                start="2024-04-10T00:00:00Z"),

        # ── SharePoint Administrator (NOT protected) ───────────────────────────
        _active("u-henry", _SHAREPOINT_ADMIN, "SharePoint Administrator",
                start="2023-10-05T00:00:00Z"),

        # ── Cloud Application Administrator (NOT protected, time-limited) ─────
        _active("u-kevin", _CLOUD_APP_ADMIN, "Cloud Application Administrator",
                start="2025-01-01T00:00:00Z", end="2026-05-15T23:59:59Z"),

        # ── Application Administrator (NOT protected — service principal) ─────
        _active("sp-devops", _APP_ADMIN, "Application Administrator",
                start="2024-06-15T00:00:00Z"),

        # ── Intune Administrator (NOT protected, time-limited) ────────────────
        _active("u-grace", _INTUNE_ADMIN, "Intune Administrator",
                start="2024-09-01T00:00:00Z", end="2026-08-31T23:59:59Z"),

        # ── Hybrid Identity Administrator (NOT protected) ─────────────────────
        _active("u-liam", _HYBRID_ID_ADMIN, "Hybrid Identity Administrator",
                start="2023-12-01T00:00:00Z"),

        # ── Lower-privilege roles ─────────────────────────────────────────────
        _active("u-maya",     _REPORTS_READER, "Reports Reader",
                start="2025-02-01T00:00:00Z"),
        _active("u-isabella", _LICENSE_ADMIN,  "License Administrator",
                start="2024-11-01T00:00:00Z"),
        _active("u-liam",     _GROUPS_ADMIN,   "Groups Administrator",
                start="2024-08-15T00:00:00Z"),
        _active("u-carol",    _USAGE_REPORTS,  "Usage Summary Reports Reader",
                start="2024-01-01T00:00:00Z"),
    ]


def get_eligible_role_assignments() -> list[dict]:
    """
    Returns 6 PIM-eligible assignments — roles that can be activated on demand.
    """
    return [
        _eligible("u-isabella", _GLOBAL_ADMIN,    "Global Administrator",
                  start="2025-01-01T00:00:00Z", end="2026-12-31T23:59:59Z"),
        _eligible("u-carol",    _USER_ADMIN,       "User Administrator",
                  start="2024-06-01T00:00:00Z", end="2026-12-31T23:59:59Z"),
        _eligible("u-kevin",    _SEC_ADMIN,        "Security Administrator",
                  start="2025-03-01T00:00:00Z", end="2026-09-30T23:59:59Z"),
        _eligible("u-david",    _HYBRID_ID_ADMIN,  "Hybrid Identity Administrator",
                  start="2024-07-01T00:00:00Z", end="2026-12-31T23:59:59Z"),
        _eligible("u-alice",    _PRIV_AUTH_ADMIN,  "Privileged Authentication Administrator",
                  start="2024-10-01T00:00:00Z", end="2026-10-01T23:59:59Z"),
        _eligible("u-bob",      _AUTH_POLICY_ADMIN, "Authentication Policy Administrator",
                  start="2025-04-01T00:00:00Z", end="2026-12-31T23:59:59Z"),
    ]


def get_ca_policies() -> list[dict]:
    """
    Returns 5 Conditional Access policies:
      1. Require MFA for Global + Privileged Role Admins  (enforced)
      2. Require phishing-resistant MFA for Security + CA Admins  (enforced)
      3. Block legacy authentication for named accounts  (enforced, no MFA grant)
      4. MFA for All Employees — REPORT ONLY (not enforced)
      5. Require compliant device for finance apps  (enforced, no MFA grant)
    """
    return [
        # Policy 1: MFA for the most sensitive admin roles
        {
            "id": "ca-policy-001",
            "displayName": "Require MFA — Global Administrators",
            "state": "enabled",
            "conditions": {
                "users": {
                    "includeRoles": [_GLOBAL_ADMIN, _PRIV_ROLE_ADMIN],
                    "includeUsers": [],
                },
                "clientAppTypes": ["all"],
            },
            "grantControls": {
                "operator": "OR",
                "builtInControls": ["mfa"],
            },
        },
        # Policy 2: Phishing-resistant MFA for security team roles
        {
            "id": "ca-policy-002",
            "displayName": "Require MFA — Security & CA Admins",
            "state": "enabled",
            "conditions": {
                "users": {
                    "includeRoles": [_SEC_ADMIN, _CA_ADMIN],
                    "includeUsers": [],
                },
                "clientAppTypes": ["all"],
            },
            "grantControls": {
                "operator": "OR",
                "builtInControls": [],
                "authenticationStrength": {
                    "id": "00000000-0000-0000-0000-000000000004",
                    "displayName": "Phishing-resistant MFA",
                },
            },
        },
        # Policy 3: Block legacy auth for specific named accounts (no MFA grant)
        {
            "id": "ca-policy-003",
            "displayName": "Block Legacy Authentication",
            "state": "enabled",
            "conditions": {
                "users": {
                    "includeUsers": [
                        "u-alice", "u-bob", "u-carol",
                        "u-david", "u-jasmine",
                    ],
                },
                "clientAppTypes": ["exchangeActiveSync", "other"],
            },
            "grantControls": {
                "operator": "OR",
                "builtInControls": ["block"],
            },
        },
        # Policy 4: Report-only — doesn't count as enforced protection
        {
            "id": "ca-policy-004",
            "displayName": "MFA for All Employees (Report Only)",
            "state": "enabledForReportingButNotEnforced",
            "conditions": {
                "users": {
                    "includeUsers": ["All"],
                },
            },
            "grantControls": {
                "operator": "OR",
                "builtInControls": ["mfa"],
            },
        },
        # Policy 5: Compliant device for finance apps — no MFA control
        {
            "id": "ca-policy-005",
            "displayName": "Require Compliant Device — Finance Apps",
            "state": "enabled",
            "conditions": {
                "users": {
                    "includeUsers": ["u-isabella", "u-maya"],
                },
                "clientAppTypes": ["browser"],
            },
            "grantControls": {
                "operator": "OR",
                "builtInControls": ["compliantDevice"],
            },
        },
    ]
