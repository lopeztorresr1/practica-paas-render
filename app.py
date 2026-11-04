import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
  return jsonify({
      'estado': 'Exitoso',
      'mensaje': '¡API desplegada con éxito en la Nube mediante PaaS!',
      'materia': 'Servicios en la Nube',
      'version': '2.0.0',
      'cicd_status': 'Despliegue continuo automático funcionando correctamente',
  })


@app.route('/saludo/<nombre>', methods=['GET'])
def saludar(nombre):
  return jsonify({
      'usuario': nombre,
      'mensaje': f'¡Hola {nombre}, bienvenido a la plataforma cloud!',
  })


if __name__ == '__main__':
  # El puerto lo asigna dinámicamente la plataforma en producción
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)