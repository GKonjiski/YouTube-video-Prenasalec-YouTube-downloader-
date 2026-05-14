import yt_dlp
import sys, os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox


#za exe

if getattr(sys, 'frozen', False):
    base = sys._MEIPASS
    ffmpeg_path = sys._MEIPASS
else:
    base = os.path.dirname(__file__)
    ffmpeg_path = os.path.dirname(os.path.abspath(__file__))



#spremenljivke za funkcijo download

videji_za_potegnt=[]

f720p= "bestvideo[height=720]+bestaudio"
f1080p="bestvideo[height=1080]+bestaudio"
f1440p="bestvideo[height=1440]+bestaudio"
f4k="bestvideo[height=2160]+bestaudio"
audio="bestaudio/best"

opcije=["720p","1080p", "1440p", "audio"]

video_opcije=["bestvideo[height=720]+bestaudio",
              "bestvideo[height=1080]+bestaudio", 
              "bestvideo[height=1440]+bestaudio"]

             
#FUNKCIJA ZA DOWNLOAD


def video_download(link,resolucija,lokacija):

    if resolucija in video_opcije:
        opt={
        "ffmpeg_location": ffmpeg_path,
        "format":resolucija,
        "outtmpl": f'{lokacija}\\%(title)s.%(ext)s',
        "merge_output_format": "mp4",
        'progress_hooks': [progress_hook]
        }

        with yt_dlp.YoutubeDL(opt) as ydl:
            info = ydl.extract_info(link, download=True)
            print(f"{info['title']}")
            

    else:
        opt={
            "ffmpeg_location": ffmpeg_path,
            'progress_hooks': [progress_hook],
            "format":"bestaudio/best",
            "outtmpl": f'{lokacija}\\%(title)s.%(ext)s',
            'ffmpeg_location': base,                        #add-binary "C:\ffmpeg\bin\ffmpeg.exe;
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            
        }]}

        with yt_dlp.YoutubeDL(opt) as ydl:
            info = ydl.extract_info(link, download=True)
            print(f"{info['title']}")
            

#GUI

#MAIN

okno= Tk()
okno.title("Prenos YouTube posnetkov")
#okno.geometry("720x720")
okno.config(background="#1d2433")
ikona = PhotoImage(file=os.path.join(base, "profilka.png"))
fotka = PhotoImage(file=os.path.join(base, "fotka.png"))

okno.iconphoto(True,ikona)


#SPREMENLJIVKE

izb_resolucija = StringVar(value="bestvideo[height=720]+bestaudio") #default resolucija
y=IntVar()
izbrana_lokacija=StringVar()


#COMMANDI ZA GUMBE

def prenos():
    x=0

    try:
        for i in videji_za_potegnt:

            video_download(i,izb_resolucija.get(),izbrana_lokacija.get())
            x+=1
            if x>=len(videji_za_potegnt):
                messagebox.showinfo(title="Prenos uspešen", message="Prenos je bil uspešen")

    except yt_dlp.utils.DownloadError as e:
        if "Permission denied" in str(e):
            messagebox.showerror(title="Napaka", message="Napčna lokacija shrambe")
            print("Napačen path")
        elif "Requested format is not available" in str(e):
            messagebox.showerror(title="Napaka", message="Format ni na voljo")
            print("Format ni na voljo")
        elif "URL" in str(e):
            messagebox.showerror(title="Napaka", message="Napačna povezava")
            print("Napačen link")
        else:
            messagebox.showerror(title="Napaka", message="Prišlo je do napake")

    #finally:
        #messagebox.showerror(title="Napaka", message="Prišlo je do napake")

    
def izbra_resolucije():
    if y.get() == 0:
        izb_resolucija.set("bestvideo[height=720]+bestaudio")
        print(izb_resolucija.get())

    elif y.get() == 1:
        izb_resolucija.set("bestvideo[height=1080]+bestaudio")
        print(izb_resolucija.get())
    
    elif y.get()== 2:
        izb_resolucija.set("bestvideo[height=1440]+bestaudio")
        print(izb_resolucija.get())

    else: 
        izb_resolucija.set("bestaudio/best")
        print(izb_resolucija.get())


def izberi_output():
    folder=filedialog.askdirectory()
    if folder:
        izbrana_lokacija.set(folder)   
        
        print(izbrana_lokacija.get())



def progress_hook(d):
    global bar
    if d["status"] == "finished":
        bar.destroy()
        bar = ttk.Progressbar(okno, length=300)
        bar.pack()
        bar.pack_forget()  
        return

    if d["status"] == "downloading":
        vsi_bajti = d.get("total_bytes") or d.get("total_bytes_estimate", 0)
        if vsi_bajti:
            bar["value"] = d['downloaded_bytes'] / vsi_bajti * 100
            okno.update_idletasks()
            bar.pack()

bar = ttk.Progressbar(okno, orient=HORIZONTAL, length=300)


def dodaj_povezavo():  
    if url.get() != "":
        try:
            info_naslov= yt_dlp.YoutubeDL().extract_info(url.get(), download=False)  
            info_naslov=info_naslov["title"]
            info_seznam=Label(seznam_frame,
                            text=info_naslov,
                            bg="#A8DDAC",
                            fg="#1d2433"
                            ).pack()
            videji_za_potegnt.append(url.get())

        except yt_dlp.utils.DownloadError as e:
            if "URL" in str(e):
                messagebox.showerror(title="Napaka", message="Napačna povezava")
                print("Napačen link")

def počisti_seznam():
    global seznam_frame
    videji_za_potegnt.clear()
    for i in seznam_frame.winfo_children():
        i.destroy()
    seznam_frame.pack_propagate(True)
    seznam_frame.config(height=1)
    okno.update_idletasks()
    
            
#WIDGETI

#barve
modra="#1d2433"
kremasta="#ffcc66"
sivo_kremasta="#4bb475"
naslov_barva="#7c4dff"

#frejmi
url_frame=Frame(okno,
                bg=kremasta,
                width=60)

url_gumbi_frame=Frame(okno,
                      bg=kremasta,
                      width=60)

seznam_frame=Frame(okno,
                   bg=kremasta,
                   width=60
                   )

radio_frame=Frame(okno,
                  bg=kremasta,
                  width=60)


#dejsnki vidgeti

naslov=Label(okno,
             text="Prenos YouTube posnetkov",
             font=("TimesNewRoman", 20, "bold"),
             bg=naslov_barva,
             fg=modra,
             width=25,
             relief="sunken",
             )


naslov_seznam=Label(okno,
                    text="Seznam dodanih posnetkov:",
                    font=("TimesNewRoman", 10, "bold"),
                    bg=kremasta,
                    fg=modra,
                    width=53,)


url=Entry(url_frame,
          bg="#f8dca3",
          width=50,
          fg=modra,
          )

url_tekst=Label(url_frame,
                text="Vnesi povezavo:",
                bg=kremasta,
                width=15,
                font=("TimesNewRoman", 10, "bold"),
                fg=modra,
                )

dodaj_url_gumb=Button(url_gumbi_frame,
                      text="Dodaj povezavo",
                      command=dodaj_povezavo,
                      bg=sivo_kremasta,
                      fg=modra,
                      width=29
                      )

počisti_seznam_gumb=Button(url_gumbi_frame,
                           text="Počisti seznam",
                           command=počisti_seznam,
                           bg=sivo_kremasta,
                           fg=modra,
                           width=30
                           )

url_tekst.pack(side=LEFT)
url.pack(side=LEFT)
dodaj_url_gumb.pack(side=LEFT)
počisti_seznam_gumb.pack(side=LEFT)


prenos_gumb=Button(okno,
                 text="Prenesi", 
                 command= prenos,
                 bg=sivo_kremasta,
                 fg=modra,
                 width=60)

gumb_izberi_lokacijo=Button(okno, 
                            text="Izberi lokacijo", 
                            command=izberi_output,
                            bg=sivo_kremasta,
                            fg=modra,
                            width=60)



for i in range(len(opcije)):
    opcije_radio=Radiobutton(radio_frame,
                             text=opcije[i],
                             variable=y,
                             value=i,
                             command=izbra_resolucije,
                             bg=kremasta,
                             fg=modra,
                             width=11)
    opcije_radio.pack(side=LEFT)

fotka_l=Label(okno,
             image=fotka,
             bg=modra
             )



#PACKI

normaln_pady=(0,5)

naslov.pack(pady=normaln_pady)

fotka_l.pack(pady=normaln_pady)

url_frame.pack(pady=normaln_pady)
url_gumbi_frame.pack(pady=normaln_pady)
naslov_seznam.pack(pady=normaln_pady)
seznam_frame.pack(pady=normaln_pady)
gumb_izberi_lokacijo.pack(pady=normaln_pady)

radio_frame.pack(pady=normaln_pady)
prenos_gumb.pack(pady=normaln_pady)


okno.mainloop()






