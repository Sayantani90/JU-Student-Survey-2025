import pandas as pd
import json

# === CONFIG ===
excel_path = "Exit_Survey_2025_Science.xlsx"  # your Excel file
output_json = "sc_dept_feedback.json"

# Columns Q–V (questions)
question_cols = [
    "Curriculum and syllabus of the course attended",
    "Overall learning environment",
    "Library Infrastructure",
    "Laboratory Infrastructure (if applicable)",
    "Wi-Fi and Internet facility",
    "Career Guidance and Assistance"
]

# === MAIN ===
xlsx = pd.ExcelFile(excel_path)
data = {}

for sheet in xlsx.sheet_names:
    df = pd.read_excel(excel_path, sheet_name=sheet, usecols="Q:V")
    df.columns = ["curriculum", "learning", "library", "lab", "wifi", "career"]

    # Drop NaNs and keep numeric values only
    df = df.apply(pd.to_numeric, errors="coerce").dropna(how="all")

    data[sheet] = {
        "curriculum": df["curriculum"].dropna().tolist(),
        "learning": df["learning"].dropna().tolist(),
        "library": df["library"].dropna().tolist(),
        "lab": df["lab"].dropna().tolist(),
        "wifi": df["wifi"].dropna().tolist(),
        "career": df["career"].dropna().tolist(),
    }

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Saved: {output_json}")
