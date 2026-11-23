# EPP Zusammenfassungen (HS26) – LaTeX-Quelle

Drei getrennte Zusammenfassungen, je eine pro MEP-Teil, mit **gemeinsamer
Präambel**. A4 hoch, 2 Spalten, 8pt, nach Themen gegliedert.

| Dokument | Inhalt | Seiten | MEP erlaubt |
|---|---|---:|---:|
| `main_performance.tex` | Cache, MMU, SIMD, DMA, RISC-V, Multicore, FPGA/PIO | 9 | 12 (6 Blätter) |
| `main_docker.tex` | Docker Teil 1–4 | 4 | 4 (2 Blätter) |
| `main_power.tex` | Embedded Power, Teil 1–7 | 4 | 4 |

## Bauen

```
latexmk -pdf main_performance.tex
latexmk -pdf main_docker.tex
latexmk -pdf main_power.tex
```

In VS Code (Profil „latex“): Workspace öffnen, speichern baut automatisch.
Die drei Root-Dateien sind in `EPP_ZF.code-workspace` eingetragen, jede
Datei unter `sections/` trägt oben ihr `% !TEX root`.

## Struktur

```
preamble.tex              Layout, Farbe, Boxen, Befehle – gilt für alle drei
main_performance.tex      \input-Liste + \doctitle/\docsubject
main_docker.tex
main_power.tex
mkreg.py                  erzeugt die drei Stichwortregister
sections/
  performance/  00_navigation 01_cache 02_mmu 03_neon 04_rvv
                05_dma 06_riscv 07_multicore 08_reconfig
                90_referenz 99_register
  docker/       00_navigation 01_grundlagen 02_container 03_images
                04_dockerfile 05_multistage 90_referenz 99_register
  power/        00_navigation 01_grundlagen 02_hardware 03_software
                04_kinetis 05_freertos 06_messen 90_referenz 99_register
figures/                  Bilder (PNG), via \fig{...}
```

Jedes Dokument hat denselben Aufbau: **Navigationstabelle** („Wenn die
Aufgabe lautet …“) → Inhaltsverzeichnis → Themenabschnitte → `90_referenz`
(Formeln und durchgerechnete Beispiele) → `99_register` (Stichwortregister).

Reihenfolge ändern: `\input`-Zeilen in der jeweiligen `main_*.tex`
umsortieren. Thema weglassen: Zeile auskommentieren.

## Wie man etwas findet

Drei Wege, absichtlich redundant:

1. **Navigationstabelle** auf Seite 1 – von der Aufgabenstellung direkt
   zur Abschnittsnummer.
2. **Stichwortregister** am Ende – vom Begriff zur Abschnittsnummer.
3. **Farbige Boxen** – die Farbe sagt, was für ein Inhalt das ist:

| Box | Farbe | Bedeutung |
|---|---|---|
| `formel` | blau | Formel oder Kernaussage |
| `falle` | rot | typischer Fehler |
| `rezept` | grün | Schritt-für-Schritt-Vorgehen |
| `bsp` | grau | durchgerechnetes Beispiel |
| `achtung` | gelb | Randbedingung |

## Eigene Befehle (in `preamble.tex` definiert)

| Befehl | Zweck |
|---|---|
| `\R{...}` | Register, Code, Kommando (Typewriter) |
| `\T{...}` | Fettes Schlüsselwort im Fliesstext |
| `\SW{...}` | Stichwort am Absatzanfang (blau, fett) |
| `\ra` | Pfeil → mit passenden Abständen |
| `\merkzeile` | Blaues ▶ für eine Merksatz-Zeile |
| `\fig[breite]{datei}{bildunterschrift}` | Bild aus `figures/` |
| `ztab` | Tabelle mit `tabularx` + Booktabs-Linien |

## Stichwortregister

Erzeugt, **nicht von Hand ändern**:

```
python3 -I mkreg.py performance   # oder docker, power, all
```

Neue Begriffe in `mkreg.py` in der passenden Liste `REG[...]` ergänzen;
sortiert wird automatisch. Spaltenzahl pro Dokument oben in `NCOL`.

## Platz

Reicht der Platz nicht:

1. Ränder in `preamble.tex` (`geometry`) enger,
2. dann die Schriftgrösse in `\documentclass[8pt]{extarticle}` der
   betroffenen `main_*.tex` (erlaubt: 8, 9, 10, 11, 12, 14, 17, 20pt),
3. `NCOL` im Register hochsetzen,
4. zuletzt Inhalt kürzen.

Umgekehrt: Performance hat noch 3 Seiten Reserve – Platz für eigene
Notizen oder für Stoff, der noch kommt.

## Abhängigkeiten

Standardpakete einer vollen TeX-Distribution. Nicht ganz minimal sind
`extsizes` (für `extarticle`), `tcolorbox`, `environ`, `titlesec`,
`lastpage`. MiKTeX installiert sie beim ersten Build automatisch nach.

## Quellen

**Performance:** `EPP_P1_MemHier_260819`, `EPP_P2_SIMD_250926` (enthält
seit der Aktualisierung zusätzlich die RISC-V-Vektorerweiterung,
Folien 23–33), `EPP_P3_DMA_251002`, `EPP_P4_RV32_261008`,
`EPP_P5_MultiProc_251016`, `EPP_P6_ReconfigHW_250821`.

**Docker:** `EPP_H25-Docker-Teil_1-v3.09`, `EPP_H26-Docker-Teil 2 v3.10`,
`EPP_H26-Docker-Teil_3-v3.12`, `EPP_H26-Docker-Teil_4-v3.13`.

**Power:** `Teil 1 – Einführung` bis `Teil 7 – Abschluss`
(Prof. Erich Styger, Stand 2. November 2026).

Nicht aufgenommen, weil die Folien es ausdrücklich als nicht
prüfungsrelevant markieren:

- Docker Teil 4, Folie 362: GPIO mit Raspi/Docker/C#, Portainer,
  Docker Networking („der Reduktion von 4 auf 3 Lektionen zum Opfer
  gefallen“).

## Zu prüfen (Fehler in den Folien, in der Zusammenfassung korrigiert)

- P2 Folie 10: `MSR FPEXC,r0` – korrekt ist `VMSR FPEXC, r0`
- P2 Folie 22: `r0 = &Array1` beim zweiten Array – gemeint ist `r1 = &Array2`
- P2 Folie 22, Schritt 7: `padd.f32` – gemeint ist `vpadd.f32`
- P2 Folie 6/7: „16 128-bit registers“ gilt für ARMv7; AArch64 (Pi 4/5) hat 32
- P2 Folie 19: `B[k*j_idx + k_idx]` – gemeint ist `B[4*j_idx + k_idx]`
- P3 Folie 5: „Interconnect 64B / 32B“ – gemeint ist Bit, nicht Byte
- P3 Folie 22: „RP1250“ – gemeint ist RP2350
- P1 Folie 13: Bitgruppierung bei `0x41` im Fliesstext verrutscht, Tabelle stimmt
- P1 Folie 4: „shared L3 Cahce“ – Tippfehler
- Docker Folie 69: „wir nutzen hier Debian“ – dieses Semester Ubuntu
  (steht auch so auf der Folie)
- Docker Teil 4, Folie 337 gegen 338: im Text „Alpine ca. 14 MB, Debian
  ca. 200 MB“, in der `docker images`-Ausgabe derselben Folien 7.46 MB
  bzw. 118 MB (arm64). Die Zusammenfassung nennt beides: Folienwerte für
  den Grössenvergleich, Messwerte in der Beispieltabelle.
- Docker Teil 4, Folie 330 gegen 338: `my-hello-world` einmal 1.15 GB,
  einmal 1.18 GB (unterschiedliche `gcc`-Image-Version) – die
  Grössenordnung ist gemeint, nicht der exakte Wert.
- Power Teil 5, Folien 79–81: die `ENERGY`-Werte der drei Modi (52.6 /
  60.2 / 13.7 µWh) stammen aus **unterschiedlichen Zeitfenstern** und
  sind nicht direkt vergleichbar; vergleichbar sind die Ströme.
