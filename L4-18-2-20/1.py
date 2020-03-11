from apyori import apriori
import pyfpgrowth
import numpy as np
import time

"""
chess_data=[i.strip().split() for i in open("chess.dat").readlines()]
connect_data=[i.strip().split() for i in open("connect.dat").readlines()]
mushroom_data=[i.strip().split() for i in open("mushroom.dat").readlines()]
print(len(chess_data),len(connect_data),len(mushroom_data))

"""

transactions1 = [[1, 2, 5],
                [2, 4],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [1, 2, 3, 5],
                [1, 2, 3]]

transactions2 = [[1, 3, 7],
                [2, 3, 7],
                [1, 2, 3],
                [2, 3],
                [2, 3, 4, 5],
                [2, 3],
                [1, 2, 3, 4, 6],
                [2, 3, 4, 6],
                [1],
                [1, 3]]

print("Size\tApriori Time\tFP Growth time")
for data in [transactions1, transactions2]:
    #print("Apriori:")
    start1=time.time()
    rules=apriori(data,min_support=(2/len(data)))
    end1=time.time()
    rules=list(rules)
    result1=[]
    for i in rules:
        result1.append("".join([str(j) for j in i[0]]))

    #print("FP Growth")
    result2=[]
    start2=time.time()
    patterns = pyfpgrowth.find_frequent_patterns(data, 2)
    end2=time.time()
    for i in patterns:
        result2.append(''.join([str(x) for x in i]))
    
    print(str(len(data))+"\t"+str(end1-start1)+"\t"+str(end2-start2))
