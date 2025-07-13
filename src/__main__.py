import actions
import core
from colorama import Fore

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
  while True:
    print(f"{core.kura_response} my available actions are: {str.join(', ', core.available_actions.keys())} ₍^. .^₎Ⳋ")
    
    print(f"{core.kura_response} what do you want to do?")

    command = input(f"{core.user_interaction} ").replace("kura", "")
    
    interpret = core.interpret_command(command)

    core.loading()

    if interpret == 'hi':
      actions.hi()
    elif interpret == 'calculator':
      actions.calculator()
    elif interpret == 'current_time':
      actions.current_time()
    elif interpret == 'close':
      actions.close()
    elif interpret == None:
      actions.action_not_found()

if __name__ == "__main__":
  main()

