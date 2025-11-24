import sys
import os

class ExitException(Exception):
    pass

def cmd_register(cmds: dict, cmd: str):
    def decorator(func):
        cmds[cmd] = func.__func__
        return func
    return decorator

class Terminal:

    cmds = {}

    @staticmethod
    def cmd_not_found(cmd):
        sys.stdout.write(f"{cmd}: command not found\n")

    @cmd_register(cmds, "exit")
    @staticmethod
    def _exit(*args, **kwargs):
        raise ExitException("Exiting")
    
    @cmd_register(cmds, "echo")
    @staticmethod
    def echo(*args, **kwargs):
        s = " ".join([word for word in args])+"\n"
        sys.stdout.write(s)

    @cmd_register(cmds, "type")
    @staticmethod
    def typeof(*args, **kwargs):
        type_cmd = " ".join(args)
        if type_cmd in Terminal.cmds:
            sys.stdout.write(f"{type_cmd} is a shell builtin\n")
        else:
            dirs = kwargs["PATH"].split(":")
            for dir in dirs:
                try:
                    for file in os.listdir(dir):
                        if file == type_cmd:
                            file_path = dir+file
                            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                                sys.stdout.write(f"{type_cmd} is {file_path}\n")
                                return
                except FileNotFoundError:
                    pass
        
            sys.stdout.write(f"{type_cmd}: not found\n")

    @staticmethod
    def execute(st, PATH):
        st_a = st.split(" ")
        [cmd, *args] = st_a
        kwargs = {
            "PATH": PATH
        }
        if cmd in Terminal.cmds:
            Terminal.cmds[cmd](*args,**kwargs)
        else:
            Terminal.cmd_not_found(cmd)

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        PATH = os.environ["PATH"]
        sys.stdout.write("$ ")
        cmd = input()
        try:
            Terminal.execute(cmd, PATH)
        except ExitException as e:
            return    


if __name__ == "__main__":
    main()
