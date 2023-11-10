temp_readings = [36.8, 37.2, 36.9, 37.5, 38.0, 37.4, 36.6]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


temp_sum = 0
for reading in temp_readings:
    temp_sum += reading

average_temp = temp_sum / len(temp_readings)

print(f"The average temperature for the week is: {average_temp:.2f} °C")


days_above_average = []
for counter, reading in enumerate(temp_readings):
    if reading > average_temp:
        days_above_average.extend([weekdays[counter]])


days_above_average = ", ".join(days_above_average)
print(f"Days with above-average temperatures: {days_above_average}")
