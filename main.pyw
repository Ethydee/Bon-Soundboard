import threading

import wget
import os
from tkinter import *
import json

from playsound import playsound

buttons = []
sounds = 0
soundurls = {"bon.mp3": "https://drive.google.com/uc?export=download&id=1-rttPcbBTyIzZkV5hVucpciEgz3Him4t",
             "bawnongas.mp3": "https://drive.google.com/uc?export=download&id=1HHICB-UD9_l8d_VatqWqq6u3z8YeFCmK",
             "bawnongashell.mp3": "https://drive.google.com/uc?export=download&id=1ekdf_Nk--el58YMq-qRf4SlazFos47q9",
             "soldierhumor.mp3": "https://drive.google.com/uc?export=download&id=1pi_0FnYO9vPWPdnA18iBXkRyBlh1XuFR"}

if "sounds.json" not in os.listdir():
    with open('sounds.json', 'w+') as f:
        json.dump(soundurls, f, indent=2, sort_keys=True)
else:
    f = open("sounds.json", "r")
    soundurls = json.loads(f.read())
    f.close()

def gasboi(file_name):
    global sounds
    if not "audio" in os.getcwd():
        os.chdir("audio")
    playsound(os.path.join(file_name), True)
    sounds -= 1


def threadgas(file_name):
    global sounds
    gas = threading.Thread(target=gasboi, args=([file_name]))
    sounds += 1
    gas.start()


def on_closing():
    root.destroy()
    os._exit(0)


if "audio" not in os.listdir():
    os.mkdir("audio")

for file, url in soundurls.items():
    if file not in os.listdir("audio"):
        wget.download(url, os.path.join("audio"))

root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("270x130")
root.title("bon soundboard")

labeltext = StringVar()
numbalabel = Label(root, textvariable=labeltext).pack()
for file in soundurls.keys():
    buttons += [Button(root, text=file, command=lambda x=file: threadgas(x)).pack()]
print(buttons)
while True:
    root.update()
    labeltext.set("Sounds Playing: " + str(sounds))
