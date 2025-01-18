from TeamGenerator import get_data
import time
import keyboard
import threading

def room_timer(duration, room = "innovation project"):
    start_time = time.time()
    print(f"time for {room} room:")
    while True:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        print(f"\r{minutes:02}:{seconds:02}", end="")
        
        if keyboard.is_pressed('q'):
            print(f"\nwhat the sigma? {room} room stopped at {elapsed_time} seconds")
            break
        
        if elapsed_time >= duration:
            print("\n{room} room is over.")
            break
        
        time.sleep(1)

def main():
    timer_thread = threading.Thread(target=room_timer, args=(60))
    timer_thread.start()

    while True:
        print("You can add / remove thingys out of the rubric as you wish:")
        


room_timer(30, "robot design")