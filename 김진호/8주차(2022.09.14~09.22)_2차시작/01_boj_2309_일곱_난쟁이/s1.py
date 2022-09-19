import sys
sys.stdin = open("input.txt")


def chk_liars():
    for i in range(8):
        for j in range(i+1,9):
            if keys[i]+keys[j] == sum_liars:
                del keys[j]
                del keys[i]
                return


keys = [int(input()) for _ in range(9)]
sum_liars = sum(keys) - 100
keys.sort()
chk_liars()
for key in keys:
    print(key)


print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
