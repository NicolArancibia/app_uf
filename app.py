from flask import Flask, render_template, request, flash, redirect, url_for
import requests
from datetime import datetime


NOMBRES_MESES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}



app = Flask(__name__)
app.secret_key = 'clavenecesariaparalascookies'

@app.route('/', methods=['GET', 'POST'])
def index():
    datos = {}
    mensaje_aviso = ""
    
    if request.method == 'POST':
        year = request.form['year']

        if not year.isdigit() or len(year) != 4:
            flash('Por favor ingresa un año válido de 4 dígitos.')
            return redirect(url_for('index'))

        datos = obtener_datos_uf(year)

        if not datos:
            flash('No se encontró información para el año ingresado.')
            return redirect(url_for('index'))

        
        if int(year) == datetime.now().year:
            mensaje_aviso = "⚡ Solo se muestran datos hasta el mes actual porque estás consultando el año en curso."

    return render_template('index.html', datos=datos, NOMBRES_MESES=NOMBRES_MESES, mensaje_aviso=mensaje_aviso)


def obtener_datos_uf(year):
    apikey = "0a6b62e4c83bbad6f156ab9e48f8394be576efec"
    url = f"https://api.sbif.cl/api-sbifv3/recursos_api/uf/{year}?apikey={apikey}&formato=json"
    response = requests.get(url)

    # 🔵 Aquí va el debug:
    print("[DEBUG] Código de respuesta HTTP:", response.status_code)
    print("[DEBUG] Respuesta JSON:")
    print(response.text)  # Imprime la respuesta completa en texto

    if response.status_code != 200:
        return None  # error en la API

    data = response.json()
    lista_ufs = data.get('UFs', [])

    if not lista_ufs:
        return None  # no hay datos

    return procesar_uf(lista_ufs)


def procesar_uf(lista_ufs):
    from collections import defaultdict
    import datetime

    meses = defaultdict(list)

    for registro in lista_ufs:
        fecha = datetime.datetime.strptime(registro['Fecha'], "%Y-%m-%d")
        valor = float(registro['Valor'].replace('.', '').replace(',', '.'))
        meses[fecha.month].append((fecha, valor))

    resultados = {
        'subida': [],
        'bajada': [],
        'sin_cambio': [],
        'maximo': None,
        'minimo': None,
    }

    max_valor = (-1, None)
    min_valor = (999999999, None)

    for mes, valores in meses.items():
        if not valores:
            continue

        valores.sort()
        inicio = valores[0][1]
        fin = valores[-1][1]
        variacion = fin - inicio

        if variacion > 0:
            resultados['subida'].append((mes, variacion))
        elif variacion < 0:
            resultados['bajada'].append((mes, variacion))
        else:
            resultados['sin_cambio'].append(mes)

        for fecha, valor in valores:
            if valor > max_valor[0]:
                max_valor = (valor, fecha)
            if valor < min_valor[0]:
                min_valor = (valor, fecha)

    resultados['subida'] = sorted(resultados['subida'], key=lambda x: x[1])
    resultados['bajada'] = sorted(resultados['bajada'], key=lambda x: abs(x[1]), reverse=True)
    resultados['sin_cambio'] = sorted(resultados['sin_cambio'], key=lambda m: NOMBRES_MESES[m])
    resultados['maximo'] = max_valor
    resultados['minimo'] = min_valor

    return resultados




if __name__ == '__main__':
    app.run(debug=True)
