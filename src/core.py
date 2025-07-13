from fuzzywuzzy import fuzz
from colorama import Fore
import random
import time

kura_response = Fore.MAGENTA + "kura:" + Fore.WHITE
user_interaction = Fore.GREEN + "you: " + Fore.WHITE

available_actions = {
  "hi": ["hi", "hola"],
  "calculator": ["open calculator", "calculator", "show calculator", "calculadora"],
  "current_time": ["current time", "time", "show current time", "hora es", "hora"],
  "close": ["exit", "i want exit", "close", "salir", "adios", "chao"]
}

loading_phrases = [
  f"did you know that I have {len(available_actions)} actions you can use? ꒰ᐢ. .ᐢ꒱",
  "my name is kura, and yours? ₍ᐢ. .ᐢ₎"
]

def interpret_command(command: str):
  best_action = "unknown"
  best_score = 0

  for action, phrases in available_actions.items():
    for phrase in phrases:
      score = fuzz.ratio(command.lower(), phrase)
      
      if score > best_score:
        best_action = action
        best_score = score
  
  if best_score >= 60:
    return best_action
  
def loading():
  print(f"{kura_response} looking in my systems. {loading_phrases[random.randrange(0, len(loading_phrases))]}")
  time.sleep(0.8)