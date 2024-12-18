from flask import Flask, render_template, request

from processing import get_prediction

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def index():
    message="Здесь будет рекомендация от нейросети* (дисклеймер: если все параметры введены правильно и приложение отработало без сбоев)"
    if request.method == "POST":
        parameter_1 = request.form.get("parameter_1")
        parameter_2 = request.form.get("parameter_2")
        
        predc = get_prediction(parameter_1, parameter_2)
        message = f"Рекомендуемое соотношение при значениях параметра 1 {parameter_1}, параметра 2 {parameter_2} составляет {predc}"
        
        print(predc)

    return render_template("index.html", message=message)

