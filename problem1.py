# to print A-Z in odd pattern



start_char = 'A'
rows = 6

for i in range(1, rows + 1):
    for j in range(i*2 - 1):
        print(start_char, end=" ")
        start_char = chr(ord(start_char) + 1)
        if(ord(start_char) == 91):
            break
    print()