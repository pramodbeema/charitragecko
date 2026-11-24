# AMO Reviewer Notes for CHARITRA (Gecko MV3)

Use these pre-tested notes when submitting **CHARITRA** to the Mozilla Add-ons (AMO) Developer Hub.

---

## 1. Quick Copy Options (Handling AMO Character Limits)

### Option A: Ultra-Short (< 250 characters)
```text
Desktop privacy vault extension with Metro UI. Blocks domains from browser history and stores visits in client-side AES-256-GCM encrypted vault.
Test:
1. Open popup, set master password
2. Add "example.com"
3. Visit example.com -> wiped from history in 1.5s
```

### Option B: Short (< 500 characters) — ⭐ Recommended
```text
CHARITRA is a private browsing history vault with Windows Phone Metro styling.
Zero remote code. Zero data collection (data_collection_permissions: none).

How to test:
1. Click toolbar icon to open first-run setup; set master password (e.g. TestPass123).
2. On Dashboard, type "example.com" and click "+ BLOCK".
3. Visit https://example.com in any tab.
4. Open history (Ctrl+H) -> visit is wiped within 1.5 seconds.
5. Open extension popup -> enter password -> Vault tab displays encrypted visit.
```

### Option C: Detailed (< 1000 characters)
```text
CHARITRA is a zero-knowledge private browsing history vault built with authentic Windows Phone / Nokia Lumia Metro UI.

Test instructions for reviewers:
1. First Run: Click the toolbar icon. The first-run setup wizard appears. Select a theme (Dark/Light/System) and set a vault password (e.g. "TestPassword123").
2. Domain Blocking: On the Dashboard or Blocked tab, add a domain (e.g. "example.com" or "wikipedia.org").
3. Verification: Open a new tab and navigate to the blocked domain (e.g. https://example.com). Wait 1.5 seconds.
4. History Scrubbing: Press Ctrl+H (or Library -> History) in Firefox. Notice the visit has been automatically removed.
5. Vault Verification: Click the extension icon. Enter the master password to unlock. Switch to the Vault tab to view the vaulted visit with timestamp and page title.
6. Clean Wipe / Security: In Settings, try the Wipe Data option to completely erase stored ciphertext.

Architecture:
- 100% offline & client-side (AES-256-GCM via native Web Crypto API crypto.subtle).
- PBKDF2-SHA256 with 310,000 iterations.
- Zero tracking, zero analytics, zero external network requests.
```

---

## 2. Technical Review Reference

| Field | Detail |
|---|---|
| **Extension ID** | `charitra@pramodbeema` |
| **Manifest Version** | MV3 (`manifest_version: 3`) |
| **Strict Min Version** | `142.0` (required for `data_collection_permissions: ["none"]`) |
| **Background Script** | Event page: `"background": { "scripts": ["js/background.js"] }` |
| **External CDNs** | None. 100% self-contained offline fonts and CSS. |
| **Libraries** | Plain vanilla ES6 JavaScript. No minifiers, bundlers, or obfuscation. |
