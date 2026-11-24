/**
 * CHARITRA — Welcome Page Script
 * Must be an external file (MV3 CSP forbids inline scripts on extension pages).
 */

document.addEventListener('DOMContentLoaded', () => {

  // ── Apply saved theme & accent ──────────────────────────────────────────────
  chrome.storage.local.get('hb_config', data => {
    const cfg    = data?.hb_config || {};
    const theme  = cfg.theme  || 'dark';
    const accent = cfg.accent || 'blue';
    document.documentElement.setAttribute('data-theme',  theme);
    document.documentElement.setAttribute('data-accent', accent);
  });

  // ── Pivot tab navigation ────────────────────────────────────────────────────
  document.getElementById('pivotHeader').addEventListener('click', e => {
    const tab = e.target.closest('[data-tab]');
    if (!tab) return;
    document.querySelectorAll('.pivot-tab').forEach(t =>
      t.classList.toggle('active', t === tab)
    );
    document.querySelectorAll('.panel').forEach(p =>
      p.classList.toggle('active', p.id === 'tab-' + tab.dataset.tab)
    );
  });

  // ── Open keyboard shortcuts settings ───────────────────────────────────────
  document.getElementById('openShortcutsBtn').addEventListener('click', () => {
    const isFirefox = navigator.userAgent.includes('Firefox');
    const targetUrl = isFirefox ? 'about:addons' : 'chrome://extensions/shortcuts';
    try {
      chrome.tabs.create({ url: targetUrl }).catch(() => {
        showShortcutHint();
      });
    } catch (_) {
      showShortcutHint();
    }
  });

  function showShortcutHint() {
    const btn = document.getElementById('openShortcutsBtn');
    btn.textContent = 'Go to about:addons ⚙ → Manage Extension Shortcuts';
    btn.style.background = 'var(--success, #107c10)';
  }

  // ── "Open Extension" CTA ────────────────────────────────────────────────────
  // Can't open the popup programmatically — instead open a helpful message
  // and close this welcome tab so the user clicks the toolbar icon themselves.
  document.getElementById('ctaOpenExtension').addEventListener('click', () => {
    // Replace content with a friendly nudge, then close after a short delay
    const btn = document.getElementById('ctaOpenExtension');
    btn.textContent = 'Look for the CHARITRA icon in your toolbar ↗';
    btn.style.pointerEvents = 'none';
    btn.style.opacity = '0.7';
    setTimeout(() => window.close(), 2500);
  });

});
