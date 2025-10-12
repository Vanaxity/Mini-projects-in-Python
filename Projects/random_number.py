import time 

def count(end_seconds, start_seconds=0):
    for t in range(start_seconds, end_seconds + 1):
        minutes, seconds = divmod(t, 60)
        print(f"{minutes:02d}:{seconds:02d}")
        time.sleep(1)


count(100)
