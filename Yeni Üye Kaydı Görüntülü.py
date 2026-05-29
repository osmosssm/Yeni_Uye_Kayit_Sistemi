import os
from turtle import *
import time

setup(1000,750)

hideturtle()
bgcolor("gray")
pencolor("green")
penup()
goto(0,300)
pendown()
write("Yeni Üye Kayıt Sistemi",align="center" ,font=("Arial" , 35 , "italic"))
penup()
goto(0,200)
pendown()
write("Aşağıda sırasıyla İsim Soyisim mailadresi ve şifre giriniz",align="center" ,font=("Arial" , 35 , "italic"))
time.sleep(2)

pencolor("white")
İsim=textinput("İsim","İsminizi giriniz:")
Soyisim=textinput("Soyisim","Soyisiminizi giriniz:")
Mail=textinput("Mail","Mailadresinizi giriniz:")
Şifre=textinput("Şifre","Şifre giriniz:")

os.chdir("D://Yeniüye Kayıt kodu klasörü")
dosya = open("Kayıt Bilgi.txt","w")
dosya.write("İsim:"+ İsim +"          ")
dosya.write("Soyİsim:"+ Soyisim +  "\n")
dosya.write("MailAdresi:"+ Mail +  "\n")
dosya.write("Şifre:"+ Şifre +  "\n")
dosya.write("\n")
dosya.write("\n")
dosya.close()

os.startfile("D://Yeniüye Kayıt kodu klasörü//Kayıt Bilgi.txt")

done()