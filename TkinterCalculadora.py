import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Campo de texto para mostrar los resultados
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4)
        result_entry.grid(row=0, column=0, columnspan=4)

        # Botones
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', 'C', '=', '+'
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
        if value == '=':
            button = tk.Button(self.root, text=value, padx=40, pady=20, font=('Arial', 18), command=self.calculate_result)
        elif value == 'C':
            button = tk.Button(self.root, text=value, padx=40, pady=20, font=('Arial', 18), command=self.clear_result)
        else:
            button = tk.Button(self.root, text=value, padx=40, pady=20, font=('Arial', 18), command=lambda: self.append_value(value))

        button.grid(row=row, column=col)

    def append_value(self, value):
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    def clear_result(self):
        self.result_var.set("")

    def calculate_result(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
