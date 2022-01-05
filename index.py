def count_code(str):
    count = 0
    for i in range(len(str)):
        letters = str[i: i+4]
        if len(letters) == 4 and letters[0] == 'c' and letters[2] == 'd' and letters[3] == 'e':
            count += 1

    return count


print(count_code('codexxcode'))
