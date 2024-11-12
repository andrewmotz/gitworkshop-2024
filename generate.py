import json
import shutil

SOURCE_DIR = "template"

with open("names.json", "r") as f:
    name_json = json.load(f)

    for name in name_json["names"]:
        name = name.strip().replace(" ", "")
        shutil.copytree(SOURCE_DIR, f"workspaces/{name}")
