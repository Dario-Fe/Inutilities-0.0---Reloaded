import tkinter as tk

class CursorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cursore Gelindo")
        self.root.resizable(False, False)


        # Dimensioni della finestra
        window_width = 400
        window_height = 100

        # Ottieni le dimensioni dello schermo
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcola le coordinate per centrare la finestra
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Imposta la geometria della finestra (dimensioni + posizione)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.canvas = tk.Canvas(root, width=400, height=50)
        self.canvas.pack()

        self.cursor = self.canvas.create_rectangle(10, 10, 30, 30, fill="blue")
        self.direction = 1  # 1 per destra, -1 per sinistra
        self.distance = 0  # Distanza percorsa in metri
        self.speed = 5  # Velocità del cursore

        self.label = tk.Label(root, text="Distanza percorsa: 0 km")
        self.label.pack()

        self.move_cursor()

    def move_cursor(self):
        # Muovi il cursore
        self.canvas.move(self.cursor, self.direction * self.speed, 0)
        pos = self.canvas.coords(self.cursor)

        # Controlla se il cursore ha raggiunto il bordo della finestra
        if pos[2] >= 400 or pos[0] <= 0:
            self.direction *= -1  # Inverti la direzione

        # Aggiorna la distanza percorsa
        self.distance += float(0.000005) # Converti in chilometri

        # Aggiorna l'etichetta con la distanza percorsa
        self.label.config(text=f"Distanza percorsa: {self.distance:.3f} km")

        # Richiama la funzione dopo 20 millisecondi
        self.root.after(20, self.move_cursor)

if __name__ == "__main__":
    root = tk.Tk()
    app = CursorApp(root)
    root.mainloop()