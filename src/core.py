from fuzzywuzzy import fuzz;
from colorama import Fore

kura_response = Fore.MAGENTA + "kura:" + Fore.WHITE
user_interaction = Fore.GREEN + "you: " + Fore.WHITE

available_actions = {
  "hi": ["hi", "hola"],
  "calculator": ["open calculator", "calculator", "show calculator", "calculadora"],
  "current_time": ["current time", "time", "show current time", "hora es", "hora"],
  "close": ["exit", "i want exit", "close", "salir", "adios", "chao"]
}

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