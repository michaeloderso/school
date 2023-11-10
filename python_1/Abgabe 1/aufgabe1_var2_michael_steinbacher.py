#Variante ohne datetime-Import
alter = int(input("Wie alt bist du?: "))
jetzt_jahr = int(input("Welches Jahr haben wir?: "))

jahrgang = jetzt_jahr - alter
jahre_bis_hundert = 100 - alter
jahrgang_bis_hundert = jahre_bis_hundert + jetzt_jahr

print("Du bist im Jahr " + str(jahrgang) + " geboren")
print("Du wirst in " + str(jahre_bis_hundert) + " Jahren Einhundert Jahre alt sein.")
print("Das wird im Jahr " + str(jahrgang_bis_hundert) + " sein.")

