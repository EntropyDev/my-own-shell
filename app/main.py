import sys

class ExitException(Exception):
    pass

def cmd_register(cmds: dict, cmd: str):
    def decorator(func):
        cmds[cmd] = func.__name__
        return func
    return decorator

class Terminal:
    cmds = {}

    @cmd_register(cmds, "exit")
    @staticmethod
    def _exit():
        raise ExitException("Exiting")
    
    @cmd_register(cmds, "echo")
    @staticmethod
    def echo(cmd, *args):
        s = " ".join([word for word in args])+"\n"
        sys.stdout.write(s)
    
    @staticmethod
    def cmd_not_found(cmd):
        sys.stdout.write(f"{cmd}: command not found\n")

    @cmd_register(cmds, "type")
    @staticmethod
    def typeof(cmd, *args):
        type_cmd = " ".join(args)
        if type_cmd in Terminal.cmds:
            sys.stdout.write(f"{type_cmd} is a shell builtin\n")
        else:
            sys.stdout.write(f"{type_cmd}: not found\n")
    @staticmethod
    def execute(st):
        st_a = st.split(" ")
        [cmd, *args] = st_a
        
        if cmd in Terminal.cmds:
            Terminal.cmds[cmd](cmd, *args)
        else:
            Terminal.cmd_not_found(cmd)

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        cmd = input()
        try:
            Terminal().execute(cmd)
        except ExitException as e:
            return    


if __name__ == "__main__":
    main()
