from guizero import App, Text, Picture, Box
import subprocess
import psutil
import sys
import time

if(len(sys.argv) >= 2):
    if(sys.argv[1] == "--nogui"):
        print("Raspberry Pi State Checker By Oein")
        time.sleep(1)
        while True:
            try:
                result = str(subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE).stdout).replace('b"',"").replace('\\n',"").replace('"',"").replace("temp=","")
                print("CPU Temperature : " + str(result))
            except:
                print("CPU Temperature : Have to install vcgencmd")
            try:
                print("CPU Usage : " + str(psutil.cpu_percent()) + " / 100")
            except:
                print("Some error occurred")
            try:
                print("Ram Usage : " + str(psutil.virtual_memory().percent) + " / 100")
            except:
                ramU.value = "Some error occurred"
            time.sleep(0.5)
else:
    app = App(title="RPi State Checker", width=800)

    box = Box(app, layout="grid", grid=[0, 0])

    picture = Picture(box, image="rpi.png", grid=[2, 0])

    intro = Text(box, text="Raspberry Pi State Checker", grid=[1, 0], size=30)

    boxtwo = Box(app, layout="grid", grid=[0, 2])

    temp = Text(boxtwo, text="CPU Temperature : ?'C", size=20, align="left", grid=[0, 1])

    cpuU = Text(boxtwo, text="CPU Usage : ? / 100", size=20, align="left", grid=[0, 2])

    ramU = Text(boxtwo, text="Ram Usage : ? / 100", size=20, align="left", grid=[0, 3])

    def change():
        try:
            result = str(subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE).stdout).replace('b"',"").replace('\\n',"").replace('"',"").replace("temp=","")
            temp.value = "CPU Temperature : " + str(result)
        except:
            temp.value = "CPU Temperature : Have to install vcgencmd"
        try:
            cpuU.value = "CPU Usage : " + str(psutil.cpu_percent()) + " / 100"
        except:
            cpuU.value = "Some error occurred"

        try:
            ramU.value = "Ram Usage : " + str(psutil.virtual_memory().percent) + " / 100"
        except:
            ramU.value = "Some error occurred"

    app.repeat(500, change)

    app.display()


# pip install speedtest-cli
# pip install psutil
# pip install guizero
# pip install subprocess