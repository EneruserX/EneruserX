import webbrowser
import time

timer = 0
while timer < 3:
    time.sleep(0.01)
    webbrowser.open("https://www.youtube.com/watch?v=80TuzzbLhPg")
    timer = timer + 1


