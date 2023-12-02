gewicht = int(input("Wie schwer bist du in kg?: "))
groesse = int(input("Wie gross bist du in cm?: "))

bmi = gewicht / ((groesse/100) ** 2)

if bmi < 18.5:
    message = ("untergewichtig")

elif 18.5 <= bmi < 25:
    message = ("im normalen Bereich")

elif  25 <= bmi < 30:
    message = ("übergewichtig")

elif bmi >= 30:
    message = ("fettleibig/stark übergewichtig")


print("Du bist " + message + " und dein BMI beträgt ungefähr " + str(int(bmi)))

