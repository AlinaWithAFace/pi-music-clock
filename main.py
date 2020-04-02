import datetime
import time
import subprocess

wakeMusic = "https://tunein.com/radio/The-Basement-913-s44920/"

workMusic = "https://www.youtube.com/watch?v=5qap5aO4i9A"

relaxMusic = "https://somafm.com/player/#/now-playing/lush"

sleepMusic = "https://somafm.com/player/#/now-playing/deepspaceone"

wakeTime = 7

workTime = 10

relaxTime = 15

sleepTime = 23

now = datetime.datetime.now().hour

playing = False

music = sleepMusic

# while True:
if now < wakeTime:
    music = sleepMusic
elif now >= sleepTime:
    music = sleepMusic
elif now >= relaxTime:
    music = relaxMusic
elif now >= workTime:
    music = workMusic
elif now >= wakeTime:
    music = wakeMusic

mycmd = r'start chrome /new-tab {}'.format(music)
p = subprocess.Popen(mycmd, shell=True)
time.sleep(10)
p.terminate()

#todo run continuously