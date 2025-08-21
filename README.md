# Unit Converter  

A simple **Unit Converter** project built with Python.  
This repository contains both the core conversion logic and a graphical user interface (GUI) to make the tool more user-friendly.  

---

## 📂 Files  

- **maincode.py**  
  Contains the main conversion logic (functions for handling unit conversion, calculation, etc.).  

- **GUI.py**  
  Provides the graphical user interface for the unit converter.  
  Includes:
  - Dropdown menus for selecting units.  
  - Input and output text boxes.  
  - A **Convert** button to trigger the conversion.  
  - Integrated **logo** in the title bar.  

- **logo.png**  
  A small image file used as the application’s logo.  

---

## 🚀 Features  

- Conversion between different units.  
- Easy-to-use GUI with text input and result display.  
- Logo integrated for a more polished interface.  

---

## ⚙️ Requirements  

Make sure you have **Python 3.x** installed.  
The project uses **Tkinter**, which comes pre-installed with Python.  

Additional dependencies (if any):  
```bash
pip install pillow
## ▶️ How to Run

Clone this repository:

bash
Copier
Modifier
git clone https://github.com/yourusername/unit-converter.git
cd unit-converter
Run the GUI file:

bash
Copier
Modifier
python GUI.py
The application window will open, where you can enter a value, select units, and press Convert.

## 🛠️ Development Notes

- While developing, I integrated the logo into the title bar.

- Built a dropdown menu for selecting conversion categories, which caused some alignment bugs that I’m still improving.

- Added input/output text boxes for conversion.

- Encountered common Tkinter issues such as widget stretching, text alignment, and callback errors when wiring up the Convert button.
