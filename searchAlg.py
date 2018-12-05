class Node:
    def __init__(self,Board,parent,label):
        self.Board=Board
        self.parent=parent
        self.label=label
 
        #ilk frontierdan pop edince bu metoda girecek
        #1.Goal State check true ise path dönecek false ise childlar bulunacak
        #her bir hamle için bir  metot olacak orada board değişikliği silme ,label hesabı yapılıp, parent atanıp obje yaratılsın
   
        
    def firstBoardCheck(self,explored):
        allChildren=[]
        willCheck=self.Board
        v='X'
        for i, x in enumerate(willCheck): # get index value of 'X' to goal state check
            if v in x:
                indexes= [i, x.index(v)] 
                
        if sum(x.count('X') for x in willCheck) ==1 & indexes==[3,3]: #goal state 
            #find path in explored list
            search=self.parent
            Node.printSolo(self) #Şuanki node u bastır
            for i in range(len(explored)-1,-1,-1): #explored listesinde sondan başa doğru parentları bul ve boardlarını bastır
                if explored[i]==search:
                    Node.printSolo(explored[i])
                    print()
                    search=explored[i].parent
            
            
        else: #find children
            for row in willCheck: #her bir index için 4 tarafı kontrol edip bütün olası hamleleri dönüyor
                for item in row:
                    if (willCheck[row][item] == 'X' and (not(row ==0 or row ==1))) and  willCheck[row-1][item]=='X' and  willCheck[row-2][item]==0 : #UP check
                       start=[row,item]
                       end=[row-2,item]
                       direc='U'
                       allChildren.append( Node.createChild(self,start,end,direc))
                    if (willCheck[row][item] == 'X' and (not(item==5 or item==6))) and willCheck[row][item+1]=='X' and willCheck[row][item+2]==0: #RIGHT check
                       start=[row,item]
                       end=[row,item+2]
                       direc='R'
                       allChildren.append(Node.createChild(self,start,end,direc))
                    if (willCheck[row][item] == 'X' and (not(row==5 or row==6)))  and willCheck[row+1][item]=='X' and willCheck[row+2][item]==0:#DOWN check
                        start=[row,item]
                        end=[row+2,item]
                        direc='D'
                        allChildren.append(Node.createChild(self,start,end,direc))
                    if (willCheck[row][item] == 'X' and (not(item==0 or item==1))) and willCheck[row][item-1]=='X' and willCheck[row][item-2]==0: #LEFT check
                        start=[row,item]
                        end=[row,item-2]
                        direc='L'
                        allChildren.append(Node.createChild(self,start,end,direc))
            return allChildren
    
    
    def createChild(self,start,end,direc):
        LabelledBoard=[[-1,-1,1,2,3,-1,-1],[-1,-1,4,5,6,-1,-1],[7,8,9,10,11,12,13],
        [14,15,16,17,18,19,20],[21,22,23,24,25,26,27],[-1,-1,28,29,30,-1,-1],[-1,-1,31,32,33,-1,-1] ]
        newBoard=self.Board
        newBoard[start[0]][start[1]]=0 #başlangıç yeri 0 oldu
        newBoard[end[0]][end[1]]=1     #bitiş yeri 1 oldu
        label=LabelledBoard[start[0]][start[1]]+LabelledBoard[end[0]][end[1]]
        
        if(direc=='U'):
            newBoard[start[0]-1][start[1]]=0 #yan etki aradaki X silindi , label hesabı yap onu da ver Node un içine
            Node(newBoard,self,label)
        if (direc=='R'):
            newBoard[start[0]][start[1]+1]=0
            Node(newBoard,self,label)
        if (direc=='D'):
            newBoard[start[0]+1][start[1]]=0
            Node(newBoard,self,label)
        if(direc=='L'):
            newBoard[start[0]][start[1]-1]=0
            Node(newBoard,self,label)                        
            
      
    def printSolo(self):
        a=self.Board
        for i in range(len(a)):
            for j in range(len(a[i])):
                print(a[i][j], end=' ')
            print()
      
       
        
board=[[-1,-1,'X','X','X',-1,-1],[-1,-1,'X','X','X',-1,-1],['X','X','X','X','X','X','X'],
       ['X','X','X','0','X','X','X'],['X','X','X','X','X','X','X'],[-1,-1,'X','X','X',-1,-1],[-1,-1,'X','X','X',-1,-1] ]

board1=[[-1,-1,'X','X','X',-1,-1],[-1,-1,'X','X','X',-1,-1],['X','X','X','X','X','X','X'],
       ['X','X','X','0','X','X','X'],['X','X','0','X','X','X','X'],[-1,-1,'X','X','0',-1,-1],[-1,-1,'X','X','X',-1,-1] ]

board2=[[-1,-1,'X','X','X',-1,-1],[-1,-1,'X','X','X',-1,-1],['X','X','X',0,'X','X','X'],
       ['X','X','X','0','X','X','X'],['X','X','','X','X','X','X'],[-1,-1,'X',0,'X',-1,-1],[-1,-1,'X','X','X',-1,-1] ]

board3=[[-1,-1,'X','X','X',-1,-1],[-1,-1,'X',0,'X',-1,-1],['X','X',0,'X',0,'X','X'],
       ['X','X','X',0,'X','X','X'],['X','X','X',0,'X','X','X'],[-1,-1,'X','X',0,-1,-1],[-1,-1,'X',0,'X',-1,-1] ]


f1=Node(board,0,30)
a1=Node(board1,f1,12)
b1=Node(board2,a1,15)
c1=Node(board3,b1,17)
d1=Node(board,c1,19)
e1=Node(board1,d1,21)
explored=[a1,b1,c1,d1,e1]
search=e1.parent
#print(search.Board)
Node.printSolo(e1)
print()
for i in range(len(explored)-1,-1,-1):
    if explored[i]==search:
        Node.printSolo(explored[i])
        print(explored[i].label)
        print()
        search=explored[i].parent



a1.parent
a1.label

b1.parent
b1.label


