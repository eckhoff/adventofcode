def is_sorted(lst):
    if len(lst) == len(set(lst)):
        if lst == sorted(lst):
            return True
        elif lst == sorted(lst, reverse=True):
            return True
        else:
            return False
    else:
        return False


def num_gap(lst):
    for i in range(len(lst) - 1):
        if abs(lst[i] - lst[i+1]) > 3:
            return False
    return True


safe_count = 0
with open('day2-input.txt', 'r') as file:
    for line in file:
        value1 = line.split()
        int_value = [int(item) for item in value1]

        if is_sorted(int_value) is True and num_gap(int_value) is True:
            safe_count += 1
        else:
            for i in range(len(int_value)):
                sublist = int_value[:i] + int_value[i+1:]
                if is_sorted(sublist) is True and num_gap(sublist) is True:
                    safe_count += 1
                    break


print(safe_count)
