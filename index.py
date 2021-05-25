def extra_end(str):
    result = ""
    ending = str[len(str) - 2:]
    for index in range(3):
        result += ending
    return result


print(extra_end('hello'))
