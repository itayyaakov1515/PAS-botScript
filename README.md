# Satec_PAS_BOT
This Python script automates the execution of two separate Python scripts (Pas_Device_Updater.py and Record_player.py) using subprocesses. It also utilizes the schedule library to schedule the execution of the main() function every 8 hours. Upon execution, it triggers Record_player.py first, waits for 10 seconds using time.sleep(), and then triggers Pas_Device_Updater.py. 

# PAS-botScript
The script automates the extraction of data from an MDB file, converting it to CSV and JSON formats, then sending it to a server, likely for analysis or storage, possibly as part of a data logging or monitoring system.


# bot.py
script is designed to automate some actions in a Windows GUI application called PAS (Power Analysis Software). It opens the PAS application, clicks on specific buttons within the application, triggers an external Python script, and then minimizes the PAS window. It uses the pywinauto library for GUI automation and subprocess module to run external scripts. Additionally, it uses ctypes for interacting with Windows API to manipulate windows.

# Pas_Device_Updater
script exports data from an MDB file to a CSV file, converts the CSV file to JSON format, and then sends the JSON data to a server using a command-line tool 


# updater.py
The code automates the process of exporting data from a Microsoft Access database (MDB) file to a CSV file, converting the CSV file to JSON format, and sending the JSON data to a server. It utilizes various libraries such as pyodbc, csv, json, and subprocess for database connectivity, file handling, and executing external commands. Additionally, it uses the schedule module to schedule the data export and transmission process to run every 8 hours.


# import ctypes
This Python script reads a mouse record file and replays the recorded mouse actions using the pynput library. It parses the record file, extracts timestamped mouse events (move, scroll, click), and replays them with appropriate timing. It also prints information about the playback process, such as current time, elapsed time, remaining time, and the actions being performed. Finally, it completes the mouse record replay process.
