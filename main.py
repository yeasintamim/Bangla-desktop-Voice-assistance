from tkinter import *
import tkinter.messagebox as tmgs
import tkinter.font as font
#this first portion is the most valuable part it transfers bangla language to english and english to bangla



from gtts import gTTS
from googletrans import Translator
translator = Translator()
import os   
def transi(s):
      translated = translator.translate(s, src='en', dest='bn') 
      return translated.text
def transi2(s):
      translated = translator.translate(s, src='bn', dest='en') 
      return translated.text  


#translated = translator.translate('kemon achho', src='bn', dest='en')  
#print(translated.text)
from playsound import playsound
import pygame


globalStore='k'
#code begins here

import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import smtplib
import goslate
import random

gs = goslate.Goslate()

#sara will search here

#sara will speak here

def speak(ps,flag):
    global globalStore
    global r
    #globalStore+='k'
    if(r.get()==2):
        tts=gTTS(ps,lang='bn')
    else:
        tts=gTTS(ps,lang='en')
    tts.save(globalStore+'.mp3')
    pygame.init()
    pygame.mixer.init()
    with open('k.mp3', 'rb') as file_object:
        pygame.mixer.music.load(file_object)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
    #pygame.mixer.music.play(0)
    pygame.mixer.quit()
    pygame.quit()
    os.remove('k.mp3')    

#this will make every text from bangla to english
def boom():
    global globalStore
    globalStore+='k'
    tts="add"
    tts.save(globalStore+'.mp3')
    playsound(globalStore+'.mp3')
    os.remove(globalStore+'.mp3')    
def trans(s):
      translated = translator.translate(s, src='bn', dest='en') 
      return translated.text.lower()

#making wish me function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Salam , Good morning , i am sojol",0)
        #speak("Hello, Good morning , i am eva",1)
    elif(hour>=12 and hour <18):
        speak("salam, Good Afternoon! , i am sojol",0)
        #speak("Hello, Good Afternoon! , i am eva",1) 
    else:
        speak("salam, Good Evening! , i am sojol",0)
       # speak("Hello, Good Evening! , i am eva",1)
    #master.after(3000,wishMe)
        

# this function will take the commands by microphone and act like that
 
def takeCommand():
    global scValue
    r = sr.Recognizer()
    with sr.Microphone() as source:
        scValue.set("Listening....")
        screen.update()
        #print("Listening....")
        r.pause_threshold =1 
        audio = r.listen(source)
    try:
        scValue.set("Recognizing....")
        screen.update()
        query = r.recognize_google(audio, language='en-bn')
        print("User Said ",query)    
    except Exception as e:
        print(e)
        print("Say that again....")
        return "Nothing found please say that again(click and say)"

   
    return query

#speak whatever is in frame
def say(event):
    global scValue
    global ot
    ot.delete(1.0,END)
    ot.insert(1.0,"Wait.....")
    global line
    global r
    num=int(line.get())
    query=scValue.get()
    if(len(query)==0):
        ot.delete(1.0,END)
        ot.insert(1.0,"Give Us some input")
        return
    results="!!"
    if(r.get()==1):
        wikipedia.set_lang("en")
    else:
        wikipedia.set_lang("bn")
    try:
        results = wikipedia.summary(query,sentences=num)
    except wikipedia.DisambiguationError as e:
        ot.delete(1.0,END)
        ot.insert(1.0,e)
        ot.insert(END,"\nChose which one you want to know and type or say that again in the input bar")
        speak("Choose any word from above and search with that word",1)
    except wikipedia.exceptions.PageError:
        ot.delete(1.0,END)
        ot.insert(1.0,"NO Results Found!")
        speak("No results found",1)
    else:
        if(results=="!!"):
            ot.delete(1.0,END)
            ot.insert(1.0,"NO Results Found!")
            speak("No results found",1)
    
    cnt=0

    comp=StringVar()
    comp=''
    if(r.get()==2):
        for val in results:
            if val == '।':
                cnt=cnt+1
            if cnt>num:
                break
            comp+=val
    screen.update()
    if(results!="!!"):
        ot.delete(1.0, END)
        if(r.get()==2):
            ot.insert(1.0,comp)
            speak(comp,1)
        else:
            ot.insert(1.0,results)
            speak(results,1)






#input bar     
def click(event):
    global scValue
    text=takeCommand().lower()
    scValue.set(text)
    screen.update()

#search is made here


def src(event):
    global scValue
    global ot
    ot.delete(1.0,END)
    ot.insert(1.0,"Wait.....")
    global line
    global r
    num=int(line.get())
    query=scValue.get()
    if(i.get()==2):
        query=transi2(query)
    if(len(query)==0):
        ot.delete(1.0,END)
        ot.insert(1.0,"Give Us some input")
        return
    results="!!"
    if(r.get()==1):
        wikipedia.set_lang("en")
    else:
        wikipedia.set_lang("bn")
    try:
        results =wikipedia.summary(query,sentences=num )
    except wikipedia.DisambiguationError as e:
        ot.delete(1.0,END)
        ot.insert(1.0,e)
        ot.insert(END,"\nChose which one you want to know and type or say that again in the input bar")
        speak("Choose any word from above and search with that word",1)
    except wikipedia.exceptions.PageError:
        ot.delete(1.0,END)
        ot.insert(1.0,"NO Results Found!")
    else:
        if(results=="!!"):
            ot.delete(1.0,END)
            ot.insert(1.0,"NO Results Found!")
    
    #print(results.count('।'))
    cnt=0

    comp=StringVar()
    comp=''
    if(r.get()==2):
        for val in results:
            if val == '।':
                cnt=cnt+1
            if cnt>num:
                break
            comp+=val
    
    screen.update()
    if(results!="!!"):
        ot.delete(1.0, END)
        if(r.get()==2):
            ot.insert(1.0,comp)
        else:
            ot.insert(1.0,results)
def stopmusic(event):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.stop()
def google(event):
    webbrowser.open("google.com")
def youtube(even):
    webbrowser.open("youtube.com")
def facebook(event):
    webbrowser.open("facebook.com")
def hhh():
    tmgs.showinfo("Name : Zubair Ahmed Rafi ","HE LOVES SABA")
def rafi():
    tmgs.showinfo("ZUBAIR AHMED RAFI","SUST CSE 16 \n Reg No : 2016331037\n Mobile : 01759139913")
def yasin():
    tmgs.showinfo("Yasin Tamim","SUST CSE 14 \n Reg No : 2014331047\n Mobile : 01759139913")
def misba():
    tmgs.showinfo("Misbah Vai","SUST CSE 04 \n Reg No : 2004331037\n Mobile : 01759139913")
def guide():
    tmgs.showinfo("How to use wiki searcher","Type any word or sentence you want to know about\n in the first bar your give voice input as well then\n click convert to know about it \n click speak if you want to hear about it\n you can set the languse endlish or bangla ")
def hhh1(i):
    global line
def setlanen():
    global r
    r.set("1")
    global b
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    b['text']="Voice Input"
    b2['text']="Seacrh"
    b3['text']="Speak"
    b4['text']="Stop"
    b5['text']="Open Google"
    b6['text']="Open Youtube"
    b7['text']="Open Facebook"   
    screen.update()
def setlanban():
    global r
    r.set("2")
    global b
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    b['text']="মুখে ইনপুট নিন"
    b2['text']="অনুসন্ধান"
    b3['text']="বলুন "
    b4['text']="থামুন"
    b5['text']="গুগল খুলুন"
    b6['text']="ইউটিউব খুলুন"
    b7['text']="ফেইসবুক খুলুন"
    screen.update()
def setline1():
    global line
    line.set("1")
    screen.update()
def setline2():
    global line
    line.set("2")
    screen.update()
def setline3():
    global line
    line.set("3")
    screen.update()
def setline4():
    global line
    line.set("4")
    screen.update()
def setline5():
    global line
    line.set("5")
    screen.update()
def setline6():
    global line
    line.set("6")
    screen.update()
def setline7():
    global line
    line.set("7")
    screen.update()
def setline8():
    global line
    line.set("8")
    screen.update()
def setline9():
    global line
    line.set("9")
    screen.update()
def setline10():
    global line
    line.set("10")
    screen.update()
   
#Gui start here

root=Tk()

root.geometry("950x750")
root.title("WIKI SEARCHER")

root.config(bg = "black")


scValue=StringVar()
scValue.set("")
screen=Entry(root,textvar=scValue,font="lucida 30 bold",bg="grey")
screen.pack(fill=X,padx=10,pady=20)



f=Frame(root)
myFont = font.Font(family='lucida 5 bold')

# create button
b = Button(root, text='Voice Input', bg='#0052cc', fg='white',activebackground='#0052cc',activeforeground='white')
# apply font to the button label
b['font'] = myFont
b.pack()
b.bind("<Button-1>",click)
i=IntVar()
i.set("1")
rd3=Radiobutton(root,text="INPUT IN ENGLISH",variable=i,value=1,bg='#0052cc').pack()
rd4=Radiobutton(root,text="INPUT IN BANGLA",variable=i,value=2,bg='#0052cc').pack()
f.pack()


scrollbar= Scrollbar(root)
scrollbar.pack(side = RIGHT, fill=Y)



ot=Text(root,height=25,width=100,yscrollcommand=scrollbar.set,bg="grey")

text="hello"
ot.insert(1.0,text)
ot.pack(fill=X,padx=15,pady=15)
scrollbar.config(command=ot.yview)



f2=Frame(root,bg="grey")
myFont = font.Font(family='lucida 5 bold')


#ALL the buttons inisializer

b2 = Button(root, text='Search', bg='#0052cc' ,fg='white',activebackground='#0052cc',activeforeground='white')
b2['font'] = myFont
b3=Button(root,text="Speak", bg='#0052cc', fg='white')
b3['font']=myFont
line=StringVar()
line.set("2")
r=IntVar()
r.set("1")
drop= OptionMenu(root,line,1,2,3,4,5,6,7,8,9,10)
drop['width']=10
drop['bg']='#0052cc'
drop['fg']='white'
b4=Button(root,text="stop",bg='#0052cc',fg='white')
b5=Button(root,text="Open Google",bg='#0052cc',fg='white')
b6=Button(root,text="Open Youtube",bg='#0052cc',fg='white')
b7=Button(root,text="Open Facebook",bg='#0052cc',fg='white')


#all the buttons packing

b2.pack(side=LEFT,pady=1,padx=25)
b2.bind("<Button-1>",src)
b3.pack(side=LEFT,pady=1,padx=7)
b3.bind("<Button-1>",say)
drop.pack(side=LEFT,padx=25,pady=1)
rd1=Radiobutton(root,text="ENGLISH",variable=r,value=1,bg='#0052cc',command=setlanen).pack(side=LEFT,padx=7,pady=1)
rd2=Radiobutton(root,text="BANGLA",variable=r,value=2,bg='#0052cc',command=setlanban).pack(side=LEFT,padx=25,pady=1)
b5.pack(side=LEFT,padx=7,pady=1)
b5.bind("<Button-1>",google)
b6.pack(side=LEFT,padx=25,pady=1)
b6.bind("<Button-1>",youtube)
b7.pack(side=LEFT,padx=7,pady=1)
b7.bind("<Button-1>",facebook)
f2.pack()


yourmenubar= Menu(root)

m1=Menu(yourmenubar)
m1.add_command(label="Misbah",command=misba)
m1.add_command(label="Yasin",command=yasin)
m1.add_command(label="Rafi",command=rafi)

m2=Menu(yourmenubar)
m2.add_command(label="Guidelines",command=guide)

m3=Menu(yourmenubar)


m3.add_command(label="Bangla",command=setlanban)
m3.add_command(label="English",command=setlanen)

m4=Menu(yourmenubar)

m4.add_command(label="1",command=setline1)
m4.add_command(label="2",command=setline2)
m4.add_command(label="3",command=setline3)
m4.add_command(label="4",command=setline4)
m4.add_command(label="5",command=setline5)
m4.add_command(label="6",command=setline6)
m4.add_command(label="7",command=setline7)
m4.add_command(label="8",command=setline8)
m4.add_command(label="9",command=setline9)
m4.add_command(label="10",command=setline10)




root.config(menu=yourmenubar)


yourmenubar.add_cascade(label="Credits",menu=m1)
yourmenubar.add_cascade(label="Help",menu=m2)
yourmenubar.add_cascade(label="Set Language",menu=m3)
yourmenubar.add_cascade(label="Set Lines",menu=m4)


root.mainloop()


# main function starts here
