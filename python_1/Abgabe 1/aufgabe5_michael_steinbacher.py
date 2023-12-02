systolic = int(input("Enter systolic value: "))
diastolic = int(input("Enter diastolic value: "))

if systolic < 120 and diastolic < 80:
    message = ("The patient has normal blood pressure.")

elif 120 <= systolic < 130 and diastolic < 80:
    message = ("The patient has elevated blood pressure.")

elif 130 <= systolic < 140 or 80 <= diastolic < 89:
    message = ("The patient is in Hypertension Stage 1.")

elif 140 <= systolic <= 180 or 90 <= diastolic <= 120:
    message = ("The patient is in Hypertension Stage 2.")
    
elif systolic > 180 or diastolic > 120:
    message = ("The patient is in a hypertensive crisis. Seek immediate medical attention.")

print(message)


# Normal: systolic < 120 and diastolic < 80
# Elevated: systolic 120–129 and diastolic < 80
# Hypertension Stage 1: systolic 130–139 or diastolic 80–89
# Hypertension Stage 2: systolic ≥ 140 or diastolic ≥ 90
# Hypertensive Crisis: systolic > 180 and/or diastolic > 120

