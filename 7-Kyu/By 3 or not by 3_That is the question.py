def divisible_by_three(st):
    total = 0

    for num in st:
        total += int(num)

    return total % 3 == 0
