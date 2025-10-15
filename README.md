# 📦 Manifest Validator CLI

CLI tool to validate asset presence against a manifest file. Built for deployment audits, static site integrity checks, and CI validation.

---

## 🔧 Tools Included

| File | Description |
|------|-------------|
| `validate_manifest.py` | Checks if all manifest assets exist locally. |
| `report_generator.py` | Generates an HTML report of missing assets. |
| `manifest.json` | Maps logical asset names to file paths. |

---

## 🚀 Usage

1. Define your asset paths in `manifest.json`:
   json
   {
     "main_css": "static/css/main.css",
     "logo": "static/img/logo.png"
   }

2. 	Run the validator:
    python3 validate_manifest.py

3. (Optional) Generate a report:
   python3 report_generator.py

   ---

## 🧠 Notes

• 	Paths are relative to the repo root.
• 	Extend to support remote URLs, S3 buckets, or KV namespaces.
• 	Ideal for static site validation, asset audits, and CI/CD pipelines
