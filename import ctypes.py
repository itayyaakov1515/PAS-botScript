import time
from pywinauto import Desktop , Application
import subprocess
import schedule
import ctypes

def open_pas():
    app = Application().start(cmd_line= "C:\Pas\Pas.exe")
    time.sleep(5)


def click_buttons_by_text(program_name, button_texts, delay):
     app = Desktop,Application(backend="uia").window(title="Pas.exe")
     app.wait('visible', timeout=240)  

     for text in button_texts:
        button = app.child_window(title=text, control_type='Button')
        button.click()
        time.sleep(delay) 


def trigger_script(file_path):
    print(f"Triggering script with file path: {file_path}")
    subprocess.run(["python", file_path])   


def main():
    window_title = "PAS"
    minimize_window(window_title)
    open_pas()
    program_name = "PAS"  
    button_texts = ["Monitor", "RT Data Monitor", "Data Set 0 BASIC MEASUREMENTS", "RT Logging On\Off","Save" , "Close",] ## Add here the PAS buttons that save the log ##
    delay_between_clicks = 2  
    click_buttons_by_text(program_name, button_texts, delay_between_clicks)
    file_path = "C:\Pas\Pas_Device_Updater.py"
    trigger_script(file_path)
    minimize_window(program_name)  


def minimize_window(window_title):
    hwnd = ctypes.windll.user32.FindWindowW(None, window_title)
    if hwnd != 0:
        ctypes.windll.user32.ShowWindow(hwnd, 6)  # SW_MINIMIZE = 6


if __name__ == "__main__":
    main()