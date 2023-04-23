from tkinter import *
import time
from pygame import mixer
from tkinter import messagebox

root = Tk()
root.title("Alarm Clock")
root.geometry("660x430")

alarmtime = StringVar()
msgi = StringVar()

mixer.init()   # for playing sound


def alarm():
    a = alarmtime.get()
    AlarmTime = a
    CurrentTime = time.strftime("%H:%M")

    while AlarmTime != CurrentTime:
        CurrentTime = time.strftime("%H:%M")

    if AlarmTime == CurrentTime:
        mixer.music.load('ringtone.mp3')
        mixer.music.play()
        msg = messagebox.showinfo('IT is time', f'{msgi.get()}')
        if msg == 'ok':  # if 'ok' pressed, sound will stop
            mixer.music.stop()

head = Label(root, text="Alarm Clock", font=('comic sans', 20))
head.grid(row=0, columnspan=3, pady=10)

clockimg = PhotoImage(file="clock.png")

img = Label(root, image=clockimg)
img.grid(rowspan=4, column= 0)

input_time = Label(root, text="Input Time : ", font=('cosmic sans', 18))
input_time.grid(row=1, column=1)

alarm_time = Entry(root,textvariable=alarmtime, font=('cosmic sans', 18), width=6)
alarm_time.grid(row = 1,column=2)

msg = Label(root, text = "Message", font=('cosmic sans', 18))
msg.grid(row=2, column=1, columnspan=2)

msg_input = Entry(root, textvariable=msgi,  font=('cosmic sans', 18))
msg_input.grid(row=3, column=1, columnspan=2, padx=10)

submit = Button(root, text="SUBMIT", font=('cosmic sans', 18), command=alarm)
submit.grid(row=4, column=1, columnspan=2)




root.mainloop()
