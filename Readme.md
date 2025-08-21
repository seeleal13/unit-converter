# Unit Converter
<img width="3780" height="1890" alt="Image" src="https://github.com/user-attachments/assets/dbd22e47-fabf-4561-a0ff-98a0bc9d657f" />

A simple Python project for converting between different units. It includes both a **command-line interface (CLI)** and a **graphical user interface (GUI)** built with `tkinter`.

---

## Features
- **CLI**: Run conversions from the terminal (`maincode.py`).
- **GUI**: User-friendly window app (`GUI.py`) with dropdowns, input/output boxes, live updates, and a history view.
- **Custom Logo**: `logo.png` is used in the window and as the app icon (if available).

---

## 💻 Software Stack

- Python 3.x  
- Tkinter (built-in with Python)  
- Pillow (`PIL`) for logo handling  

---

## 📁 Project Structure
```bash
unit-converter/
│
├── maincode.py # CLI app
├── GUI.py # Tkinter GUI app
├── logo.png # App logo
└── README.md # This file

```

---

## 🚀 How to Run

### 1. Install Requirements
```bash
pip install pillow
```

### 2. Run the CLI
```bash
python maincode.py
```

### 3. Run the GUI
```bash
python GUI.py
```
💡 On some systems, use python3 instead of python.

---

## 🖼️ GUI Preview

![hippo](https://media.giphy.com/media/TusDtBsXl2uxExYZLg/giphy.gif)

---

## 📝 Notes
- If logo.png is missing, the GUI will still work but without the logo.
- Large values (e.g. > 1e6) are rejected in the CLI to prevent crashes.
- Precision can be adjusted (0–5 decimal places).

---

## 🔧 Future Improvements
- Add more units (time, speed, currency, etc.)
- Dark/Light theme for the GUI
- Save history to a file