# DIRECTORY_LOCKOUT_AD

Generic example. Field values, group names and work-note patterns are illustrative.

---

## 1. PURPOSE

Domain-level Active Directory account lockout caused by repeated failed sign-in attempts.
Restoring access requires unlocking the account in Active Directory Users and Computers (ADUC).

---

## 2. INCIDENT TEMPLATE (ServiceNow Entry)

### Top Fields
- Category: Access
- Subcategory: Account Lockout
- Assignment Group: Service Desk
- Impact: 3 - Low (2 - Medium if a provider or other critical role is blocked from working)
- Urgency: 2 - Medium
- Configuration Item: User's AD account (if searchable)

---

### Short Description Format

AD Account Locked - [User Full Name]

---

### Description (Customer Visible)

User reports they cannot sign in to their domain account.
Error indicates the account is locked.

---

### Work Notes (Internal Baseline)

Verified identity per policy.
Confirmed account locked in ADUC.
Unlocked account in ADUC.
User confirmed successful sign-in.
Incident resolved.

---

### Work Note Variants

If the user reset their password:
User reset password through the self-service password portal.

If cached credentials were the cause:
Removed stored credentials from Credential Manager and restarted the device.

---

### Closure Information

Close Code: Resolved by Service Desk

Close Notes:
Account was locked in AD. Unlocked and confirmed successful sign-in with the user.

---

## 3. WHEN NOT TO USE

- Account is disabled, not locked
- A security alert or suspicious sign-in pattern is present
- The lock is inside an application only (EHR, single sign-on, MFA app)
- The same account keeps locking (recurring pattern)

---

## 4. ESCALATION RULE

Escalate to the security team only if a suspicious authentication pattern is observed.

---

## 5. VERBATIM WORK NOTE PATTERNS (DATA-OBSERVED)

In a live playbook this section lists the exact phrases analysts used in past tickets, pulled from the export. Illustrative shape:

- Unlocked.
- Unlocked account in AD. User can now log in.
- Unlocked in ADUC. User reset password through self-service.

---

## 6. DATA BASIS

- Total tickets: [count from coverage analysis]
- % of total dataset: [share of troubleshooting volume]
- Sample size validated: [number of tickets read by hand]
- Last validation date: [date]
