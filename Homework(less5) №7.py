import json

result = dict()
all_profit = 0
num = 0
with open('text_7.txt', encoding='utf-8') as f:
    for line in f:
        name, form_of_ownership, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        if profit >= 0:
            all_profit += profit
            num += 1
        result[name] = profit
all_profit /= num
with open('text_7.json', 'w', encoding='utf-8') as f:
    json.dump([result, {'average_profit': all_profit}], f, ensure_ascii=False)
