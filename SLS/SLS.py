import random

class SLS:
    cost_dict=[[]] # Space complexity:O(2n)
    nearestNeighbors = []
    N = 0; # total number of city
    path = []
    currentCost = 0

    # cost_dict: Assume cost_dict is read-only, therefore we don't copy it. Instead we pass it by reference
    def __init__(self,cost_dict,N):
        self.nearestNeighbors = []
        self.N = N
        self.cost_dict = cost_dict
        self.currentCost = 0
        self.path = []

    def initializeState(self):
        visited = set()
        currPosition = random.randint(0, self.N-1)
        nextPosition = 0;
        for i in range(0, self.N):
            self.nearestNeighbors.append(sorted(range(len(self.cost_dict[i])), key=lambda k: self.cost_dict[i][k]))

        for i in range(1, self.N):
            self.path.append(currPosition)
            visited.add(currPosition)
            candidate = []
            for j in range(0, len(self.nearestNeighbors[currPosition])):
                if self.nearestNeighbors[currPosition][j] not in visited:
                    candidate.append(self.nearestNeighbors[currPosition][j])
                    if len(candidate)==3: break
            nextPosition = random.choice(candidate)
            self.currentCost+= self.cost_dict[currPosition][nextPosition]
            currPosition = nextPosition
            print(self.path, self.currentCost)

        self.path.append(currPosition)
        self.currentCost+= self.cost_dict[currPosition][self.path[0]]
        return self.path, self.currentCost

