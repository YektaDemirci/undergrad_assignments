import numpy as np
import math

# Given transition probability matrix and observation estimates for every state
# Return the probability of the given observations to occur
def forward(trans, estimate, obs):
    it=len(obs)
    ittrans=len(trans)-2
    matrix = [[0 for x in range(it)] for y in range(ittrans)]

    for i in range(0,ittrans):
        matrix[i][0]=trans[0][i+1]*estimate[i+1][obs[0]]
        
    for t in range(1, it):
        for j in range(0, ittrans):
            for i in range(0, ittrans):
                matrix[j][t] = matrix[j][t]+matrix[i][t-1]*trans[i+1][j+1]*estimate[j+1][obs[t]]
    res=0   
    for i in range(0,ittrans):
        res = res + (matrix[i][it-1]*trans[i+1][ittrans+1])
    return res

# Given the transition probability matrix and observation estimates for every state
# Return the hidden states that the given observations cause HMM to visit with highest probability
# Hidden states should be returned as indexes as their names will not be supplied
# Do not include start and end states
def viterbi(trans, estimate, obs):
    it=len(obs)
    ittrans=len(trans)-2
    matrix = [[0 for x in range(it)] for y in range(ittrans)]
    holder = [[0 for x in range(it)] for y in range(ittrans)]
    res = [0 for x in range(it)]
    
    for i in range(0, ittrans):
        matrix[i][0]=trans[0][i+1]*estimate[i+1][obs[0]]

    for t in range(1, it):
        for j in range(0, ittrans):
            for i in range(0, ittrans):
                dum=matrix[i][t-1]*trans[i+1][j+1]*estimate[j+1][obs[t]]
                if(dum>matrix[j][t]):
                    matrix[j][t]=dum
                    holder[j][t]=i+1
                    
    dum1=matrix[0][it-1]*trans[1][ittrans+1]                
    for i in range(0,ittrans):
        dum2=matrix[i][it-1]*trans[i+1][ittrans+1]
        if(dum2>dum1):
            dum1=dum2
            res[it-1]=i+1
    it1=it-1        
    for a in range(0,it-1):
        res[it1-1]=holder[res[it1]-1][it1]
        it1=it1-1

    return res

# Example transition matrixes from the notes. First column and row is the start state, last column and row are end state.
# trans[row][col] indicates transition from state represented with a row to a state represented with a column.
trans_matrix_example = [
     [0.0, 0.0743, 0.1352, 0.1534, 0.1456, 0.1688, 0.3227, 0.0],
     [0.0, 0.056, 0.2833, 0.2007, 0.064, 0.075, 0.2515, 0.0695],
     [0.0, 0.1071, 0.128, 0.2121, 0.1496, 0.117, 0.2009, 0.0853],
     [0.0, 0.0248, 0.2431, 0.1859, 0.2164, 0.1004, 0.1761, 0.0533],
     [0.0, 0.3176, 0.189, 0.0691, 0.1065, 0.2229, 0.0109, 0.084],
     [0.0, 0.1009, 0.0659, 0.0734, 0.0417, 0.263, 0.2514, 0.2037],
     [0.0, 0.2202, 0.0034, 0.0301, 0.3312, 0.0992, 0.1029, 0.213],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
 ]

observation_types_examples = [1, 2, 3]
# Estimates include start and end states as well but they are guaranteed to be zero.
observation_estimates =[
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [0.1504, 0.0983, 0.0668, 0.1586, 0.1886, 0.0796, 0.0932, 0.1644],
     [0.0462, 0.1213, 0.1256, 0.2104, 0.2302, 0.0047, 0.0559, 0.2058],
     [0.1522, 0.048, 0.1708, 0.1389, 0.0738, 0.0565, 0.2167, 0.143],
     [0.0836, 0.0424, 0.0068, 0.2924, 0.0458, 0.2093, 0.2829, 0.0368],
     [0.2812, 0.0403, 0.1687, 0.0271, 0.1419, 0.1155, 0.1147, 0.1107],
     [0.0912, 0.0656, 0.1448, 0.2317, 0.1722, 0.0102, 0.2503, 0.0342],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
 ]

y=viterbi(trans_matrix_example, observation_estimates,[0, 0, 7, 6, 0, 1, 6, 1, 2])
print(y)


# Feel free to try many more examples like these to check your implementation

