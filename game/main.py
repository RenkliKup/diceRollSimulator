from tkinter import *
from tkinter import messagebox
import random as rnd
pencere=Tk()
pencere.title("Zar atma oyunu")
pencere.geometry("500x500")

zar=["1","2","3","4","5","6"]
zar1=["1","2","3"]
button_adresleri=[]
def zar_at():
    global button_adresleri
    if len(button_adresleri)==1:
        button_adresleri[0].config(text=rnd.choices(zar))
    if len(button_adresleri)==2:
        button_adresleri[0].config(text=rnd.choices(zar))
        button_adresleri[1].config(text=rnd.choices(zar))
    if len(button_adresleri)==3:
        button_adresleri[0].config(text=rnd.choices(zar))
        button_adresleri[1].config(text=rnd.choices(zar))
        button_adresleri[2].config(text=rnd.choices(zar))
    
def oyuna_gir():
        global button_adresleri
        text=zar_sayisi.get()
        if text in zar1:
            label1.destroy()
            label2.destroy()
            Button_giris.destroy()
            zar_sayisi.destroy()
            label3.destroy()
            Button_zar_at=Button(pencere,text="Zar at",command=zar_at)
            Button_zar_at.grid(columnspan=3,row=1,column=0)
            Button_cikis=Button(pencere,text="oyundan çık",command=lambda:pencere.destroy())
            Button_cikis.grid(row=2,column=2,columnspan=5)
            for i in range(1,int(text)+1):
                var=Button(pencere,text=rnd.choices(zar),width=3,height=3)
                var.grid(column=i,row=0)
                button_adresleri.append(var)
        else:
            var=messagebox.askyesnocancel("Hata","Lütfen 1-3 sayılarını giriniz")


             
label1=Label(pencere,text="Zar Atma Oyununa hoş geldiniz :)")
label1.grid(columnspan=5,row=0)
label2=Label(pencere,text="sadece 1-3 degerler girmelisiniz:")
label2.grid(columnspan=5,row=1,column=0)
label3=Label(pencere,text="Zar sayısı:")
label3.grid(column=0,row=2)
zar_sayisi=Entry(pencere)
zar_sayisi.grid(column=1,row=2)
Button_giris=Button(pencere,text="Oyuna giriş",command=oyuna_gir)
Button_giris.grid(column=1,row=3)
pencere.mainloop()