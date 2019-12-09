import os
import sys
import argparse

class Southeros:
    def __init__(self):
        self.ruler = 'None'
        self.allies = []
        
    def setRuler(self, kingdom ):
        kings = {'space':'King Shan'}
        if len(self.allies ) > 2 :
            self.ruler = kings[ kingdom ]
        else:
            self.ruler = 'None'
    
    def getRuler(self ):
        print( self.ruler )
    
    def getAllies( self ):
        if len( self.allies ) < 3 :
            print('None')
        else:
            print( ', '.join( self.allies ) )
            
    def sendMsg(self, msg, sender = 'space'):
        validMsg = {
           'air':{'o':1, 'w':1, 'l':1},
           'land': {'p':1, 'a':2,'d':1},
           'water': {'o':2, 'c':1, 'p':1, 'u':1, 's':1 },
           'ice': {'m':3, 'a':1, 'o':1, 't':1, 'h':1},
           'fire': {'d':1, 'r':1, 'a':1, 'g':1, 'o':1, 'n' :1 },
           'space': {'g':1, 'o':1, 'r':1, 'i':1, 'l':2, 'a' :1}
        }
        msg = msg.strip().split(',', 1)
        ruler = msg[0].strip()
        if ruler == sender :
            return
            
        secretCode = validMsg.get( ruler.lower(), None )
        if secretCode is None:
            print('no secretCode')
            return
        
        isAlly = True
        for char in secretCode:
            if msg[1].lower().count( char ) != secretCode[ char ]:
                isAlly = False
                break
        if isAlly and ruler not in self.allies:
            self.allies.append( ruler )
            
        self.setRuler( sender )
        
      
def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 
        
def fnRest( obj ):
    obj.ruler = 'None'
    obj.allies = []
        
def fnInitiate( obj ):
    print('''
    
1. Find Ruler
2. Find Allies
3. Send Msg ( paste, if multiline add quit at last )
4. Send Msg ( enter file path )
9. Reset
0. Exit

''')
    ch = input('Enter Choice: ')
    clear()
    if ch == '0':
        return False
    elif ch == '9':
        fnRest( obj )
    elif ch == '1':
        obj.getRuler()
    elif ch == '2':
        obj.getAllies()
    elif ch == '3':
        while True:
            line = sys.stdin.readline().rstrip('\n')
            if line == 'quit':
                print('Input Completed')
                break
            else:
                obj.sendMsg( line )
                
    elif ch == '4':
        filePath = input('Enter File Path: ' )
        fnReadFile( filePath, obj )
        
def fnReadFile( filePath, obj ):
        if not os.path.exists( filePath ):
            print('File Does Not Exist')
        else:
            with open( filePath, 'r' ) as fr :
                for line in fr:
                    obj.sendMsg( line )
            print('Input Completed')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments passed')
    parser.add_argument('-f', '--file', action="store", default='')
    args = parser.parse_args()
    file = args.file.strip()
    
    clear()
    toRun = 1
    obj = Southeros()
    
    if file != '':
        fnReadFile(file, obj )
        obj.getRuler()
        obj.getAllies()
    
    while toRun != False:
        fnInitiate( obj )

        
        
        
        
        
        
        