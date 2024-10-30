def unhash(hash):
    # CTF Hash[i] = i + (input[i] * 100) - 10
    flag = ''
    for i in range(15):
        flag += chr((hash[i] + 10 - i) // 100)
    return flag

if __name__ == '__main__':
    expected_hash = [0x1a22, 0x20c7, 0x1b50, 0x2515, 0x29c6, 0x28ff, 0x2d4c, 0x2d4d, 0x2646, 0x2f43, 0x2f44, 0x2f45, 0x0c82, 0x16ab, 0x1a94]
    print(unhash(expected_hash))
