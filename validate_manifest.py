import json
import os

def load_manifest(path="manifest.json"):
    with open(path) as f:
        return json.load(f)

def validate_assets(manifest):
    missing = []
    for label, path in manifest.items():
        if not os.path.exists(path):
            missing.append((label, path))
    return missing

if __name__ == "__main__":
    manifest = load_manifest()
    missing = validate_assets(manifest)

    if missing:
        print("[!] Missing assets:")
        for label, path in missing:
            print(f"- {label}: {path}")
    else:
        print("[✓] All assets present")
