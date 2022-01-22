import os

def get_process(proc):
    w = ''
    n = ''
    if proc[0] == '':
        return "skip"
    else:
        for i in proc[0]:
            if i.isdigit():
                n = n + i
            else:
                w = w + i
        arr = {
            'ProcessName': w,
            'ProcessID': int(n)
        }
    return arr

def return_id(e):
    return e['ProcessID']

def main():
    output = os.popen('wmic process get description, processid').read().split('\n')

    initial_array = []
    for out in output:
        initial_array.append(out.replace(" ", "").split('\n'))

    final_array = []
    for x in initial_array:
        if x[0] == 'DescriptionProcessId':
            continue
        else:
            res = get_process(proc=x)
            if res == "skip":
                continue
            else:
                final_array.append(res)

    final_array.sort(key=return_id)

    for x in final_array:
        proc = f'{x["ProcessName"]} {x["ProcessID"]} \n'
        f = open("task-3-output.txt", "a")
        f.write(proc)
        f.close()


if __name__ == '__main__':
    main()