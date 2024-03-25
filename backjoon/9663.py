import random

def is_attack(table, row, col):
    
    for i in range(N):
        if table[row][i] == 1:
            return True
    
    for i in range(N):
        if table[i][col] == 1:
            return True
    
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and abs(row - i) == abs(col - j):
                return True
    
    return False

def count_safe_arrangements(N):
    cnt = 0
    max_attempts = N*N  # 임의 배치를 위한 최대 시도 횟수
    attempts = 0

    while attempts < max_attempts:
        table = [[0]*N for _ in range(N)]
        queens_placed = 0

        # 퀸 랜덤하게 배치
        while queens_placed < N:
            row = random.randint(0, N - 1)
            col = random.randint(0, N - 1)

            if not is_attack(table, row, col):
                table[row][col] = 1
                queens_placed += 1

        # 모든 퀸이 서로 공격할 수 없는 경우
        if queens_placed == N:
            cnt += 1

        attempts += 1

    return cnt

N = int(input())
print(count_safe_arrangements(N))
