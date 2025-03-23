import tkinter as tk
import time

# Funzione per simulare il Format C:
def simulate_format():
    # Simboli rotanti
    ROTATING_SYMBOLS = ["/", "-", "\\", "|"]

    # Numero di simulazione cilindri e cluster
    cylinders = int(25)
    clusters_per_cylinder = 100
    step= int(1)

    # Messaggio di verifica disco
    output_label.config(text="Verifica del disco in corso...")
    root.update()
    time.sleep(1.5)  # Ritardo per l'animazione

    # Messaggi di simulazione
    messages = [
        "Avvio della formattazione di C:...",
        "25% completato... (forse)",
        "50% completato... (speriamo bene)",
        "75% completato... (quasi quasi mi fermo)",
    ]

    # Mostra i messaggi uno alla volta
    for msg in messages:
        output_label.config(text=msg)
        root.update()
        time.sleep(2)  # Simula un'attesa
        for cylinder in range(1, cylinders + 1):
            for symbol in ROTATING_SYMBOLS:
                 output_label.config(text=f"Formattando C: cilindro {step} di {clusters_per_cylinder}... {symbol}")
                 root.update()
                 time.sleep(0.1)  # Ritardo per l'animazione
            step = step + 1

    # Messaggio di fine formattazione
    output_label.config(text="Formattazione disco C 100% completata! (scherzavo, non ho fatto nulla)")
    time.sleep(2)  # Simula un'attesa

# Creazione della finestra principale
root = tk.Tk()
root.title("Inutilities 0.0 - Format C:")
root.geometry("800x400")
root.configure(bg="black")

# Stile DOS-like
output_label = tk.Label(root, text="", fg="white", bg="black", font=("Courier", 14))
output_label.pack(pady=50)

# Pulsante per avviare la formattazione
format_button = tk.Button(root, text="Formatta C:", command=simulate_format, bg="gray", fg="white", font=("Arial", 12))
format_button.pack(pady=20)

# Avvio dell'applicazione
root.mainloop()