from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import gtts
from playsound import playsound
from gtts import gTTS
import textblob
from tkinter.filedialog import askopenfilename
from PIL import Image
import pytesseract
from pytesseract import *
import os


def readFimage():
    global text
    path = PathTextBox.get('1.0', 'end-1c')
    try:
        if path:
            im = Image.open(path)
            text = pytesseract.image_to_string(im, lang=com.get())
            ResultTextBox.delete('1.0', END)
            ResultTextBox.insert(END, text)


        else:
            ResultTextBox.delete('1.0', END)
            ResultTextBox.insert(END, "FILE CANNOT BE READ")
    except Exception as e:
        messagebox.showerror("ocr", "please select language for ocr")

def sound():
    try:
        language = "en"

        if os.path.exists("asi.mp3"):
            os.remove("asi.mp3")

        eoutput = gTTS(text=text, lang=language, slow=False)
        eoutput.save('asi.mp3')
        playsound('asi.mp3')
    except Exception as e:
        messagebox.showerror("ocr", "please read image first")

def op():
    global language, text
    path = PathTextBox.get('1.0', 'end-1c')
    if path:
        im = Image.open(path)
        text = pytesseract.image_to_string(im, lang='eng')
        ResultTextBox.delete('1.0', END)
        ResultTextBox.insert(END, text)

        trans = Tk()
        trans.title("Google Translator")
        trans.geometry("1080x400")

        def label_change():
            c = combo1.get()
            c1 = combo2.get()
            label1.configure(text=c)
            label2.configure(text=c1)
            trans.after(1000, label_change)

        def translate_now():
            global language, lan_
            try:

                text_ = text1.get(1.0, END)
                print(type(text_))
                c2 = combo1.get()
                c3 = combo2.get()
                if (text_):
                    words = textblob.TextBlob(text_)
                    lan = words.detect_language()
                    for i, j in language.items():
                        if (j == c3):
                            lan_ = i
                    words = words.translate(from_lang=lan, to=str(lan_))
                    text2.delete(1.0, END)
                    text2.insert(END, words)

                    sou = text2.get(1.0, END)
                    language = "en"

                    if os.path.exists("t.mp3"):
                        os.remove("t.mp3")
                    else:
                        print("The file does not exist")
                    output = gTTS(text=sou, lang=language, slow=False)
                    output.save('t.mp3')

                    def play():
                        playsound('t.mp3')

                    # playb = Button(trans, text="play", font="Roboto 15 bold italic", activebackground="violet",
                    #                cursor="hand2", bd=5, bg="red", fg="white", padx=15, pady=15, command=play)
                    #
                    # playb.place(x=480, y=350)











            except Exception as e:
                print(e)
                messagebox.showerror("googletrans", "please try again")

        # icon
        # image_icon=PhotoImage(file="google.png")
        # trans.iconphoto(False,image_icon)
        # arrow
        # arrow_image=PhotoImage(file="arrow.png")
        # image_label1=Label(trans,image=arrow_image,width=150)
        # image_label1.place(x=460,y=50)

        language = googletrans.LANGUAGES
        languageV = list(language.values())
        lang1 = language.keys()
        combo1 = ttk.Combobox(trans, values=languageV, font="Roboto 14", state="r")
        combo1.place(x=110, y=20)
        combo1.set("ENGLISH")

        label1 = Label(trans, text="ENGLISH", font="segoe 30 bold", bg="blue", width=18, bd=5, relief=GROOVE)
        label1.place(x=10, y=50)

        f = Frame(trans, bg="Black", bd=5)
        f.place(x=10, y=110, width=440, height=210)

        text1 = Text(f, font="RobotV 14", bg="white", relief=GROOVE, wrap=WORD)

        text1.place(x=0, y=0, width=430, height=200)
        text1.insert(INSERT, text)
        # text1.config(state=DISABLED)

        scrollbar1 = Scrollbar(f)
        scrollbar1.pack(side="right", fill="y")

        scrollbar1.configure(command=text1.yview)
        text1.configure(yscrollcommand=scrollbar1.set)

        combo2 = ttk.Combobox(trans, values=languageV, font="RobotV 14", state="r")
        combo2.place(x=730, y=20)
        combo2.set("SELECT LANGUAGE")

        label2 = Label(trans, text="ENGLISH", font="segoe 30 bold", bg="pink", width=18, bd=5, relief=GROOVE)
        label2.place(x=620, y=50)

        f1 = Frame(trans, bg="Black", bd=5)
        f1.place(x=620, y=110, width=440, height=210)

        text2 = Text(f1, font="RobotV 14", bg="white", relief=GROOVE, wrap=WORD)
        text2.place(x=0, y=0, width=430, height=200)

        scrollbar2 = Scrollbar(f1)
        scrollbar2.pack(side="right", fill="y")

        scrollbar2.configure(command=text2.yview)
        text2.configure(yscrollcommand=scrollbar2.set)

        translate = Button(trans, text="Translate", font="Roboto 15 bold italic", activebackground="yellow",
                           cursor="hand2",
                           bd=5, bg="orange", fg="white", command=translate_now)

        translate.place(x=480, y=250)

        def play():
            playsound('t.mp3')

        playb = Button(trans, text="play", font="Roboto 15 bold italic", activebackground="violet",
                       cursor="hand2", bd=5, bg="red", fg="white", padx=15, pady=15, command=play)

        playb.place(x=480, y=350)



        label_change()

        trans.configure(bg="white")

        trans.mainloop()
    else:
        ResultTextBox.delete('1.0', END)
        ResultTextBox.insert(END, "FILE CANNOT BE READ")


def OpenFile():
    name = askopenfilename(initialdir="C:\\py ocr gui\\ocr",
                           filetypes=(("PNG File", "*.png"), ("BMP File", "*.bmp"), ("JPEG File", "*.*")),
                           title="Choose a file."
                           )
    PathTextBox.delete("1.0", END)
    PathTextBox.insert(END, name)


root = Tk()
Title = root.title("F4 cwp project")
root.iconbitmap()
# language = googletrans.LANGUAGES
# languageV = list(language.values())
# lang1 = language.keys()
options = ['eng','mar','hin','tam','tel','guj','nep']
com = ttk.Combobox(root, values=options, font="Roboto 14", state="r")

com.grid(row=1, column=3)
com.set("Select language for ocr")

path = StringVar()

HeadLabel1 = Label(root, text="Image ")
HeadLabel1.grid(row=1, column=1, sticky=(E))
HeadLabel2 = Label(root, text=" Reader")
HeadLabel2.grid(row=1, column=2, sticky=(W))

InputLabel = Label(root, text="INPUT IMAGE:")
InputLabel.grid(row=2, column=1)

BrowseButton = Button(root, text="Browse", command=OpenFile)
BrowseButton.grid(row=2, column=2)

PathLabel = Label(root, text="Path:")
PathLabel.grid(row=3, column=1, sticky=(W))

PathTextBox = Text(root, height=2)
PathTextBox.grid(row=4, column=1, columnspan=2)

ReadButton = Button(root, text="READ FROM IMAGE", command=readFimage)
ReadButton.grid(row=5, column=2)
ReadButton = Button(root, text="Translate", command=op)
ReadButton.grid(row=6, column=2)
pandu = Button(root, text="Play",command=sound,padx=20,pady=20)
pandu.grid(row=9, column=2)

DataLabel = Label(root, text="DATA IN IMAGE:")
DataLabel.grid(row=6, column=1, sticky=(W))

ResultTextBox = Text(root, height=6)
ResultTextBox.grid(row=7, column=1, columnspan=2)
root.mainloop()
