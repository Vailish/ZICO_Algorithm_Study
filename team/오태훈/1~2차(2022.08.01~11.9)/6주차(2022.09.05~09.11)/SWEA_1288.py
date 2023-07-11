# 1288. 새로운 불면증 치료법
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN


for t in range(1, int(input()) + 1):
    n = int(input())
    # set을 활용해 지금까지 나온 숫자 카운트
    chk_num = set()

    k = 1
    # 0 ~ 9까지 모두 나오면 set의 길이는 10
    while len(chk_num) < 10:
        kn = k * n
        # 문자열로 바꿔 쪼개기
        str_kn = str(kn)
        # for i in str_kn:
        #     chk_num.add(i)
        chk_num.update(str_kn)
        k += 1
    print(f'#{t} {kn}')
