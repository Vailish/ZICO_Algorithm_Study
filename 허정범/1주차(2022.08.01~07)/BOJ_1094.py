X = int(input())
bar = 64
count_bar = 0
while True:
    if X < bar:
        bar = bar / 2
    elif X > bar:
        X = X - bar
        count_bar += 1
    else:
        count_bar += 1
        break
print(count_bar)
