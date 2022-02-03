# DSA-RASA: Teil des Semesterprojektes
(von Andrej Alpatov, Marco Ohnesorg und Danny Staus im Wintersemester 2021/22)

## Beschreibung
Mit `Rasa` können wir einen Chatbot erstellen, um ein *Experiment* für unser Semesterprojekt durchzuführen. 
Das *Experiment* besteht zum Einen aus der Übertragung von Intents und Utterances von der `Amazon Developer Console` 
in `Rasa` und zum Anderen aus dem Vergleich zwischen verschiedenen `Rasa Pipelines` und `Alexa` bezüglich der *Erkennungsgenauigkeit* von Benutzereingaben.

## Funktionalität
Der Chatbot verfügt, im Vergleich zum `Mensa Skill`, über *eingeschränktere* Funktionalität. Die Standard-Intents wurden auf die deutsche Sprache umgeändert.
#### Beispielfragen des Chatbots:
- Wie bediene ich diesen Skill?
- Wann kann ich in die Mensa essen gehen?
- Bis wie viel Uhr kann ich in die Mensa gehen?
- Gibt es Coca Cola am Kiosk?
- Darf ich am Kaffeeautomaten meinen eigenen Becher befüllen?
- Zu welcher Organisation gehört die Mensa?
- Was sind die Themen des Studierendenwerks Vorderpfalz?
- Betreibt das Studierendenwerk der Vorderpfalz noch weitere Mensen?
- Kannst du mir etwas zum Betreiber der Mensa sagen?
#### Die folgenden Intents wurden mit *fiktiven* Antworten Implementiert:
- OpeningHoursIntent
- KioskMenuWhatIntent
- PriceQueryIntent
- QueryMenuIntent
- HelpIntent

## Projektstruktur
### models:
Hier sind drei ätere Models mit verschiedenen Classifiers und Anzahl an Utterances enthalten, um die verschiedenen Chatbots zu trainieren.
Die aktuellen Models wurden per Mail abgegeben.

### actions:
Hier ist die Datei `actions.py` enthalten, die das Backend für zwei Intents implementiert *(OpeningTimeIntent und KioskMenuIfIntent)*

### data:
Dieser Ordner besteht aus mehreren Teilen:
#### nlu:
Hier sind alles Intents mit den zugehörigen Utterances enthalten.

#### rules:
Legt den Kontroll- und Datenfluss des Gesprächs fest.

### Dokumention:
Die Dokumentation besteht aus *zwei* Teilen:
#### 1. Externe Dokumentation:
Die Dateien der externen Dokumentation wurden per Mail übergeben um im Folgenden aufgelistet:
- Freitext *(Datei: `Dokumentation.pdf`)*
- Rasa Ergebnisse *(Datei: `RASA_accuracy.pdf`)*
- Demo-Video *(Datei: `Demo_Video.mp4`)*
#### 2. Interne Code-Dokumentation:
Die interne Dokumentation ist eine Code-Dokumentation und wurde mit `pdoc3` umgesetzt. Die zugehörigen *HTML-Dateien* befinden sich im Ordner `doc`.
