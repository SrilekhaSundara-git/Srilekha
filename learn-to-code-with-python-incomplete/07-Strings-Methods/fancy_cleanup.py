# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurrence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).

def fancy_cleanup(param):
    param = param.strip()
    param = param.replace('g','z')
    param = param.replace(" ","!")
    return param
#
fancy_cleanup("       geronimo crikey  ")   #=> "zeronimo!crikey"
# fancy_cleanup("       nonsense  ")          => "nonsense"
# fancy_cleanup("grade")                      => "zrade"