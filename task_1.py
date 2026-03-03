time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_values = time.split(',')
total_minutes = 0
for time_value in time_values:
    parts = time_value.split()
    current_minutes = 0
    for part in parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
            current_minutes += hours * 60
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            current_minutes += minutes
        elif 's' in part:
            seconds = int(part.replace('s', ''))
            current_minutes += seconds // 60
    total_minutes += current_minutes
print(f'Общее количество минут: {total_minutes}')