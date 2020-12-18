import random
from twoOPT import *
import signal
import time as realtime

class SLS:
    cost_dict=[[]] # Space complexity:O(2n)
    nearestNeighbors = []
    N = 0; # total number of city
    best_path = []

    # cost_dict: Assume cost_dict is read-only, therefore we don't copy it. Instead we pass it by reference
    def __init__(self,cost_dict,N):
        self.nearestNeighbors = []
        self.N = N
        self.cost_dict = cost_dict
        self.currentCost = 0

    def handler(self,signum, frame):
      ("Forever is over!")
      raise Exception("end of time")

    def GRASP(self,time:int) -> int:
        signal.signal(signal.SIGALRM, self.handler)
        signal.alarm(time);
        count = 0

        
        start_position = random.randint(0, self.N-1)
        
        timeOut = False
        min_cost = float('inf')

        start_time = realtime.time()
        try:
          while (count < 50):
              subsolution ,U = self.initializeState(start_position)
              OPT = twoOPT(self.cost_dict,subsolution,U)
              subsolution ,U = OPT.local_search_2_opt()
              if U < min_cost:
                  self.best_path = subsolution
                  min_cost = U

              count += 1
        except Exception as e:
            timeOut = True
        if timeOut:
          print('Time out')
        else:
           print("Time = %.4f" % (realtime.time() - start_time))
              


        return self.best_path,min_cost
                

    def initializeState(self,start_position):
        path = []
        currentCost = 0
        visited = set()
        currPosition = random.randint(0, self.N-1)
        nextPosition = 0;
        currentCost = 0
        if len(self.nearestNeighbors) == 0:
            for i in range(0, self.N):
              self.nearestNeighbors.append(sorted(range(len(self.cost_dict[i])), key=lambda k: self.cost_dict[i][k]))

        for i in range(1, self.N):
            path.append(currPosition)
            visited.add(currPosition)
            candidate = []
            for j in range(0, len(self.nearestNeighbors[currPosition])):
                if self.nearestNeighbors[currPosition][j] not in visited:
                    candidate.append(self.nearestNeighbors[currPosition][j])
                    if len(candidate)== 5: break
            nextPosition = random.choice(candidate)
            currentCost+= self.cost_dict[currPosition][nextPosition]
            currPosition = nextPosition
            

        path.append(currPosition)
        currentCost+= self.cost_dict[currPosition][path[0]]
        
        path.append(path[0])
        
        
        return path, currentCost

