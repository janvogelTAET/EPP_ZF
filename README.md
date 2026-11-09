# EPP Zusammenfassung (HS26) – LaTeX-Quelle

A4 hoch, 2 Spalten, 8pt, 7 Seiten. Nach **Themen** gegliedert, nicht nach
Vorlesungswochen.

## Bauen
- **`EPP_ZF.code-workspace` mit VS Code öffnen** (Doppelklick oder *Datei → Arbeitsbereich aus Datei öffnen*).
  Darin sind alle LaTeX-Workshop-Einstellungen: Auto-Build beim Speichern, 2× pdflatex, PDF im VS-Code-Tab.
  VS Code fragt beim ersten Öffnen, ob du dem Ordner vertraust → *Ja*. Fehlt LaTeX Workshop, schlägt VS Code die Installation vor.
- Jede Datei in `sections/` hat `% !TEX root = ../main.tex`, Speichern in einem Kapitel baut also immer das ganze Dokument.
- `main.tex` öffnen und speichern → baut automatisch (2× pdflatex). PDF anzeigen: `Ctrl+Alt+V`.
- Ohne VS Code: `pdflatex main.tex` zweimal ausführen, oder `latexmk -pdf main.tex`.

> `EPP_ZF.code-workspace`, `vscode-settings.json` und das gebaute `main.pdf`
> stehen in `.gitignore` – sie liegen lokal, sind aber nicht im Repo.
> Nach einem frischen `git clone` sind sie also nicht da; die Workspace-Datei
> kannst du aus `LEAS_ZF` kopieren und `LEAS` durch `EPP` ersetzen.

## Struktur
| Datei | Inhalt |
|---|---|
| `main.tex` | Layout, Farbe, Boxen, Kopf/Fuss, eigene Befehle, Titel + Inhaltsverzeichnis, `\input`-Liste |
| `sections/00_navigation.tex` | Tabelle „Wenn die Aufgabe lautet …“ + Legende |
| `sections/01_cache.tex`, `02_mmu.tex` | Speicher |
| `sections/03_neon.tex`, `04_rvv.tex` | Datenparallelität (SIMD) |
| `sections/05_dma.tex` | Datentransport |
| `sections/06_riscv.tex`, `07_multicore.tex` | Prozessor |
| `sections/08_reconfig.tex` | Hardware statt Software (FPGA, CGRA, PIO) |
| `sections/09_docker.tex` | Werkzeuge |
| `sections/10_referenz.tex` | alle Formeln, sieben durchgerechnete Beispiele |
| `sections/11_register.tex` | Stichwortregister (erzeugt, siehe unten) |
| `figures/` | Bilder (PNG), via `\fig{...}` |

Reihenfolge ändern: `\input`-Zeilen in `main.tex` umsortieren.
Thema weglassen: Zeile auskommentieren.
Die `\input`-Liste ist mit Kommentaren in Themengruppen unterteilt.

## Wie man etwas findet
1. **Seite 1** – Tabelle „Wenn die Aufgabe lautet …“ geht von der Aufgabenstellung direkt zur Abschnittsnummer.
2. **Abschnitt 11** – Stichwortregister, 117 Begriffe → Abschnittsnummer.
3. **Inhaltsverzeichnis** – die 11 Themen mit Seitenzahl.

Es gibt **eine** durchgehende Akzentfarbe. Die Farben der Boxen stehen für
die *Art* des Inhalts, nicht für eine Vorlesungswoche:

| Box | Bedeutung |
|---|---|
| blau | Formel oder Kernaussage |
| rot | typische Falle, häufiger Fehler |
| grün | Rezept, Schritt für Schritt |
| gelb | durchgerechnetes Beispiel |

## Eigene Befehle (in `main.tex` definiert)
- `\R{VADD.I16}` – Register, Befehl, Code inline (Monospace)
- `\T{Begriff}` – Schlüsselbegriff (fett)
- `\SW{Stichwort}` – farbiges Stichwort am Zeilenanfang, macht die Seite scanbar
- `\merkzeile` – Zeile mit Pfeil-Marker für einen Merksatz
- `\ra` – Pfeil mit passenden Abständen
- `\begin{ztab}{@{}Xr@{}} Kopf & Kopf \\ \midrule … \end{ztab}` – kompakte Tabelle über die Spaltenbreite
- `\begin{formel}[Titel] … \end{formel}` – Formel/Kernaussage
- `\begin{falle}[Titel] … \end{falle}` – typischer Fehler
- `\begin{rezept}[Titel] … \end{rezept}` – Schritt für Schritt
- `\begin{bsp}[Titel] … \end{bsp}` – durchgerechnetes Beispiel
- `\fig[0.6]{name}` – Bild aus `figures/`, Breite als Anteil der Spaltenbreite

## Stichwortregister
`sections/11_register.tex` ist von `mkreg.py` erzeugt. Neue Einträge dort in
die Liste `E` eintragen und

```
python mkreg.py sections/11_register.tex
```

laufen lassen – sortiert alphabetisch und verteilt auf drei Spaltenpaare
(`NCOL` im Skript). Von Hand einsortieren geht genauso, die Datei ist
normales LaTeX.

## Platz
Reicht der Platz nicht:
1. Ränder in `main.tex` (`geometry`) enger,
2. dann die Schriftgrösse in `\documentclass[8pt]{extarticle}` (erlaubt: 8, 9, 10, 11, 12, 14, 17, 20pt),
3. zuletzt Inhalt kürzen.

## Abhängigkeiten
Standardpakete einer vollen TeX-Distribution. Nicht ganz minimal sind
`extsizes` (für `extarticle`), `tcolorbox`, `environ`, `titlesec`,
`lastpage`. MiKTeX installiert sie beim ersten Build automatisch nach.

## Quellen
`EPP_P1_MemHier_260819`, `EPP_P2_SIMD_250926` (enthält seit der
Aktualisierung zusätzlich die RISC-V-Vektorerweiterung, Folien 23–33),
`EPP_P3_DMA_251002`, `EPP_P4_RV32_261008`, `EPP_P5_MultiProc_251016`,
`EPP_P6_ReconfigHW_250821`, `EPP_H25-Docker-Teil_1-v3.09`, `EPP_H26-Docker-Teil 2 v3.10`.

> **Achtung MEP:** Die Docker-Folien nennen für den Docker-Teil eine
> *eigene* Prüfung mit *eigenem* Hilfsmittel-Limit – vier A4-Seiten auf zwei
> Blättern, doppelseitig. Der Performance-Teil erlaubt zwölf Seiten auf sechs
> Blättern. Falls das zwei getrennte Prüfungen sind, gehört Abschnitt 9
> vermutlich in ein eigenes Dokument; dann die Zeile
> `\input{sections/09_docker}` in `main.tex` auskommentieren und daraus eine
> zweite `main.tex` bauen.

## Zu prüfen (Fehler in den Folien, in der Zusammenfassung korrigiert)
- P2 Folie 10: `MSR FPEXC,r0` – korrekt ist `VMSR FPEXC, r0`
- P2 Folie 22: `r0 = &Array1` beim zweiten Array – gemeint ist `r1 = &Array2`
- P2 Folie 22, Schritt 7: `padd.f32` – gemeint ist `vpadd.f32`
- P2 Folie 6/7: „16 128-bit registers“ gilt für ARMv7; AArch64 (Pi 4/5) hat 32
- P3 Folie 5: „Interconnect 64B / 32B“ – gemeint ist Bit, nicht Byte
- P3 Folie 22: „RP1250“ – gemeint ist RP2350
- P1 Folie 13: Bitgruppierung bei `0x41` im Fliesstext verrutscht, Tabelle stimmt
- Docker Folie 69: „wir nutzen hier Debian“ – dieses Semester Ubuntu (steht auch so auf der Folie)
