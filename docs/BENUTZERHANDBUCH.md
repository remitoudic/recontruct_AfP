# AfP Pfandhaus-Software - Benutzerhandbuch

Willkommen beim Benutzerhandbuch für die AfP Pfandhaus-Software. Dieses Programm wurde entwickelt, um Ihre täglichen Geschäftsabläufe im Pfandhaus zu vereinfachen – von der Kundenregistrierung über die Ausstellung von Pfandscheinen bis hin zum Kassenabschluss am Ende des Tages.

---

## 1. Dashboard & Übersicht
Wenn Sie sich in der Anwendung anmelden, werden Sie vom **Dashboard** begrüßt.
Hier sehen Sie:
*   **Tagesübersicht:** Gesamteinnahmen und -ausgaben des aktuellen Tages.
*   **Ablaufende Pfänder:** Warnungen für Pfandscheine, die fällig sind oder bald ablaufen, sodass Sie rechtzeitig nachfassen oder Versteigerungen vorbereiten können.

---

## 2. Kundenverwaltung (Kunden)
Bevor Sie einen Pfandschein ausstellen können, muss die Person im System registriert werden.

### Einen neuen Kunden anlegen
1. Navigieren Sie zum Reiter **Kunden**.
2. Klicken Sie auf **Kunde hinzufügen**.
3. Geben Sie die Details ein: Vorname, Nachname, Geburtsdatum und Adresse.
4. **Zwingende Identitätsprüfung:** Sie müssen die Ausweisnummer (`Personr`), die Art des Ausweises (`Legitimation`) und die ausstellende Behörde (`Behörde`) erfassen.

### Einen Kunden sperren
Wenn ein Kunde keine Gegenstände mehr verpfänden darf (z.B. wegen vorheriger Zahlungsausfälle oder Betrugsverdacht), können Sie sein Profil auf **Gesperrt** (`sperre`) setzen. Das System verhindert dann die Ausstellung neuer Pfandscheine für diesen Kunden.

---

## 3. Pfandverwaltung (Pfand)
Dieses Modul verwaltet die Annahme von Gegenständen und die Auszahlung von Barkrediten.

### Einen neuen Pfandschein ausstellen
1. Wählen Sie einen registrierten Kunden aus und klicken Sie auf **Neuer Pfandschein**.
2. **Gegenstandsdetails:** Geben Sie eine genaue Beschreibung des Gegenstands ein (`Gegenstand`).
3. **Lagerung:** Notieren Sie genau, wo der Gegenstand im Lager aufbewahrt wird (`Lager`), damit er später leicht gefunden werden kann.
4. **Finanzen:** Geben Sie den Auszahlungsbetrag an den Kunden (`Betrag`) und eventuelle anfängliche Gebühren (`Unkosten`) ein.
5. **Drucken:** Das System erstellt einen Pfandschein als PDF. Drucken Sie diesen aus und übergeben Sie ihn dem Kunden.

### Einen Pfandschein verlängern
Wenn das Fälligkeitsdatum (`Enddatum`) erreicht ist und der Kunde den Kredit verlängern möchte, anstatt den Gegenstand auszulösen:
1. Suchen Sie den aktiven Pfandschein.
2. Klicken Sie auf **Verlängern**.
3. Der Kunde muss die angefallenen Zinsen und Gebühren bezahlen. Sobald diese bezahlt sind, markiert das System den alten Schein automatisch als abgeschlossen und erstellt einen **neuen Pfandschein**, der mit dem alten verknüpft ist (über `Vorgaenger` und `Nachfolger`).

### Einen Gegenstand auslösen
Wenn ein Kunde zurückkehrt, um seinen Kredit zurückzuzahlen:
1. Suchen Sie den Pfandschein.
2. Klicken Sie auf **Auslösen**.
3. Kassieren Sie den ursprünglichen Kreditbetrag zuzüglich aller angefallenen Gebühren. Das System markiert den Pfandschein als geschlossen und aktualisiert das Kassenbuch.

---

## 4. Das Kassenbuch (Einaus)
Das Kassenbuch ist das finanzielle Herzstück des Pfandhauses. Es stellt sicher, dass jeder Cent nachverfolgt wird.

### Automatische Einträge
Sie müssen selten Dinge manuell eintragen. Das System erstellt automatisch Kassenbucheinträge, wenn:
*   Bargeld für einen neuen Pfandschein ausgezahlt wird.
*   Bargeld aus einer Pfandverlängerung eingeht (Kassierte Gebühren).
*   Bargeld aus einer Pfandauslösung eingeht (Kreditrückzahlung + Gebühren).

### Täglicher Kassenabschluss
Navigieren Sie am Ende des Tages zum Reiter **Kassenbuch**.
*   Vergleichen Sie den **Systembestand** mit dem tatsächlichen Bargeld in Ihrer Kasse.
*   Wenn Sie manuelle Anpassungen vornehmen müssen (z.B. Bezahlung einer Reinigungskraft aus der Kasse oder Bareinzahlung bei der Bank), können Sie auf **Manuellen Eintrag hinzufügen** klicken und den Betrag sowie den Grund (`Posten`) angeben.
