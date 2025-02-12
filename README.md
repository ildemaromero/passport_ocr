# README

## PassportOCR
PassportOCR es una herramienta diseñada para extraer datos procesables de imágenes de pasaportes utilizando la API de OpenAI. Convierte la información presente en una imagen de pasaporte en un formato JSON estructurado y en inglés.

Este proyecto es útil para automatizar la lectura de datos de pasaportes, como nombres, números de pasaporte, fechas de emisión y vencimiento, y más, eliminando la necesidad de ingresar manualmente esta información.

## Ejemplo de Salida
Al procesar una imagen de pasaporte, PassportOCR devuelve un JSON con la siguiente estructura:

```json
{
  "first_name": "Roxon",
  "last_name": "Ortiz Molina",
  "passport_number": "138673602",
  "nationality": "Venezuelan",
  "issue_date": "2016-08-16",
  "expiration_date": "2021-08-15",
  "place_of_birth": "Ciudad Ojeda, Venezuela",
  "date_of_birth": "1991-04-20",
  "gender": "M",
  "passport_country": "VEN"
}
```

## Requisitos

- Python 3.8+
- Bibliotecas:
  - `openai`
  - `python-dotenv`
  - `validators`
- Archivo .env: Debe contener la clave de la API de OpenAI. Ejemplo:
  - API_KEY=tu_api_key
- Una cuenta activa en OpenAI con acceso a la API

## Instalación

1. Clona este repositorio:
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Configura el archivo .env colocando tu clave de API de OpenAI:
    ```bash
    echo "API_KEY=tu_api_key" > .env
    ```

## Uso

### Código de Ejemplo

```python
from PassportOCR import PassportOCR

passport_ocr = PassportOCR()

# Procesar una imagen desde una URL
image_url = "https://example.com/passport.jpg"
data = passport_ocr.get_passport_data(image_url)
print(data)

# Procesar una imagen desde una ruta local
image_path = "/ruta/a/tu/imagen.jpg"
data = passport_ocr.get_passport_data(image_path)
print(data)
``` 

### Entrada Válida
PassportOCR acepta:
- **URL de una imagen:** Una URL pública válida que apunte a una imagen de pasaporte.
- **Ruta local:** La ruta completa a un archivo de imagen en tu sistema.

### Salida
La función get_passport_data devuelve un diccionario JSON con los datos extraídos. Si ocurre un error, devuelve un mensaje de error.

## Manejo de Errores

- **Error: "Invalid Image URL or PATH"**  
  Asegúrate de que la URL es válida o que la ruta al archivo local existe y apunta a una imagen.

- **Error al conectarse a la API de OpenAI**  
  Verifica que tu clave de API es válida y que tienes acceso a la API.

- **Salida inesperada o vacía**  
  Asegúrate de que la imagen contiene un pasaporte legible y que el modelo puede procesarlo correctamente.
