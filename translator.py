


from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob

    
root=Tk()
root.title("Google Translator")
root.geometry("1080x400")
def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    global language
    try:
        
        text_=text1.get(1.0,END)
        print(type(text_))
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=i
            words=words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans","please try again")


#icon
# image_icon=PhotoImage(file="google.png")
# root.iconphoto(False,image_icon)
#arrow
# arrow_image=PhotoImage(file="arrow.png")
# image_label1=Label(root,image=arrow_image,width=150)
# image_label1.place(x=460,y=50)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()
combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="blue",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=110,width=440,height=210)

text1=Text(f,font="RobotV 14",bg="white",relief=GROOVE,wrap=WORD)

text1.place(x=0,y=0,width=430,height=200)
text1.insert(INSERT,'HI')
# text1.config(state=DISABLED)


scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2=ttk.Combobox(root,values=languageV,font="RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="pink",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=110,width=440,height=210)

text2=Text(f1,font="RobotV 14",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate=Button(root,text="Translate",font="Roboto 15 bold italic",activebackground="yellow",cursor="hand2",bd=5,bg="orange",fg="white",command=translate_now)

translate.place(x=480,y=250)
translate=Button(root,text="play",font="Roboto 15 bold italic",activebackground="violet",cursor="hand2",bd=5,bg="red",fg="white",padx=15,pady=15)

translate.place(x=480,y=350)


label_change()


root.configure(bg="white")
root.mainloop()

