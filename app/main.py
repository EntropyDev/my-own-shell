import sys

def validate(cmd):
    return False

def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")
    cmd = sys.stdin.readline().strip()
    if not validate(cmd):
        sys.stdout.write(f"{cmd}: command not found")    


if __name__ == "__main__":
    main()
