import tkinter as tk
import pyautogui as pag
import os
import json
import tkinter.messagebox 

#儲存成json
def _hit1():
    savelinK[enteName.get()]=enteLink.get()
    with open("link.json","w",encoding="utf-8") as filE:
        json.dump(savelinK,filE,ensure_ascii=False,indent=4)
    lisT.insert(tk.END, enteName.get())
    enteName.delete(0,tk.END)
    enteLink.delete(0,tk.END)
#前往選的網站
def _hit2():
    lisTloC=lisT.curselection()
    saveLinkkeY=lisT.get(lisTloC)

    goTo=savelinK[saveLinkkeY]
        
    pag.moveTo(222*changeW,1059*changeH,0)
    pag.click()
        
    pag.hotkey('ctrl','t')
    pag.PAUSE=1
        
    pag.moveTo(312*changeW,52*changeH,0)
    pag.click()
    pag.write(goTo)
    pag.press('enter')
    
def _hit3():
    qQ=tk.messagebox.askokcancel("離開確定","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()
#刪除       
def _hit4():
    lisTloC=lisT.curselection()
    deleteLinkkeY=lisT.get(lisTloC)
    del savelinK[deleteLinkkeY]
    with open("link.json","w",encoding="utf-8") as filE:
        json.dump(savelinK,filE,ensure_ascii=False,indent=4)
    lisT.delete(lisTloC)
    


wiN = tk.Tk()
wiN.title("懶人專用機器(ಠ ಠ )")
wiN.geometry("550x500+1100+100")
wiN.resizable(False, False)
wiN.configure(background='black')

if os.path.exists('link.json'):
    with open("link.json","r",encoding="utf-8") as filE:
        savelinK=json.load(filE)
else:
    savelinK={}


w,h=pag.size()
changeW=w/1920
changeH=h/1080

labeLName=tk.Label(wiN, text='網站名稱:', font=("Arial Black", 20), fg ="red", bg ="black")
labeLName.place(x=0,y=0)
enteName=tk.Entry(wiN,font=("Arial",18),bd=5,fg="red", bg ="black")
enteName.place(x=150,y=0) 
labeLLink=tk.Label(wiN, text='網站網址:', font=("Arial Black", 20), fg ="red", bg ="black")
labeLLink.place(x=0,y=50)
enteLink=tk.Entry(wiN,font=("Arial",18),bd=5,fg="red", bg ="black")
enteLink.place(x=150,y=50) 

btN1 = tk.Button(wiN, text="儲存連結ˇ.ˇ",fg="red", bg ="black", font=("Arial Black", 18), width=7, height=1, command=_hit1)
btN1.place(x=50,y=100)

btN2 = tk.Button(wiN, text="開啟(¬_¬)",fg="red", bg ="black", font=("Arial Black", 18), width=7, height=1, command=_hit2)
btN2.place(x=220,y=100)

btN3 = tk.Button(wiN, text="離開(掰掰)",fg="red", bg ="black", font=("Arial Black", 18), width=7, height=1, command=_hit3)
btN3.place(x=390,y=100)

btN4 = tk.Button(wiN, text="刪除",fg="red", bg ="black", font=("Arial Black", 18), width=4, height=1, command=_hit4)
btN4.place(x=440,y=25)

list_str=tk.StringVar()
lisT=tk.Listbox(wiN, font=("Arial Black", 20), fg ="white", bg ="black",height=40,  listvariable=list_str,  selectmode=tk.EXTENDED)
lisT.place(x=0,y=175,width=550,height=320)
for linkS in savelinK:
   lisT.insert(tk.END, linkS)

wiN.mainloop()

