key = []
pages = []

with open('input-key.txt') as file:
    for line in file:
        line = line.strip()
        parts = line.split('|')
        key.append((int(parts[0].strip()), int(parts[1].strip())))

with open('input-pages.txt') as file:
    pages = [list(map(int, line.strip().split(','))) for line in file]


def get_key(key, number):
    key_pairs = []
    for i in key:
        if i[0] == number:
            key_pairs.append(i[1])

    return key_pairs


def get_middle(lst):
    return lst[len(lst)//2]


result = 0
unsorted = []

for page in pages:
    reversed_page = page[::-1]
    page_status = True
    for i in range(len(page)):
        keys = get_key(key, reversed_page[i])
        for number in keys:
            if number in reversed_page[i+1:]:
                page_status = False
                break
    if page_status == True:
        #result += get_middle(page)
        result = 0
    else:
        unsorted.append(page)

for page in unsorted:
    reversed_page = page[::-1]
    for i in range(len(page)):
        keys = get_key(key, reversed_page[i])
        for number in keys:
            if number in reversed_page[i+1:]:
                index = reversed_page.index(number)
                reversed_page[index], reversed_page[i] = reversed_page[i], reversed_page[index]
    result += get_middle(reversed_page)
    print(reversed_page)
                

print(result)

# 4444 is too low
# 4601 is too low