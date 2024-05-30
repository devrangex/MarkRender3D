from tkinter import *

window = Tk()
window.title("My Calculator")

# A.디스플레이창 2줄


#B. 값만 표시하기
display_1_txt = StringVar()
# 첫번째 디스플레이
display_1 = Entry(window, textvariable = display_1_txt, width=33, bg="yellow")
# 0번째 행 위치에 표시
display_1.grid(row=0, column=0, columnspan=5)

#값 더하기
display_2_txt = StringVar()

# 두번째 디스플레이
display_2 = Entry(window, textvariable = display_2_txt, width=33, bg="yellow")

# 1번째 행 위치에 표시
display_2.grid(row=1, column=0, columnspan=5)

#버튼추가
button_list = [
'MC',   'MR',   'M-',   'M+',   '%',
'√',    '7',    '8',    '9',    '/',
'OFF',    '4',    '5',    '6',    '*',
'CE',    '1',    '2',    '3',    '-',
'ON/C',    '0',    '.',    '=',    '+',]

# '=' 기능 구현
def equal_function():
    # 식의 값을 계산한다.
    result = eval(display_1_txt.get())
    # 정수를 문자로 변경한다.
    s = str(result)
    # 디스플레이 1번에 표시
    # B -> 추가가 아니고
    #display_1.insert(END, "=" + s)
        
    # B -> display 1과 연결된 변수에 대입
    display_1_txt.set(s)
    

#2.A 메모리 값 지우기 함수
def clear_txt() :
    display_2_txt.set('')

#2.B 메모리 값 불러오기 함수
def come_txt() :
     if display_2_txt.get() != '':
            display_1_txt.set(display_2_txt.get())

#2.C 메모리에 더하기 함수
def plus_txt() :
    result = eval(display_1.get())
    if display_2_txt.get() != '':
        result = int(display_2_txt.get()) + result
    display_2_txt.set(str(result))

#2.D 메모리에 빼기  함수
def minus_txt() :
    result = -eval(display_1_txt.get())
    if display_2_txt.get() != '':
        result = int(display_2_txt.get()) + result
            
    display_2_txt.set(str(result))


#100으로 나누어 실수로 표현 함수
def division_txt() :
    if display_1_txt.get() != '':
            result = eval(display_1_txt.get())
            result = result / 100
            display_1_txt.set(str(result))

#제곱근 구하기 함수
def square_root():
        if display_1_txt.get() != '':
            result = eval(display_1_txt.get())
            result = result ** 0.5
            display_1_txt.set(str(result))
            
# ce 기능 구현
def ce_f():
    txt = display_1_txt.get()
    txt_len = len(txt)
    while True:        
        if txt_len <= 0:
            break        
        
        if txt[txt_len-1] == '+': 
            display_1_txt.set(txt[:txt_len-1])
            break
        elif txt[txt_len-1] == '-':
            display_1_txt.set(txt[:txt_len-1])
            break
        elif txt[txt_len-1] == '*':
            display_1_txt.set(txt[:txt_len-1])
            break
        elif txt[txt_len-1] == '/':
            display_1_txt.set(txt[:txt_len-1])
            break
        
        txt_len -= 1

def click(key):
    # B -> '=' 클릭할 경우
    if key == "=":
        equal_function()
        
        
    # 2.A-> 메모리에 해당 값 지우기
    elif key == 'MC':
        clear_txt()

    #2.B -> 메모리값 불러오기
    elif key == 'MR':
        come_txt()
       
    # 2.C -> 메모리에 해당 값을 더하기
    elif key == 'M+':
        plus_txt()
                    
    
    # 2.D-> 메모리에 해당 값을 빼기
    elif key == 'M-':
        minus_txt()
       
        
    #100으로 나누어 실수로 표현
    elif key == '%':
        division_txt()


    #제곱근 구하기
    elif key == '√':
        square_root()
        
    # 3번 OFF(프로그램 종료)
    elif key == 'OFF':
        exit(1)
    # 3번 ON/C(계산 결과 지우고 디스플레이에 0 나타남)
    elif key == 'ON/C':
        display_1_txt.set('0')
        
    elif key == 'CE':
        ce_f()

    else:
        # B ->
        display_1_txt.set(display_1_txt.get() + key)
        #display_1.insert(END, key)

    

#2번째 행 위치로 변경
row_index = 2
col_index = 0
for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window, text=button_text, width=5,    
      command=process).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0

window.mainloop()
