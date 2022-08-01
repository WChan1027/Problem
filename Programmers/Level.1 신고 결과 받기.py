'''

문제 설명
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.


각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
    신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
    한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.

k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
    유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.


제한사항
2 ≤ id_list의 길이 ≤ 1,000
    1 ≤ id_list의 원소 길이 ≤ 10
    id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
    id_list에는 같은 아이디가 중복해서 들어있지 않습니다.

1 ≤ report의 길이 ≤ 200,000
    3 ≤ report의 원소 길이 ≤ 21
    report의 원소는 "이용자id 신고한id"형태의 문자열입니다.
    예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
    id는 알파벳 소문자로만 이루어져 있습니다.
    이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
    자기 자신을 신고하는 경우는 없습니다.
1 ≤ k ≤ 200, k는 자연수입니다.
return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.


'''

def solution(id_list, report, k):
    answer = []
    reported_user = dict.fromkeys(id_list,0)
    suspended_user = []

    report = list(set(report))

    for i in report:
        reported_user[i.split()[1]] += 1

    for i in range(len(reported_user)):
        if list(reported_user.values())[i] >= k :
            suspended_user += [list(reported_user.keys())[i]]

    reported_user = dict.fromkeys(id_list,0)

    for i in report :
        if i.split()[1] in suspended_user:
            reported_user[i.split()[0]] += 1
    answer = list(reported_user.values())
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))