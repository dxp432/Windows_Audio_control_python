import tkinter as tk
from tkinter import ttk
from subprocess import Popen
import datetime
import time

hour = ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00']
min = ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
       '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
       '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
       '00', '00', '00']
myswitch = ['1', '1', '1', '1', '1', '1', '1']

# print(len(min))
# print(myswitch)


def read_load():
    for num in range(1, 8):
        f = open("hour" + str(num) + ".txt")
        line = f.readline()
        hour[num - 1] = line
        f.close()

    for num_min in range(1, 7):
        f = open("min" + str(num_min) + ".txt")
        line = f.readline()
        min[num_min - 1] = line
        f.close()

    for num_switch in range(1, 7):
        f = open("switch" + str(num_switch) + ".txt")
        line = f.readline()
        myswitch[num_switch - 1] = line
        f.close()


def callbackFunc_hour(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('hour1.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_min(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('min1.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_hour1(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('hour2.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_min1(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('min2.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_hour2(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('hour3.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_min2(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('min3.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_hour3(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('hour4.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_hour4(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('hour5.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_hour5(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('hour6.txt', 'w')

        f.write(event.widget.get())

        f.close()

def callbackFunc_min3(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('min4.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_min4(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('min5.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_min5(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('min6.txt', 'w')

        f.write(event.widget.get())

        f.close()


def callbackFunc_combo_switch(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        print("event.widget:", event.widget.get())

        f = open('switch1.txt', 'w')
        if event.widget.get() == '关':
            f.write('0')
        else:
            f.write('1')

        f.close()


def callbackFunc_combo_switch2(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('switch2.txt', 'w')

        if event.widget.get() == '关':
            f.write('0')
        else:
            f.write('1')

        f.close()


def callbackFunc_combo_switch3(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('switch3.txt', 'w')

        if event.widget.get() == '关':
            f.write('0')
        else:
            f.write('1')

        f.close()


def callbackFunc_combo_switch4(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('switch4.txt', 'w')

        if event.widget.get() == '关':
            f.write('0')
        else:
            f.write('1')
        f.close()




def callbackFunc_combo_switch5(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('switch5.txt', 'w')

        if event.widget.get() == '关':
            f.write('0')
        else:
            f.write('1')
        f.close()



def callbackFunc_combo_switch6(event):
    # print('----------------------------')
    # print("New Element Selected")

    if event:  # <-- this works only with bind because `command=` doesn't send event
        # print("event.widget:", event.widget.get())

        f = open('switch6.txt', 'w')

        if event.widget.get() == '关':
            f.write('0')
        else:
            f.write('1')
        f.close()


read_load()


# print(hour)
# print(min)
app = tk.Tk()
app.title("定时开关")
app.geometry('800x500')


def clock():
    mytime = datetime.datetime.now()
    # print("after定时执行" + str(mytime))
    app.after(10000, clock)
    read_load()
    # print(myswitch[0])
    # print(mytime.hour)
    # print(mytime.minute)
    if (mytime.hour == int(hour[0])) and (mytime.minute == int(min[0])):
        # print("lai")
        if str(myswitch[0]) == '0':
            # print("net_stop_AudioSrv")
            p = Popen("net_stop_AudioSrv.bat")
            stdout, stderr = p.communicate()
        elif str(myswitch[0]) == '1':
            # print("net_start_AudioSrv")
            p = Popen("net_start_AudioSrv.bat")
            stdout, stderr = p.communicate()
    if (mytime.hour == int(hour[1])) and (mytime.minute == int(min[1])):
        # print("lai")
        if str(myswitch[1]) == '0':
            # print("net_stop_AudioSrv")
            p = Popen("net_stop_AudioSrv.bat")
            stdout, stderr = p.communicate()
        elif str(myswitch[1]) == '1':
            # print("net_start_AudioSrv")
            p = Popen("net_start_AudioSrv.bat")
            stdout, stderr = p.communicate()

    if (mytime.hour == int(hour[2])) and (mytime.minute == int(min[2])):
        # print("lai")
        if str(myswitch[2]) == '0':
            # print("定时执行11")
            p = Popen("net_stop_AudioSrv.bat")
            stdout, stderr = p.communicate()
        elif str(myswitch[2]) == '1':
            # print("net_start_AudioSrv")
            p = Popen("net_start_AudioSrv.bat")
            stdout, stderr = p.communicate()

    if (mytime.hour == int(hour[3])) and (mytime.minute == int(min[3])):
        # print("lai")
        if str(myswitch[3]) == '0':
            # print("net_stop_AudioSrv")
            p = Popen("net_stop_AudioSrv.bat")
            stdout, stderr = p.communicate()
        elif str(myswitch[3]) == '1':
            # print("net_start_AudioSrv")
            p = Popen("net_start_AudioSrv.bat")
            stdout, stderr = p.communicate()
    if (mytime.hour == int(hour[4])) and (mytime.minute == int(min[4])):
        # print("lai")
        if str(myswitch[4]) == '0':
            # print("net_stop_AudioSrv")
            p = Popen("net_stop_AudioSrv.bat")
            stdout, stderr = p.communicate()
        elif str(myswitch[4]) == '1':
            # print("net_start_AudioSrv")
            p = Popen("net_start_AudioSrv.bat")
            stdout, stderr = p.communicate()
    if (mytime.hour == int(hour[4])) and (mytime.minute == int(min[4])):
        # print("lai")
        if str(myswitch[4]) == '0':
            # print("net_stop_AudioSrv")
            p = Popen("net_stop_AudioSrv.bat")
            stdout, stderr = p.communicate()
        elif str(myswitch[4]) == '1':
            # print("net_start_AudioSrv")
            p = Popen("net_start_AudioSrv.bat")
            stdout, stderr = p.communicate()
clock()

labelTop = tk.Label(app, text="选择")
labelTop.grid(column=0, row=0)

combo_hour = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23"], state='readonly')

combo_hour.grid(column=0, row=1)
combo_hour.current(int(hour[0]))

label_hour = tk.Label(app, text="时")
label_hour.grid(column=1, row=1)

combo_min = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"], state='readonly')

combo_min.grid(column=2, row=1)
combo_min.current(int(min[0]))

label_min = tk.Label(app, text="分")
label_min.grid(column=3, row=1)

combo_switch = ttk.Combobox(app, values=[
    "关",
    "开"], state='readonly')

combo_switch.grid(column=4, row=1)
combo_switch.current(int(myswitch[0]))

#


combo_hour2 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23"], state='readonly')

combo_hour2.grid(column=0, row=2)
combo_hour2.current(int(hour[1]))

label_hour2 = tk.Label(app, text="时")
label_hour2.grid(column=1, row=2)

combo_min2 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"], state='readonly')

combo_min2.grid(column=2, row=2)
combo_min2.current(int(min[1]))

label_min2 = tk.Label(app, text="分")
label_min2.grid(column=3, row=2)

combo_switch2 = ttk.Combobox(app, values=[
    "关",
    "开"], state='readonly')

combo_switch2.grid(column=4, row=2)
combo_switch2.current(int(myswitch[1]))

#


combo_hour3 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23"], state='readonly')

combo_hour3.grid(column=0, row=3)
combo_hour3.current(int(hour[2]))

label_hour3 = tk.Label(app, text="时")
label_hour3.grid(column=1, row=3)

combo_min3 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"], state='readonly')

combo_min3.grid(column=2, row=3)
combo_min3.current(int(min[2]))

label_min3 = tk.Label(app, text="分")
label_min3.grid(column=3, row=3)

combo_switch3 = ttk.Combobox(app, values=[
    "关",
    "开"], state='readonly')

combo_switch3.grid(column=4, row=3)
combo_switch3.current(int(myswitch[2]))

#


combo_hour4 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23"], state='readonly')

combo_hour4.grid(column=0, row=4)
combo_hour4.current(int(hour[3]))

label_hour4 = tk.Label(app, text="时")
label_hour4.grid(column=1, row=4)

combo_min4 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"], state='readonly')

combo_min4.grid(column=2, row=4)
combo_min4.current(int(min[3]))

label_min4 = tk.Label(app, text="分")
label_min4.grid(column=3, row=4)

combo_switch4 = ttk.Combobox(app, values=[
    "关",
    "开"], state='readonly')

combo_switch4.grid(column=4, row=4)
combo_switch4.current(int(myswitch[3]))

# 5

combo_hour5 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23"], state='readonly')

combo_hour5.grid(column=0, row=5)
combo_hour5.current(int(hour[4]))

label_hour5 = tk.Label(app, text="时")
label_hour5.grid(column=1, row=5)

combo_min5 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"], state='readonly')

combo_min5.grid(column=2, row=5)
combo_min5.current(int(min[4]))

label_min5 = tk.Label(app, text="分")
label_min5.grid(column=3, row=5)

combo_switch5 = ttk.Combobox(app, values=[
    "关",
    "开"], state='readonly')

combo_switch5.grid(column=4, row=5)
combo_switch5.current(int(myswitch[4]))


# 6

combo_hour6 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23"], state='readonly')

combo_hour6.grid(column=0, row=6)
combo_hour6.current(int(hour[5]))

label_hour6 = tk.Label(app, text="时")
label_hour6.grid(column=1, row=6)

combo_min6 = ttk.Combobox(app, values=[
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"], state='readonly')

combo_min6.grid(column=2, row=6)
combo_min6.current(int(min[5]))

label_min6 = tk.Label(app, text="分")
label_min6.grid(column=3, row=6)

combo_switch6 = ttk.Combobox(app, values=[
    "关",
    "开"], state='readonly')

combo_switch6.grid(column=4, row=6)
combo_switch6.current(int(myswitch[5]))

label_min6 = tk.Label(app, text="请不要关闭本窗口和黑色的窗口，关闭的话就不能用了。")
label_min6.grid(column=0, row=7, columnspan=8)
label_min6 = tk.Label(app, text="选择好时间后即时生效，不用保存。")
label_min6.grid(column=0, row=8, columnspan=8)
label_min6 = tk.Label(app, text="本软件使用python编写，开源免费，欢迎下载：https://github.com/dxp432/Windows_Audio_control_python")
label_min6.grid(column=0, row=9, columnspan=8)


# 触发
combo_hour.bind("<<ComboboxSelected>>", callbackFunc_hour)
combo_min.bind("<<ComboboxSelected>>", callbackFunc_min)
combo_hour2.bind("<<ComboboxSelected>>", callbackFunc_hour1)
combo_min2.bind("<<ComboboxSelected>>", callbackFunc_min1)
combo_hour3.bind("<<ComboboxSelected>>", callbackFunc_hour2)
combo_min3.bind("<<ComboboxSelected>>", callbackFunc_min2)
combo_hour4.bind("<<ComboboxSelected>>", callbackFunc_hour3)
combo_min4.bind("<<ComboboxSelected>>", callbackFunc_min3)
combo_hour5.bind("<<ComboboxSelected>>", callbackFunc_hour4)
combo_min5.bind("<<ComboboxSelected>>", callbackFunc_min4)
combo_hour6.bind("<<ComboboxSelected>>", callbackFunc_hour5)
combo_min6.bind("<<ComboboxSelected>>", callbackFunc_min5)
combo_switch.bind("<<ComboboxSelected>>", callbackFunc_combo_switch)
combo_switch2.bind("<<ComboboxSelected>>", callbackFunc_combo_switch2)
combo_switch3.bind("<<ComboboxSelected>>", callbackFunc_combo_switch3)
combo_switch4.bind("<<ComboboxSelected>>", callbackFunc_combo_switch4)
combo_switch5.bind("<<ComboboxSelected>>", callbackFunc_combo_switch5)
combo_switch6.bind("<<ComboboxSelected>>", callbackFunc_combo_switch6)

app.mainloop()
