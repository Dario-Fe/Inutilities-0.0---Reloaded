import os
import sys
import time

def autodistruggi():
    percorso_script = sys.argv[0]

    if os.path.exists(percorso_script):
        print("Sto per autodistruggermi...")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        print("Boom! 💥")
        os.remove(percorso_script)
        print("Fatto! Sono stato cancellato.")
    else:
        print("Il file non esiste già. Non posso autodistruggermi!")

if __name__ == "__main__":
    # autodistruggi()   ATTENZIONE HO COMMENTATO LA RIGA PER EVITARE LA CANCELLAZIONE INVOLONTARIA