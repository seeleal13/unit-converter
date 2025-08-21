# Unit Converter
<img width="3780" height="1890" alt="Image" src="https://github.com/user-attachments/assets/dbd22e47-fabf-4561-a0ff-98a0bc9d657f" />

A simple Python project for converting between different units. It includes both a **command-line interface (CLI)** and a **graphical user interface (GUI)** built with `tkinter`.


---

## Features
- **CLI**: Run conversions from the terminal (`unit_converter_cli.py`).
- **GUI**: User-friendly window app (`unit_converter_gui.py`) with dropdowns, input/output boxes, live updates, and a history view.
- **Custom Logo**: `logo.png` is used in the window and as the app icon (if available).


---

## 💻 Software Stack

- Python 3.11+  
- Tkinter (built-in with Python)  
- Pillow (`PIL`) for logo handling  


---

## 📁 Project Structure
```bash
unit-converter/
│
├── unit_converter_cli.py # CLI app
├── unit_converter_gui.py # Tkinter GUI app
├── logo.png # App logo
├── README.md # This file
├── .gitignore #Git config file
└── pyproject.toml #unit converter metadata

```


---

## 🚀 How to Run

### option 1: run on your own code editor:

### 1. Install Requirements
```bash
pip install pillow
```

### 2. Run the CLI
```bash
python unit_converter_cli.py
```

### 3. Run the GUI
```bash
python unit_converter_gui.py
```
💡 On some systems, use python3 instead of python.

```bash
python3 unit_converter_gui.py
```


### option 2: run code from built/distributed package:

- Make sure you have Python 3.11 or higher installed.
- To check if Python is installed, run in your terminal:

```bash
python --version
```
### 1. open your terminal:

- Windows: Press Win + R, type cmd, and hit Enter.
- macOS/Linux: Open your terminal app.

### 2. install the package in your machine:
```bash
pip install -i https://test.pypi.org/simple/ unit-converter-cli==0.0.0
```
### 3. Verify Installation:
```bash
pip show unit-converter-cli
```
### 4. Run the CLI:
```bash
unit-converter-cli
```
- make sure you are executing in the right path 
```bash
cd (package_path)
```
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
