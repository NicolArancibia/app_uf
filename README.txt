UF Visualizer - Consulta de Variación de la Unidad de Fomento (UF) por Año
==========================================================================

Este proyecto permite consultar y visualizar la variación mensual de la UF (Unidad de Fomento) 
en Chile a lo largo de un año, utilizando la API pública de la Comisión para el Mercado Financiero (CMF).

------------------------------------------------------------------------
Tecnologías utilizadas
------------------------------------------------------------------------
- Python 3
- Flask
- HTML + CSS (modo claro/oscuro)
- JavaScript (para el cambio de tema)
- API pública CMF/SBIF

------------------------------------------------------------------------
Instrucciones para ejecutar la aplicación
------------------------------------------------------------------------

1. Asegúrate de tener Python 3 instalado en tu computador.

2. Abre una terminal o línea de comandos:
   - En Windows: busca "cmd" o "Windows Terminal".
   - En macOS: abre "Terminal".
   - En Linux: abre tu terminal habitual.

3. Instala Flask ejecutando el siguiente comando en la terminal:

   pip install flask

4. Descarga y descomprime el proyecto en una carpeta local.

5. No es necesario modificar el archivo `app.py`, ya contiene una API Key funcional.

6. Desde la misma terminal, ubícate dentro de la carpeta del proyecto (por ejemplo, "uf_app") y ejecuta:

   python app.py

7. Una vez que Flask indique que está corriendo, abre tu navegador web y entra a:

   http://localhost:5000

------------------------------------------------------------------------
Descripción funcional
------------------------------------------------------------------------

- Permite ingresar un año (por ejemplo, 2023 o 2024) para consultar los valores de la UF.
- Utiliza la API oficial de la CMF para obtener los valores diarios de la UF.
- Clasifica y muestra los resultados de la siguiente forma:
   - Meses en que la UF subió (ordenados de menor a mayor variación).
   - Meses en que la UF bajó (ordenados de mayor a menor bajada, considerando la magnitud).
   - Meses sin variación (ordenados alfabéticamente por nombre del mes).
- Muestra el día con el mayor valor y el día con el menor valor de la UF en el año consultado.
- Si se consulta el año actual, muestra un aviso indicando que solo hay datos disponibles hasta el mes actual.
- Diseño adaptable para escritorio y dispositivos móviles.
- Incorpora un botón para cambiar entre modo claro y modo oscuro, guardando la preferencia del usuario en el navegador.

------------------------------------------------------------------------
Estructura del proyecto
------------------------------------------------------------------------

uf_app/
├── app.py
├── README.txt
├── static/
│   └── style.css
└── templates/
    └── index.html

------------------------------------------------------------------------
Notas adicionales
------------------------------------------------------------------------

- La API Key integrada en el proyecto es funcional para efectos de esta prueba técnica.
- La API gratuita de la CMF puede tener restricciones en cuanto a la frecuencia de uso o disponibilidad de datos actualizados.
