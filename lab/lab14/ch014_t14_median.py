def median(numbers):
    ordered = sorted(numbers)
    length = len(ordered)
    middle = length // 2

    if length % 2 == 1:
        return ordered[middle]
    else:
        return (ordered[middle - 1] + ordered[middle]) / 2.0