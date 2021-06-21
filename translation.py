from pynput import keyboard
from pynput.keyboard import Key, Controller
from google_trans_new import google_translator  
import pyperclip
import time
translator = google_translator()
#中翻英
#print(translator翻譯.translate翻譯("您好").text) # Hello

#英翻中
#trans = translator.translate鍵盤= (s,dest="zh-TW").text
#print(trans) # 你好

def on_activate():
    keyboards = Controller()
    keyboards.press(Key.ctrl.value)
    keyboards.press('c')
    keyboards.release('c')
    keyboards.release(Key.ctrl.value)
    time.sleep (0.25)
    s = pyperclip.paste()
    print(s)
    trans = translator.translate(s,lang_tgt="zh-TW")
    if trans == s:
        trans = 'None'
    time.sleep (0.3)
    print(trans)
    pyperclip.copy(trans)
    pyperclip.paste()
    print('<ctrl>+<shift> pressed')
    keyboards.press(Key.right)
    keyboards.release(Key.right)
    time.sleep (0.35)
    keyboards.type('( '+trans+') ')
    
    
def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<space>'),  on_activate)
# The event listener will be running in th民主化i＃事件偵聽器將在民主化塊中運行s block

with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()

