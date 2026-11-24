#!/usr/bin/env python3
"""
CHARITRA for Firefox (Gecko MV3) — AMO Production Packager
Generates POSIX-compliant .zip and .xpi archives with forward slashes (/)
to pass Mozilla Add-ons (AMO) validation with 0 errors.
"""
import os
import zipfile
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_NAME = os.path.join(ROOT_DIR, "CharitraGecko-v1.0.0-firefox.zip")
XPI_NAME = os.path.join(ROOT_DIR, "CharitraGecko-v1.0.0-firefox.xpi")

# Items to include in production package
ENTRIES = [
    "manifest.json",
    "LICENSE",
    "css",
    "icons",
    "js",
    "pages"
]

def build_package():
    # Remove old builds
    for path in [ZIP_NAME, XPI_NAME]:
        if os.path.exists(path):
            os.remove(path)

    print(f"Packaging {ZIP_NAME} with POSIX forward slashes (/)...")
    with zipfile.ZipFile(ZIP_NAME, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for entry in ENTRIES:
            entry_path = os.path.join(ROOT_DIR, entry)
            if not os.path.exists(entry_path):
                print(f"Warning: {entry} not found!")
                continue

            if os.path.isfile(entry_path):
                # Single file at root
                arcname = entry.replace('\\', '/')
                zf.write(entry_path, arcname)
                print(f" + {arcname}")
            elif os.path.isdir(entry_path):
                # Directory tree
                for root, _, files in os.walk(entry_path):
                    for file in sorted(files):
                        file_full = os.path.join(root, file)
                        rel_path = os.path.relpath(file_full, ROOT_DIR)
                        arcname = rel_path.replace('\\', '/')
                        zf.write(file_full, arcname)
                        print(f" + {arcname}")

    # Copy to XPI
    shutil.copyfile(ZIP_NAME, XPI_NAME)

    # Validate raw bytes for backslashes
    with open(ZIP_NAME, 'rb') as fp:
        raw_bytes = fp.read()
    
    # Check for backslash path separators in zip entries
    has_backslash = False
    for entry in ['css\\', 'js\\', 'icons\\', 'pages\\']:
        if entry.encode('utf-8') in raw_bytes:
            has_backslash = True
            break

    if has_backslash:
        raise RuntimeError("ERROR: Zip archive contains Windows backslashes! AMO validator will reject it.")
    
    print("\n" + "=" * 58)
    print("  CHARITRA Gecko MV3 Package Built Successfully!")
    print("=" * 58)
    print(f" - Archive (ZIP): {os.path.basename(ZIP_NAME)} ({os.path.getsize(ZIP_NAME) / 1024:.1f} KB)")
    print(f" - Package (XPI): {os.path.basename(XPI_NAME)} ({os.path.getsize(XPI_NAME) / 1024:.1f} KB)")
    print(" - POSIX Slash Compliance: Verified 100% forward slashes (/)")
    print("=" * 58)
    print("Ready to upload to:")
    print("https://addons.mozilla.org/en-US/developers/addon/submit/upload-listed\n")

if __name__ == '__main__':
    build_package()
