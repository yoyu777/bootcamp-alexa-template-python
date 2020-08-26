from utils import bootcamp_builder


# Example intent

# 1. Add a custom intent - addIntent(<intent_name>)
bootcamp_builder.addIntent("hello_world")

# 2. Define a handler function 
def hello_world_intent_handler(handler_input):
    speak_output = "Hello from Python"

    return handler_input.response_builder.speak(speak_output).response

# 3. Link the handler function to the intent 
bootcamp_builder.linkHandlerFunction("hello_world",hello_world_intent_handler)

# End of the example


pass