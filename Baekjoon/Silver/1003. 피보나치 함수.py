'''
https://www.acmicpc.net/problem/1003

[문제]

다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }

fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

'''

T = int(input())

a = [0] * 41
b = [0] * 41
a[0], a[2], a[3] = 1, 1, 1
b[1], b[2], b[3] = 1, 1, 2
for i in range(4, 41):
    a[i] = a[i - 1] + a[i - 2]
    b[i] = b[i - 1] + b[i - 2]

for _ in range(T):
    N = int(input())
    print(a[N], b[N])