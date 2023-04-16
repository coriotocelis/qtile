
import os

autostart = [

    "nitrogen --restore &"
    "xrandr --output Virtual1 --mode 1920x1080 --rate 60"

]

for x in autostart:
    os.system(x)
