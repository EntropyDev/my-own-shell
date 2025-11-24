import sys

def validate(cmd):
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
