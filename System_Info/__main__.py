'''
Created on 1 Feb 2018

@author: elenalanigan
'''

import platform

def main():
    print("Architecture:", platform.architecture())
    print("OS:", platform.system())
    print("Machine:", platform.machine())
    print("Platform:", platform.platform())
    print("Processor:", platform.processor())
    print("Compiler:", platform.python_compiler())
    return
    
if __name__ == '__main__':
    main()