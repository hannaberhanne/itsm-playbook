# APP_ROUTER

Generic example. The strings below are illustrative; a live router uses the exact short descriptions found in the organization's ticket export.

Purpose: Route tickets about a core business application (for example an EHR) to the correct sub-model based on the user's exact wording.

Rule: Do not infer. Match the wording to a bucket below. If nothing matches, use the general application model and flag the wording for review.

---

## A) SIGN-IN / ACCOUNT FAILURES

The application rejects the user or their account is locked inside the app.

Example strings:
- Account locked in [app]
- Unable to log into [app]
- [app] lockout
- AD and [app] account locked

If the domain account is also locked, start with DIRECTORY_LOCKOUT_AD.

---

## B) LAUNCH FAILURES

The application will not open or a session cannot start.

Example strings:
- [app] not opening
- [app] won't launch
- Virtual desktop not opening [app]

---

## C) RUNTIME FREEZE / NOT RESPONDING

The application opens but hangs or the session freezes.

Example strings:
- [app] not responding
- [app] froze
- Session stuck

---

## D) MISSING CONFIGURATION / ICON / PERIPHERAL

Something expected is missing inside the application, or a device does not work with it.

Example strings:
- No [app] icon
- Unable to scan into [app]
- Keyboard not working in [app]

---

## E) RECORD LOCKED BY ANOTHER USER

Concurrency lock: another session has the record open.

Example strings:
- Record locked in [app] by another user
