import time

def countdown_timer(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

time_in_seconds = int(input("Enter time in seconds: "))
countdown_timer(time_in_seconds)
