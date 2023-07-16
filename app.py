import sys
import datetime
import time
import winsound
from win10toast import ToastNotifier


def run_popup(title, message, time=1):
    pop_up = ToastNotifier()
    pop_up.show_toast(title,
                    message,
                    icon_path = None,
                    duration = time,
                    threaded = True)
    

def alarm(set_alarm_timer):
    current_time = datetime.datetime.now()
    date = current_time.strftime("%d/%m/%Y")
    print("The Set Date is:",date)
    while True:
        time.sleep(1)
        now = str(datetime.datetime.now().strftime("%H:%M:%S"))
        print(now.time())
        sys.stdout.write("\033[F")
        if now == set_alarm_timer:
            winsound.Beep(500, 1000)
            run_popup("Time Has Come", 'Time is Up', time=10)
            print("Time is Up")
            break

def get_time():
    
    while True:
        print('enter the time in "HH:MM:SS" format')
        print(f'now:\n {datetime.datetime.now().strftime("%H:%M:%S")}')
        t = input()
        hour = t[:2]
        min = t[3:5]
        sec = t[6:]
        set_alarm_timer = f"{hour}:{min}:{sec}"
        set_alarm_timer = datetime.datetime.strptime(set_alarm_timer, "%H:%M:%S")      
        now = str(datetime.datetime.now().strftime("%H:%M:%S"))
        now = datetime.datetime.strptime(now, "%H:%M:%S")
        print(f'now: {now.time()} set_alarm_timer: {set_alarm_timer.time()}')
        if set_alarm_timer <= now:  
            print("too late to set alarm, try another time")
            continue
        else:
            break
    alarm(set_alarm_timer)
    
get_time()
