# Aplicación de Premios Nobel

Esta aplicación web muestra información sobre los ganadores de Premios Nobel, incluyendo una gráfica de barras que muestra la cantidad de ganadores por país y una sección para cargar aleatoriamente información de 5 ganadores mediante AJAX.

## Estructura del Proyecto

```
nobel_prize_app/
├── app.py              # Aplicación principal de Flask
├── api.py              # Endpoints de la API de Flask
├── database.py         # Configuración y operaciones de la base de datos
├── static/
│   ├── css/
│   │   └── style.css   # Estilos personalizados para la interfaz
│   └── js/
│       └── main.js     # JavaScript para AJAX y generación de gráficos
└── templates/
    └── index.html      # Plantilla HTML principal
```

## Características

1. **Base de datos SQLite**:
   - Almacena información de ganadores de Premios Nobel
   - Se inicializa y puebla automáticamente al iniciar la aplicación

2. **API REST**:
   - `/api/winners-by-country`: Retorna la cantidad de ganadores por país
   - `/api/random-winners`: Retorna 5 ganadores aleatorios

3. **Interfaz de Usuario**:
   - Gráfico de barras horizontales que muestra los países con más ganadores
   - Sección para cargar y mostrar información de ganadores aleatorios mediante AJAX
   - Diseño atractivo con fuentes y colores no convencionales

## Cómo ejecutar la aplicación

1. Asegúrate de tener el archivo `winners.json` en el directorio raíz del proyecto.

2. Instala las dependencias necesarias:
   ```
   pip install flask
   ```

3. Ejecuta la aplicación:
   ```
   python app.py
   ```

4. Abre tu navegador y visita:
   ```
   http://localhost:5000
   ```

## Tecnologías utilizadas

- **Backend**: Flask (Python)
- **Base de datos**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Gráficos**: Chart.js

## Funcionalidades implementadas

- Inicialización y población automática de la base de datos
- API REST para acceder a los datos
- Gráfico de barras interactivo y visualmente atractivo
- Carga dinámica de datos mediante AJAX
- Interfaz de usuario con diseño moderno y atractivo
