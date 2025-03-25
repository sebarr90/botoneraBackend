from flask import Flask, request, jsonify
from pynput.keyboard import Controller, Key

app = Flask(__name__)
keyboard = Controller()  # Controlador del teclado

# Mapeo de teclas especiales
SPECIAL_KEYS = {
    "shift": Key.shift,
    "ctrl": Key.ctrl,
    "alt": Key.alt,
    "tab": Key.tab,
    "enter": Key.enter,
    "esc": Key.esc,
    "backspace": Key.backspace,
    "delete": Key.delete,
    "up": Key.up,
    "down": Key.down,
    "left": Key.left,
    "right": Key.right,
    "space": Key.space,
    "f1": Key.f1,
    "f2": Key.f2,
    "f3": Key.f3,
    "f4": Key.f4,
    
}

@app.route('/press', methods=['POST'])
def press_key():
    data = request.json  # Recibe los datos enviados desde el frontend
    key = data.get('key')  # Obtiene la tecla a presionar

    if key:
        try:
            if key in SPECIAL_KEYS:
                # Si es una tecla especial, usa Key.shift, Key.ctrl, etc.
                keyboard.press(SPECIAL_KEYS[key])
                keyboard.release(SPECIAL_KEYS[key])
            else:
                # Para teclas normales, envía el carácter directamente
                keyboard.press(key)
                keyboard.release(key)

            return jsonify({"message": f"Tecla '{key}' presionada"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return jsonify({"error": "No se envió ninguna tecla"}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
