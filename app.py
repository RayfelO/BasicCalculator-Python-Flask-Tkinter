import os

from flask import Flask, render_template, request, send_from_directory

from calculator_engine import safe_eval

TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
app = Flask(__name__, template_folder=TEMPLATE_DIR)


class Calculator:
    def __init__(self):
        self.result = ""

    def append_value(self, value):
        self.result += str(value)

    def clear_result(self):
        self.result = ""

    def calculate_result(self):
        try:
            self.result = str(safe_eval(self.result))
        except ZeroDivisionError:
            self.result = "Error"
        except Exception:
            self.result = "Error"


@app.route("/", methods=["GET", "POST"])
def index():
    calculator = Calculator()

    if request.method == "POST":
        action = request.form.get("action")
        value = request.form.get("value", "")
        current_input = request.form.get("current_input", "")

        if action == "append":
            calculator.result = current_input + value
        elif action == "clear":
            calculator.clear_result()
        elif action == "calculate":
            calculator.result = current_input
            calculator.calculate_result()

        return render_template(
            "index.html", result=calculator.result, current_input=calculator.result
        )

    return render_template("index.html", result="", current_input="")


@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory("assets", filename)


if __name__ == "__main__":
    app.run(debug=True)
