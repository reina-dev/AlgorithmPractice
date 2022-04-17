import numpy as np

def solution(arr):
    A = np.array(arr)
    answer = A.mean()
    return answer

    # return np.array(arr).mean() 로 축약 가능 !