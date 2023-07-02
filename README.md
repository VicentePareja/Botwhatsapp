# WhatsApp Message Sender

Este script de Python automatiza el envío de mensajes a través de WhatsApp Web utilizando `pyautogui`, una biblioteca de Python para automatizar interacciones de usuario. Carga una lista de números de teléfono desde un archivo Excel y envía un mensaje a cada número a través de WhatsApp Web.

## Requisitos

Necesitas tener las siguientes bibliotecas de Python instaladas:

- `pandas`
- `pyautogui`
- `time`

Puedes instalar estas bibliotecas con el siguiente comando:

´´´shell
pip install pandas pyautogui
´´´´


Además, necesitas tener acceso a un archivo Excel (`.xlsx`) que contenga los números de teléfono a los que deseas enviar los mensajes.

## Cómo utilizar

1. Clona o descarga este repositorio en tu máquina local.

2. Asegúrate de tener todas las bibliotecas necesarias instaladas.

3. Abre el script `whatsapp_sender.py` y configura las constantes en la parte superior del archivo:

    - `EXCEL_FILE`: Ruta al archivo Excel que contiene los números de teléfono.
    - `PHONE_COLUMN`: Nombre de la columna en el archivo Excel que contiene los números de teléfono.
    - `MESSAGE`: Mensaje que deseas enviar. Si deseas incluir saltos de línea en tu mensaje, puedes hacerlo con el carácter de nueva línea (`\n`).

4. Ejecuta el script de Python con el comando `python whatsapp_sender.py` desde la terminal.

5. Una vez que el script se esté ejecutando, no debes interactuar con tu computadora hasta que se hayan enviado todos los mensajes, ya que `pyautogui` controlará tu ratón y teclado.

## Advertencia

El uso de scripts de automatización para enviar mensajes a través de WhatsApp puede estar en contra de sus términos de servicio. Este script se proporciona solo con fines educativos y de prueba. Utilízalo con responsabilidad y solo para enviar mensajes a destinatarios que hayan dado su consentimiento. El autor no se responsabiliza del uso indebido de este script.

## Autor

Vicente Pareja

## Licencia

Este proyecto fué creado por mi pero es open source. Sientete libre de colaborar.
