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
### Note: this project needs python in order to function , dowload and install from : https://www.python.org/downloads/

- go to your local terminal after you download the whole unit converter folder from github
- and by local terminal , I mean either : windows powershell or CMD 


### 1. Install Requirements
copy & paste this into your terminal in order to install pillow ( very small sized) required for the GUI to work : ( skip if you want just a preview , look below )
```bash
pip install pillow
```

### 2. Run the CLI

```bash
python maincode.py
```

### 3. Run the GUI
you can just preview it in the next part below so you can skip this part if not interested in trying it yourself

```bash
python GUI.py
```

💡 On some systems, use python3 instead of python.

```bash
python3 GUI.py
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
