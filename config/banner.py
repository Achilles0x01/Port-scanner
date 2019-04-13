colors = {
    'ITALIC':'\033[3m',
    'GREEN':'\033[92m',
    'YELLOW':'\033[1;93m',
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
