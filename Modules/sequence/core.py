def create_sequence(n):
    final_result = [0, 1]
    for i in range(n-2): # 0 1 2 3 4 5 6 7 8 9
        final_result.append(final_result[-1] + final_result[-2])
    return final_result

def locate_number(n, sequence):
    try:
        index = sequence.index(n)
        return f"The number - {n} is at index {index}"
    except ValueError:
        return f"The number {n} is not in the sequence"