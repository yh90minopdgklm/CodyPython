import time
import json

def read_log():
    with open('mission_computer_main.log', encoding="utf-8") as f:
        read_data = f.read()
    return read_data

def validate_log(f):
    lines = f.splitlines()
    if lines[0] != 'timestamp,event,message':
        return False
    for i in range(len(lines)):
        if i == 0:
            continue
        field = lines[i].split(',', 2)
        if len(field) != 3:
            return False
        if field[0] == '' or field[1] == '' or field[2] == '':
            return False
        time.strptime(field[0], '%Y-%m-%d %H:%M:%S')
    return True

def main():
    try:
        f = read_log()
        if validate_log(f) == False:
            raise ValueError
        print(f)
        lines = f.splitlines()
        log_list = []
        for i in range(len(lines)):
            if i == 0:
                continue
            field = lines[i].split(',', 2)
            log_list.append([field[0], field[2]])
        print(log_list)
        for i in range(len(log_list)):
            log_list[i][0] = time.mktime(time.strptime(log_list[i][0], '%Y-%m-%d %H:%M:%S'))
        log_list.sort(reverse=True)
        for i in range(len(log_list)):
            log_list[i][0] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log_list[i][0]))
        print(log_list)
        log_dict = dict(log_list)
        with open('mission_computer_main.json', 'w', encoding='utf-8') as f:
            json.dump(log_dict, f, ensure_ascii=False, indent=4)
    except OSError:
        print('File open error')
        return
    except UnicodeDecodeError:
        print('Decode error')
        return
    except ValueError:
        print('Invalid log format')
        return
    except:
        print('error occurred')
        return
    return

if __name__ == '__main__':
    main()