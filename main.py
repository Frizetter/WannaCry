import curses, json, locale
from datetime import datetime
def main():
    while True:
        screen = curses.initscr()
        screen.clear()
        UI()

        height, width = screen.getmaxyx()
        items = [['1.', 'GetTable'], ['2.', 'CreateTask'], ['3.', 'DeleteTask']]
        
        for item in items:
            line = str(item[0]) + ' ' + str(item[1])
            x = width // 2 - len(line) // 2
            y = height // 2 - len(items) // 2 + items.index(item)
            screen.addstr(y, x, line)
        screen.addstr(height - 2, width // 2 - 13 // 2, 'Press key... ')

        screen.refresh()

        c = screen.getch()
        if chr(c) == '1':
            GetTable()
            break
        elif chr(c) == '2':
            Create()
            break
        elif chr(c) == '3':
            DeleteTask()
            break

def GetTable():
    while True:
        screen = curses.initscr()
        screen.clear()
        UI()

        height, width = screen.getmaxyx()

        with open('maintable.json', encoding='utf-8') as f:
            data = json.load(f)
        d = '14.02.2025'
        weekday = getweekday(d)
        tasks = data[weekday]
        k = 0
        for name, times in sorted(tasks.items(), key=lambda item: item[1]["timestart"]):
            line = f'{name} {get24fbday(times["timestart"])} - {get24fbday(times["timefinish"])}'
            x = width // 2 - len(line) // 2
            y = height // 2 - len(data[weekday]) // 2 + k
            screen.addstr(y, x, line)
            k += 1
        screen.addstr(height - 2, width // 2 - 25 // 2, 'Press 1 to go to the menu')
        screen.refresh()
        c = screen.getch()
        if chr(c) == '1':
            main()
            break

def getweekday(d):
    try:
        date = datetime.strptime(d, "%d.%m.%Y")
        day = date.weekday()
        days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        return days[day]
    except ValueError:
        return 'error'
    
def getminsfbday(t):
    try:
        hours, mins = t.split(':')
        return int(hours) * 60 + int(mins)
    except TypeError or ValueError:
        return 'error'
def get24fbday(t):
    t = int(t)
    return f'{str(t // 60).zfill(2)}:{str(t % 60).zfill(2)}'

def Create():
    while True:
        screen = curses.initscr()
        screen.clear()
        UI()

        items = [['1.', 'MakeSchedule'], ['2.', 'MakeTask']]
        height, width = screen.getmaxyx()
        
        for item in items:
            line = str(item[0]) + ' ' + str(item[1])
            x = width // 2 - len(line) // 2
            y = height // 2 - len(items) // 2 + items.index(item)
            screen.addstr(y, x, line)
        screen.addstr(height - 2, width // 2 - 13 // 2, 'Press key... ')
        screen.refresh()
        c = screen.getch()
        if chr(c) == '1':
            Create()
            break
        elif chr(c) == '2':
            MakeTask()
            break


def MakeTask():
    while True:
        screen = curses.initscr()
        screen.clear()
        UI()

        curses.echo()
        height, width = screen.getmaxyx()
        day = ''
        name = ''
        timestart = ''
        timefinish = ''

        while True:
            screen.clear()
            locale.setlocale(locale.LC_ALL, '')
            UI()
            screen.addstr(height // 2, width // 2 - 37 // 2, 'Enter the DAY to create the task ...')
            screen.addstr(height // 2 + 1, width // 2 - 16 // 2, 'Ex. : 01.01.1970')
            input_string = screen.getstr(height // 2 + 2, width // 2 - 10 // 2, 10).decode()
            if getweekday(input_string) != 'error':
                day = input_string
                break
            screen.refresh()
        while True:
            screen.clear()
            UI()
            screen.addstr(height // 2, width // 2 - 37 // 2, 'Enter the NAME to create the task ...')
            input_string = screen.getstr(height // 2 + 1, width // 2 - 25 // 2, 40).decode('utf-8')
            if input_string != '' or input_string != ' ':
                name = input_string
                break
            screen.refresh()
        while True:
            screen.clear()
            UI()
            screen.addstr(height // 2, width // 2 - 37 // 2, 'Enter the TIME START to create the task ...')
            input_string = screen.getstr(height // 2 + 1, width // 2 - 5 // 2, 5).decode()
            if getminsfbday(input_string) != 'error':
                timestart = input_string
                break
            screen.refresh()
        while True:
            screen.clear()
            UI()
            screen.addstr(height // 2, width // 2 - 37 // 2, 'Enter the TIME FINISH to create the task ...')
            input_string = screen.getstr(height // 2 + 1, width // 2 - 5 // 2, 5).decode()
            if getminsfbday(input_string) != 'error':
                timefinish = input_string
                break
            screen.refresh()
        try:
            with open('secondarytable.json', 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        if day not in data:
            data[day] = {}
        data[day][name] = {'timestart':timestart, 'timefinish':timefinish}

        with open('secondarytable.json', 'w') as f:
            json.dump(data, f, indent=4)

        while True:
            screen.clear()
            UI()
            screen.addstr(height // 2, width // 2 - 26 // 2, 'Press 1 to go to menu ...')
            c = screen.getch()
            if chr(c) == '1':
                main()
                break
            screen.refresh()

def DeleteTask():
    print('sdfsdf')

def UI():
    screen = curses.initscr()
    height, width = screen.getmaxyx()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    screen.attron(curses.color_pair(1))
    screen.border()
    screen.attroff(curses.color_pair(1))
    screen.addstr(1, width // 2 - 13 // 2, 'WannaCry v1.0', curses.color_pair(2) | curses.A_BOLD)

if __name__ == '__main__':
    main()