import colorama

RED = '\u001b[31m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

# print(MAGENTA,"This will be magenta")
# print(RESET,"Hello everyone")
# print(BOLD,"Hello everyone")

def colour_print(text:str, effect:str)->None:
    """Print 'text' using ANSI sequences to changes colour

    Args:
        text (str): text to print
        effect (str): the effect we want, one of the constraints
        defined at the start of this module
    """    
    output_string = "{0}{1}{2}".format(effect,text,RESET)
    print(output_string)

colorama.init()
colour_print("HELLO WORLD",CYAN)
colour_print("HELLO WORLD",MAGENTA)
colorama.deinit()
