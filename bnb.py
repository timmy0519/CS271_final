from PartialAssigned import PartialAssigned
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
        step,domain = stack[-1]
        if not domain: # not empty
            p.unassignVariable(step) # update currentcost
            stack.pop()
        else:
            val, h_cost = domain.pop()
            p.assignVariable(step,val) # update currentcost
            # print(p.vars,p.currentCost)
            if p.currentCost<0:
                raise ValueError("negative current cost {}".format(p.currentCost))
            if  p.currentCost + h_cost >=U:
                continue
            elif p.hasFullAssignment():
                U = p.currentCost + h_cost;
                bestAssignment = list(p.vars)
            else:
                var = p.pickUnAssignedVariable()
                domain = p.orderedDomainValues(p.curStep)
                stack.append((p.curStep,domain))
    # print(bestAssignment,">>")
    return bestAssignment, U