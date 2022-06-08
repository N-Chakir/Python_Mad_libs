from tkinter import messagebox
import os 
from config.definitions import ROOT_DIR
from tkinter import *
from tkinter import ttk
from ctypes import windll
from tkinter import font as tkFont
from turtle import color
from PIL import *
from PIL import Image, ImageTk
from random import seed
from random import randint     
    
def popup_quit():
    win.destroy()
    Btn1.config(state="normal")
    Btn2.config(state="normal")
    Btn3.config(state="normal")
def popup_quit2():
    win2.destroy()
    Btn1.config(state="normal")
    Btn2.config(state="normal")
    Btn3.config(state="normal")
def popup_quit3():
    win3.destroy()
    Btn1.config(state="normal")
    Btn2.config(state="normal")
    Btn3.config(state="normal")
    
#The window
root = Tk();
root.title("Python Mad Libs")
root.geometry("700x600+50+50");
root.resizable(1,0)
root.attributes("-alpha",0.99)
root.iconbitmap(os.path.realpath(os.path.join(ROOT_DIR, 'pictures','madlibs.ico')))
#root.style = ttk.Style(root).theme_use("classic")


#resizing img dynamically
def size(event):
    # resize the image with width and height of root
    resized = bg.resize((event.width, 600))
    img =ImageTk.PhotoImage(resized)
    label.config(image=img)
    label.image=img
     
#image
bg = Image.open(os.path.realpath(os.path.join(ROOT_DIR, 'pictures','madlibs_back_alt.png')))
resised = bg.resize((600,600))
img = ImageTk.PhotoImage(resised)

class input() :
    def __init__(self,root,master,name,row):
        style = ttk.Style(root)
        style.theme_use('alt')
        style.configure("Custom.TLabel",font=('Forte',15),weight='bold',background="grey99",foreground='black')
        style.configure("Custom.TEntry",front=('Helvetika',17),foreground="#3776AB")
        self.r = row
        self.n = name
        self.label_box = ttk.Label(master, text=self.n+"",style="Custom.TLabel")
        self.label_box.grid(column=0,row=self.r,pady=10);
        self.entry_box = ttk.Entry(master,style='Custom.TEntry')
        self.entry_box.grid(column=1,row=self.r,pady=10);

    def text(self) :
        return (self.entry_box).get()
    def clear(self) :
        self.entry_box.delete(0, 'end')
        
        
#canvas
canvas = Canvas(root)
canvas.pack(fill='x')

canvas.columnconfigure(0,weight=1)
canvas.columnconfigure(1,weight=3)
canvas.columnconfigure(2,weight=1)

#label 
label = ttk.Label(canvas,image=img)
label.grid(column = 0, row =0,columnspan=3,rowspan=10,sticky=N+E+W+S)

#image 
i = Image.open(os.path.realpath(os.path.join(ROOT_DIR, 'pictures','paragraph.png')))
j= ImageTk.PhotoImage(i.resize((40,40)))
i = Image.open(os.path.realpath(os.path.join(ROOT_DIR, 'pictures','V.png')))
k=ImageTk.PhotoImage(i.resize((40,40)))
i = Image.open(os.path.realpath(os.path.join(ROOT_DIR, 'pictures','N.png')))
l=ImageTk.PhotoImage(i.resize((40,40)))

#ttk requires Style to modify font unlike classic 
s=ttk.Style();
s.theme_use("alt")
s.configure("T.TButton",font=('curlz mt', 23),weight='bold')
s.map("T.TButton",foreground=[('!active', 'black'),('pressed', 'white'), ('active', '#FFD749')],
      background=[ ('!active','grey99'),('pressed', '#3776AB'), ('active', '#3776AB')])

#defining the buttons' actions
#first story
  
def func1() : 
    Btn1.config(state="disable");
    Btn2.config(state="disable");
    Btn3.config(state="disable");
    global win;
    win = Tk();
    win.geometry('405x745+751+50');
    win.title("Paragraph")
    win.iconbitmap(os.path.realpath(os.path.join(ROOT_DIR, 'pictures','paragraph.ico')))
    
    s = ttk.Style(win)
    s.theme_use("alt")
    s.configure("A.TFrame",background='grey99')
    s.configure("A.TLabel",font='curlz mt',size=30,weight='bold')
    s.configure("B.TLabel",font="SimSun bold",size=80)
    s.configure("T.TEntry",font="SimSun bold",size=20)
    s.configure("T.TButton",font=('curlz mt', 12),weight='bold')
    s.map("T.TButton",foreground=[('!active', 'black'),('pressed', 'white'), ('active', '#FFD749')],
      background=[ ('!active','grey100'),('pressed', '#3776AB'), ('active', '#3776AB')])
    
    frame = ttk.Frame(win,style="A.TFrame")
    frame.place(height=745,width=405)
    frame.columnconfigure(0,weight=1)
    frame.columnconfigure(1,weight=1)

    def check1() :
        for i in range(9) :
            if len(ins[i].text()) == 0 :
                messagebox.showwarning('Invalid','An entry was left empty!');
                break;
            else :
                pass
        else:
            Done1.config(state="disable")
            int = randint(0, 3)
            if int == 0 :
                String ="I loved the "+ins[0].text()+" that I bought at a(n) "+ins[1].text()+". It fit "+ins[2].text()+".I wore it "+ins[3].text()+" to a(n) "+ins[4].text()+" and glowed when a person exclaimed, “Oh, how "+ins[5].text()+"” Yes, I was "+ins[6].text()+" , until she added "+ins[7].text()+", “Hang on to it, honey."+ins[8].text()+"s will come back someday.“" 
            elif int == 1:
                String ="I hated the "+ins[0].text()+" I read last night in "+ins[1].text()+". It was so "+ins[2].text()+" and "+ins[3].text()+" that I would have prefered doing anything else. I "+ins[4].text()+" about about it in a(n) "+ins[5].text()+" I attended the same week. Everyone was unimpressed with it, except for Emma who suddently "+ins[6].text()+" : “You people are "+ins[7].text()+" uneducated!“ She tipped her "+ins[8].text()+" and left."
            elif int ==2 : 
                String = ins[0].text()+ " is/are fascinating " +ins[1].text()+", they thrive on the " +ins[2].text()+" corpses of the deceased. What we consider the "+ins[3].text()+" end of "+ins[4].text()+". Which shows the "+ins[5].text()+" reality, that life is "+ins[6].text()+" and "+ins[7].text()+" it always comes to an end. Whether it be a living thing, or a(n) "+ins[8].text()
            else :
                String = ins[0].text()+" […]Short "+ins[1].text()+" is/are "+ins[2].text()+" to read and "+ins[3].text()+" to understand. At "+ins[4].text()+", Writing experts are "+ins[5].text()+" recommend they be no more than 150 words. They should be "+ins[7].text()+", and never be longer than 250 words. Vary the lengths of your "+ins[8].text()+" to make them so."
            global msg
            msg = Message(frame,
                      text=String,
                      font=("SimSun",18),
                      borderwidth=2,
                      relief="raised",
                      background="grey99"
                      )
            msg.grid(column=0,columnspan=2,row=11)  
    def check2() :
        msg.destroy()
        Done1.config(state="normal")
        for j in range(9):
            ins[j].clear()
        
    #labels and associated entries
    global ins 
    ins = [input]*9
    str = ["Noun      ","Noun      ","Adjective ","Adjective ","Noun      ",
            "Adjective ","Verbing   ","Adverb    ","Noun      "]
    i=0
    while i < len(str):
        ins[i] = input(win,frame,str[i],i)
        i+=1
    global Done1
    Done1 = ttk.Button(frame, text = 'Done',style="T.TButton", command = check1)
    Done1.grid(column=1,row=10,sticky=E,padx=5)
    global Reset1
    Reset1 = ttk.Button(frame, text = 'Reset',style="T.TButton", command = check2)
    Reset1.grid(column=1,row=10,sticky=W,padx=5)
    
    win.resizable(0,1)
    win.attributes("-alpha",0.99)
    #win.lift();
    win.protocol("WM_DELETE_WINDOW", popup_quit);
def func2() :
    Btn1.config(state="disable")
    Btn2.config(state="disable")
    Btn3.config(state="disable")
    global win2
    win2 = Tk()
    s = ttk.Style(win2)
    s.theme_use("alt")
    s.configure("A.TFrame",background='grey99')
    s.configure("A.TLabel",font='curlz mt',size=30,weight='bold')
    s.configure("B.TLabel",font=("SimSun bold",15),borderwidth=2,relief="groove",background="grey90")
    s.configure("T.TEntry",font="SimSun bold",size=20)
    s.configure("T.TButton",font=('curlz mt', 12),weight='bold')
    s.map("T.TButton",foreground=[('!active', 'black'),('pressed', 'white'), ('active', '#FFD749')],
      background=[ ('!active','grey100'),('pressed', '#3776AB'), ('active', '#3776AB')])
    
    frame = ttk.Frame(win2,style="A.TFrame")
    frame.place(height=200, width=400)
    frame.columnconfigure(0,weight=1)
    frame.columnconfigure(1,weight=1)
    frame.rowconfigure(2,weight=1)
    frame.rowconfigure(3,weight=1)
    
    def check1():
        global label_verb
        if len(verb_input.text()) == 0 :
                messagebox.showwarning('Invalid','Entry was left empty!');
        else :      
            int = randint(0,12) 
            global tt
            if int == 0:
                tt = "To  "+verb_input.text()+" a Mockingbird"
                pass
            if int == 1:
                tt = "Fortune "+verb_input.text()+"s the bold." 
                pass
            if int == 2:
                tt= "I think, therefore I "+verb_input.text()
                pass
            if int == 3:
                tt="When life gives you lemons, "+verb_input.text()+"\nlemonade."
                pass
            if int == 4:
                tt="Practice "+verb_input.text()+"s perfect."
                pass
            if int == 5:
                tt="You only "+verb_input.text()+" once, but if you do \nit right, once is enough."
                pass
            if int == 6:
                tt="Tis better to "+verb_input.text()+" and lose than to \nnever "+verb_input.text()+" at all."
                pass
            if int == 7:
                tt = "A person is but what they "+verb_input.text()+"."
                pass
            if int == 8:
                tt = "In three words I can sum up everything I’ve \nlearned about life: It "+verb_input.text()+"s on."
                pass
            if int == 9:
                tt = "If you judge people, you have no time to \n"+verb_input.text()+" them."
                pass
            if int == 10:
                tt = "Have no fear of perfection, you’ll never \n"+verb_input.text()+" it"
                pass
            if int == 11:
                tt = "If you want to be happy, "+verb_input.text()+"."
                pass
            label_verb = ttk.Label(frame,text=tt,style="B.TLabel")
            label_verb.grid(column=0,row=2,columnspan=2,rowspan=2,ipadx=5,ipady=5)
            Done2.config(state='disable')
        pass
    def check2():
        Done2.config(state='normal')
        label_verb.destroy()
        verb_input.clear()
        pass
    
    
    global Done2
    Done2 = ttk.Button(frame, text = 'Done',style="T.TButton", command = check1)
    Done2.grid(column=1,row=1,sticky=E,padx=5)
    global Reset2
    Reset2 = ttk.Button(frame, text = 'Reset',style="T.TButton", command = check2)
    Reset2.grid(column=1,row=1,sticky=W,padx=5)
    global verb_input
    verb_input = input(win2,frame,"Verb  ",0)
    win2.title("Verb")
    win2.iconbitmap(os.path.realpath(os.path.join(ROOT_DIR, 'pictures','V.ico')))
    win2.resizable(0,1)
    win2.attributes("-alpha",0.99)
    win2.geometry('400x200+800+120')
    win2.lift()
    win2.protocol("WM_DELETE_WINDOW", popup_quit2)
    pass 
def func3() :
    Btn1.config(state="disable")
    Btn2.config(state="disable")
    Btn3.config(state="disable")
    global win3
    win3 = Tk()
    s = ttk.Style(win3)
    s.theme_use("alt")
    s.configure("A.TFrame",background='grey99')
    s.configure("A.TLabel",font='curlz mt',size=30,weight='bold')
    s.configure("B.TLabel",font=("SimSun bold",15),borderwidth=2,relief="groove",background="grey99")
    s.configure("T.TEntry",font="SimSun bold",size=20)
    s.configure("T.TButton",font=('curlz mt', 12),weight='bold')
    s.map("T.TButton",foreground=[('!active', 'black'),('pressed', 'white'), ('active', '#FFD749')],
      background=[ ('!active','grey100'),('pressed', '#3776AB'), ('active', '#3776AB')])
    
    frame = ttk.Frame(win3,style="A.TFrame")
    frame.place(height=200, width=400)
    frame.columnconfigure(0,weight=1)
    frame.columnconfigure(1,weight=1)
    frame.rowconfigure(2,weight=1)
    frame.rowconfigure(3,weight=1)
    
    def check1():
        global label_noun
        if len(noun_input.text()) == 0 :
                messagebox.showwarning('Invalid','Entry was left empty!');
        else :      
            int = randint(0,7) 
            global tt
            if int == 0:
                tt = "It don’t mean a thing if it ain’t got that \n"+noun_input.text()
                pass
            if int == 1:
                tt = "Rumble in the "+noun_input.text()
                pass
            if int == 2:
                tt= "I can’t start my day without my "+noun_input.text()
                pass
            if int == 3:
                tt="The opposite of love is not hate; it’s "+noun_input.text()
                pass
            if int == 4:
                tt="The journey of a thousand miles begins with \none "+noun_input.text()
                pass
            if int == 5:
                tt="Life is either a(n) "+noun_input.text()+" or nothing at all"
                pass
            if int == 6:
                tt="Dreaming, after all, is a form of "+noun_input.text()
                pass
            label_noun = ttk.Label(frame,text=tt,style="B.TLabel")
            label_noun.grid(column=0,row=2,columnspan=2,rowspan=2,ipadx=5,ipady=5)
            Done3.config(state='disable')
        pass
    def check2():
        Done3.config(state='normal')
        label_noun.destroy()
        noun_input.clear()
        pass
    
    
    global Done3
    Done3 = ttk.Button(frame, text = 'Done',style="T.TButton", command = check1)
    Done3.grid(column=1,row=1,sticky=E,padx=5)
    global Reset3
    Reset3 = ttk.Button(frame, text = 'Reset',style="T.TButton", command = check2)
    Reset3.grid(column=1,row=1,sticky=W,padx=5)
    global noun_input
    noun_input = input(win3,frame,"Verb  ",0)
    
    
    win3.title("Verb")
    win3.iconbitmap(os.path.realpath(os.path.join(ROOT_DIR, 'pictures','N.ico')))
    win3.resizable(0,1)
    win3.attributes("-alpha",0.99)
    win3.geometry('400x200+800+120')
    win3.lift()
    win3.protocol("WM_DELETE_WINDOW", popup_quit3)
    pass 
    
#buttons
    #creation
Btn1 = ttk.Button(canvas, text = "Paragraph",style= "T.TButton",image = j ,command = func1,compound=LEFT )
Btn2 = ttk.Button(canvas, text = "Verb", style= "T.TButton",image = k, command = func2,compound=LEFT )
Btn3 = ttk.Button(canvas, text = "Noun", style= "T.TButton",image = l, command = func3,compound=LEFT)
    #insertion
Btn1.grid(column = 1, row =2,ipadx=40,ipady=10)
Btn2.grid(column = 1, row =3,ipadx=40,ipady=10)
Btn3.grid(column = 1, row =4,ipadx=40,ipady=10)
windll.shcore.SetProcessDpiAwareness(1);
root.bind("<Configure>",size)
root.mainloop()
