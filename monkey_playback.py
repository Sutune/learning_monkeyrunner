import sys  
from com.android.monkeyrunner import MonkeyRunner as mr  
  
CMD_MAP = {  
    'TOUCH':lambda dev,arg:dev.touch(**arg),  
    'DRAG': lambda dev,arg:dev.drag(**arg),  
    'TYPE': lambda dev,arg:dev.type(**arg),  
    'PRESS': lambda dev,arg:dev.press(**arg),  
    'WAIT': lambda dev,arg:mr.sleep(**arg)  
}  
       
def process_file(f,device):  
    for line in f:  
        (cmd,rest)=line.split('|')  
        try:  
           rest = eval(rest)  
        except:  
           print 'unable to parse options'  
           continue  
        if cmd not in CMD_MAP:  
           print 'unknown command: ' + cmd  
           continue  
        CMD_MAP[cmd](device, rest)  
		
def main():  
    file = sys.argv[1]  
    f = open(file,'r')  
    device = mr.waitForConnection()  
    process_file(f,device)  
    f.close()  

if __name__=='__main__':
	main()