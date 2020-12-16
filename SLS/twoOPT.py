class twoOPT:
    
    cost_dict=[[]] # Space complexity:O(2n)
    N = 0; # total number of city
    best_path = []
    bestCost = 0 
    
    def __init__(self,cost_dict,bestPath,bestCost):
        self.cost_dict = cost_dict
        self.bestPath = bestPath
        self.bestCost = bestCost

    def dist(self,c1, c2):
        return self.cost_dict[c1][c2]

    def local_search_2_opt(self):
      swaps = 1
      iteration_count = 0
      
      while (swaps != 0 and iteration_count < 100): # loop until no improvements can be made or reach Max iteration limit (100 in our case)
        swaps = 0
        minChange = 0
        mini = 0
        mink = 0
        for i in range(1,len(self.bestPath) - 2):
          for j in range(i + 1, len(self.bestPath) - 1):                            # consider all possible arc swaps
            change = self.dist(self.bestPath[i - 1],self.bestPath[j]) + self.dist(self.bestPath[i], self.bestPath[j + 1])- self.dist(self.bestPath[i - 1],self.bestPath[i]) - self.dist(self.bestPath[j],self.bestPath[j + 1])
            if (change < minChange):                                                # if there is improvement we can swap
                swaps = 1                                                        
                minChange = change
                mini = i
                minj = j
        if (swaps == 1):
          self.bestPath = self.bestPath[:mini] + list(reversed(self.bestPath[mini:minj + 1])) + self.bestPath[minj + 1:]
          self.bestCost = self.bestCost + minChange
          
        iteration_count += 1;    
        
      return self.bestPath,self.bestCost


    

    
        
 
        
