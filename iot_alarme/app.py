from flask import Flask, render_template, redirect
import random
import datetime

app = Flask(__name__)

movimento = False
led = False
rele = False
alarme_ativo = True
historico = []
contador = 0

def sensor_pir():
    return random.choice([True, False])

def atualizar_sistema():
    global movimento, led, rele, contador
    
    if alarme_ativo:
        movimento = sensor_pir()
    else:
        movimento = False
    
    if movimento:
        led = True
        rele = True
        contador += 1
        historico.append(datetime.datetime.now().strftime("%H:%M:%S"))
    else:
        led = False
        rele = False

@app.route("/")
def index():
    atualizar_sistema()
    return render_template(
        "index.html",
        movimento=movimento,
        led=led,
        rele=rele,
        alarme=alarme_ativo,
        historico=historico[-10:],
        contador=contador,
        historico_json=historico[-10:]
    )

@app.route("/toggle")
def toggle():
    global alarme_ativo
    alarme_ativo = not alarme_ativo
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)