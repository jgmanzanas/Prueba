if __name__ == '__main__':
    in_data = input("Write an integer: ")
    try:
        number = int(in_data) + 1 #Check Type
    except ValueError:
        ValueError("Data introduced is not a integer")

    new_data = list(map(str, in_data))
    original_len = len(new_data)
    pos = original_len % 3

    # Care with multiple of 3 in original_len
    n_commas = original_len // 3 if pos != 0 else (original_len // 3) - 1
    data_range = range(n_commas + 1)
    result = ''
    for i in data_range:
        #Avoid comma in first iteration in position 0
        if i == 0 and pos == 0:
            pos = 3

        #Avoid comma in last position
        if pos != len(new_data):
            new_data.insert(pos, ',')

        result += ''.join(new_data[0:pos + 1])
        new_data = new_data[pos + 1::]
        pos = len(new_data) % 3 if len(new_data) % 3 != 0 else 3

    print(result)
