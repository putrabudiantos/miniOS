import time

def countdown(self, times):
        while times:
            mins, sec = divmod(times, 60)
            timer = '{:02d}:{:02d}'.format(mins, sec)
            print(timer, end='\r')
            timer.sleep(1)
            times -= 1