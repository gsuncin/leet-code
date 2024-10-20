def count_password_possibilities(password):
    if len(password) > 10**5:
        raise "Error"

    count = 0
    password_list = list(password)
    length = len(password_list)
    for i in range(length):
        for x in range(i + 1, length):
            if password_list[i] != password_list[x]:
                count += 1

    return count

password = "abaa"
possibilities = count_password_possibilities(password)

