import tkinter as tk
import sys
from PIL import Image, ImageTk

class Unitconverter(tk.Frame):
    
    def __init__(self, root):
        self.colour1 = '#5E17EB'
        self.colour2 = "#FFFFFF"
        self.colour3 = "#000000"

        self.conversions_available = [
            'km --> m', 'm --> km', 'kg --> g',
            'g --> kg', '°F --> °C', '°C --> °F'
        ]

        super().__init__(root, bg=self.colour1)

        self.master = root
        self.master.title("Unit Converter by @Seeleal13")
        self.master.geometry("450x300")
        self.master.configure(bg=self.colour1)

        self.history = []

        self.hamburger_frame = tk.Frame(self.master, bg=self.colour1)
        self.hamburger_frame.pack(fill='x')

        self.menu_button = tk.Button(
            self.hamburger_frame,
            text="☰",
            font=('Helvetica World', 16, 'bold'),
            bg=self.colour1,
            fg=self.colour2,
            command=self.toggle_menu,
            border=0
        )
        self.menu_button.pack(side='left', padx=10)

        self.header_frame = tk.Frame(self.master, bg=self.colour1)
        self.header_frame.pack(pady=15, fill='x')

        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=1)

        tk.Label(self.header_frame, bg=self.colour1).grid(row=0, column=0)

        self.title_frame = tk.Frame(self.header_frame, bg=self.colour1)
        self.title_frame.grid(row=0, column=1, sticky='ew')

        try:
            img = Image.open("logo.png")  
            img = img.resize((40, 60), Image.Resampling.LANCZOS)  
            self.logo = ImageTk.PhotoImage(img)
            self.master.iconphoto(True, self.logo)
            logo_label = tk.Label(self.title_frame, image=self.logo, bg=self.colour1)
            logo_label.pack(side=tk.LEFT, padx=10)
        except FileNotFoundError:
            print("Warning: logo.png not found. Skipping logo and icon display.")

        self.title = tk.Label(
            self.title_frame,
            bg=self.colour1,
            fg=self.colour2,
            font=('Helvetica World', 22, 'bold'),
            text='Unit Converter'
        )
        self.title.pack(side=tk.LEFT)

        tk.Label(self.header_frame, bg=self.colour1).grid(row=0, column=2)

        self.sidebar = tk.Frame(self.master, bg=self.colour1, width=150)
        self.main_page = tk.Frame(self.master, bg=self.colour1)
        self.history_page = tk.Frame(self.master, bg=self.colour1)
        self.about_page = tk.Frame(self.master, bg=self.colour1)

        self.main_page.pack(fill='both', expand=True)

        tk.Button(
            self.sidebar,
            text="Main Page",
            bg=self.colour1,
            fg=self.colour2,
            font=('Helvetica World', 14),
            command=lambda: self.show_page('main'),
            border=0
        ).pack(fill='x', pady=5)
        tk.Button(
            self.sidebar,
            text="History",
            bg=self.colour1,
            fg=self.colour2,
            font=('Helvetica World', 14),
            command=lambda: self.show_page('history'),
            border=0
        ).pack(fill='x', pady=5)
        tk.Button(
            self.sidebar,
            text="About Us",
            bg=self.colour1,
            fg=self.colour2,
            font=('Helvetica World', 14),
            command=lambda: self.show_page('about'),
            border=0
        ).pack(fill='x', pady=5)

        self.conversion = tk.StringVar()
        self.conversion.set(self.conversions_available[0])

        self.select_conversion = tk.OptionMenu(
            self.main_page,
            self.conversion,
            *self.conversions_available
        )
        self.select_conversion.config(
            bg=self.colour1,
            fg=self.colour2,
            activebackground=self.colour2,
            activeforeground=self.colour1,
            font=('Helvetica World', 14),
            width=12,
            border=1,
            highlightthickness=0
        )
        self.select_conversion.pack(pady=15)

        io_frame = tk.Frame(self.main_page, bg=self.colour1)
        io_frame.pack(pady=10)

        self.entry_box = tk.Entry(io_frame, font=('Helvetica World', 14), width=10)
        self.entry_box.grid(row=0, column=0, padx=(10, 5))
        self.input_unit = tk.Label(
            io_frame,
            text="km",
            bg=self.colour1,
            fg=self.colour2,
            font=('Helvetica World', 14)
        )
        self.input_unit.grid(row=0, column=1, padx=(0, 10))

        self.arrow_label = tk.Label(
            io_frame,
            text="→",
            bg=self.colour1,
            fg=self.colour2,
            font=('Helvetica World', 14)
        )
        self.arrow_label.grid(row=0, column=2, padx=10)

        self.result_box = tk.Entry(
            io_frame,
            font=('Helvetica World', 14),
            width=10,
            state="readonly"
        )
        self.result_box.grid(row=0, column=3, padx=(5, 5))
        self.output_unit = tk.Label(
            io_frame,
            text="m",
            bg=self.colour1,
            fg=self.colour2,
            font=('Helvetica World', 14)
        )
        self.output_unit.grid(row=0, column=4, padx=(0, 10))

        io_frame.grid_columnconfigure(0, weight=1)
        io_frame.grid_columnconfigure(1, weight=0)
        io_frame.grid_columnconfigure(2, weight=1)
        io_frame.grid_columnconfigure(3, weight=1)
        io_frame.grid_columnconfigure(4, weight=0)

        self.entry_box.bind('<KeyRelease>', lambda event: self.convert_value())

        self.conversion.trace('w', lambda *args: self.update_unit_labels())
        self.update_unit_labels()

        self.history_list = tk.Listbox(
            self.history_page,
            font=('Helvetica World', 12),
            bg=self.colour1,
            fg=self.colour2,
            width=40,
            height=10
        )
        self.history_list.pack(pady=20, padx=20)

        tk.Label(
            self.about_page,
            text="Unit Converter by @Seeleal13\nVersion 1.0\nA simple tool for converting units\nBuilt with Tkinter and PIL",
            bg=self.colour1,
            fg=self.colour2,
            font=('Helvetica World', 14),
            justify='center'
        ).pack(pady=20)

    def toggle_menu(self):
        if self.sidebar.winfo_ismapped():
            self.sidebar.pack_forget()
        else:
            self.sidebar.pack(side='left', fill='y', before=self.hamburger_frame)

    def show_page(self, page):
        self.main_page.pack_forget()
        self.history_page.pack_forget()
        self.about_page.pack_forget()
        self.sidebar.pack_forget()
        if page == 'main':
            self.main_page.pack(fill='both', expand=True)
        elif page == 'history':
            self.history_list.delete(0, tk.END)
            for i, entry in enumerate(self.history, 1):
                self.history_list.insert(tk.END, f"{i}. {entry}")
            self.history_page.pack(fill='both', expand=True)
        elif page == 'about':
            self.about_page.pack(fill='both', expand=True)

    def update_unit_labels(self):
        conv = self.conversion.get()
        units = {
            'km --> m': ('km', 'm'),
            'm --> km': ('m', 'km'),
            'kg --> g': ('kg', 'g'),
            'g --> kg': ('g', 'kg'),
            '°F --> °C': ('°F', '°C'),
            '°C --> °F': ('°C', '°F')
        }
        input_unit, output_unit = units.get(conv, ('', ''))
        self.input_unit.configure(text=input_unit)
        self.output_unit.configure(text=output_unit)

    def convert_value(self):
        try:
            value = self.entry_box.get()
            if value == "":
                result = ""
            else:
                value = float(value)
                conv = self.conversion.get()
                if conv == 'km --> m':
                    result = value * 1000
                elif conv == 'm --> km':
                    result = value / 1000
                elif conv == 'kg --> g':
                    result = value * 1000
                elif conv == 'g --> kg':
                    result = value / 1000
                elif conv == '°F --> °C':
                    result = (value - 32) * 5/9
                elif conv == '°C --> °F':
                    result = (value * 9/5) + 32
                else:
                    result = "Error"
                result = f"{result:.2f}"
                self.history.append(f"{value} {self.input_unit.cget('text')} = {result} {self.output_unit.cget('text')}")

            self.result_box.configure(state="normal")
            self.result_box.delete(0, tk.END)
            self.result_box.insert(0, result)
            self.result_box.configure(state="readonly")

        except ValueError:
            self.result_box.configure(state="normal")
            self.result_box.delete(0, tk.END)
            self.result_box.insert(0, "Invalid")
            self.result_box.configure(state="readonly")

def main():
    operating_system = sys.platform
    root = tk.Tk()
    unit_converter_app = Unitconverter(root)
    root.resizable(width=True, height=True)
    root.mainloop()

if __name__ == "__main__":
    main()
