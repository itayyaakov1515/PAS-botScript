# PAS-botScript
The script automates the extraction of data from an MDB file, converting it to CSV and JSON formats, then sending it to a server, likely for analysis or storage, possibly as part of a data logging or monitoring system.


# bot.py
script is designed to automate some actions in a Windows GUI application called PAS (Power Analysis Software). It opens the PAS application, clicks on specific buttons within the application, triggers an external Python script, and then minimizes the PAS window. It uses the pywinauto library for GUI automation and subprocess module to run external scripts. Additionally, it uses ctypes for interacting with Windows API to manipulate windows.

# Pas_Device_Updater
script exports data from an MDB file to a CSV file, converts the CSV file to JSON format, and then sends the JSON data to a server using a command-line tool 
