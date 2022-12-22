import os,sys,time
import requests,json,datetime
import math
import speedtest
from datetime import date
from datetime import datetime
from requests import post,get
#Warna
Green="\033[1;92m"
White="\033[1;97m"
Gray="\033[1;90m"
Yellow="\033[1;93m"
Purple="\033[1;95m"
Red="\033[1;31m"
Blue="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"
#<------------------JAM + TANGGAL------------------>
current = datetime.now()
hari = current.day
bulan_number = current.month
nama_bulan= {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = nama_bulan[str(bulan_number)]
tahun = current.year
all_day=(f"{White}{hari}{Red}-{White}{bulan}{Red}-{White}{tahun}")

#""" WAKTU(JAM)"""
detik = datetime.now().strftime('%H')
menit = datetime.now().strftime('%M')
jam = datetime.now().strftime('%S')
all_waktu=(f"{detik}-{menit}-{jam}")
#<------------------API------------------>
API = 'https://api.ipify.org'
APII = 'http://free.ipwhois.io/json/'
DataBaseAPI = 'https://pastebin.com/raw/5fqM7NAk'
try:
  YourIP=requests.get(API).text
  Data=requests.get(APII+YourIP).json()
  DataBase=requests.get(DataBaseAPI).json()
except requests.exceptions.ConnectionError:
  print (f"{White}[{Red}!{White}] Tidak Ada Koneksi Internet...")
  sys.exit()
Menu01 = DataBase["MENU"]["Menu01"]
Menu02 = DataBase["MENU"]["Menu02"]
Menu03 = DataBase['MENU']['Menu03']
Menu04 = DataBase['MENU']['Menu04']
Menu05 = DataBase['MENU']['Menu05']
Menu1 = Menu01.center(16)
Menu2 = Menu02.center(16)
Menu3 = Menu03.center(16)
Menu4 = Menu04.center(16)
Menu5 = Menu05.center(16)
#STATUS Nomor 1
if Menu01 == "Active":
   Status1 = "\033[1;92m"
if Menu01 == "Inactive":
   Status1 = "\033[1;31m"
if Menu01 == "Maintenance!":
   Status1 = "\033[1;31m"
#STATUS Nomor 2
if Menu02 == "Active":
   Status2 = "\033[1;92m"
if Menu02 == "Inactive":
   Status2 = "\033[1;31m"
if Menu02 == "Maintenance!":
   Status2 = "\033[1;31m"
#STATUS Nomor 3
if Menu03 == "Active":
   Status3 = "\033[1;92m"
if Menu03 == "Inactive":
   Status3 = "\033[1;31m"
if Menu01 == "Maintenance!":
   Status3 = "\033[1;31m"
#STATUS Nomor 4
if Menu04 == "Active":
   Status4 = "\033[1;92m"
if Menu04 == "Inactive":
   Status4 = "\033[1;31m"
if Menu01 == "Maintenance!":
   Status4 = "\033[1;31m"
   
#<----------------TAMBAHAN/PELENGKAP---------------->
def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
def Tanya():
    a = input(f"{White}[{Yellow}?{White}] Back Tools? ({Yellow}Y{White}/{Yellow}n{White}){Red} :{Green} ")
    if a == "y" or a == "Y":
       os.system("python Menu.py")
    if a == "n" or a == "N":
        print (f"{White}[{Red}!{White}] Exited From Program")
        sys.exit()
    if a == "" or a == "":
        print (f"{White}[{Red}!{White}] Masukkan Pilihan Dengan Benar {Red}!!!{White}")
        Tanya()
    else:
      print (f"{White}[{Red}!{White}] Masukkan Pilihan Dengan Benar {Red}!!!{White}")
      Tanya()
#<------------------SPEEDTEST------------------>
def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{White}{size} {White}Mbps"
def Mahir_Speedtest():
    M = speedtest.Speedtest()
    ping_results = M.results.ping
    download_speed = M.download()
    upload_speed = M.upload()
    print (f"{White}Ping results {Red}:{White} {M.results.ping} ms")
    print (f"{White}Dowload Speed {Red}:", bytes_to_mb(download_speed))
    print (f"{White}Upload Speed {Red}:", bytes_to_mb(upload_speed))
    Tanya()
#<------------------PREMIUM/ADMIN------------------>

#<------------------BANNER------------------>
def Mahir_Banner():
    autoketik (f"""{White}
         ╔╗╔╔═╗╔╦╗╦ ╦╔═╗╦═╗╦╔═╦╔╗╔╔═╗   ╔╦╗╔═╗╔═╗╦  ╔═╗
         ║║║║╣  ║ ║║║║ ║╠╦╝╠╩╗║║║║║ ╦    ║ ║ ║║ ║║  ╚═╗
         ╝╚╝╚═╝ ╩ ╚╩╝╚═╝╩╚═╩ ╩╩╝╚╝╚═╝    ╩ ╚═╝╚═╝╩═╝╚═╝
       {White}─────────────────────────┬────────────────────────
  {White}┌─────────────────────────────┼────────────────────────────┐
  {White}│ Author{Red}:{White}Mahir Mandala        │ Version{Red} :{Green} 1.0{White}({Yellow}Beta Edition{White})│
  {White}│ Github{Red}:{White}Mahirmandala471      │Tools Ini Dalam Pengembangan{White}│
  {White}│ Bahasa Pemrograman{Red}:{Gray}Python{White}   │ Bila SC {Red}Error{White} Harap Lapor{Red}! {White}│
  {White}│ Tools{Red}:{White} Networking Tools     {White}│Dilarang Menjual Script Ini{Red}!{White}│
  {White}└─────────────────────────────┴────────────────────────────┘""")
#<------------------MENU------------------>
def Mahir_Menu():
    print (f"""{White}
    ┌──────┬─────────────────────────────┬────────────────┐
    │  NO  │             MENU            │     Status     │
    ├──────┼─────────────────────────────┼────────────────┤
    {White}│ {White}[{Blue}01{White}] │ {White}Clash For Termux ({Yellow}New{White})      │{Status1}{Menu1}{White}│
    {White}│ {White}[{Blue}02{White}] │ {White}SpeedTest ({Yellow}New{White})             │{Status2}{Menu2}{White}│
    {White}│ {White}[{Blue}03{White}] │ {White}YourIP ({Yellow}New{White})                │{Status3}{Menu3}{White}│
    {White}│ {White}[{Blue}04{White}] │ {White}Report Bug/Error            {White}│{Status4}{Menu4}{White}│
    {White}│ {White}[{Blue}05{White}] │ {White}Exit Tools                  │{Blue}      Null      {White}│
    {White}└──────┴─────────────────────────────┴────────────────┘""")
def Pilih01():
    if Menu01 == "Active":
       print (f"{all_day}")
       Tanya()
    if Menu01 == "Inactive":
       print (f"{White}[{Red}!{White}] Tools Tidak Aktif,Tunggu Admin Mengaktifkan Toolsnya Baru Bisa Digunakan {Red}!!!{White}")
       Tanya()
    if Menu01 == "Maintenance!":
       print (f"{White}[{Red}!{White}] Server/Rest Api Sedang Maintenance Harap Sabar {Red}!!!{White}")
       Tanya()
def Pilih02():
    if Menu02 == "Active":
       Mahir_Speedtest()
    if Menu02 == "Inactive":
       print (f"{White}[{Red}!{White}] Tools Tidak Aktif,Tunggu Admin Mengaktifkan Toolsnya Baru Bisa Digunakan {Red}!!!{White}")
       Tanya()
    if Menu02 == "Maintenance!":
       print (f"{White}[{Red}!{White}] Server/Rest Api Sedang Maintenance Harap Sabar {Red}!!!{White}")
       Tanya()
def Pilih03():
    if Menu03 == "Active":
       Pilih3()
    if Menu03 == "Inactive":
       print (f"{White}[{Red}!{White}] Tools Tidak Aktif,Tunggu Admin Mengaktifkan Toolsnya Baru Bisa Digunakan {Red}!!!{White}")
       Tanya()
    if Menu03 == "Maintenance!":
       print (f"{White}[{Red}!{White}] Server/Rest Api Sedang Maintenance Harap Sabar {Red}!!!{White}")
       Tanya()
def Main():
    os.system("clear")
    Mahir_Banner()
    Mahir_Menu()
    pil=input(f"        Input Number : ")
    if pil == "1" or pil == "01":
        Pilih01()
    if pil == "2" or pil == "02":
        Pilih02()
    if pil == "3" or pil == "03":
        print (f"Your Ip: {Data['ip']}")
        Tanya()
    if pil == "4" or pil == "04":
        os.system("xdg-open https://wa.me/+6281943658387?text=Assalamualaikum+Om,+Mau+Lapor+Bug/Error.")
        print (f"{Yellow}${White} Terima Kasih Telah Report Bug/Error,Author Akan Segera Memperbaiki Bug/Error")
        Tanya()
    if pil == "5" or pil == "05":
        print (f"{White}[{Red}!{White}] Exited From Program")
        sys.exit()
    else:
      sys.exit()
Main()