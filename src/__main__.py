import actions
import core
from colorama import Fore
import webbrowser
import yt_dlp

import speech_recognition as sr

def main():
  print(Fore.YELLOW + 
"""

.-. .-')              _  .-')     ('-.     
\  ( OO )            ( \( -O )   ( OO ).-. 
,--. ,--. ,--. ,--.   ,------.   / . --. / 
|  .'   / |  | |  |   |   /`. '  | \-.  \  
|      /, |  | | .-') |  /  | |.-'-'  |  | 
|     ' _)|  |_|( OO )|  |_.' | \| |_.'  | 
|  .   \  |  | | `-' /|  .  '.'  |  .-.  | 
|  |\   \('  '-'(_.-' |  |\  \   |  | |  | 
`--' '--'  `-----'    `--' '--'  `--' `--' 

                     kura ai agent v.1.0.0
""")
  mode = None
  voiceLanguage = None

  # Select mode
  while mode == None:
    modesKeys = core.available_modes.keys()

    print(f"{core.kura_response} select a mode to interact with me: ")
    
    for key, value in core.available_modes.items():
      print(f"{core.kura_response}" + Fore.YELLOW + f" [{key}]:" + Fore.WHITE + f" {value}")
    
    selectMode = input(f"{core.user_interaction} ")

    if selectMode not in modesKeys:
      print(f"{core.kura_response}" + Fore.RED + " the mode you entered is incorrect (ó﹏ò｡)")
      continue
    
    mode = selectMode
    print(f"{core.kura_response} you selected to interact with me, using the mode" + Fore.YELLOW + f" [{mode}]" + Fore.WHITE)

  # Select voice language
  while mode == "voice" and voiceLanguage == None:
    modesKeys = core.available_languages.keys()

    print(f"{core.kura_response} select a language to communicate with me")
    
    for key, value in core.available_languages.items():
      print(f"{core.kura_response}" + Fore.YELLOW + f" [{key}]:" + Fore.WHITE + f" {value}")
    
    selectMode = input(f"{core.user_interaction} ")

    if selectMode not in modesKeys:
      print(f"{core.kura_response}" + Fore.RED + " the language you entered is incorrect (ó﹏ò｡)")
      continue
    
    voiceLanguage = selectMode
    print(f"{core.kura_response} you have selected to communicate with me in " + Fore.YELLOW + f" [{mode}]" + Fore.WHITE)
    

  # Menu
  while True:
    print(f"{core.kura_response} my available actions are:" + Fore.YELLOW + f" {str.join(', ', core.available_actions.keys())}" + Fore.WHITE + " ₍^. .^₎Ⳋ")

    print(f"{core.kura_response} what do you want to do?")
    
    command = None

    if mode == "keyboard":
      command = input(f"{core.user_interaction} ").replace("kura", "")
    elif mode == "voice":
      r = sr.Recognizer()

      with sr.Microphone() as source:
        print(f"{core.kura_response} i'm listening... ₍^. .^₎⟆")

        r.adjust_for_ambient_noise(source)

        try:
          audio = r.listen(source, timeout=5)
          command = r.recognize_google(audio, language=voiceLanguage)

          print(f"{core.kura_response} you said: {command} (๑'ᵕ'๑)⸝*")
        except sr.WaitTimeoutError:
            print(f"{core.kura_response} i didn't hear anything. try again. (•︠‿•︡)")
        except sr.UnknownValueError:
            print(f"{core.kura_response} sorry, i could not understand you. (・・ )")
        except sr.RequestError as e:
            print(f"{core.kura_response} could not request results; {e}")

    if command is not None:
      interpret = core.interpret_command(command)

      core.loading()

      if interpret == 'hi':
        actions.hi()
      elif interpret == 'calculator':
        actions.calculator()
      elif interpret == 'spotify':
        actions.spotify()
      elif interpret == 'search_on_youtube':
        actions.search_on_youtube(command)
      elif interpret == 'current_time':
        actions.current_time()
      elif interpret == 'close':
        actions.close()
      elif interpret == None:
        actions.action_not_found()

if __name__ == "__main__":
  main()

