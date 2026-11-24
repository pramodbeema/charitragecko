# Technical Certification & Security Architecture — CHARITRA for Firefox

This document provides complete technical disclosure for Mozilla Add-ons (AMO) certification and automated validation.

---

## 1. Compliance with AMO Policies

### No Remote Code Execution
- All scripts (`background.js`, `popup.js`, `storage.js`, `crypto.js`, `vault.js`, `welcome.js`) are packaged locally within the add-on archive.
- No `eval()`, no `new Function()`, no dynamic `<script>` tag injection.
- Zero external CDNs or remote dependencies.

### Zero Telemetry & Privacy
- **Data Collection**: None. Declared in `manifest.json` under `browser_specific_settings.gecko.data_collection_permissions.required: ["none"]`.
- No analytic trackers, no beacons, no external pingbacks.
- Operates entirely offline inside the client's browser profile.

---

## 2. Cryptographic Architecture

| Layer | Implementation | Purpose |
|---|---|---|
| **Cipher** | `AES-256-GCM` via native `crypto.subtle` | Authenticated encryption providing confidentiality and tamper detection. |
| **Key Derivation** | `PBKDF2-SHA256` with 310,000 rounds | OWASP-recommended iteration count preventing brute-force and dictionary attacks. |
| **Salt** | `crypto.getRandomValues(new Uint8Array(16))` | 16-byte cryptographically secure random salt generated per encryption. |
| **Password Storage** | Never stored on disk | Only a salted hash is kept in storage for login verification; the actual decryption key exists only in popup memory during active session. |
| **Data at Rest** | Base64 Ciphertext | Stored entries in `browser.storage.local` are unreadable blobs even if files on disk are inspected directly. |

---

## 3. Browser Permissions Justification

| Permission | Technical Reason |
|---|---|
| `history` | Required to delete matching visits to user-blocked domains via `chrome.history.deleteUrl()`. |
| `storage` | Required to store the encrypted vault ciphertext and user preferences in `chrome.storage.local`. |
| `tabs` | Required to inspect active tab URL and title when user blocks current site or when navigation occurs. |
| `webNavigation` | Required to detect `onCommitted` and `onHistoryStateUpdated` events for immediate history wiping (including SPAs). |
| `alarms` | Required for periodic history sweep (every 2-6 hours) and session auto-lock expiration checks. |
