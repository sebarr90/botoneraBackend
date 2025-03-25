# Backend para Botonera de Simuladores

Este es el servidor backend en Python con Flask que permite capturar datos de telemetría de Euro Truck Simulator 2 y Fernbus, además de enviar comandos de teclado al juego. Este backend está vinculado con el repositorio de la botonera Vue para proporcionar una experiencia completa.

## Características
- Captura de telemetría en tiempo real desde ETS2 y Fernbus.
- Simulación de pulsaciones de teclas mediante `pynput`.
- API REST para comunicación con la botonera Vue.
- Configuración fácil y rápida con Flask.

## Requisitos
- Python 3.8 o superior
- Flask
- pynput
- Una API de telemetría compatible (como `ETS2 Telemetry Server`)

## Instalación
1. Clona este repositorio:
   ```sh
   git clone https://github.com/sebarr90/botoneraBackend
   cd backend-botonera
   ```
2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
3. Ejecuta el servidor:
   ```sh
   python app.py
   ```

## Configuración
Asegúrate de que la API de telemetría esté corriendo en el puerto correcto. Puedes modificar la configuración en `app.py`.

## API Endpoints
### Enviar pulsaciones de teclas
`POST /api/press`
```json
{
  "key": "space"
}
```

### Obtener datos de telemetría
`GET /api/telemetry`


## Repositorio de la Botonera Vue
Este backend está diseñado para trabajar en conjunto con la botonera Vue, disponible en el siguiente repositorio:
👉 [Botonera](https://github.com/sebarr90/botonera)

## API de Telemetría
Se utiliza la API **ETS2 Telemetry Server** de **[Funbit](https://github.com/Funbit/ets2-telemetry-server)** para obtener información en tiempo real del camión.

## Licencia
Este proyecto está bajo la **Licencia MIT**. Puedes usarlo, modificarlo y distribuirlo libremente, siempre y cuando se mantenga la atribución al autor original.

---
🚛 ¡Feliz conducción! 🔥

