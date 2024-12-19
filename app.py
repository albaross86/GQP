from flask import Flask, render_template, request

from processing import get_prediction

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def index():
    message="Здесь будет рекомендация от нейросети* (дисклеймер: если все параметры введены правильно и приложение отработало без сбоев)"
    if request.method == "POST":
        plotnost = request.form.get("01_plotnost")
        modul_uprugosti = request.form.get("02_modul_uprugosti")
        otverditel = request.form.get("03_otverditel")
        epoxidy = request.form.get("04_epoxidy")
        temperatura = request.form.get("05_temperatura")
        pov_plotnost = request.form.get("06_pov_plotnost")
        modul_upr_ras = request.form.get("07_modul_upr_ras")
        proch_ras = request.form.get("08_proch_ras")
        smola = request.form.get("09_smola")
        ugol_nashivki = request.form.get("10_ugol_nashivki")
        shag_nashivki = request.form.get("11_shag_nashivki")
        plot_nashivki = request.form.get("12_plot_nashivki")
      
        predc = get_prediction(plotnost, modul_uprugosti, otverditel, epoxidy, temperatura, pov_plotnost, modul_upr_ras, proch_ras, smola, ugol_nashivki, shag_nashivki, plot_nashivki)
        
        message = f"Рекомендуемое соотношение матрица-наполнитель при значениях параметров {plotnost}, {modul_uprugosti}, {otverditel}, {epoxidy}, {temperatura}, {pov_plotnost}, {modul_upr_ras}, {proch_ras}, {smola}, {ugol_nashivki}, {shag_nashivki}, {plot_nashivki} составляет {predc}"

        print(predc)

    return render_template("index.html", message=message)

# if __name__ == "__main":
#      app.run()