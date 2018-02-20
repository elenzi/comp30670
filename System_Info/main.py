'''
Created on 1 Feb 2018

@author: elenalanigan
'''

import platform

def main():
    s = "Architecture: {}\nOS: {}".format(platform.architecture(),
                                         platform.system() )
    
    
    #print("OS:", platform.system())
    #print("Machine:", platform.machine())
    #print("Platform:", platform.platform())
    #print("Processor:", platform.processor())
    #print("Compiler:", platform.python_compiler())
    #return platform.platform()
    return s
if __name__ == '__main__':
    print(main())