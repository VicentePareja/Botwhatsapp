import time
import pandas as pd
import pyautogui

# Constants
EXCEL_FILE = "whatsapp_numbers.xlsx"
PHONE_COLUMN = 'Numero de telefono'

MESSAGE = """*Hola! Me llamo Vicente y este menaje fué enviado por un bot!*"""

# Read the phone numbers from the Excel file
def read_phone_numbers(filename, column):
    df = pd.read_excel(filename)
    return df[column].tolist()

# Send a message through WhatsApp Web
def send_message(phone_number, message):
    # Open a new browser tab
    pyautogui.hotkey('ctrl', 't')

    # Open WhatsApp Web with the specified phone number
    pyautogui.typewrite(f'https://web.whatsapp.com/send?phone={phone_number}')
    pyautogui.press('enter')

    # Wait for the page to load
    time.sleep(10)

    # Type and send the message
    for line in message.split('\n'):
        pyautogui.typewrite(line)
        pyautogui.press('enter')

    # Close the tab
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')

def main():
    # Initialize
    time.sleep(3)
    phone_numbers = read_phone_numbers(EXCEL_FILE, PHONE_COLUMN)

    # Send the message to each number in the list
    for i, phone_number in enumerate(phone_numbers, 1):
        send_message(int(phone_number), MESSAGE)
        print(f"Mensajes enviados: {i}")

if __name__ == "__main__":
    main()
