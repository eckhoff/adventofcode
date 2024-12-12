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
for page in pages:
    reversed_page = page[::-1]
    page_statue = True
    for i in range(len(page)):
        keys = get_key(key, reversed_page[i])
        for number in keys:
            if number in reversed_page[i+1:]:
                page_statue = False
                break
    if page_statue == True:
        result += get_middle(page)

print(result)