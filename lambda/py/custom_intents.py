# Import dependencies

from random import randint
from utils import bootcamp_builder
from ask_sdk_core.utils.request_util import get_slot_value

# Example intent

# 1. Declare a custom intent - addIntent(<intent_name>)
bootcamp_builder.addIntent("hello_world")

# 2. Define a handler function 
def hello_world_intent_handler(handler_input):
    speak_output = "Hello from Python"

    return handler_input.response_builder.speak(speak_output).response

# 3. Link the handler function to the intent 
bootcamp_builder.linkHandlerFunction("hello_world",hello_world_intent_handler)

# End of the example

bootcamp_builder.addIntent("play")

def play_intent_handler(handler_input):
   

    guestures=["rock", "paper", "scissors"]
    index_max=len(guestures)-1
    
    # Get any existing attributes from the incoming request
    session_attributes = handler_input.attributes_manager.session_attributes
    
    # Initialise the player_wins and computer_wins attributes if not existing
    if not ("player_wins" in session_attributes):
        session_attributes["player_wins"]=0
    
    if not ("computer_wins" in session_attributes):
        session_attributes["computer_wins"]=0
        
        
    player=get_slot_value(handler_input,"sign")

    player=player.lower()
    player_int=guestures.index(player)
    
    computer_int=randint(0,index_max)
    computer=guestures[computer_int]
    
    speak_output="You played %s, " %(player)
    speak_output+="and the computer played %s. " % (computer)
    
    if player_int==computer_int+1:
        speak_output+="You win! "
        session_attributes["player_wins"]+=1
    elif player_int==0 and computer_int==index_max:
        speak_output+="You win! "
        session_attributes["player_wins"]+=1
    elif computer_int==player_int+1:
        speak_output+="You lose. "
        session_attributes["computer_wins"]+=1
    elif computer_int==0 and player_int==index_max:
        speak_output+="You lose. "
        session_attributes["computer_wins"]+=1
    else:
        speak_output+="It's a tie. "
    
    speak_output+="%s to %s" %(session_attributes["player_wins"],session_attributes["computer_wins"])
    
    return handler_input.response_builder.speak(speak_output).ask("What will you play next?").response

# 3. Link the handler function to the intent 
bootcamp_builder.linkHandlerFunction("play",play_intent_handler)

pass