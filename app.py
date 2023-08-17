from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"

@app.route("/")
def calculator():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate_endpoint():
    expression = request.form.get("expression")
    result = calculate(expression)
    return result

if __name__ == "__main__":
    app.run(debug=False)
