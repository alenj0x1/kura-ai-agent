import subprocess
from core import kura_response
from datetime import datetime

def hi():
  print(f"{kura_response} hi ₍^. .^₎⟆")

def calculator():
  print(f"{kura_response} open the calculator")
  subprocess.Popen('calc.exe')

def current_time():
  now = datetime.now()
  print(f"{kura_response} current time is: {now.strftime('%H:%m:%S')} ( • ᴗ - ) ✧")

def action_not_found():
  print(f"{kura_response} i don't know what action you are referring to, try again. (¬_¬')")

def close():
  print(f"{kura_response} thanks for interacting with me, come back soon! ᓚ₍⑅^..^₎♡")
  exit();