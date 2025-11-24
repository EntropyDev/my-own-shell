import sys

def echo(*args):
    s = " ".join([word for word in args])+"\n"
    sys.stdout.write(s)

def validate(st):
    st_a = st.split(" ")
    [cmd, *args] = st_a
    cmds = {
        "echo": echo
    }
    if cmd in cmds:
        cmds[cmd](*args)
        return True
    return False

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        cmd = input()
        if cmd == "exit":
            return 
        if not validate(cmd):
            sys.stdout.write(f"{cmd}: command not found\n")    


if __name__ == "__main__":
    main()
