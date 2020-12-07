import PartialAssigned
def BnB(p: PartialAssigned, Uinit: int) -> int: 
    curStep = p.pickUnAssignedVariable()
    domain = p.orderedDomainValues(curStep)
    stack = []
    # push tuple onto the stack for DFS(curStep: int, domain: list)
    stack.append((curStep,domain)) 
    bestAssignment = None
    U = Uinit
    
    #DFS
    while stack:
        curStep,domain = stack[-1]
        if domain: # not empty
            p.unassignVariable(curStep) # update currentcost
            stack.pop()
        else:
            val, h_cost = domain.pop()
            p.assignVariable(curStep,val) # update currentcost
            if  p.currentCost + h_cost >=U:
                continue
            elif p.hasFullAssignment():
                U = p.currentCost + h_cost;
                bestAssignment = p.var
            else:
                var = p.pickUnAssignedVariable()
                domain = p.orderDomainValues(curStep)
                stack.append((curStep,domain))
        return bestAssignment