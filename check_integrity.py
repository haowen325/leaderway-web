import os
import sys

# ---------------------------------------------------------
# 🛡️ Leaderway SRE Protocol: Integrity Check
# ---------------------------------------------------------
# Last Updated: 2026-01-24
# ---------------------------------------------------------

REQUIRED_FILES = [
    # 1. Mandatory Core (Global)
    "approval_lib.py",
    "config_gas.json",

    # 2. Project Core (Web Frontend)
    "index.html",
    "style.css",
    "script.js",
    "robots.txt",
    "sitemap.xml",

    # 3. Project Core (Tools & Scripts)
    "tools/process_certs.ps1",
    "tools/process_certs_safe.ps1",
    "tools/process_new_certs.ps1",
    "tools/processor.html"
]

def check_integrity():
    print("--------------------------------------------------")
    print("[SRE] Leaderway SRE Integrity Check")
    print("--------------------------------------------------")
    
    missing_files = []
    
    for relative_path in REQUIRED_FILES:
        # Check relative to current working directory
        if os.path.exists(relative_path):
            print(f"[OK] Found: {relative_path}")
        else:
            print(f"[MISSING] {relative_path}")
            missing_files.append(relative_path)
            
    print("--------------------------------------------------")
    
    if missing_files:
        print(f"[FAILED] Integrity Check FAILED! {len(missing_files)} files missing.")
        print("Required Action: Restore missing files immediately.")
        sys.exit(1)
    else:
        print("[SUCCESS] System Integrity: HEALTHY")
        print("--------------------------------------------------")
        sys.exit(0)

if __name__ == "__main__":
    check_integrity()
