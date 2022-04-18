def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            arr_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(arr_sum)
        
    return answer

# numpy를 활용해서 문제 풀기

import numpy as np

def solution(arr1, arr2):
    answer = np.array(arr1) + np.array(arr2)
    return answer.tolist()