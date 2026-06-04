from flask import Flask, render_template, request

app = Flask(__name__)


class Calculator:
    def __init__(self):
        self.result = ""

    def append_value(self, value):
        self.result += str(value)

    def clear_result(self):
        self.result = ""

    def calculate_result(self):
        try:
            self.result = str(eval(self.result))  # Evalúa la expresión actual
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
            calculator.result = ""
        elif action == "calculate":
            calculator.result = current_input
            calculator.calculate_result()

        # Renderiza la plantilla con el resultado
        return render_template(
            "index.html", result=calculator.result, current_input=calculator.result
        )

    return render_template("index.html", result="", current_input="")


if __name__ == "__main__":
    app.run(debug=True)
