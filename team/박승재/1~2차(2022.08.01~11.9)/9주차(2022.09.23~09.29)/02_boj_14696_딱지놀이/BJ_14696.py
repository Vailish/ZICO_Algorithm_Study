def sol():
    def find_winner(player1, player2):
        for j in range(4, 0, -1):
            chk_a = player1.count(j)
            chk_b = player2.count(j)
            if chk_a > chk_b:
                print("A")
                return
            elif chk_a < chk_b:
                print("B")
                return
        print("D")
        return

    games = int(input())
    for _ in range(games):
        find_winner(list(map(int, input().split()))[1:], list(map(int, input().split()))[1:])


sol()
