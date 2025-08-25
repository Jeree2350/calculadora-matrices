from flask import Flask, jsonify, request
from flask_cors import CORS
from matrix_operations import MatrixCalculator
from logger_config import logger
import traceback

app = Flask(__name__)
CORS(app)

calculator = MatrixCalculator()

# Middleware for logging request
@app.before_request
def log_request_info():
    logger.info(f"Request: {request.method} {request.url}")
    if request.method == 'POST' and request.is_json:
        logger.info(f"Request data keys: {list(request.get_json().keys()) if request.get_json() else 'None'}")

# Manejo global de errores
@app.errorhandler(Exception)
def handle_exception(e): 
    logger.error(f"Unhandled Exception: {str(e)}")
    logger.error(traceback.format_exc())
    return jsonify({
        "success": False,
        "error": "Error interno del servidor",
        "message": "Ocurrió un error inesperado. Por favor, inténtelo de nuevo más tarde."
    }), 500

# Endpoints
@app.route('/test', methods=['GET'])
def test():
    return jsonify({ "message": "Backend funcionando correctamente!" })