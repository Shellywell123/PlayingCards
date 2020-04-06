


def run(text_input):
    import sys
    import StringIO
    f1 = sys.stdin
    f = StringIO.StringIO(text_input) # <-- HERE
    sys.stdin = f
    f.close()
    sys.stdin = f1


def start(text_input):
    import sys
    import StringIO
    f1 = sys.stdin
    f = StringIO.StringIO(text_input) # <-- HERE
    sys.stdin = f
    import play
    f.close()
    sys.stdin = f1


start('25')
run('h')