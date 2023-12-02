import time

for hour in range(0, 24, 1):
    if hour % 4 == 0:
        print(f"Hour {hour}: Please take your medication!")
        time.sleep(0.5)
    else:
        print(f"Hour {hour}: ¯\_(ツ)_/¯")
        time.sleep(0.5)
        