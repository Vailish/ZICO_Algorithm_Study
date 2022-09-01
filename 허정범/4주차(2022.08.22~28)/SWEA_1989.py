t = int(input())
for tc in range(t):
    word = input()
    if word == word[::-1]:
        print(f"#{tc + 1} 1")
    else:
        print(f"#{tc + 1} 0")