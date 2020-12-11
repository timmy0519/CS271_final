from Graph import Graph

class PartialAssigned:
    cost_dict=[[]]; # Space complexity:O(2n)
    N = 0; # total number of city
    vars = []  #Space complexity: O(n)
    curStep = 0;
    currentCost = 0;
    mstcost_dict = {}
    # cost_dict: Assume cost_dict is read-only, therefore we don't copy it. Instead we pass it by reference
    # Var: 
    def __init__(self,cost_dict,N):
        self.curStep = 0
        self.currentCost = 0
        self.N = N
        self.cost_dict = cost_dict 
        self.vars = [None for i in range(N)]

    # Ting:
    # Be wary of the usage of curStep! I
    # It seems that some input is not restricted to curStep
    # We may pass in a step that is curStep+1?
    # Also, if it's curStep, we already remember it in the instance by self.curStep.
    
    def pickUnAssignedVariable(self):
        return self.curStep

    def getPossibledomain(self,step: int):
        prev = set( self.vars[i] for i in range(step) if self.vars[i] is not None)
        possibleStep = set( i for i in range(len(self.vars)))
        for p in prev:
            possibleStep.remove(p)
        defaultH = 0
        possibleStep = list(map(lambda x: [x, defaultH],list(possibleStep)))
        return possibleStep
        
    def orderedDomainValues(self,step:int):
        domain = self.getPossibledomain(step)

        if step==0:
            return domain
        
        for d in domain:
            
            H_cost = 0

            tempDomain = [i[0] for i in domain]
            if self.vars[0] is None:
                pass
            else:
                H_cost+= self.cost_dict[self.vars[self.curStep-1]][d[0]]
                tempDomain.append(self.vars[0])          
            tempDomain.sort() 

            key = '-'.join(str(x) for x in tempDomain)
            if key in self.mstcost_dict:
                H_cost = self.mstcost_dict[key]
            else:
                tempGraph = self.buildGraph(tempDomain)
                H_cost += tempGraph.KruskalMST()
                self.mstcost_dict[key] = H_cost
           
            d[1] = H_cost 
        domain.sort(key = lambda x: x[1])
        return domain

    def assignVariable(self,step: int, value: int):
        prevCost = 0
        if self.vars[step]!=None and step>0:
            prevCost = self.cost_dict[self.vars[step-1]][self.vars[step]]
        # print("assign",prevCost, self.currentCost - prevCost)
        self.vars[step] = value
        if step!=0:
            self.currentCost = self.currentCost - prevCost + self.cost_dict[self.vars[step-1]][value]
        self.curStep = step + 1

    def unassignVariable(self,step: int):
        if step>0:
            self.currentCost -= self.cost_dict[self.vars[step-1]][self.vars[step]]
            # avoid errors from float pointer calculation
            if abs(self.currentCost)<0.00001:
                self.currentCost = 0
        self.vars[step] = None
        self.curStep = step-1 

    def hasFullAssignment(self):
        return self.vars[-1] is not None

    def buildGraph(self,domain: list):
        g = Graph(domain)
        for i in range(len(domain)):
            for j in range(0, i):
                if self.cost_dict[domain[i]][domain[j]]!=float('inf') :
                    g.addEdge(domain[i], domain[j], self.cost_dict[domain[i]][domain[j]])
        return g
        
    
    