# 1928. Base64 Decoder
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PR4DKAG0DFAUq

for test_case in range(1, int(input()) + 1):
    base64 = input()
    full_bin = ''
    string = ''
    for text in base64:
        ascii_num = ord(text)
        if 65 <= ascii_num <= 90:
            decoding_num = ascii_num - 65
        elif 97 <= ascii_num <= 122:
            decoding_num = ascii_num - 71
        elif 48 <= ascii_num <= 57:
            decoding_num = ascii_num + 4
        elif ascii_num == 43:
            decoding_num = ascii_num + 19
        else:
            decoding_num = ascii_num + 16
        decoding_bin = format(decoding_num, 'b')
        while len(decoding_bin) < 6:
            decoding_bin = '0' + decoding_bin
        full_bin += decoding_bin
    for bin_index in range(8, len(full_bin), 8):
        string += chr(int(full_bin[bin_index - 8 : bin_index], 2))
    print(f'#{test_case} {string}.')
