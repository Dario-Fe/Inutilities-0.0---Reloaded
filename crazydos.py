import tkinter as tk
from tkinter import scrolledtext, font, messagebox
import random

# Lista di comandi "supportati" con relative risposte
COMMANDS = {
    "help": """I comandi disponibili sono:
dir - Cancella tutti i file (simulato)
del - Elenca file immaginari
format c: - Simula formattazione (senza fare nulla)
cd - Cambia directory (virtualmente)
cls - Pulisce lo schermo (ma non troppo)
mem - Mostra memoria (finta)
ver - Versione DOS (fantasiosa)
exit - Esci (forse)""",

    "del": """ Volume in drive C is SYSTEM
 Directory of C:\\

IO      SYS     42,069  01-01-1980  12:00a
MSDOS   SYS     69,420  01-01-1980  12:00a
COMMAND COM      9,999  01-01-1980  12:00a
CONFIG  SYS         42  01-01-1980  12:00a
AUTOEXECBAT      666  01-01-1980  12:00a
FILE    TXT    123,456  01-01-1980  12:00a
SECRET  DOC          0  01-01-1980  12:00a
       7 file(s)    245,652 bytes
       0 dir(s)   1,024.00 MB free""",

    "format c:": """Avvio formattazione di C:...
Attenzione! Tutti i dati saranno persi!
Procedere (S/N)? S
0%% completato... (aspetta un attimo)
25%% completato... (forse)
50%% completato... (o forse no)
Formattazione completata con successo!
PS: Scherzavo, non ho fatto nulla!""",

    "cd": "Directory cambiata con successo! (nella tua immaginazione)",

    "cls": "",  # Gestito separatamente

    "mem": """Memory Type       Total       Used       Free
Conventional     640K        420K       220K
Upper            384K        128K       256K
Extended        1024K       1024K         0K
Total Memory    2048K       1572K       476K

PS: Questi numeri sono totalmente inventati""",

    "ver": """MS-DOS Version 6.66 (Ultimate Edition)
Copyright (C) 1981-1993 Microsoft Corp
Licensed to: Inutilities 0.0 User""",

    "exit": "No grazie, resto qui a divertirmi!",
}

# Variabile per memorizzare l'ultimo comando "dir"
last_dir_command = None


def execute_command():
    global last_dir_command
    command = entry.get().strip().lower()
    output.config(state=tk.NORMAL)

    # Aggiunge il prompt al testo
    output.insert(tk.END, f"C:\\>{command}\n")

    # Gestione speciale per cls
    if command == "cls":
        output.delete(1.0, tk.END)
    elif command == "dir":
        last_dir_command = command
        output.insert(tk.END, "Are you sure (Y/N)? ")
        output.mark_set("input_start", tk.END)
        output.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        return
    elif command in ["y", "n"] and last_dir_command == "dir":
        if command == "y":
            output.insert(tk.END, "\nDeleting all files... just kidding!\n")
        else:
            output.insert(tk.END, "\nOperation cancelled by user\n")
        last_dir_command = None
    elif command in COMMANDS:
        output.insert(tk.END, f"{COMMANDS[command]}\n")
    else:
        responses = [
            "Comando non riconosciuto. Digita 'help' per aiuto",
            "Bad command or file name",
            "Questo comando è troppo utile per le Inutilities!",
            "Il sistema si rifiuta di eseguire questa richiesta",
            "Errore 404: Comando non trovato"
        ]
        output.insert(tk.END, f"{random.choice(responses)}\n")

    output.see(tk.END)
    output.config(state=tk.DISABLED)
    entry.delete(0, tk.END)


def on_enter(event):
    execute_command()


# Creazione della finestra
root = tk.Tk()
root.title("Inutilities DOS Shell")
root.geometry("800x600")
root.configure(bg="black")

# Font stile DOS
dos_font = font.Font(family="Courier New", size=12)

# Area di output
output = scrolledtext.ScrolledText(
    root,
    bg="black",
    fg="white",
    insertbackground="white",
    font=dos_font,
    wrap=tk.WORD,
    state=tk.DISABLED
)
output.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

# Prompt di input
entry_frame = tk.Frame(root, bg="black")
entry_frame.pack(fill=tk.X, padx=5, pady=5)

label = tk.Label(entry_frame, text="C:\\>", bg="black", fg="white", font=dos_font)
label.pack(side=tk.LEFT)

entry = tk.Entry(
    entry_frame,
    bg="black",
    fg="white",
    insertbackground="white",
    font=dos_font,
    relief=tk.FLAT
)
entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
entry.bind("<Return>", on_enter)
entry.focus()

# Messaggio iniziale
output.config(state=tk.NORMAL)
output.insert(tk.END,
              """Microsoft(R) Inutilities DOS Version 6.66
              (C) Copyright Inutilities Corp 1980-1990. All rights reserved.
              
              Digita 'help' per la lista dei comandi\n\n""")
output.config(state=tk.DISABLED)

root.mainloop()
