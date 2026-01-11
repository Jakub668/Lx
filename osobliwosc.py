import os
import time
import threading
import math

def obciazenie():
    # Tworzy sztuczne "ciepło" procesora
    while parowanie:
        [math.exp(i) for i in range(1000)]

def efekt_swietlny():
    # Manipuluje jasnością (wymaga dostępu do plików systemowych)
    # Jeśli nie zadziała, pominie ten krok
    try:
        backlight = "/sys/class/backlight/intel_backlight/brightness"
        with open(backlight, "r") as f:
            max_br = int(open("/sys/class/backlight/intel_backlight/max_brightness").read())
            while parowanie:
                for b in range(max_br, 0, -500):
                    os.system(f"echo {b} | sudo tee {backlight} > /dev/null")
                    time.sleep(0.01)
    except:
        pass

parowanie = True
print("\033[91m[!!!] OSTRZEŻENIE: WCHODZISZ W HORYZONT ZDARZEŃ [!!!]\033[0m")
threading.Thread(target=obciazenie, daemon=True).start()

masa = 100
try:
    while masa > 0:
        # Zniekształcanie tekstu terminala
        kolor = f"\033[38;5;{232 + (100-masa)//4}m"
        znieksztalcenie = " " * (100 - masa) + "VOID"
        print(f"{kolor}MASA: {masa:3} | {znieksztalcenie}\033[0m")
        
        masa -= 1
        time.sleep(0.1 if masa > 20 else 0.02) # Przyspieszenie na końcu
        
    parowanie = False
    print("\n\033[41m BUM! SYSTEM WYPAROWAŁ \033[0m")
    os.system("kill -9 $PPID") # Samobójstwo terminala
except KeyboardInterrupt:
    parowanie = False
