from datetime import date

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

benchmark = date(1900, 1, 1)
start_date = date(1901, 1, 1)
middle_date = date(1901, 12, 31)
end_date = date(2000, 12, 31)

if __name__ == '__main__':
    print(f'{benchmark} is {days[benchmark.weekday()]}')
    print(f'{start_date} in ordinal is: {start_date.toordinal()}')
    print(f'{end_date} in ordinal is: {end_date.toordinal()}')

    count = 0
    for dat in range(start_date.toordinal(), end_date.toordinal() + 1):
        # Counting the number of Sundays on 1st of month
        if days[date.fromordinal(dat).weekday()] == 'Sunday' and date.fromordinal(dat).day == 1:
            count += 1
    print(f'Total number of Sunday from {start_date} to {end_date} is {count}.')
