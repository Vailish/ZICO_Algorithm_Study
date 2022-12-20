def sol():
    for tc in range(1, int(input()) + 1):
        # input 받아오기
        n, k = map(int, input().split())
        # 1부터 n까지의 리스트를 만든 다음에 제출한 숙제들과 차집합을 구하고 오름차순 정렬
        k_list = sorted(list(set(list(range(1, n + 1))) - set(map(int, input().split()))))
        print(f'#{tc}', end=" ")
        print(*k_list)


sol()
