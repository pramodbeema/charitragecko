# Privacy Policy for CHARITRA (Firefox Add-on)

**Last Updated:** November 2026

## 1. Overview
CHARITRA is an open-source, client-side browser privacy extension built for Mozilla Firefox. Our core mission is providing uncompromising privacy and security without collecting any user information.

## 2. Information We Collect
**None.** 
- We do not collect, store, transmit, or sell any personal data, browsing history, device identifiers, or usage analytics.
- CHARITRA contains zero tracking scripts, zero cookies, and zero third-party telemetry libraries.

## 3. Data Storage & Encryption
- All domains, visited URLs, page titles, and timestamps saved in the vault are encrypted on your local machine using **AES-256-GCM** authenticated encryption with **PBKDF2-SHA256** key derivation (310,000 iterations).
- Encrypted records are stored exclusively in your local Firefox profile (`browser.storage.local`).
- Your master password is never stored on disk.
- All cryptographic keys remain strictly in local browser memory and are destroyed when the vault is locked or the browser session ends.

## 4. Permissions Usage
- `history`: Required strictly to delete matching visits to user-specified domains from the browser's local history.
- `storage`: Required strictly to store your encrypted vault ciphertext and personal theme settings locally.
- `tabs` & `webNavigation`: Required to intercept URL navigations to blocked domains in order to scrub them from the history list.
- `alarms`: Required to run periodic background history sweeps and manage auto-lock expiration.

## 5. Contact & Source Code
CHARITRA is licensed under GNU General Public License v3.0 (GPLv3).
Source code is publicly auditable on GitHub: https://github.com/pramodbeema/charitragecko
Developer: Pramod Beema (bp.beema@gmail.com)
