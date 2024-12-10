def remove_first_duplicate(lst):
    seen = set()
    for i, num in enumerate(lst):
        if num in seen:
            lst.pop(i)
            return lst
        seen.add(num)


def make_sorted_by_removing_one(lst):
    def is_sorted_helper(sublist):
        return sublist == sorted(sublist) or sublist == sorted(sublist, reverse=True)

    for i in range(len(lst)):
        sublist = lst[:i] + lst[i+1:]
        if is_sorted_helper(sublist) and num_gap(sublist) is True:
            return True


def is_sorted(lst):
    if len(lst) == len(set(lst)):
        if lst == sorted(lst) and num_gap(lst) is True:
            return True
        elif lst == sorted(lst, reverse=True) and num_gap(lst) is True:
            return True
        else:
            if make_sorted_by_removing_one(lst) is True:
                return True
            else:
                return False
    else:
        new_lst = remove_first_duplicate(lst)
        if len(new_lst) == len(set(new_lst)):
            if new_lst == sorted(new_lst) and num_gap(new_lst) is True:
                return True
            elif new_lst == sorted(new_lst, reverse=True) and num_gap(new_lst) is True:
                return True
            else:
                return False


def num_gap(lst):
    for i in range(len(lst) - 1):
        if abs(lst[i] - lst[i+1]) > 3:
            return False
    return True


safe_count = 0
total = 0
with open('day2-input.txt', 'r') as file:
    for line in file:
        value1 = line.split()
        int_value = [int(item) for item in value1]

        if is_sorted(int_value) is True:
            print(int_value, True)
            safe_count += 1
            total += 1
        else:
            print(int_value, False)
            total += 1


print(safe_count)
print(total)
