#!/usr/bin/env python3
# Generiert sections/10_register.tex: alphabetisch sortiert, zweispaltig.
import unicodedata, sys

E = [
    ("Adresszerlegung", "rez:zerlegung"),
    ("AMAT", "form:amat"),
    ("Amdahl", "form:amdahl"),
    ("Assoziativität", "sec:cache"),
    ("Autopull/-push", "sec:reconfig"),
    ("AXI-Burst", "sec:dma"),
    ("Bandbreite", "form:bw"),
    (r"\R{BR}/\R{BG}", "sec:dma"),
    (r"\R{BSWAP}", "sec:dma"),
    ("Cache Line", "sec:cache"),
    ("CAM", "sec:cache"),
    (r"\R{CCR}", "rez:ccr"),
    ("CGRA", "sec:cgra"),
    (r"\R{CHAIN\_TO}", "sec:dma"),
    ("Control Block", "rez:ti"),
    ("Copy-on-write", "sec:mmu"),
    (r"\R{CPACR}", "sec:neon"),
    ("CRC im DMA", "sec:dma"),
    ("Cycle Stealing", "sec:dma"),
    ("Dirty Bit", "sec:cache"),
    (r"\R{DMAWFP}", "sec:dma"),
    ("Doorbell", "sec:multicore"),
    ("DREQ / TREQ", "sec:dma"),
    ("Exclusive Monitor", "sec:multicore"),
    ("Flags (fehlen)", "sec:rvflags"),
    (r"\R{FPEXC}", "sec:neon"),
    ("FPGA / LUT", "sec:reconfig"),
    ("FreeRTOS-API", "sec:multicore"),
    ("Harvard", "sec:cache"),
    ("Index", "rez:zerlegung"),
    ("Intrinsics", "sec:neon"),
    ("Kohärenz (Cache)", "falle:dma"),
    ("Kohärenz (Multicore)", "sec:kohaerenz"),
    ("Lanes", "sec:neon"),
    ("Locality", "sec:cache"),
    ("Loop Peeling", "sec:dma"),
    ("Loop Unrolling", "sec:neon"),
    ("LRU", "sec:cache"),
    (r"MAC / \R{VMLA}", "sec:neon"),
    ("Mailbox", "sec:kohaerenz"),
    (r"Maske (\R{VBSL})", "sec:neon"),
    ("Matrixmult. NEON", "sec:neon"),
    ("MFIFO", "sec:dma"),
    ("MMU", "sec:mmu"),
    ("MPU", "sec:mmu"),
    ("Mutex", "sec:kohaerenz"),
    (r"\R{NEXTCONBK}", "rez:ti"),
    ("NMRU", "sec:cache"),
    ("Offset", "rez:zerlegung"),
    ("Page Fault", "sec:mmu"),
    ("Page Table", "sec:mmu"),
    ("Pairwise", "sec:neon"),
    ("Panic-Signal", "sec:dma"),
    (r"\R{PERMAP}", "rez:ti"),
    ("PIO", "sec:reconfig"),
    ("PL330", "sec:dma"),
    ("Prädikation", "sec:neon"),
    ("Priority Inversion", "sec:kohaerenz"),
    ("Race Condition", "sec:kohaerenz"),
    ("Reentranz", "sec:multicore"),
    ("Replacement", "sec:cache"),
    ("Ringpuffer (HW)", "sec:dma"),
    ("RISC-Prinzipien", "sec:riscv"),
    ("Routing-Delay", "sec:reconfig"),
    ("RV32C", "sec:riscv"),
    ("Sättigung (Q)", "rez:neondecode"),
    ("Scatter-Gather", "falle:dma"),
    ("Semaphore", "sec:kohaerenz"),
    ("Shape L/W/N", "rez:neondecode"),
    ("Side-Set", "sec:reconfig"),
    ("SIO", "sec:multicore"),
    (r"\R{SLTU}", "sec:rvflags"),
    ("SMP / AMP", "sec:multicore"),
    ("Spinlock", "sec:multicore"),
    (r"\R{SRC\_INC}", "rez:ti"),
    ("Strip Mining", "sec:rvv"),
    ("Swapping", "sec:mmu"),
    ("Tag", "rez:zerlegung"),
    ("Tail-Handling", "sec:simdgrenzen"),
    (r"\R{TI}-Register", "rez:ti"),
    ("TLB", "sec:mmu"),
    ("Trashing", "bsp:trash"),
    ("Valid Bit", "sec:cache"),
    ("VALID/READY", "sec:dma"),
    ("Vektorlänge VL", "sec:rvv"),
    (r"\R{VLD3}", "sec:neon"),
    (r"\R{vm\_stat}", "sec:mmu"),
    (r"\R{vsetvl}", "sec:rvv"),
    ("Write-Back", "sec:cache"),
    ("Wrapping (PIO)", "sec:reconfig"),
]


def key(label):
    """Sortierschluessel: LaTeX-Markup weg, Umlaute normalisieren."""
    s = label
    for junk in (r"\R{", r"\T{", "}", "\\", "_"):
        s = s.replace(junk, "")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.upper()


E.sort(key=lambda p: key(p[0]))
half = (len(E) + 1) // 2
left, right = E[:half], E[half:]
right += [("", "")] * (len(left) - len(right))

out = [
    "% !TEX root = ../main.tex",
    "% ---------------------------------------------------------------------",
    "%  Stichwortregister -- vom Begriff zur Abschnittsnummer",
    "%  ERZEUGT von mkreg.py. Neue Eintraege dort ergaenzen und neu laufen",
    "%  lassen, oder hier von Hand alphabetisch einsortieren.",
    "% ---------------------------------------------------------------------",
    r"\vlsec{cREF}{REF}{Stichwortregister}",
    "",
    r"\scriptsize",
    r"\begin{tabularx}{\linewidth}{@{}Xr@{\hskip6pt}Xr@{}}",
]
for (la, ra_), (lb, rb) in zip(left, right):
    a = f"{la} & \\ref{{{ra_}}}" if la else " & "
    b = f"{lb} & \\ref{{{rb}}}" if lb else " & "
    out.append(f"{a} & {b} \\\\")
out += [r"\end{tabularx}", r"\normalsize", ""]

with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print(f"{len(E)} Eintraege, {len(left)} Zeilen")
