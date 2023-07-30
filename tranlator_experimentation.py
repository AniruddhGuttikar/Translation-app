from tkinter import *
from tkinter import ttk 
import googletrans
from googletrans import Translator 
from tkinter import filedialog 
from langdetect import detect 
from gtts import gTTS
import os

window = Tk()

bkimage = PhotoImage(file="image.png")
labelbg = Label(window, image = bkimage)
labelbg.place(x = 0, y = 0, relwidth=1, relheight=1)

window.title("TRANSlATOR")
window.geometry("1280x720")
window.resizable(False, False)

check_autodet = False

def label_change() :
    
    c1 = combo1.get()
    c2 = combo2.get()

    if (check_autodet) :
        
        language1 = googletrans.LANGUAGES
        detect_lang_value= language1[detect_lang]
        label1.configure(text=detect_lang_value.upper())
    else :
        label1.configure(text=c1.upper())

    label2.configure(text=c2.upper())

    window.after(100, label_change)

def translate_now() :
    in_text = text1.get(1.0, END)
    t1 = Translator()
    if(check_autodet) :
        in_lang = detect_lang
    else :
        in_lang = combo1.get()
    out_text = t1.translate(in_text, src = in_lang, dest = combo2.get() )
    out_text = out_text.text
    text2.delete(1.0, END)
    text2.insert(END, out_text)


def browse_file() :
    filepath = filedialog.askopenfilename()
    f1 = open(filepath, 'r')
    file_in = f1.read()
    f1.close()
    
    t1 = Translator()
    
    file_out = t1.translate(file_in, src = combo1.get(), dest = combo2.get() )
    file_out = file_out.text
    file_out = str(file_out)

    
    filepath1 = filepath[:len(filepath) - 4]
    
    
    with open(filepath1+"_tranlated.txt", 'w', encoding='utf-8') as f1:
        f1.write(file_out)
        f1.close()

    
    window.destroy()
    

def auto_detect() :
    global detect_lang
    global check_autodet

    
    detect_lang = detect(text1.get(1.0, END))
    check_autodet = True

def play_sound() :
    language1 = googletrans.LANGUAGES
    lang_val = combo2.get()
    lang_key = str({i for i in language1 if language1[i] == lang_val})
    lang_key = lang_key[2:-2]
    tts = gTTS(text=text2.get(1.0, END), lang=lang_key)
    tts.save("hello.mp3")
    os.startfile('hello.mp3')
    
    


icon_photo = PhotoImage(file="icon_image.png")
window.iconphoto(False, icon_photo)


arrow_photo= PhotoImage(file="double-arrow (1).png")


language = googletrans.LANGUAGES 
languageV = list(language.values())



combo1 = ttk.Combobox(window, values = languageV, font = ("Futura", 18), state= 'r')
combo1.place(x=100, y = 36)
combo1.set ("english") 

label1 = Label(master = window,
            font = ("Futura", 30, "bold"),
            bg = "#398498", width=16,
            border=5, relief=RAISED)

label1.place(x = 12, y = 90)



combo2 = ttk.Combobox(window, values = languageV,
                    font = ("Futura", 18),
                    state = 'r' )
combo2.place(x = 850, y = 36)
combo2.set("select language") 

label2 = Label(window, 
            font = ("Futura", 30, "bold"),
            bg = "#398498", width=16,
            border=5, relief=RAISED)

label2.place(x = 760, y = 90)


f1 = Frame(window, bg = 'black', bd = 2)
f1.place(x= 12, y = 198, width=450, height = 372)

text1 = Text(f1, font = ("Comic Sans", 20), bg="#ceecff",relief=GROOVE, wrap=WORD )
text1.place(x = 0, y = 0, width=434, height =368)


scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill = 'y') 
scrollbar1.configure(command=text1.yview) 
text1.configure(yscrollcommand = scrollbar1.set) 


f2 = Frame(window, bg = "black", bd = 2)
f2.place(x= 828, y = 198, width=450, height = 372)

text2 = Text(f2, font = ("Comic Sans", 20), bg="#ceecff",
                relief=GROOVE, wrap=WORD, )
text2.place(x = 0, y = 0, width=434, height =368)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill = 'y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand = scrollbar2.set)

translate = Button(window, text = "TRANSLATE",
                font = ("Comic Sans", 20), activebackground= '#6fbad1',
                cursor='hand2', width= 255, height=200, bg = '#08181e',
                fg = 'white', command=translate_now, image=arrow_photo, 
                compound=TOP, relief=RAISED, border=1)
translate.place(x = 515, y = 250)


browse_button = Button(window, text="Choose file", command=browse_file, 
                        font=("Futura", 20), bg = "#c0e2ed", activebackground = "#c0e2ed",
                        state=ACTIVE, cursor='hand2')
browse_button.place(x= 12, y = 576)

detect_button = Button( window, text = "Auto detect", command=auto_detect, 
                        font=("Futura", 20),state = ACTIVE, bg = "#c0e2ed", cursor='hand2', 
                        activebackground= "#c0e2ed")
detect_button.place(x = 270, y = 576 )

play_button = Button( window, text = "PLAY", command=play_sound, 
                        font=("Futura", 20, "bold"),state = ACTIVE, bg = "#c0e2ed", cursor='hand2', 
                        activebackground= "#c0e2ed")
play_button.place(x = 830, y = 576 )


label_change()
window.mainloop()

