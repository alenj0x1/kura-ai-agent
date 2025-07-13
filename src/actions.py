import subprocess
import webbrowser
import yt_dlp
from core import kura_response
from datetime import datetime

def hi():
  print(f"{kura_response} hi ₍^. .^₎⟆")

def calculator():
  print(f"{kura_response} opening calculator")
  subprocess.Popen('calc.exe')

def spotify():
  print(f"{kura_response} opening spotify")
  subprocess.Popen('spotify.exe')

def search_on_youtube(query: str):
  ydl_opts = {
    'quiet': True,
    'skip_download': True,
    'extract_flat': True
  }

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(f"ytsearch:{query}", download=False)
    
    if 'entries' in info and len(info['entries']) > 0:
      url = info['entries'][0]['url']
      webbrowser.open(url)
    else:
      None

def current_time():
  now = datetime.now()
  print(f"{kura_response} current time is: {now.strftime('%H:%M:%S')} ( • ᴗ - ) ✧")

def action_not_found():
  print(f"{kura_response} i don't know what action you are referring to, try again. (¬_¬')")

def close():
  print(f"{kura_response} thanks for interacting with me, come back soon! ᓚ₍⑅^..^₎♡")
  exit();