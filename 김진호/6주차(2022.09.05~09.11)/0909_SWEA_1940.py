for test_case in range(1,int(input())+1):
    speed = 0
    distance= 0
    for case in range(int(input())):
        command = input()
        if command[0] == '1':
            speed += int(command[2])
        elif command[0] == '2':
            speed -= int(command[2])
            if speed < 0:
                speed = 0
        distance += speed
    print(f'#{test_case} {distance}')