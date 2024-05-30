from tkinter import *
import math

window = Tk()
window.title("My Calculator")

##디스플레이 변수##
d1= StringVar()
d2= StringVar()

#첫 번째 디스플레이
display1 = Entry(window,textvariable=d1, width=33, bg="yellow")
display1.grid(row=0, column=0, columnspan=5)

#두 번째 디스플레이
display2 = Entry(window,textvariable=d2, width=33, bg="yellow")
display2.grid(row=1, column=0, columnspan=5)

button_list = [
'MC',   'MR',   'M-',   'M+',   '%',
'√',    '7',    '8',    '9',    '/',
'OFF',  '4',    '5',    '6',    '*',
'CE',   '1',    '2',    '3',    '-',
'ON/C', '0',    '.',    '=',    '+', ]


def equal_f():
    try : 
        result = eval(d1.get())
        d1.set(str(result))
    except :
        d1.set("ERROR")
        
def mc_f():
    d2.set('')

def mr_f():
    if d2.get() != '':
        d1.set(d2.get())
        
def mplus_f():
    if d2.get() != '':
        result = float(d2.get()) + eval(display1.get())
        d2.set(str(result))
    else :
        result = eval(display1.get())
        d2.set(str(result))
        
def mminus_f():
    if d2.get() != '':
        result = float(d2.get()) - eval(display1.get())
        d2.set(str(result))
    else :
        result = eval(display1.get())
        d2.set(str(result))
        
def ce_f():
    d1_text = d1.get()
    text_len = len(d1_text)
    while True:        
        if text_len <= 0:
            break        
        
        if d1_text[text_len-1] == '+' or d1_text[text_len-1] == '-' or d1_text[text_len-1] == '*' or d1_text[text_len-1] == '/':
            d1_text = d1_text[:text_len-1]            
            break
        
        text_len -= 1
    
    d1.set(d1_text)        
    
def percent_f():
    if d1.get() != '':
        d1.set(str(float(eval(d1.get())/100)))
        
def squarer_f():
    if d1.get() != '':
        d1.set(str(math.sqrt(float(d1.get()))))

def click(key):
    # 0이 있을 경우
    if d1.get() == '0':
        d1.set('')
    # '=' 클릭할 경우
    if key == "=":
        equal_f()

    #2-A. 메모리 값 지우기
    elif key == 'MC':
        mc_f()
        
    #2-B. 메모리 값 불러오기
    elif key == 'MR':
        mr_f()
        
    #2-C. 메모리의 해당 값 더하기
    elif key == 'M+':
        mplus_f()
        
    #2-D. 메모리의 해당 값 뺴기
    elif key == 'M-':
        mminus_f()

    #2-E. 클리어 엔트리 
    elif key == 'CE':
        ce_f()
        
    #3. % (100으로 나누어 실수 표현)
    elif key == '%':
        percent_f()
        
    # '제곱근' 계산 
    elif key == '√':
        squarer_f()
        
    #3. OFF(프로그램 종료)
    elif key == 'OFF':
        exit()
        
    #3. ON/C
    elif key == 'ON/C':
        d1.set('0')
    else :
        d1.set(d1.get()+key)

##버튼 리스트 생성##
r_index = 2 #버튼 위치할 행#
c_index = 0 #열
for button_text in button_list:

    def process(n=button_text):
        click(n)

    Button(window, text=button_text, width=5,    
      command=process).grid(row=r_index, column=c_index)
    c_index += 1
    if c_index > 4:
        r_index += 1
        c_index = 0

window.mainloop()
