# CHARITRA — Private Browsing History Vault

> **Your private browsing history vault** — powered by military-grade AES-256-GCM encryption, dressed in authentic Windows Phone / Nokia Lumia Metro style.

---

## Summary

CHARITRA silently intercepts visits to specific domains you choose, wipes them from your Firefox history within 1.5 seconds, and preserves those visits inside a password-protected, AES-256-GCM encrypted private vault.

The vault data stored on disk is opaque Base64 ciphertext — completely unreadable without the correct master password, even if someone opens Firefox's profile storage files directly.

---

## Key Features

### 🛡️ Silent History Scrubbing
- **Instant 1.5s Wipe**: Matching visits are removed from Firefox history within 1.5 seconds of navigation.
- **SPA & PushState Aware**: Catches client-side page transitions in React, Vue, and Angular applications.
- **7-Day Auto-Sweep**: Periodically sweeps the last 7 days of browsing history in the background to ensure no trace persists.
- **Active Schedule**: Define a daily time window (e.g. 09:00–17:00) during which protection is active.

### 🔒 Military-Grade Encryption
- **AES-256-GCM Authenticated Encryption**: Both confidentiality and integrity are cryptographically verified.
- **PBKDF2-SHA256**: Key derivation with 310,000 iterations (OWASP recommendation).
- **Zero Plaintext on Disk**: Visited URLs, page titles, and timestamps are encrypted before being written to storage.
- **Zero-Knowledge**: Your master password is never stored or transmitted anywhere.

### ⊞ Windows Phone / Nokia Lumia Metro UI
- Authentic flat Metro aesthetics inspired by Windows Phone 8 and Nokia Lumia.
- Bold typography with **Bebas Neue** and **Segoe UI**.
- Glanceable Live Tiles displaying real-time blocked domain counts, vault entries, and sweep status.
- Fluid Pivot tab navigation.

### 🎨 Customization & Themes
- **Dark, Light, and System Themes**: Follows your operating system's color scheme preference automatically.
- **8 Signature Lumia Accent Colors**: Cobalt Blue, Crimson Red, Electric Cyan, Emerald Green, Royal Purple, Sunset Orange, Deep Teal, and Magenta Pink.

### 📊 Visual Analytics & Search (Full-Page Vault)
- **Multi-Field Search**: Instant keyword search across URLs, page titles, and domains.
- **Date Range Filters**: Filter captures by custom dates or quick presets (Today, This Week).
- **Top Blocked Sites Chart**: Horizontal frequency breakdown of your most visited blocked sites.
- **12-Month Activity Heatmap**: GitHub/Metro-style calendar heatmap visualizing your browsing privacy trends.
- **Offline JSON Export**: Backup your entire encrypted vault with 1-click password confirmation.

---

## Privacy Policy & Security

- **100% Offline & Client-Side**: All encryption happens directly inside your browser.
- **Zero Data Collection**: No analytics, no trackers, zero remote servers.
- **Open Source**: Licensed under GPL v3.
