time = int(input('Enter time in seconds: '))
hour = int(time // 3600)
minutes = (time - hour * 3600) // 60
seconds = time % 60
print('You entered the following time: ', '%.2d' % hour,':', '%.2d' % minutes,':', '%.2d' % seconds)

