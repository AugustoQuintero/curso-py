from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def hola():
    return render_template("index.html")

# from flask import Flask, request
@app.route('/link', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        return 'Este es un POST', 201
    return 'Este es un GET'
# Hacer un CURL en otro CMD:
# curl -i -X POST http...

# from flask import Flask, request, jsonify
@app.route('/api/info')
def api_info():
    datos = {
        'nombre': 'Notas_app',
        'version': '1.1'
    }
    return jsonify(datos)


# if __name__ == "__main__":
#     app.run(debug=True)
# 👆🏻 asi se corre con python app.py    
