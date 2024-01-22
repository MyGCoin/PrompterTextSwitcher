import os
import json
import subprocess

def beende_prozess(prozessname):
    try:
        subprocess.run(["taskkill", "/f", "/im", prozessname], check=True)
        print(f"Prozess {prozessname} wurde erfolgreich beendet.")
    except subprocess.CalledProcessError:
        print(f"Konnte Prozess {prozessname} nicht beenden. Möglicherweise läuft er nicht.")


def starte_prozess(prozesspfad):
    try:
        subprocess.Popen(prozesspfad)
        print(f"Prozess {prozesspfad} wurde erfolgreich gestartet.")
    except Exception as e:
        print(f"Fehler beim Starten des Prozesses: {e}")


# Beenden der "Camera Hub.exe"
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

# Pfad zur JSON-Datei dynamisch erzeugen
appdata_pfad = os.getenv('APPDATA')
json_datei_pfad = os.path.join(appdata_pfad, 'Elgato', 'CameraHub', 'AppSettings.json')

# Basispfad für Textdateien
basispfad_textdateien = "e:\\textfiles\\"

# Liste der Textdateien
textdateien = [basispfad_textdateien + 'text1.txt', basispfad_textdateien + 'text2.txt',basispfad_textdateien + 'text3.txt',basispfad_textdateien + 'text4.txt',basispfad_textdateien + 'text5.txt',basispfad_textdateien + 'text6.txt',basispfad_textdateien + 'text7.txt',basispfad_textdateien + 'text8.txt',basispfad_textdateien + 'text9.txt', basispfad_textdateien + 'text10.txt']

# Benutzerauswahl
print("Bitte wählen Sie eine Textdatei aus:")
for i, datei in enumerate(textdateien, 1):
    print(f"{i}. {datei}")
auswahl = int(input("Geben Sie die Nummer der Datei ein: "))

# Sicherstellen, dass die Auswahl gültig ist
if 1 <= auswahl <= len(textdateien):
    ausgewaehlte_datei = textdateien[auswahl - 1]
    neuer_text = lese_textdatei(ausgewaehlte_datei)
    aktualisiere_json(json_datei_pfad, neuer_text)
    print(f"Die Datei {ausgewaehlte_datei} wurde erfolgreich in die JSON-Datei eingefügt.")

    # Starten der "Camera Hub.exe" nach erfolgreicher Aktualisierung
    camera_hub_pfad = "C:\Program Files\Elgato\CameraHub/Camera Hub.exe"
    starte_prozess(camera_hub_pfad)

else:
    print("Ungültige Auswahl.")
