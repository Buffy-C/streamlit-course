# Streamlit Course — Section 2 Notes
**Date:** 19/07/2026
**Source:** andybek.com

## Environment Setup

- Create a virtual environment: `python -m venv env`
- **Windows (PowerShell)** activation differs from Mac/Linux — there's no `bin` folder on Windows, it's `Scripts`, and `source` doesn't exist in PowerShell:
  ```powershell
  .\env\Scripts\Activate.ps1
  ```
  If blocked by execution policy, run once first:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
  ```
- **Mac/Linux (zsh/bash)** activation:
  ```bash
  source env/bin/activate
  ```
- NTS (note to self): update Streamlit after the course finishes.

## Running & Stopping Apps

- `streamlit run app.py` — starts the app, serves at `http://localhost:8501`
- `Ctrl + C` in the terminal — stops the running app (needed before running a different file, e.g. `challenge1.py`)

## Key Gotcha: Unsaved Changes

- A **dot in the VS Code file tab** means the file has unsaved changes — Streamlit won't pick up edits until the file is saved.
- Fix: turn on **Auto Save** in VS Code so this stops being an issue.

## Markdown Elements

- Markdown is a simple way to add different text formatting (headers, bold, links, lists, tables) inside `st.markdown()`.
- Reference: markdownguide.org
- Table syntax:
  ```
  |Col1|Col2|Col3|
  |----|----|----|
  |a|b|c|
  ```
- Keep a closing `|` on every row for consistency, even though Streamlit renders it fine without one on the last cell.

## Images

- Download images into the project folder and reference locally — don't embed external URLs directly (e.g. LinkedIn CDN links contain expiring signed tokens and will eventually break).
- Basic usage:
  ```python
  st.image("photo.jpg")
  ```
- With a caption:
  ```python
  st.image("photo.jpg", caption="A photo")
  ```

## Challenge 1 (Bio Page) — Learnings

- Built a bio page using `st.header`, `st.image`, `st.markdown`, `st.text`, and a markdown table.
- Fixed the initial version's reliance on an external LinkedIn image URL by switching to a local `st.image("BCImage.jpg")`.
- Noted inconsistency between `st.text` (plain, preserves whitespace, no markdown rendering) and `st.markdown` (supports bold/bullets/links) — worth being intentional about which one to use per section.
- For future/longer bios: consider storing each job entry as a dict (title, dates, bullets) in a list and looping to render, rather than one long hardcoded markdown string — easier to maintain as content grows.

## Glossary

| Term | Meaning |
|------|---------|
| `ls` | list (directory contents) |
| `env` | environment |
| `bin` | binary folder (Mac/Linux venv — where `activate` lives) |
| `Scripts` | Windows equivalent of `bin` in a venv |
| `lib` | library folder inside the venv |
| `venv` | Python's built-in virtual environment tool |
| `pip` | Python package installer |

## Useful Reminders

- Dot in file tab = unsaved changes
- `Ctrl + C` = stops the running app
