import actions
import core
from colorama import Fore

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
  # Load configuration
  config = core.load_config()

  username = config["username"]
  mode = config["mode"]
  voice_language = config["voice_language"]

  # Select username
  while username == "":
    print(f"{core.kura_response} what should i call you? ᓚ₍⑅^..^₎")
    username = input(f"{core.user_interaction} ")

    print(f"{core.kura_response} nice to meet you" + Fore.YELLOW + f" {username}" + Fore.WHITE + " ᓚ₍⑅^..^₎♡ !!!")

  # Select mode
  while mode == "":
    modes_keys = core.available_modes.keys()

    print(f"{core.kura_response} select a mode to interact with me, {username}: ")
    
    for key, value in core.available_modes.items():
      print(f"{core.kura_response}" + Fore.YELLOW + f" [{key}]:" + Fore.WHITE + f" {value}")
    
    selected_mode = input(f"{core.user_interaction} ")

    if selected_mode not in modes_keys:
      print(f"{core.kura_response}" + Fore.RED + " the mode you entered is incorrect (ó﹏ò｡)")
      continue
    
    mode = selected_mode
    print(f"{core.kura_response} you selected to interact with me, using the mode" + Fore.YELLOW + f" [{mode}]" + Fore.WHITE)

  # Select voice language
  while mode == "voice" and voice_language == "":
    voice_language_keys = core.available_languages.keys()

    print(f"{core.kura_response} select a language to communicate with me, {username}")
    
    for key, value in core.available_languages.items():
      print(f"{core.kura_response}" + Fore.YELLOW + f" [{key}]:" + Fore.WHITE + f" {value}")
    
    selected_voice_language = input(f"{core.user_interaction} ")

    if selected_voice_language not in voice_language_keys:
      print(f"{core.kura_response}" + Fore.RED + " the language you entered is incorrect (ó﹏ò｡)")
      continue
    
    voice_language = selected_voice_language
    print(f"{core.kura_response} you have selected to communicate with me in " + Fore.YELLOW + f" [{voice_language}]" + Fore.WHITE)
    
  # Automatic configuration save
  if config["username"] is not username or config["mode"] is not mode or config["voice_language"] is not voice_language:
    config["username"] = username
    config["mode"] = mode
    config["voice_language"] = voice_language
    
    core.save_config(config=config)
    
    print(f"{core.kura_response}" + Fore.BLUE + " i noticed that you set some of my settings, so i've saved it for you for next time ₍ᐢ. .ᐢ₎ ₊˚⊹♡ !!!! " + Fore.WHITE)

  # Welcome
  print(f"{core.kura_response} welcome, {username} ₍^. .^₎⟆")

  # Menu    
  while True:
    print(f"{core.kura_response} my available actions are:" + Fore.YELLOW + f" {str.join(', ', core.available_actions.keys())}" + Fore.WHITE + " ₍^. .^₎Ⳋ")

    print(f"{core.kura_response} what do you want to do, {username}?")
    
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
          command = r.recognize_google(audio, language=voice_language)

          print(f"{core.kura_response} you said:" + Fore.BLUE + f" {command} (๑'ᵕ'๑)⸝*")
        except sr.WaitTimeoutError:
            print(f"{core.kura_response}" + Fore.RED +  " i didn't hear anything. try again. (•︠‿•︡)")
        except sr.UnknownValueError:
            print(f"{core.kura_response}" + Fore.RED +  " sorry, i could not understand you. (・・ )")
        except sr.RequestError as e:
            print(f"{core.kura_response}" + Fore.RED +  " could not request results; {e}")

    if command is not None:
      interpret = core.interpret_command(command)

      core.loading()

      if interpret == 'hi':
        actions.hi(username=username)
      elif interpret == 'calculator':
        actions.calculator()
      elif interpret == 'spotify':
        actions.spotify()
      elif interpret == 'search_on_youtube':
        actions.search_on_youtube(query=command)
      elif interpret == 'current_time':
        actions.current_time()
      elif interpret == 'close':
        actions.close(username=username)
      elif interpret == None:
        actions.action_not_found()

if __name__ == "__main__":
  main()

