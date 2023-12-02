heart_rate_readings = [58, 65, 78, 72, 110, 89, 94]

normal_range_count = 0
for reading in heart_rate_readings:
    if 100 >= reading >= 60:
        normal_range_count += 1

print(f"{normal_range_count} heart rates are within the normal range")


