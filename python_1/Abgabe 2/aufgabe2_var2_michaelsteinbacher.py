
import time

while 1 != 0: # Infinite Loop (Nicht zwingend notwendig für diese Aufgabe)
        for local_var in range(0, 24, 1):
                if int(local_var / 4) == float(local_var / 4):
                        print(f"Hour {local_var}: Please take your medication!")
                        time.sleep(0.5)
                else:
                        print(f"Hour {local_var}: ¯\_(ツ)_/¯")
                        time.sleep(0.5)

