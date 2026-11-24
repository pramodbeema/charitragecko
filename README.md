# CHARITRA for Firefox (Gecko MV3)

> **Your private browsing history vault** — powered by AES-256-GCM encryption, dressed in authentic Windows Phone / Nokia Lumia Metro style.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue)](LICENSE)
[![Firefox Add-on](https://img.shields.io/badge/Firefox-Add--on-orange?logo=firefox-browser)](https://addons.mozilla.org/en-US/firefox/addon/charitra-gecko/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-charitragecko-181717?logo=github)](https://github.com/pramodbeema/charitragecko)

---

## 🚀 Quick Start & Local Testing in Firefox

1. Open Mozilla Firefox and navigate to:
   ```text
   about:debugging#/runtime/this-firefox
   ```
2. Click **Load Temporary Add-on...**
3. Select `manifest.json` inside this folder (`CharitraGecko`).
4. The **CHARITRA** shield icon will appear in your Firefox toolbar.
5. Click the icon to launch the first-run wizard:
   - Select your theme (**Dark**, **Light**, or **System**)
   - Create your master vault password
   - Add domains you wish to block from browser history (e.g. `reddit.com`, `x.com`)
   - Browse normally — visits are wiped from history within 1.5 seconds and sealed in your encrypted vault.

---

## 📦 Building the AMO Package

Run the included PowerShell script to generate production `.zip` and `.xpi` archives:
```powershell
.\package.ps1
```
This packages all essential runtime files into:
- `CharitraGecko-v1.0.0-firefox.zip`
- `CharitraGecko-v1.0.0-firefox.xpi`

---

## 🔒 Security Architecture

| Layer | Implementation |
|---|---|
| **Cipher** | AES-256-GCM (Authenticated Encryption via native Web Crypto API) |
| **Key Derivation** | PBKDF2-SHA256 with 310,000 iterations (OWASP standard) |
| **Salt** | Cryptographically secure 16-byte random salt per encryption |
| **Password Storage** | Never stored — only a salted verification hash is kept |
| **Storage at Rest** | Base64 ciphertext in `browser.storage.local` |
| **Telemetry** | 0% (zero remote code, zero external network requests) |

---

## 📂 File Structure

```text
CharitraGecko/
├── manifest.json              # Gecko MV3 manifest (ID: charitra@pramodbeema, min 142.0)
├── package.ps1                # Automated AMO package builder (.zip / .xpi)
├── AMO_REVIEW_NOTES.md        # Pre-formatted review notes with character limits
├── CERTIFICATION_NOTES.md    # Mozilla compliance and security disclosures
├── DESCRIPTION.md            # AMO store listing description
├── PRIVACY.md                # Offline privacy policy
├── LICENSE                   # GNU General Public License v3
├── css/
│   └── metro.css              # Windows Phone / Nokia Lumia Metro design system
├── icons/                    # Extension icons (16, 24, 32, 48, 128, 256)
├── js/
│   ├── background.js          # Non-persistent event page for history scrubbing
│   ├── crypto.js              # Web Crypto AES-256-GCM implementation
│   ├── storage.js             # Vault and configuration storage controller
│   ├── popup.js               # 380x580 Metro popup controller
│   ├── vault.js               # Full-screen vault analytics & search page
│   └── welcome.js             # Onboarding setup script
├── pages/
│   ├── popup.html             # Toolbar popup interface
│   ├── vault.html             # Full-screen vault tab with activity heatmap
│   └── welcome.html           # Welcome & setup guide page
└── store listing images/      # High-res screenshots (1280x800) & promo tiles
```
