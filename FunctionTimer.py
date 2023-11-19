import time

def TimeFunction(func):
    
    def inner(*args):
        start_time = time.time()
        nArgs = len(args)
        
        if nArgs == 0:
            func()
        elif nArgs == 1:
            func(SingleArg(args))
        elif nArgs == 2:
            func(TwoArgs(args))
        elif nArgs == 3:
            func(ThreeArgs(args))
        elif nArgs == 4:
            func(FourArgs(args))
        elif nArgs > 4:
            print("Too many args, not supported")
            raise ValueError()
        
        print("Executed in: ", time.time() - start_time, func.__name__)
    return inner

def AsyncTimeFunction(func):
    async def inner(*args, **kwargs):
        start_time = time.time()
        await func(*args)
        print("Executed in:", time.time() - start_time, func.__name__, "\n")
    return inner


def SingleArg(args):
    arg = args[0]
    return arg

def TwoArgs(args):
    arg1 = args[0]
    arg2 = args[1]
    return arg1, arg2

def ThreeArgs(args):
    arg1 = args[0]
    arg2 = args[1]
    arg3 = args[2]
    return arg1, arg2, arg3

def FourArgs(args):
    arg1 = args[0]
    arg2 = args[1]
    arg3 = args[2]
    arg4 = args[3]
    return arg1, arg2, arg3, arg4
 


'''
USE:

@TimeFunction    
def main():
    print("starting")
    time.sleep(2)
    print("ending")

main()
'''