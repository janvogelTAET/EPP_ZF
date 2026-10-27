# EPP Performance Zusammenfassung (HS26) – LaTeX-Quelle

Blöcke P1–P6 für die MEP. A4 hoch, 2 Spalten, 8pt, aktuell 6 Seiten
(die MEP erlaubt 12 – die andere Hälfte bleibt für Embedded Power).

## Bauen
- **`EPP_ZF.code-workspace` mit VS Code öffnen** (Doppelklick oder *Datei → Arbeitsbereich aus Datei öffnen*).
  Darin sind alle LaTeX-Workshop-Einstellungen: Auto-Build beim Speichern, 2× pdflatex, PDF im VS-Code-Tab.
  VS Code fragt beim ersten Öffnen, ob du dem Ordner vertraust → *Ja*. Fehlt LaTeX Workshop, schlägt VS Code die Installation vor.
- Jede Datei in `sections/` hat `% !TEX root = ../main.tex`, Speichern in einem Kapitel baut also immer das ganze Dokument.
- `main.tex` öffnen und speichern → baut automatisch (2× pdflatex). PDF anzeigen: `Ctrl+Alt+V`.
- Ohne VS Code: `pdflatex main.tex` zweimal ausführen, oder `latexmk -pdf main.tex`.

## Struktur
| Datei | Inhalt |
|---|---|
| `main.tex` | Layout (A4 hoch, 2 Spalten), Farben, Boxen, Kopf/Fuss, eigene Befehle, Titel + Inhaltsverzeichnis |
| `sections/00_navigation.tex` | Farblegende + Tabelle „Wenn die Aufgabe lautet …“ |
| `sections/01_cache.tex` … `08_reconfig.tex` | ein Vorlesungsblock pro Datei |
| `sections/09_referenz.tex` | alle Formeln, sieben durchgerechnete Beispiele |
| `sections/10_register.tex` | Stichwortregister (erzeugt, siehe unten) |
| `figures/` | Bilder (PNG), via `\fig{...}` |

Reihenfolge ändern: `\input`-Zeilen in `main.tex` umsortieren.
Block weglassen: Zeile auskommentieren.

## Wie man etwas findet
1. **Farbe** – jeder Block hat eine eigene Balkenfarbe (P1 blau … P6 petrol).
2. **Abschnitt 10** – Stichwortregister, 90 Begriffe → Abschnittsnummer.
3. **Seite 1** – Tabelle „Wenn die Aufgabe lautet …“ geht von der Aufgabenstellung direkt zur Nummer.

## Eigene Befehle (in `main.tex` definiert)
- `\vlsec{cP3}{P3}{Titel}` – Blocküberschrift, setzt zugleich die Blockfarbe
- `\R{VADD.I16}` – Register, Befehl, Code inline (Monospace)
- `\T{Begriff}` – Schlüsselbegriff (fett)
- `\SW{Stichwort}` – farbiges Stichwort am Zeilenanfang, macht die Seite scanbar
- `\ra` – Pfeil mit passenden Abständen
- `\begin{ztab}{@{}Xr@{}} Kopf & Kopf \\ \midrule … \end{ztab}` – kompakte Tabelle über die Spaltenbreite
- `\begin{formel}[Titel] … \end{formel}` – Formel/Kernaussage, färbt sich mit dem Block
- `\begin{falle}[Titel] … \end{falle}` – typischer Fehler (rot)
- `\begin{rezept}[Titel] … \end{rezept}` – Schritt für Schritt (grün)
- `\begin{bsp}[Titel] … \end{bsp}` – durchgerechnetes Beispiel (gelb)
- `\fig[0.6]{name}` – Bild aus `figures/`, Breite als Anteil der Spaltenbreite

## Stichwortregister
`sections/10_register.tex` ist von `mkreg.py` erzeugt (liegt im selben Ordner).
Neue Einträge dort in die Liste `E` eintragen und

```
python mkreg.py sections/10_register.tex
```

laufen lassen – sortiert alphabetisch und verteilt auf zwei Spaltenpaare.
Von Hand einsortieren geht genauso, die Datei ist normales LaTeX.

## Platz
Reicht der Platz nicht:
1. Ränder in `main.tex` (`geometry`) enger,
2. dann die Schriftgrösse in `\documentclass[8pt]{extarticle}` (erlaubt: 8, 9, 10, 11, 12, 14, 17, 20pt),
3. zuletzt Inhalt kürzen.

## Abhängigkeiten
Standardpakete einer vollen TeX-Distribution. Nicht ganz minimal sind
`extsizes` (für `extarticle`), `tcolorbox`, `environ`, `titlesec`,
`lastpage`. MiKTeX installiert sie beim ersten Build automatisch nach.

## Stand der Folien
Quelle sind `EPP_P1_MemHier_260819`, `EPP_P2_SIMD_250926`,
`EPP_P3_DMA_251002`, `EPP_P4_RV32_261008`, `EPP_P5_MultiProc_251016`,
`EPP_P6_ReconfigHW_250821`.
P2 enthält seit der Aktualisierung zusätzlich die RISC-V-Vektorerweiterung
(Folien 23–33) – das ist Abschnitt 4.

## Zu prüfen (Fehler in den Folien, in der Zusammenfassung korrigiert)
- P2 Folie 10: `MSR FPEXC,r0` – korrekt ist `VMSR FPEXC, r0`
- P2 Folie 22: `r0 = &Array1` beim zweiten Array – gemeint ist `r1 = &Array2`
- P2 Folie 22, Schritt 7: `padd.f32` – gemeint ist `vpadd.f32`
- P2 Folie 6/7: „16 128-bit registers“ gilt für ARMv7; AArch64 (Pi 4/5) hat 32
- P3 Folie 5: „Interconnect 64B / 32B“ – gemeint ist Bit, nicht Byte
- P3 Folie 22: „RP1250“ – gemeint ist RP2350
- P1 Folie 13: Bitgruppierung bei `0x41` im Fliesstext verrutscht, Tabelle stimmt
