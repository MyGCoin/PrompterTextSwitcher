import os
import json
import subprocess

def beende_prozess(prozessname):
    try:
        subprocess.run(["taskkill", "/f", "/im", prozessname], check=True)
        print(f"Process {prozessname} ended successfully.")
    except subprocess.CalledProcessError:
        print(f"Could not terminate process {prozessname} . Maybe it's not running.")


def starte_prozess(prozesspfad):
    try:
        subprocess.Popen(prozesspfad)
        print(f"Process {prozesspfad} was started successfully.")
    except Exception as e:
        print(f"Error while trying to start the process: {e}")


# Exit "Camera Hub.exe"
beende_prozess("Camera Hub.exe")
def lese_textdatei(dateipfad):
    with open(dateipfad, 'r', encoding='utf-8') as file:
        return [zeile.strip() for zeile in file]

def aktualisiere_json(json_pfad, neuer_text):
    with open(json_pfad, 'r+', encoding='utf-8') as file:
        daten = json.load(file)
        daten["applogic.prompter.source.text"] = neuer_text
        file.seek(0)
        json.dump(daten, file, indent=4)
        file.truncate()

# Dynamically generate path to JSON file
appdata_pfad = os.getenv('APPDATA')
json_datei_pfad = os.path.join(appdata_pfad, 'Elgato', 'CameraHub', 'AppSettings.json')

# Base path for text files
basispfad_textdateien = "e:\\textfiles\\"

# List of text files
textdateien = [basispfad_textdateien + 'text1.txt', basispfad_textdateien + 'text2.txt',basispfad_textdateien + 'text3.txt',basispfad_textdateien + 'text4.txt',basispfad_textdateien + 'text5.txt',basispfad_textdateien + 'text6.txt',basispfad_textdateien + 'text7.txt',basispfad_textdateien + 'text8.txt',basispfad_textdateien + 'text9.txt', basispfad_textdateien + 'text10.txt']

# Select text file
print("Please select a text file:")
for i, datei in enumerate(textdateien, 1):
    print(f"{i}. {datei}")
auswahl = int(input("Enter the file number: "))

# Make sure the selection is valid
if 1 <= auswahl <= len(textdateien):
    ausgewaehlte_datei = textdateien[auswahl - 1]
    neuer_text = lese_textdatei(ausgewaehlte_datei)
    aktualisiere_json(json_datei_pfad, neuer_text)
    print(f"The file {ausgewaehlte_datei} was successfully inserted into the JSON file.")

    # Start the “Camera Hub.exe” after a successful update
    camera_hub_pfad = "C:\\Program Files\\Elgato\\CameraHub\\Camera Hub.exe"
    starte_prozess(camera_hub_pfad)

else:
    print("Invalid selection.")
