from bnb import *
from typing import List
import argparse
def parseMatrix(filename: str,n:int ) -> List[List[int]]:
    dists = []
    try:
        with open(filename, 'r') as fp:
            f_n = fp.readline().strip()
            if n!= int(f_n):
                raise  ValueError('Error:********{0} doesn\'t match n = {1}**********'.format(f_n,n))
            
            content = fp.read()
            for line in content.strip().split('\n'):
                dists.append(list( map(float, line.strip().split()) ) )
            if len(dists)!=int(n):
                raise  ValueError('The row of input= {0} does not match {1}'.format(len(dists),n))
            for i,r in enumerate(dists):
                if len(r)!=n:
                    raise  ValueError('The number of input in row {0} = {1} does not match {2}'.format(len(r),n))
    except Exception as e:
        print(e);
    return dists

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',help="input file in the format of tsp-problem-n-k-u-v-p")
    args = parser.parse_args()

    filename = args.i
    if not filename:
        filename = 'tsp-problem-10-5-10-1-1.txt'
    n,k,u,v = map(int,filename.split('-')[2:6])
    mat = parseMatrix(filename,n)
    # error occurs
    if not mat:
        return
        
    p = PartialAssigned(mat,n)
    solution, U = BnB(p,float('inf'))
    print(solution,U)
    # test if the cost of the solution is properly calculated
    
    prev = None
    actualCost = 0
    for v in solution:
        if prev is not None:
            actualCost += mat[prev][v]
        prev = v
    actionCost += mat[prev][solution[0]]
    if abs(actualCost-U)>0.0001:
        raise Exception("The difference of actualCost and BnB is {}".format(abs(actualCost-U)))
    
if __name__ == "__main__":
    main()
