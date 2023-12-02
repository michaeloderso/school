import math

gewicht = int(input("Wie schwer bist du in kg?: "))
groesse = int(input("Wie gross bist du in cm?: "))

bmi = gewicht / ((groesse/100) ** 2)
bsa = math.sqrt((groesse * gewicht) / 3600)

print("Dein BMI ist " + str(bmi))
print("Dein BSA ist " + str(bsa))

