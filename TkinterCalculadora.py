import os
import tkinter as tk
from functools import partial

from calculator_engine import safe_eval


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("basic-tkinter-calculator")
        self.root.geometry("400x600")

        icon_path = os.path.join(os.path.dirname(__file__), "logo.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        result_entry = tk.Entry(
            self.root,
            textvariable=self.result_var,
            font=("Arial", 24),
            bd=10,
            insertwidth=4,
            width=14,
            borderwidth=4,
        )
        result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            "C",
            "=",
            "+",
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, value, row, col):
        if value == "=":
            cmd = self.calculate_result
        elif value == "C":
            cmd = self.clear_result
        else:
            cmd = partial(self.append_value, value)

        button = tk.Button(
            self.root,
            text=value,
            padx=40,
            pady=20,
            font=("Arial", 18),
            command=cmd,
        )
        button.grid(row=row, column=col)

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
