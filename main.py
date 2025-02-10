import curses, json
def main():
    while True:
        items = [['1.', 'GetTable'], ['2.', 'CreateTask'], ['3.', 'DeleteTask']]

        screen = curses.initscr()
        height, width = screen.getmaxyx()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        screen.attron(curses.color_pair(1))
        screen.border()
        screen.attroff(curses.color_pair(1))
        screen.addstr(1, width // 2 - 13 // 2, 'WannaCry v1.0', curses.color_pair(2) | curses.A_BOLD)
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
            CreateTask()
            break
        elif chr(c) == '3':
            DeleteTask()
            break

def GetTable():
    while True:
        screen = curses.initscr()
        screen.clear()
        height, width = screen.getmaxyx()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        screen.attron(curses.color_pair(1))
        screen.border()
        screen.attroff(curses.color_pair(1))
        screen.addstr(1, width // 2 - 13 // 2, 'WannaCry v1.0', curses.color_pair(2) | curses.A_BOLD)

        with open('maintable.json', encoding='utf-8') as f:
            data = json.load(f)
        k = 0
        for item in data['friday']:
            line = f'{item} {data['friday'][item]['timestart']} {data['friday'][item]['timefinish']}' 
            x = width // 2 - len(line) // 2
            y = height // 2 - len(data['friday']) // 2 + k
            screen.addstr(y, x, line)
            k += 1
        screen.addstr(height - 2, width // 2 - 13 // 2, 'Press key... ')
        screen.refresh()

def CreateTask():
    print('sdfsdf')


def DeleteTask():
    print('sdfsdf')


if __name__ == '__main__':
    main()