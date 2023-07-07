string = '1h 45m,360s,25m,30m 120s,2h 60s'
intervals = string.replace(' ', ',').split(',')
minutes = []

for interval in intervals:
    if 'h' in interval[-1]:
        hours_to_minutes = int(interval.replace('h', '')) * 60
        minutes.append(hours_to_minutes)
    elif 'm' in interval[-1]:
        minutes_to_minutes = int(interval.replace('m', ''))
        minutes.append(minutes_to_minutes)
    elif 's' in interval[-1]:
        seconds_to_minutes = int(interval.replace('s', '')) // 60
        minutes.append(seconds_to_minutes)

print(sum(minutes))
