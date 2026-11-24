from pathlib import Path

ENTRY = "My agent triaged my inbox overnight, archived 400 emails, and replied to my boss that I quit."

Path("/output/entry.txt").parent.mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")
