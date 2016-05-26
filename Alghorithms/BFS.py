import collections
import random
#x_in,y_in Старт x_out,y_out Финал
def BFS(x_in,y_in,x_out,y_out,Map): 
    queue = collections.deque( [(x_in,y_in,None)])
    while len(queue)>0:
        node = queue.popleft()
        x_in = node[0]
        y_in = node[1] 
        if (x_in,y_in) == (x_out,y_out):
            return Path(node)
        if (Map[x_in][y_in]!=1):
            continue 
        Map[x_in][y_in]="explored"
        for i in [[x_in-1,y_in],[x_in+1,y_in],[x_in,y_in-1],[x_in,y_in+1]]:
            queue.append((i[0],i[1],node))
    return [] 
            
def Path(node): 
    path = [] 
    while(node != None): 
        path.append((node[0],node[1])) 
        node = node[2] 
    return path 
        
def CreateMap():
    size = 0
    while(size not in range(5,11)):
        size = int(input("N(5,10) = "))
    k = int(input("k = "))
    Map = [[1]*size]*size
    print(Map)
    while(k):
        x = random.randrange(size-1)
        y = random.randrange(size-1)
        Map[x][y] = 0
        k = k-1
    return Map

def DrawMap(Map,path): 
    for x in range(0,len(Map)): 
        for y in range(0,len(Map[x])): 
            if ((x,y) in path):
                print("*",end="") 
            elif (Map[x][y]==0): 
                print(0,end="") 
            else: 
                print('1',end="") 
        print() 

        
MAP = CreateMap()
print("solved with BFS") 
print("path is ",len(BFS(1,1,3,3,MAP)," spots long") 
DrawMap(MAP,BFS(1,1,3,3,MAP))