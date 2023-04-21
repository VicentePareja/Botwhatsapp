import pyautogui
import pandas as pd
import time

# Lee la base de datos de Excel
excel_file = "whatsapp_numbers.xlsx"
df = pd.read_excel(excel_file)

# Guarda los numeros en un data frame
phone_numbers = df['Numero de telefono'].tolist()

# Se define el mensaje

message1 = """*Hola! Me llamo Vicente y te quiero recordar votar en estas elecciones!*"""
message2 = """Te toma *menos de un minuto* y lo puedes hacer mediante un correo que ya recibiste por parte de equipo@votaciones.cl"""
message3 = """Si quieres saber acerca de mi candidatura, te dejo el siguiente post:"""
message4 = """https://www.instagram.com/p/CrL0tH4A-RB/?igshid=YmMyMTA2M2Y="""


# Función para buscar y enviar mensajes a través de WhatsApp Web

time.sleep(3)


def send_message(phone_number, message1, message2, message3, message4):
    # Abre una nueva pestaña en el navegador
    pyautogui.hotkey('ctrl', 't')

    # Abre WhatsApp Web con el número de teléfono especificado
    pyautogui.typewrite(f'https://web.whatsapp.com/send?phone={phone_number}')
    pyautogui.press('enter')

    # Espera a que la página cargue
    time.sleep(10)

    # Escribe y envía el mensaje
    pyautogui.typewrite(message1)
    pyautogui.hotkey('shift', 'enter')
    pyautogui.hotkey('shift', 'enter')
    pyautogui.typewrite(message2)
    pyautogui.hotkey('shift', 'enter')
    pyautogui.hotkey('shift', 'enter')
    pyautogui.typewrite(message3)
    pyautogui.hotkey('shift', 'enter')
    pyautogui.hotkey('shift', 'enter')
    pyautogui.typewrite(message4)

    pyautogui.press('enter')

    # Cierra la pestaña
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')


# Envía el mensaje a cada número en la lista
contador = 0
for phone_number in phone_numbers:

    contador += 1
    send_message(int(phone_number), message1, message2, message3, message4)
    print(f"Mensajes enviados: {contador}")
