'''
https://www.acmicpc.net/problem/18111

[문제]

팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다.
마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.

목재를 충분히 모은 lvalue는 집을 짓기로 하였다.
하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.

lvalue는 세로 N, 가로 M 크기의 집터를 골랐다.
집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다.
우리는 다음과 같은 두 종류의 작업을 할 수 있다.

좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다.
‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.

단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다.
또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다.
땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

'''
import sys
sys.stdin = open('input.txt')
N, M, B = map(int, sys.stdin.readline().split())

ground = []
for _ in range(N):
    ground += map(int, sys.stdin.readline().split())

answer = 100000000000
height = 0
for k in range(257):
    time = 0
    count = B
    for i in range(N*M):
        if ground[i] > k:
            time += (ground[i] - k) * 2
            count += ground[i] - k
        else:
            time += k - ground[i]
            count -= k - ground[i]
    if count >= 0:
        if time <= answer:
            answer = time
            height = k

print(answer, height)