capsule = float(100) #mg
gewicht = int(input("Wie schwer bist du in kg?: "))
dosierung = int(input("Wie ist die Medikamentdosierung in mg/kg?: "))

total_dosis = float(gewicht * dosierung)
komplette_kapseln = (int(total_dosis / capsule))
defizit = float(total_dosis / capsule) - float(komplette_kapseln)

print("Die totale einnehmbare Dosierung für diesen Patienten befindet sich bei: " + str(total_dosis) + " mg.")
print("Die Anzahl kompletter einnehmbarer Kapseln beträgt: " + str(komplette_kapseln))
print("Das Defizit ist " + (str(defizit * 100)) + " mg.")

