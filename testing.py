from datetime import datetime
t = "11:00"
d = "13.02.2025"

def getweekday(d):
    try:
        date = datetime.strptime(d, "%d.%m.%Y")
        day = date.weekday()
        days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        return days[day]
    except ValueError:
        return 'valueerror'
    
def getminsfbday(t):
    try:
        hours, mins = t.split(':')
        return int(hours) * 60 + int(mins)
    except ValueError:
        return 'vallueerror'
    
if __name__ == '__main__':
    print(f'{getweekday(d)}')
    print(f'{getminsfbday(t)}')