# Ampelsteuerung
Es wird mithilfe eines Raspberry 4.0 und dem W&amp;T Schulungs - Ampelboard eine vollautomatische Ampelsteuerung realisert. Als Software wurde Python verwendet.



# Genaue Beschreibung
Es wurde ein kleines Projekt erstellt, bei dem eine Kreuzung mit 4 Verkehrsampeln und 4 Fußgängerampeln realisiert werden sollte. Die Kreuzung selbst stand uns durch das W&amp;T Schulungs - Ampelboard schon zur Verfügung und musste somit nicht mehr selbst erstellt werden. Das Python - Programm wurde dann mithilfe des Raspberrys auf das Board geladen. Die PIN - Belegungen der beiden Hardware Komponenten mussten noch recherchiert werden. 
- Als erster Zwischenschritt wurde der Ampelablauf für eine Ampel programmiert.
- Als nächstens wurde dann der Ablauf der Fußgängerampel hinzugefügt.
- Der letzte Schritt war dann das erstellen und implementieren der restlichen Ampeln.



# Voraussetztung/benötigte Geräte
- Raspberry (in unserem Fall Rapsberry 4.0)
- W&amp;T Schulungsboard mit Ampelaufbau
- Laptop bzw. PC mit einer funktionierenden Verbindung zum Raspberry



# Verbindung des Raspberrys mit dem Ampelboard
Die Verbindungen zwischen Raspberry und dem Ampelboard wird mit Jumper - Kabel hergestellt. Dabei mussten zuerst die Namen der einzelnen PINs des Steckers auf dem Ampelboard herausgefunden werden. Dies wurde einfach mit einem Multimeter gemacht. Je nachdem welche der "Ampel - LEDs" leuchtete, wussten wir mit welchem Pin diese verbunden ist. Die genaue Pinbelegung des Ampelbpoards, des Raspberrys und wie diese verbunden werden müssen, ist im PDF - Pinnbelegung nachlesbar.
Link zum File [Pinnbelegung.pdf](https://github.com/JorTur099/Ampelsteuerung/blob/master/Pinnbelegung.pdf)



# Code Beschreibung
Der Code ist nicht  unbedingt komplex, jedoch trotzdem sehr zweitaufwendig zu erstellen. Zuerst wurden die benötigten Pins festgelegt und die benötigte Methoden eingefügt. Anschließend musste der Ampelablauf implementiert werden. Da es sich um eine Kreuzung mit 4 Verkehrsampeln und vier Fußgängerampeln handelt, ist dieser Ablauf sehr lange. Die jeweiligen Zustände wuerden mit Delays für die benötigte Zeit gehalten. Zum Schluss wurde der Code noch etwas verschönert, damit dieser besser verständlich ist.

Auf dem folgenden Link kommen sie zum erstellten Code: [LED_Blinken_2](https://github.com/JorTur099/Ampelsteuerung/blob/master/LED_Blinken_2.py)



# Aufbau und Funktionalität 
Um die Funktionalität des Projektes zu zeigen haben folgendes [Video](https://github.com/JorTur099/Ampelsteuerung/blob/master/VideoAmpelsteuerung.mp4) der Ampelsteuerung erstellt.
Ebenfall haben wir ein paar [Bilder](https://github.com/JorTur099/Ampelsteuerung) Aufbaus gemacht.


Erstellt von Jordan Türtscher & Stefan Rüdisser
