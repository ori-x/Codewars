def solve(n):
    notes = [500, 200, 100, 50, 20, 10]
    count = 0

    if n % 10 != 0:
        return - 1

    for note in notes:
        count += n // note
        if n % note == 0:
            return count
        else:
            n %= note

    return count
