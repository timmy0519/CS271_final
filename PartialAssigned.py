class PartialAssigned:
    cost_dict=[[]]; # Space complexity:O(2n)
    N = 0; # total number of city
    vars = []  #Space complexity: O(n)
    curStep = 0;
    currentCost = 0;
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
    def getPossibledomain(self,curStep: int):
        return set( i for i,v in enumerate(self.vars[:curStep]) if v is not None)
    def orderedDomainValues(self,curStep:int):
        pass
    def assignVariable(self,curStep: int, value: int):
        self.vars[curStep] = value
        self.currentCost += self.cost_dict[self.vars[curStep-1]][value]
        self.curStep+=1

    def unassignVariable(self,curStep: int):
        self.var[cuStep] = NULL
        self.currentCost -= self.cost_dict[var(Curstep-1)][var(Curstep)]
        self.curStep-=1

    def hasFullAssignment(self):
        return self.vars[-1] is not None
    def buildGraph(self,domain: list):
        pass
        
    
    