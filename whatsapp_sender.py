import pywhatkit as kit
import pyautogui
import time
def send_whatsapp_message(phone_number, message):
    try:
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=20, tab_close=False, close_time=20)
        
        time.sleep(5)
        
        pyautogui.press('enter')
        
        print("Message sent successfully!")
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    send_whatsapp_message("+918078445837", "Hello from attendance system!")
