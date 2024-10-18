# Transcripciones

## Crear un entorno virtual

Para crear un entorno virtual, sigue estos pasos:

1. Abre una terminal y navega al directorio del proyecto.
2. Ejecuta el siguiente comando para crear el entorno virtual:

    ```bash
    python3 -m venv env
    ```

3. Activa el entorno virtual:

    - En Windows:

      ```bash
      .\env\Scripts\activate
      ```

    - En macOS y Linux:

      ```bash
      source env/bin/activate
      ```

4. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar el proyecto

Para ejecutar el proyecto, asegúrate de que el entorno virtual esté activado y luego ejecuta el siguiente comando:

```bash
python main.py
```
