raw_time = input('input time: ')
hours = int(raw_time) // 3600
minutes = (int(raw_time) % 3600) // 60
seconds = (int(raw_time) % 3600) % 60
print(hours)
print(minutes)
print(seconds)

out_time = print('hours,':',minutes,':',seconds)
