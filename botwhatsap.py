import time
import pandas as pd
import pyautogui
import pyperclip
from parametros import *

def send_message(phone_number, name, message_template):
    # Formatear el mensaje con el nombre del destinatario
    message = message_template.format(name=name)
    
    # Copiar el mensaje al portapapeles
    pyperclip.copy(message)

    # Abrir una nueva pestaña del navegador
    pyautogui.hotkey('ctrl', 't')

    # Abrir WhatsApp Web con el número de teléfono especificado
    pyautogui.typewrite(f'https://web.whatsapp.com/send?phone={phone_number}')
    pyautogui.press('enter')

    # Esperar a que se cargue la página
    time.sleep(10)

    # Simular un clic para asegurarse de que el cursor esté en el área de texto
    # Los valores (x, y) deberán ser ajustados según la resolución y la disposición de tu pantalla
    pyautogui.click(x=1000, y=950) 

    # Esperar un poco después del clic
    time.sleep(1)

    # Pegar el mensaje desde el portapapeles
    pyautogui.hotkey('ctrl', 'v')

    # Esperar un momento para que el mensaje se pegue correctamente
    time.sleep(1)

    # Enviar el mensaje
    pyautogui.press('enter')

    # Cerrar la pestaña
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')

def read_contacts(filename, name_column, phone_column):
    df = pd.read_excel(filename)
    print("Dataframe cargado")
    return df[name_column].tolist(), df[phone_column].tolist()

def main():
    # Inicialización
    time.sleep(3)
    names, phone_numbers = read_contacts(EXCEL_FILE, NAME_COLUMN, PHONE_COLUMN)

    # Enviar el mensaje a cada contacto en la lista
    for i, (name, phone_number) in enumerate(zip(names, phone_numbers), 1):
        send_message(int(phone_number), name, MESSAGE_TEMPLATE)
        print(f"Mensajes enviados: {i}")

if __name__ == "__main__":
    main()