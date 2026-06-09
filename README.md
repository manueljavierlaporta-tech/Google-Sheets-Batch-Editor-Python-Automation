# Google Sheets Batch Editor | Python Automation

## ⚙️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)
![gspread](https://img.shields.io/badge/gspread-API-blue?style=for-the-badge)

---

## ✍🏻 Workflow

This script was created to batch-edit multiple Google Sheets spreadsheets across different years in a single execution. It connects to each spreadsheet using a service account, reads specific columns, applies transformations, and writes the results back — all automatically.

The process works like this:

1. The script authenticates with the Google Sheets API using a `credentials.json` service account file.
2. It iterates over a dictionary containing one spreadsheet per year (2021–2025), each with its own `key` and `gid`.
3. For each spreadsheet, it reads two columns: names (`E`) and subjects (`I`).
4. It applies the corresponding transformation function to each column.
5. It writes all modified values back in a single API call per column, avoiding quota errors.

---

## 🎯 Script Objective

This automation solves the following problems:

- Manual and repetitive editing across multiple spreadsheets.
- Inconsistent name formatting across years.
- Time loss when handling large datasets spread across different files.

The script ensures:

- Batch writing with a single API call per column (avoids `429 Quota Exceeded` errors).
- Name normalization: keeps the first name and reduces the last name to initials.
- Automatic subject numbering per row.
- Scalable structure: adding a new year only requires one new entry in the dictionary.

---

## 🗂️ Spreadsheet Structure

Each year points to a different Google Sheets file:

```python
sheets = {
    "2021": {"key": "...", "gid": 875568155},
    "2022": {"key": "...", "gid": 875568155},
    "2023": {"key": "...", "gid": 1071874746},
    "2024": {"key": "...", "gid": 875568155},
    "2025": {"key": "...", "gid": 1973933532},
}
```

The `key` is the unique spreadsheet ID from its URL. The `gid` identifies the specific worksheet (tab) inside it.

---

## ✏️ Transformations Applied

### Names — Column E

Last names are reduced to their initials. Surrounding quotes are stripped if present.

```python
valor_celda = valor_celda.strip('"').strip("'")
partes = valor_celda.split(" ", 1)
nombre = partes[0]
apellido = " ".join(partes[1:])
apellido_iniciales = "".join(palabra[0] for palabra in apellido.split())
nuevo_valor_celda = f"{nombre} {apellido_iniciales}"
```

`"Juan Carlos García López"` → `"Juan CGL"`

### Subjects — Column I

Each row is assigned a sequential subject number.

```python
nuevo_valor = f"Asunto n° {i+1}"
```

---

## ⚠️ Notes

- A valid `credentials.json` service account file is required.
- The service account must have **Editor** access on each spreadsheet.
- Values are written in bulk per column to stay within Google's API write quota.
- The script does not create backups before overwriting — make sure data is backed up if needed.

---

## 🚀 Possible Improvements

- Read column ranges dynamically instead of hardcoding `E` and `I`
- Add a logging system per year
- Export a summary of changes made
- Add a rollback/backup mechanism before writing
- Support for additional transformation functions per column
