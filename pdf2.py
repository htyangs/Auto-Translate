from pynput import keyboard
from pynput.keyboard import Key, Controller
from google_trans_new import google_translator  
from googletrans import Translator
import pyperclip
from gtts import gTTS
import time
import os
import pygame
import tkinter as tk
translator = Translator()


def speak(text,language):
	tts=gTTS(text, lang=language)
	filename="audio1.mp3"
	tts.save(filename)
	pygame.mixer.init()
	pygame.mixer.music.load("audio1.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)
	pygame.mixer.quit()
	os.remove(filename)
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    #通過屬性判斷按鍵類型。

def on_release(key):
    '鬆開按鍵時執行。'
    if(key == keyboard.Key.f4):
        print('good')
        keyboards = Controller()

        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.35)
        s = pyperclip.paste()
        print(len(s))
        print(s)
        trans = translator.translate(s,dest="zh-tw").text #dest #lang_tgt
        time.sleep (0.7+len(s)/100)
        pyperclip.copy(trans)
        
        print(trans)
        #pyperclip.copy(trans)
        print('<ctrl>+<shift> pressed')

        #time.sleep (0.35)
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('v')
            keyboards.release('v')
        time.sleep (0.55)
    if(key == keyboard.Key.f2):
        print('good')
        keyboards = Controller()
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.35)
        s = pyperclip.paste()
        keyboards.press(Key.right)
        keyboards.release(Key.right)    
        print(s)
        trans = translator.translate(s,dest="zh-tw").text #dest #lang_tgt
        time.sleep (0.4+len(s)/100)
        pyperclip.copy('( '+trans+' )')
        print(trans)
        #pyperclip.copy(trans)
        print('<ctrl>+<shift> pressed')
        #time.sleep (0.35)
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('v')
            keyboards.release('v')
        time.sleep (0.35)
        keyboards.press(Key.ctrl_l.value)
        keyboards.release(Key.ctrl_l.value)     
    if(key == keyboard.Key.f5):
        print('good')
        keyboards = Controller()
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.35)
        s = pyperclip.paste()   
        speak(s,language='en')
        print(s)
        try:
            trans = translator.translate(s,dest="zh-tw").text #dest #lang_tgt
            time.sleep (0.4)
            more_lines = ['',s+" "+trans]
            with open('vocabulary.txt', 'a') as f:
                f.writelines('\n'.join(more_lines))
                
            #pyperclip.copy(trans)
            print('<ctrl>+<shift> pressed')
            #time.sleep (0.35)
            time.sleep (0.35)
        except:
            pass
    if(key == keyboard.Key.f8):
        print('good')
        
        window = tk.Tk()
        window.attributes('-topmost', 1)
        keyboards = Controller()
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.35)
        s = pyperclip.paste()  
        trans = translator.translate(s,dest="zh-tw").text #dest #lang_tgt
        time.sleep (0.4)
        '''
        window.geometry("300x100+250+150")
        label = tk.Label(window,                 # 文字標示所在視窗
                        text = s+trans,  # 顯示文字
                                #  背景顏色
                        font = ('Arial', 12),   # 字型與大小
                        width = 15, height = 2) # 文字標示尺寸   
        label.pack()
        window.mainloop()
         '''
        print(s)
        speak(s,language='en')
        speak(trans,language='zh')
       
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()  