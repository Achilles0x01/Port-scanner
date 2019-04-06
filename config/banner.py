colors = {
    'ITALIC':'\033[3m',
    'BOLD':'\033[1m',
    'GREEN':'\033[92m',
    'YELLOW':'\033[1;93m',
    'RED':'\033[1;91m',
    'END':'\033[0m',
}

_banner = """
 __         __         
|_. _  _   (_  _ _  _  
| |(_||_)  __)(_(_|| ) 
      |{YELLOW}Para estudos{END}

Sistema de aprendizado para entender 
o processo de escaneamento de portas 
em rede.

""".format(**colors)


def banner():
    return(_banner)