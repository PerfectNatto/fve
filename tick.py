import json
from openpyxl import load_workbook

EXCEL_PATH = "input.xlsx"
JSON_PATH = "existing.json"
OUTPUT_PATH = "output.json"

wb = load_workbook(EXCEL_PATH, data_only=True)
ws = wb.active

with open(JSON_PATH, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

index = {p["name"]: p for p in data["palettes"]}

blocks = {
    "melody": ("H", "I", "J", "K"),
    "chord":  ("N", "O", "P", "Q"),
    "bass":   ("T", "U", "V", "W"),
    "drums":  ("Z", "AA", "AB", "AC"),
}

for row in range(4, ws.max_row + 1):
    palette = index.get(ws[f"C{row}"].value)

    if not palette:
        continue

    for part, cols in blocks.items():
        name_col, cc0_col, cc32_col, pg_col = cols

        palette["instrument"][part]["name"] = ws[f"{name_col}{row}"].value
        palette["instrument"][part]["cc0"] = int(ws[f"{cc0_col}{row}"].value)
        palette["instrument"][part]["cc32"] = int(ws[f"{cc32_col}{row}"].value)
        palette["instrument"][part]["pg"] = int(ws[f"{pg_col}{row}"].value)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
