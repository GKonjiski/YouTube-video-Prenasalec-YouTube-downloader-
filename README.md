YouTube video prenašalec (YouTube Video Downloader)
========================

Preprosta namizna aplikacija za prenašanje YouTube videjev z grafičnim vmesnikom.

FUNKCIONALNOSTI
---------------
- Prenos videjev v resolucijah: 720p, 1080p, 1440p
- Podprti formati: MP4 (video), MP3 (samo zvok)

ZAHTEVE
-------
- Python 3.x
- yt-dlp
- ffmpeg

UPORABA
-------
Vnesi URL YouTube videa, pritisni dodaj na seznam (dodaš lahko več videjev naenkrat), izberi format in resolucijo ter pritisni Prenesi. 

STRUKTURA PROJEKTA
------------------
project/
│
├── main.py
├── ffmpeg.exe
├── fotka.png
├── profilka.png
├── README.txt
└── LICENSE

PAKIRANJE V EXE
---------------
Koda je primerna za pretvorbo v izvršljivo datoteko (.exe) z orodjem PyInstaller.
ffmpeg.exe, fotka.png in profilka.png morajo biti v isti mapi kot main.py.

Ukaz za pakiranje:
(priporočena uporaba auto-py-to-exe)
pyinstaller --onefile --windowed --add-binary "ffmpeg.exe;." --add-data "fotka.png;." --add-data "profilka.png;." main.py

LICENCA
-------
MIT License - prosta uporaba, kopiranje in spreminjanje kode.
