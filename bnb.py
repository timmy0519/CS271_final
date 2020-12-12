import signal
from PartialAssigned import PartialAssigned
def handler(signum, frame):
    ("Forever is over!")
    raise Exception("end of time")

def BnB(p: PartialAssigned, Uinit: int, time: int) -> int: 
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time);
    bestAssignment = None
    U = Uinit

    try:
        curStep = p.pickUnAssignedVariable()
        domain = p.orderedDomainValues(curStep)
        stack = []
        # push tuple onto the stack for DFS(curStep: int, domain: list)
        stack.append((curStep,domain)) 
        
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
                if p.hasFullAssignment():
                    lastEdge = p.cost_dict[p.vars[-1]][p.vars[0]]
                    if p.currentCost + lastEdge >=U:
                        continue
                    else:
                        U = p.currentCost + lastEdge;
                        bestAssignment = list(p.vars)
                else:
                    if  p.currentCost + h_cost >=U:
                        continue
                    # elif p.hasFullAssignment():
                    #     U = p.currentCost + h_cost;
                    #     bestAssignment = list(p.vars)
                    else:
                        var = p.pickUnAssignedVariable()
                        domain = p.orderedDomainValues(step+1)
                        stack.append((step+1,domain))
        # print(bestAssignment,">>")
    except Exception as e:
        print("time out")
    
    return bestAssignment, U