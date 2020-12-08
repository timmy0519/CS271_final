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
    print(BnB(p,float('inf')))
if __name__ == "__main__":
    main()
