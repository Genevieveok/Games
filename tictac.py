
class TicTacToe:
    #tictactoe game that can be played with two users or against oneself
    
    def __init__(self):
        self.value = None;
        self.position = None;
        self.arrays = ["["+str(i)+"]" for i in range(0,9)]
        self.lastval = None
        self.count =0
        
        #print array for user view along with positions
        '''
        ['[0]', '[1]', '[2]']
        ['[3]', '[4]', '[5]']
        ['[6]', '[7]', '[8]']
        '''
        a=[]
        for i in range(0,3):
            a.append(self.arrays[i])
        print(a)
        a=[]
        for i in range(3,6):
            a.append(self.arrays[i])
        print(a)
        a=[]
        for i in range(6,9):
            a.append(self.arrays[i])
        print(a)
        
    def place(self,value,position):
        
        #place value in position
        self.value = value
        self.position = position
        
 
        
        if self.value == "x":
            val = "o"
        else:
            val = "x"
                
        if self.correctvalue():
            self.lastval = self.value
        else:
            print("Please let "+str(val)+" play instead!")
            return False
        
        if self.position >= len(self.arrays):
            self.lastval = val
            print("This position is higher than the actual positions available")
            return False
        
        if self.spotavailable():
            pass
        else:
            self.lastval = val
            print("That spot has been taken, please choose another one")
            return False
    
        self.arrays[self.position] = self.value
        self.count+=1
        #print(self.arrays)
        a=[]
        for i in range(0,3):
            a.append(self.arrays[i])
        print(a)
        a=[]
        for i in range(3,6):
            a.append(self.arrays[i])
        print(a)
        a=[]
        for i in range(6,9):
            a.append(self.arrays[i])
        print(a)
        
        if self.winnerfound():
            print(self.value, "is the winner!")
            return "End"
        
        #end game 
        if self.count == 9:
            print("no more plays available")
            return "End"
        
        
    
    #check if the spot is taken by another value
    def spotavailable(self):
        
        if self.arrays[self.position] == "x" or self.arrays[self.position] == "o":
            return False
        return True
    
    #there are 8 number of combinations that determines the winner
    def winnerfound(self):
        
        if self.arrays[0]==self.value and self.arrays[1]==self.value  and self.arrays[2]==self.value :
            return True
        elif self.arrays[0]==self.value and self.arrays[3]==self.value  and self.arrays[6]==self.value :
            return True
        elif self.arrays[0]==self.value and self.arrays[4]==self.value  and self.arrays[8]==self.value :
            return True
        elif self.arrays[1]==self.value and self.arrays[4]==self.value  and self.arrays[7]==self.value :
            return True
        elif self.arrays[2]==self.value and self.arrays[5]==self.value  and self.arrays[8]==self.value :
            return True
        elif self.arrays[2]==self.value and self.arrays[4]==self.value  and self.arrays[6]==self.value :
            return True
        elif self.arrays[3]==self.value and self.arrays[4]==self.value  and self.arrays[5]==self.value :
            return True
        elif self.arrays[6]==self.value and self.arrays[7]==self.value  and self.arrays[8]==self.value :
            return True
        
        return False
        
    #check if the value played is correct in order x then o and vice versa
    #return false if the last val played is equal to the current value
    def correctvalue(self):
        #print(self.value)
        if self.lastval == self.value:
            return False
        return True
        
v = TicTacToe()
count = 9
def inputs(count):
    if count == 0:
        return "done"
    #get value and position from user
    val,position = input("Enter your value: "), input("Enter your position: ")
    
    #make sure only x and o are used as a variable
    if val !='x' and val != 'o':
        print("please use 'x' or 'o' as value")
        inputs(count)
    
    #check if position given is an interger
    
    actposition =int(position)
    '''
    try:
        actposition =int(position)
    except UnboundLocalError:
        print("unbound")
        return
    except ValueError:
        print("please use valid integer for positions")
        return
    '''
    f = v.place(val,actposition)
    #subtract number of counts if placemtn successful, else return if end has been reached
    if f == True:
        count-=1
    elif f == "End":
        return "done"
    inputs(count)
    
#callin input function
inputs(count)
