import os
import tkinter as tk
from functools import partial

from calculator_engine import safe_eval


class Calculator:
    COLORS = {
        "bg": "#2B2118",
        "card": "#FFFBF5",
        "display_bg": "#1E1510",
        "display_text": "#F0AD4E",
        "num_bg": "#FFF3E0",
        "num_text": "#4A3728",
        "operator_bg": "#F0AD4E",
        "operator_text": "#2B2118",
        "clear_bg": "#E07A5F",
        "clear_text": "#FFFBF5",
        "equals_bg": "#D4A373",
        "equals_text": "#2B2118",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("basic-tkinter-calculator")
        self.root.geometry("420x650")
        self.root.configure(bg=self.COLORS["bg"])
        self.root.resizable(False, False)

        icon_path = os.path.join(os.path.dirname(__file__), "logo.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Card container
        card = tk.Frame(self.root, bg=self.COLORS["card"], bd=0)
        card.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Display
        display = tk.Entry(
            card,
            textvariable=self.result_var,
            font=("Segoe UI", 32),
            bg=self.COLORS["display_bg"],
            fg=self.COLORS["display_text"],
            justify="right",
            relief="flat",
            bd=0,
            highlightthickness=0,
            insertbackground=self.COLORS["display_text"],
        )
        display.pack(fill=tk.X, padx=12, pady=(12, 8), ipady=18)

        # Buttons grid frame
        grid = tk.Frame(card, bg=self.COLORS["card"])
        grid.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))

        for i in range(4):
            grid.columnconfigure(i, weight=1, uniform="col")
        for i in range(4):
            grid.rowconfigure(i, weight=1, uniform="row")

        buttons = [
            ("7", "num"),
            ("8", "num"),
            ("9", "num"),
            ("/", "operator"),
            ("4", "num"),
            ("5", "num"),
            ("6", "num"),
            ("*", "operator"),
            ("1", "num"),
            ("2", "num"),
            ("3", "num"),
            ("-", "operator"),
            ("0", "num"),
            ("C", "clear"),
            ("=", "equals"),
            ("+", "operator"),
        ]

        row_val = 0
        col_val = 0

        for text, kind in buttons:
            self.create_button(grid, text, kind, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, parent, text, kind, row, col):
        if text == "=":
            cmd = self.calculate_result
        elif text == "C":
            cmd = self.clear_result
        else:
            cmd = partial(self.append_value, text)

        bg = self.COLORS.get(f"{kind}_bg", self.COLORS["num_bg"])
        fg = self.COLORS.get(f"{kind}_text", self.COLORS["num_text"])

        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 20, "bold"),
            bg=bg,
            fg=fg,
            activebackground=fg,
            activeforeground=bg,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=cmd,
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def append_value(self, value):
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    def clear_result(self):
        self.result_var.set("")

    def calculate_result(self):
        try:
            result = safe_eval(self.result_var.get())
            self.result_var.set(result)
        except Exception:
            self.result_var.set("Error")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
