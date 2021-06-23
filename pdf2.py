'''
This program aims to translate any language into chinese
With special key pressed, one can get the translation immediately
For different system user, please motify the key such as crtl to cmd for Mac users
If you have any problems, please contact me: antony880910@gmail.com or find the new version on github https://github.com/alwaysmle/Auto-Translate
Thanks and enjoy
'''
from pynput import keyboard,mouse
from pynput.keyboard import Key, Controller 
from googletrans import Translator
import pyperclip
from gtts import gTTS
import time
import os
from playsound import playsound
import tkinter as tk
translator = Translator()

def speak(text,language): #speak sounds
	tts=gTTS(text,lang=language)
	filename="audio1.mp3"
	tts.save(filename)
	playsound("audio1.mp3")
	os.remove(filename)
def display_word(trans):
    w = 280 # width for the Tk root
    h = int(50+int(len(trans)*1.3) )# height for the Tk root
    new_line = 15
    for i in range(int(len(trans)/10)):
        trans=trans[:(i+1)*new_line]+'\n'+trans[(i+1)*new_line:]
    trans = '\n'+'\n'+trans
    print(trans)
    root = tk.Tk() #create a window
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/5) 
    y = (hs/5) 

    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    label = tk.Label(root,              # 文字標示所在視窗
                    text = trans,  # 顯示文字
                    font = ('Arial', 12),   # 字型與大小
                    )  
    label.pack()
    root.wm_attributes('-topmost',1)

    root.after(1500+len(trans)*80, lambda: root.destroy())
    root.mainloop()
def on_press(key): #detect press not use here
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key): # detect release of keyboard
    '鬆開按鍵時執行。'
    if(key == keyboard.Key.f4): #for pdf file, use copy v to paste translation
        print('good')
        keyboards = Controller()

        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.35)
        s = pyperclip.paste().replace('\n', '').replace('\r', '')  
        print(len(s))
        print(s)
        trans = translator.translate(s,dest="zh-tw").text #dest #lang_tgt
        time.sleep (0.7+len(s)/100)
        pyperclip.copy(trans)
    
        print(trans)
        print('<ctrl>+<shift> pressed')
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('v')
            keyboards.release('v')
        time.sleep (0.55)
    if(key == keyboard.Key.f2): # for word file or txt file, it may insert translation to the loc next to word 
        print('good')
        keyboards = Controller()
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.25)
        s = pyperclip.paste().replace('\n', '').replace('\r', '')   
        keyboards.press(Key.right)
        keyboards.release(Key.right)    
        print(s)
        trans = translator.translate(s,dest="zh-tw").text #dest #lang_tgt
        time.sleep (0.4+len(s)/100)
        pyperclip.copy('( '+trans+' )')
        print(trans)
        print('<ctrl>+<shift> pressed')
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('v')
            keyboards.release('v')
        time.sleep (0.35)
        keyboards.press(Key.ctrl_l.value)
        keyboards.release(Key.ctrl_l.value)   

    if(key == keyboard.Key.f9): # for save file to txt
        print('good')
        keyboards = Controller()
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.35)
        s = pyperclip.paste().replace('\n', '').replace('\r', '')   
        lang = translator.detect(s).lang

        speak(s,language=lang)
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
        except Exception as e:
            print(e)
    if(key == keyboard.Key.f8 or key == keyboard.Key.f6 ): #display a window and speak
        print('good')
        
        keyboards = Controller()
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.15)
        s = pyperclip.paste()
        s = s.replace('\n', '').replace('\r', '')
        lang = translator.detect(s).lang
        
        try:
            trans = translator.translate(s,dest="zh-tw").text #dest #lang_tgt
            time.sleep (0.25)
            display_word(trans) 
            speak(s,language=lang)
        
        except Exception as e:
            print(e)
    if(key == keyboard.Key.f1 or key == keyboard.Key.f3): #display a window and speak
        print('good')
        
        keyboards = Controller()
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.15)
        s = pyperclip.paste()
        s = s.replace('\n', '').replace('\r', '')
        lang = translator.detect(s).lang
        print(s)
        try:
            trans = translator.translate(s,dest="zh-tw").text #dest #lang_tgt
            time.sleep (0.25)
            display_word(trans) 
        except Exception as e:
            print(e)

    if key == keyboard.Key.esc:
        # Stop listener
        return False
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()  
    
# test mouse function
    '''
def on_move(x, y):
    pass
x_pos=0
y_pos=0
def on_click(x, y, button, pressed):
    global x_pos,y_pos
    if(pressed==False and (x_pos!=x or y_pos !=y)):
        print('good')
        previous = pyperclip.paste()
        keyboards = Controller()
        with keyboards.pressed(Key.ctrl.value):
            keyboards.press('c')
            keyboards.release('c')
        time.sleep (0.15)
        after = pyperclip.paste()
        if(after!=previous):
            try:
                trans = translator.translate(after,dest="zh-tw").text #dest #lang_tgt
                new_line = 15
                for i in range(int(len(trans)/10)):
                    trans=trans[:(i+1)*new_line]+'\n'+trans[(i+1)*new_line:]
                print(trans)
                root = tk.Tk()
                label = tk.Label(root,              # 文字標示所在視窗
                                text = trans,  # 顯示文字
                            
                                font = ('Arial', 12),   # 字型與大小
                                width = 30, height = int(4+int(len(trans))/15)) # 文字標示尺寸  
                label.pack()
                root.wm_attributes('-topmost',1)
                print(s)
                root.after(1500+len(trans)*80, lambda: root.destroy())
                root.mainloop()
                #speak(s,language='en')
            #speak(trans,language='zh')
            except:
                pass    
    x_pos = x
    y_pos = y

    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    
def on_scroll(x, y, dx, dy):
    pass

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
'''
