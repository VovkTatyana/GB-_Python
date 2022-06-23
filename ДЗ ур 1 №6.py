revenue = int(input('Enter your company revenue: '))
costs = int(input('Enter your company costs: '))
if revenue > costs:
    profit = revenue - costs
    result = round((profit / revenue) * 100, 2)
    print('Return on revenue = ', result, '%')
    people = int(input('How many people work in the company?: '))
    personal_result = round(profit / people, 2)
    print('On average, each employee brought:', personal_result, 'profit')

else:
    print('The company is unprofitable!')