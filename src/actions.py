import subprocess
import webbrowser
import yt_dlp
from core import kura_response
from datetime import datetime
from colorama import Fore

def hi(username: str):
  print(f"{kura_response} hi, {username} ₍^. .^₎⟆")

def calculator():
  print(f"{kura_response} opening" + Fore.BLUE + " Calculator ₍ᐢ. .ᐢ₎")
  subprocess.Popen('calc.exe')

def spotify():
  print(f"{kura_response} opening" + Fore.BLUE + " Spotify ₍ᐢ. .ᐢ₎")
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
      item = info['entries'][0]

      print(f"{kura_response} opening in Youtube " + Fore.BLUE +  f"{item['title']} ₍ᐢ. .ᐢ")
      webbrowser.open(item['url'])
    else:
      None

def current_time():
  now = datetime.now()
  print(f"{kura_response} current time is: " + Fore.BLUE + f"{now.strftime('%H:%M:%S')} ₍ᐢ. .ᐢ₎")

def action_not_found():
  print(f"{kura_response}" + Fore.RED + " i don't know what action you are referring to, try again. (¬_¬')")

def close(username: str):
  print(f"{kura_response} thanks for interacting with me, {username}, come back soon! ᓚ₍⑅^..^₎♡")
  exit();