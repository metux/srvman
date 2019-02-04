
import sys

term_mode = {
    'reset':            '\033[0m',
    'bold':             '\033[1m',
    'disable':          '\033[02m',
    'italic':           '\033[3m',
    'underline':        '\033[4m',
    'blink':            '\033[5m',
    'blink2':           '\033[6m',
    'selected':         '\033[7m',
    'reverse':          '\033[7m',
    'invisible':        '\033[8m',
    'strikethrough':    '\033[9m',
    'header':           '\033[95m',
    'okblue':           '\033[94m',
    'okgreen':          '\033[92m',
    'warning':          '\033[93m',
    'fail':             '\033[91m',
    'bold':             '\033[1m',
    'underline':        '\033[4m',

}

term_textcolor = {
    'black':            '\033[30m',
    'red':              '\033[31m',
    'green':            '\033[32m',
    'orange':           '\033[33m',
    'blue':             '\033[34m',
    'purple':           '\033[35m',
    'cyan':             '\033[36m',
    'lightgrey':        '\033[37m',
    'darkgrey':         '\033[90m',
    'lightred':         '\033[91m',
    'lightgreen':       '\033[92m',
    'yellow':           '\033[93m',
    'lightblue':        '\033[94m',
    'pink':             '\033[95m',
    'lightcyan':        '\033[96m',
    'white2':           '\033[97m',
}

term_bgcolor = {
    'black':            '\033[40m',
    'red':              '\033[41m',
    'red2':             '\033[101m',
    'green':            '\033[42m',
    'green2':           '\033[102m',
    'orange':           '\033[43m',
    'yellow':           '\033[103m',
    'blue':             '\033[44m',
    'blue2':            '\033[104m',
    'purple':           '\033[45m',
    'violet':           '\033[105m',
    'cyan':             '\033[46m',
    'beige':            '\033[106m',
    'lightgrey':        '\033[47m',
    'white':            '\033[107m',
    'grey':             '\033[100m',
}

def bgcolor(name):
    write(term_bgcolor[name])

def fgcolor(name):
    write(term_textcolor[name])

def mode(name):
    write(term_mode[name])

def reset():
    write(term_mode['reset'])

def bold():
    write(term_mode['bold'])

def write(s):
    sys.stdout.write(s)
