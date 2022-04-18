#내가 작성한 코드 1
def solution(num):
    answer = 0
    
    for i in range(500):
        num = num/2 if num % 2 == 0 else (num*3) + 1
        answer += 1
        if num == 1:
            break
    if answer > 500 or num != 1:
        answer = -1
    return answer

# 자꾸 test case 13에서 실패 !

# 결국 일단 구글링 참조로 해결
def solution(num):
    for i in range(500):
        if num == 1:
            return i
        if num % 2 == 0:
            num = num/2
        else:
            num = num*3 +1
    return -1


#다른 사람의 풀이 참조를 보고 꺠달음을 얻었는데

def solution(num):
    if num == 1:
        return 0
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

# test case 13이 num = 1 이었던 것 같다 ㅠ 성공!

def solution(num):
    answer = 0
    if num == 1:
        return answer
    
    for i in range(500):
        num = num/2 if num % 2 == 0 else (num*3) + 1
        answer += 1
        if num == 1:
            break
    if answer > 500 or num != 1:
        answer = -1
    return answer

# 따라서 최종 수정 코드는 이렇게! 