my_dict = dict()
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lesson, t_work = line.split(':')
        t_work = t_work.split()
        my_sum = 0
        for part in t_work:
            if '-' in part:
                continue
            nums, type = part.split('(')
            my_sum += int(nums)
        my_dict[lesson] = my_sum
print(my_dict)

