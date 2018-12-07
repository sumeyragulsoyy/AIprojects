from random import shuffle
import copy
class Node:
    def __init__(self,Board,parent,label,depth):
        self.Board=Board
        self.parent=parent
        self.label=label
        self.depth=depth
        #ilk frontierdan pop edince bu metoda girecek
        #1.Goal State check true ise path dönecek false ise childlar bulunacak
        #her bir hamle için bir  metot olacak orada board değişikliği silme ,label hesabı yapılıp, parent atanıp obje yaratılsın
    
    def IDS_goal_check(self):
        Isgoal=0
        willCheck=self.Board
        v='X'
        cnt=0
        Is_one=0
        indexes=[0,0]
        for m in range(len(willCheck)): #X number should be 1 on the board fro goal state
            for n in range(len(willCheck)):
                if willCheck[m][n] =='X':
                    cnt +=1
 #sum(x.count('X') for x in willCheck)                
        if cnt == 1:
            for i, x in enumerate(willCheck): # get index value of 'X' to goal state check
                if v in x:
                    indexes= [i, x.index(v)]
            print(indexes)
            Is_one=1
            print("sel")
        if (Is_one == 1) & (indexes[0] == 3) & (indexes[1] == 3): #goal state 
            #find path in memory
            print("heyyo")
            search=self
            while search.parent !=0:
                Node.printSolo(search)
                print(search.label)
                print()
                search=search.parent
            Node.printSolo(search)
            print(search.label)
            Isgoal=1
            
        return Isgoal
    
    def firstBoardCheck(self):
        allChildren=[]
        Isgoal=0
        willCheck=self.Board
        v='X'
        cnt=0
        Is_one=0
        indexes=[0,0]
        for m in range(len(willCheck)): #X number should be 1 on the board fro goal state
            for n in range(len(willCheck)):
                if willCheck[m][n] =='X':
                    cnt +=1
 #sum(x.count('X') for x in willCheck)                
        if cnt == 1:
            for i, x in enumerate(willCheck): # get index value of 'X' to goal state check
                if v in x:
                    indexes= [i, x.index(v)]
            print(indexes)
            Is_one=1
            print("sel")
        if (Is_one == 1) & (indexes[0] == 3) & (indexes[1] == 3): #goal state 
            #find path in memory
            print("heyyo")
            search=self
            while search.parent !=0:
                Node.printSolo(search)
                print(search.label)
                print()
                search=search.parent
            Node.printSolo(search)
            print(search.label)
            Isgoal=1
            return Isgoal,allChildren
            
        else: #find children
            for row in range(7): #her bir index için 4 tarafı kontrol edip bütün olası hamleleri dönüyor
                for item in range(7):
                    if ((willCheck[row][item] == 'X' and (not(row ==0 or row ==1))) and  willCheck[row-1][item]=='X' and  willCheck[row-2][item]==0) : #UP check
                       start=[row,item]
                       end=[row-2,item]
                       direc='U'                      
                       allChildren.append( Node.createChild(self,start,end,direc))
                    if ((willCheck[row][item] == 'X' and (not(item==5 or item==6))) and willCheck[row][item+1]=='X' and willCheck[row][item+2]==0): #RIGHT check
                       start=[row,item]
                       end=[row,item+2]
                       direc='R'                       
                       allChildren.append(Node.createChild(self,start,end,direc))
                    if ((willCheck[row][item] == 'X' and (not(row==5 or row==6)))  and willCheck[row+1][item]=='X' and willCheck[row+2][item]==0):         
                        start=[row,item]
                        end=[row+2,item]
                        direc='D'                        
                        allChildren.append(Node.createChild(self,start,end,direc))
                    if ((willCheck[row][item] == 'X' and (not(item==0 or item==1))) and willCheck[row][item-1]=='X' and willCheck[row][item-2]==0): #LEFT check
                        start=[row,item]
                        end=[row,item-2]
                        direc='L'                        
                        allChildren.append(Node.createChild(self,start,end,direc))
            print(indexes)
            print(allChildren)
            print("hello")
            return Isgoal,allChildren
    
    
    def createChild(self,start,end,direc):
        LabelledBoard=[[-1,-1,1,2,3,-1,-1],[-1,-1,4,5,6,-1,-1],[7,8,9,10,11,12,13],
        [14,15,16,17,18,19,20],[21,22,23,24,25,26,27],[-1,-1,28,29,30,-1,-1],[-1,-1,31,32,33,-1,-1] ]
        changed=copy.deepcopy(self.Board) #take basis board
        Depth=self.depth
        changed[start[0]][start[1]]=0 #başlangıç yeri 0 oldu
        changed[end[0]][end[1]]='X'   #bitiş yeri 1 oldu
        label=LabelledBoard[start[0]][start[1]]+LabelledBoard[end[0]][end[1]]
        
        if(direc=='U'):
            changed[start[0]-1][start[1]]=0 #yan etki aradaki X silindi , label hesabı yap onu da ver Node un içine
            return Node(changed,self,label,Depth+1)
        if (direc=='R'):
            changed[start[0]][start[1]+1]=0
            return Node(changed,self,label,Depth+1)
        if (direc=='D'):
            changed[start[0]+1][start[1]]=0
            return Node(changed,self,label,Depth+1)
        if(direc=='L'):
            changed[start[0]][start[1]-1]=0
            return Node(changed,self,label,Depth+1)                        
            
      
    def printSolo(self):
        a=self.Board
        for i in range(len(a)):
            for j in range(len(a[i])):
                print(a[i][j], end=' ')
            print()
      
    def bfs(self):
        expandedNodeNum=0
        frontier=[]
        frontier.append(self) #frontier initialization with root
        #print(frontier[0].Board)
        while len(frontier) !=0: #bakılacak node lar var ve çözüm onların birinde olabilir 
            leaf=frontier[0] #will remove frontier and test it for goal state after that it's not goal ,find child add frontier 
            Isgoal,children=Node.firstBoardCheck(leaf) # return all different states(hamleler), boşta dönebilir hamle bulamamıştır
            #print(Isgoal)
            #print(children)
            if Isgoal==1:
                frontier.pop(0)
                expandedNodeNum +=1
                break
            elif len(children) !=0: #hamleleri labela göre sortla ve frontiera koy
                children_list = sorted(children, key=lambda Node: Node.label) #sorted according to label
                #print(children_list)
                frontier.pop(0) # expanded node removed from frontier
                #print(frontier)
                expandedNodeNum +=1
                for i in range(len(children_list)): # sortlanmış değerlere göre en küçüğü ilk sıraya koydum
                    frontier.append(children_list[i])
                #print(frontier)
            else:
                frontier.pop(0) #eğer board da hamle yapamıyorsak hiç o node u frontierdan çıkarıp explored a ekleyip devam ediyoruz aramaya
                print("burası")
                expandedNodeNum +=1
        print(Isgoal)
        return print(expandedNodeNum)

        
    def dfs(self):
        expandedNodeNum=0
        frontier=[]
        frontier.append(self) #frontier initialization with root
        while len(frontier) !=0: #bakılacak node lar var ve çözüm onların birinde olabilir 
            leaf =frontier[-1] #frontier son eleman expand edilecek
            Isgoal,children=Node.firstBoardCheck(leaf)
            if Isgoal==1:
                frontier.pop(-1)
                expandedNodeNum +=1
                break
            elif len(children) !=0: #hamleleri labela göre sortla ve frontiera koy
                children_list = sorted(children, key=lambda Node: Node.label) #sorted according to label
                reverseList=[]
                for i in range(len(children_list)):
                    reverseList.append(children_list[len(children_list)-1-i]) #for smallest element at the end of list
                frontier.pop(-1) #last element of frontier that is expanded is removed from frontier
                expandedNodeNum +=1
                for j in range(len(reverseList)): #reverse list like that {5,4,3,2,1}
                    frontier.append(reverseList[j])
                
            else:
                frontier.pop(-1)
                expandedNodeNum +=1
        return print(expandedNodeNum)        
    
    def dfs_normal(self):
        expandedNodeNum=0
        frontier=[]
        frontier.append(self) #frontier initialization with root
        while len(frontier) !=0: #bakılacak node lar var ve çözüm onların birinde olabilir 
            leaf =frontier[-1] #frontier son eleman expand edilecek
            Isgoal,children=Node.firstBoardCheck(leaf)
            if Isgoal==1:
                frontier.pop(-1)
                expandedNodeNum +=1
                break
            elif len(children) !=0: #hamleleri labela göre sortla ve frontiera koy
                frontier.pop(-1) #last element of frontier that is expanded is removed from frontier
                expandedNodeNum +=1
                for j in range(len(children)): #reverse list like that {5,4,3,2,1}
                    frontier.append(children)
                
            else:
                frontier.pop(-1)
                expandedNodeNum +=1
        return print(expandedNodeNum)        
        

                
    def IDS(self):
        limit=0
        expandedNodeNum=0
        while limit<=32 :
            explored=[] #to delete tree for each limit and begin from root
            frontier=[] #every limit frontier will be initialized again
            frontier.append(self)
            while len(frontier)!=0: 
                leaf=frontier[-1] # take element from frontier
                if leaf.depth ==limit: #if node is on limit
                    Isgoal=Node.IDS_goal_check(leaf) # eğer goal state ise print edecek değilse
                    expandedNodeNum +=1
                    if leaf.parent !=0: #if leaf is not root
                        explored.append(leaf) # to delete tree It is necessary
                    if Isgoal==1:
                        #frontier.pop(leaf)
                        break
                elif leaf.depth < limit:
                    Is_goal,children=Node.firstBoardCheck(leaf)
                    if Is_goal ==1:
                        frontier.pop(-1)
                        expandedNodeNum +=1
                        break
                    elif len(children) !=0: #hamleleri labela göre sortla ve frontiera koy
                        children_list = sorted(children, key=lambda Node: Node.label) #sorted according to label
                        reverseList=[]
                        for i in range(len(children_list)):
                            reverseList.append(children_list[len(children_list)-1-i]) #for smallest element at the end of list
                        frontier.pop(-1) #last element of frontier that is expanded is removed from frontier
                        expandedNodeNum +=1
                        for j in range(len(reverseList)): #reverse list like that {5,4,3,2,1}
                            frontier.append(reverseList[j])
                        explored.append(leaf)
                    else:
                        frontier.pop(-1)
                        explored.append(leaf) # to delete this node at the end of this limit
                        expandedNodeNum +=1
            limit +=1
            #delete this tree at this limit
            if Isgoal==0 or Is_goal==0:
                for z in range(len(explored)):
                    explored[z].parent=-1 #ağacı sildim
                
                
                
    def dfs_randomSel(self):
        expandedNodeNum=0
        frontier=[]
        frontier.append(self) #frontier initialization with root
        while len(frontier) !=0: #bakılacak node lar var ve çözüm onların birinde olabilir 
            leaf =frontier[-1] #frontier son eleman expand edilecek
            Isgoal,children=Node.firstBoardCheck(leaf)
            if Isgoal==1:
                frontier.pop(-1)
                expandedNodeNum +=1
                break
            elif len(children) !=0: #hamleleri labela göre sortla ve frontiera koy
                shuffle(children) #random order for selection
                frontier.pop(-1) #last element of frontier that is expanded is removed from frontier
                expandedNodeNum +=1
                for j in range(len(children)): # put frontier with random ordered children
                    frontier.append(children[j]) 
                
            else:
                frontier.pop(-1)
                expandedNodeNum +=1
                
        return print(expandedNodeNum) 
    
              
board=[[-1,-1,'X','X','X',-1,-1],[-1,-1,'X','X','X',-1,-1],['X','X','X','X','X','X','X'],
       ['X','X','X',0,'X','X','X'],['X','X','X','X','X','X','X'],[-1,-1,'X','X','X',-1,-1],[-1,-1,'X','X','X',-1,-1] ]

test1=[[-1,-1,0,0,0,-1,-1],[-1,-1,0,'X',0,-1,-1],[0,0,0,'X',0,0,0],
       [0,'X','X',0,'X','X',0],[0,0,0,'X',0,0,0],[-1,-1,0,'X',0,-1,-1],[-1,-1,0,0,0,-1,-1] ]

test2=[[-1,-1,0,0,0,-1,-1],[-1,-1,0,'X',0,-1,-1],[0,0,0,'X',0,0,0],
       [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1] ]

test3=[[-1,-1,0,0,0,-1,-1],[-1,-1,0,'X',0,-1,-1],[0,0,0,'X',0,0,0],
       [0,0,0,0,'X','X',0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1] ]


board1=[[-1,-1,'X','X','X',-1,-1],[-1,-1,'X','X','X',-1,-1],['X','X','X','X','X','X','X'],
       ['X','X','X','0','X','X','X'],['X','X','0','X','X','X','X'],[-1,-1,'X','X','0',-1,-1],[-1,-1,'X','X','X',-1,-1] ]

board2=[[-1,-1,'X','X','X',-1,-1],[-1,-1,'X','X','X',-1,-1],['X','X','X',0,'X','X','X'],
       ['X','X','X','0','X','X','X'],['X','X','','X','X','X','X'],[-1,-1,'X',0,'X',-1,-1],[-1,-1,'X','X','X',-1,-1] ]

board3=[[-1,-1,'X','X','X',-1,-1],[-1,-1,'X',0,'X',-1,-1],['X','X',0,'X',0,'X','X'],
       ['X','X','X',0,'X','X','X'],['X','X','X',0,'X','X','X'],[-1,-1,'X','X',0,-1,-1],[-1,-1,'X',0,'X',-1,-1] ]

test4=[[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],[0,'X','X',0,0,0,0],[-1,-1,0,'X',0,-1,-1],[-1,-1,0,0,0,-1,-1] ]


s1=Node(board,0,0,0)
Node.bfs(s1)
g,child=Node.firstBoardCheck(s1)
Node.dfs(s1)
Node.IDS(s1)
Node.dfs_randomSel(s1)
Node.dfs_normal(s1)


print(child)
f1=Node(board,0,30,1)
dd1=Node(board,0,40,1)
f1=Node(board,0,30,1)
a1=Node(board1,f1,12,2)
b1=Node(board2,a1,15,3)
c1=Node(board3,0,17,4)
d1=Node(board,c1,19,5)
e1=Node(board1,d1,21,6)
explored=[a1,b1,c1,d1,e1]
search=e1
start=[4,0]
end=[4,2]
direc='R'
sum=Node.createChild(s1,start,end,direc)

#print(search.Board)
Node.printSolo(e1)
print()
for i in range(len(explored)-1,-1,-1):
    if explored[i]==search:
        Node.printSolo(explored[i])
        print(explored[i].label)
        print()
        search=explored[i].parent

while search.parent !=0:
    Node.printSolo(search)
    print(search.label)
    print()
    search=search.parent
Node.printSolo(search)
print(search.label)

a1.parent
a1.label

b1.parent
b1.label







