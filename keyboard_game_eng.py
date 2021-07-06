from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import random
from pygame import mixer
import time
import os

#added a word list. words taken from https://randomwordgenerator.com/
kelime_listesi = ['widen', 'story' ,'ditch', 'dark', 'strict' ,'net' ,'lead' ,'river', 'trial', 
'sale', 'dilute', 'dance', 'sound', 'valid', 'point', 'pie', 'dip', 'strong', 'mill', 'mouse', 
'like', 'yard', 'tablet', 'elite', 'lake', 'report', 'butter', 'miss', 'grow', 'install', 
'blonde', 'affair', 'ample', 'freeze' ,'ally', 'differ', 'pin', 'swing', 'key', 'spring', 
'warm', 'ear', 'blow', 'safe', 'movie', 'ferry', 'cap', 'train', 'share', 'relate', 'sister', 
'pull', 'carpet',  'ticket',  'medium', 'hay',  'office',  'profit',  'senior',  'burn',  'beat',  
'cut',  'head',  'grave',  'trap',  'leaf',  'sphere',  'school',  'rock',  'outfit',  'smart',  
'shell',  'tell',  'detail',  'patent',  'chord',  'prison',  'movie',  'field',  'boy',  'betray',  
'slide',  'reject', 'quote',  'play',  'bench',  'ritual',  'rocket',  'empire',  'wave',  'fuss',  
'bank',  'insure',  'part',  'dilute',  'code',  'groan',  'straw',  'safari',  'guide', "hill", 
"reach", "an", "lamb", "chew", "deep", "means", "zero", "manual", "chart", "modest", "rough", 
"robot", "dilute", "real", "think", "sigh", "bait", "exile", "front", "vain", "write", "key", 
"cute", "desert", "queen", "salon", "pair", "child", "lick", "escape", "behead", "small", "chin", 
"layout", "beg", "enemy", "square", "cherry", "moment", "hit", "reader", "hope", "egg", "adjust", 
"advice", "bare", "delay", "banana", "tap", "mole", "king", "weigh", "feed", "norm", "voter", "dance", 
"switch", "slide", "shock", "crisis", "threat", "gun", "field", "reader", "row", "square", "gown", 
"fuss", "yard", "print", "pepper", "mile", "favour", "jury", "site", "break", "oak", "unit", "drink", 
"pot", "like", "mail", "aisle", "user", "file", "drive", "flight", "leak", "rally", "bronze", "maze", 
"cotton", "poetry", "learn", "stamp", "worry", "use", "leader", "damage", "acid", "braid", "decay", "feast", 
"water", "basin", "mosque", "ally", "anger", "studio", "scene", "threat", "dinner", "manual", "window", 
"means", "glory", "metal", "chalk", "apathy", "crime", "ratio", "jury", "gas", "pluck", "team", "formal", 
"iron", "ash", "cope", "effort", "attic", "preach", "pocket", "brick", "peace", "wood", "lot", "clay", 
"north", "tender", "stream", "will", "save", "tidy", "valley", "direct", "format", "pen", "grass", "rhythm", 
"hero", "wrist", "queen", "past", "attic", "acute", "report", "fire", "list", "hair", "quit", "staff", "entry", 
"trial", "far", "summer", "father", "shaft", "crime", "muscle", "grain", "fox", "fist", "beam", "table", "guilt", 
"ferry", "size", "mold", "install", "guard", "image", "snatch", "fly", "paper", "accent", "west", "by", "linen", 
"shake", "agree", "try", "cute", "field", "bat", "want", "range", "layer", "virgin", "thrust", "meat", "settle", 
"able", "flock", "eagle", "flight", "waiter", "veil", "bee", "rocket", "bake", "museum", "ethics", "bin", "gift", 
"scan", "sleeve", "ear", "breed", "patrol", "buffet", "revoke", "fear", "module", "metal", "past", "useful", 
"hip", "joy", "arm", "me", "tidy", "radio", "sacred", "strike", "touch", "flour", "tactic", "decay", "soak", 
"single", "shout", "person", "live", "rise", "pardon", "onion", "cheap", "loot"
]   

kelime_listesi=list(set(kelime_listesi))    #there are some repeated word. got rid of them

#window defining
pencere = Tk()
pencere.title('*Klavye Hız Testi*')
pencere.geometry('900x650+200+50')
pencere.resizable(False, False)
pencere.configure(bg='#F8F8F8')


score = 0
girilen_kelimeler=[]
verilen_kelimeler=[]

#frames
baslik = Frame(pencere, bg='black')
baslik.place(relx=0.1, rely=0.03, relwidth=0.80, relheight=0.1)

bilgilendirme = Frame(pencere, bg='#F8F8F8')
bilgilendirme.place(relx=0.1, rely=0.15, relwidth=0.80, relheight=0.1)

kalan_sure = Frame(pencere, bg='black')
kalan_sure.place(relx=0.42, rely=0.25, relwidth=0.16, relheight=0.08)

yazilacak_kelime = Frame(pencere, bg='black')
yazilacak_kelime.place(relx=0.20, rely=0.35, relwidth=0.6, relheight=0.17)

yazilacak_kelime_ic = Frame(pencere, bg='#F8F8F8')
yazilacak_kelime_ic.place(relx=0.23, rely=0.38, relwidth=0.54, relheight=0.11)

girdi_yeri = Frame(pencere, bg='black')
girdi_yeri.place(relx=0.20, rely=0.55, relwidth=0.6, relheight=0.17)

baslat_butonu = Frame(pencere, bg='black')
baslat_butonu.place(relx=0.20, rely=0.9, relwidth=0.28, relheight=0.05)

reset_butonu = Frame(pencere, bg='black')
reset_butonu.place(relx=0.52, rely=0.9, relwidth=0.28, relheight=0.05)

score_frame = Frame(pencere, bg='#F8F8F8')
score_frame.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.1)


#labels
baslik_label = Label(baslik, text='* Keyboard Speed Test *', font='Helvetica 20 bold', bg='black', fg='white')
baslik_label.pack(pady=15)

bilgilendirme_label = Label(bilgilendirme, text='Welcome to the Keyboard Speed Test. Try to write the displayed words as much and TRUE as possible . \nHit the ENTER key after every word. Each correct word is 1 (one) point and misspelled words have no point value. \n by:yunus  ', font='Helvetica 10 italic', bg='#F8F8F8', fg='black')
bilgilendirme_label.pack(pady=5)

kalan_sure_label = Label(kalan_sure, text=60, font='Helvetica 19 bold', bg='black', fg='white')
kalan_sure_label.pack(pady=15)


metin_girdisi = Text(girdi_yeri)
metin_girdisi.tag_configure('style', foreground='purple', font=('Helvetica', 12, 'bold'))
metin_girdisi.pack()


#text input defining
def getTextInput():
    result=metin_girdisi.get("1.0","end")
    girilen_kelimeler.append(result)
    girilen_kelimeler_düzenli = girilen_kelimeler[-1].split('\n')
    del girilen_kelimeler_düzenli[-1]
    del girilen_kelimeler_düzenli[-1]
    return girilen_kelimeler_düzenli


#counter here. fixed to 60 sec.
def sayac(count=60):
    kalan_sure_label['text'] = count
    if count > 0:
        kalan_sure.after(1000, sayac, count-1)
    elif count == 0:   
        score_label = Label(score_frame, text='Score: {} words/min'.format(score), font='Helvetica 19 bold', bg='#F8F8F8', fg='black' )
        score_label.pack(pady=15)
        
        girdi_yeri = Frame(pencere, bg='black')
        girdi_yeri.place(relx=0.20, rely=0.55, relwidth=0.6, relheight=0.17)
        
        mixer.init()
        mixer.music.load('time_up.mp3')
        mixer.music.play()
        print(score)

#ENTER key binding function defining
def gecis():
    yazilacak_kelime = Frame(pencere, bg='black')
    yazilacak_kelime.place(relx=0.20, rely=0.35, relwidth=0.6, relheight=0.17)
    yazilacak_kelime_ic = Frame(pencere, bg='#F8F8F8')
    yazilacak_kelime_ic.place(relx=0.23, rely=0.38, relwidth=0.54, relheight=0.11)
    yazilacak_kelime_label = Label(yazilacak_kelime_ic, text=random.choice(kelime_listesi), font='Helvetica 35 bold',bg='#F8F8F8', fg='black')
    yazilacak_kelime_label.pack(pady=2) 
    verilen_kelimeler.append(yazilacak_kelime_label['text'])
    
    metin_girdisi = Text(girdi_yeri)
    metin_girdisi.tag_configure('style', foreground='purple', font=('Helvetica', 12, 'bold'))
    metin_girdisi.pack()
    score_count(getTextInput(), verilen_kelimeler)


#score counter definig
def score_count(a,b):
    
    if a == []:
        pass
    elif a[-1] == b[-2]:
        global score
        score+=1

#start button definig 
def start_button ():
    sayac()
    gecis()
    

    #ENTER key binding
    def func(event):    
        gecis()
    pencere.bind('<Return>', func)
  

#restart button defining
def restart_button():
    pencere.destroy()
    os.system("keyboard_game_eng.py")
 
#buttons
Button(baslat_butonu, text='Start!', command=start_button, bg='black', fg= 'white').place(relx=0, rely=0, relwidth=1, relheight=1)
Button(reset_butonu, text='Restart', command=restart_button, bg='black', fg= 'white').place(relx=0, rely=0, relwidth=1, relheight=1)


pencere.mainloop()
