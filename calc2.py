#20211493 이주현

from tkinter import *  
import math

window = Tk()
window.title("Calculator") 

##############################################
# A. 디스플레이창 두 줄 나오게 하기

# B -> 첫 번째 줄 변수 선언
fst_dp = StringVar()
# B -> 첫 번째 디스플레이 생성
dp_1 = Entry(window, textvariable=fst_dp, width=40, bg="white")
# 첫 번째 디스플레이를 윈도우 0번째 행에 위치
dp_1.grid(row=0, column=0, columnspan=5)

# 2.C -> 두 번째 줄 변수 선언
snd_dp = StringVar()
# 두 번째 디스플레이 생성
dp_2 = Entry(window, textvariable=snd_dp, width=40, bg="white")
# 두 번째 디스플레이를 윈도우 1번째 행에 위치
dp_2.grid(row=1, column=0, columnspan=5)
################################################

# C -> 버튼 리스트 
button_list = [
    'MC', 'MR', 'M-', 'M+', '%',
    '√', '7', '8', '9', '/',
    'OFF', '4', '5', '6', '*',
    'CE', '1', '2', '3', '-',
    'ON/C', '0', '.', '=', '+'
]

# 0이 남아있는 경우
def all_clear():
    if fst_dp.get() == '0' :
        fst_dp.set('')
    if snd_dp.get() == '0' :
        snd_dp.set('')
        
# '=' 버튼이 클릭된 경우
def equal_function():
    try:
        result = eval(fst_dp.get())    
        fst_dp.set(str(result))
    except:
        fst_dp.set("Error")

# '√' 버튼이 클릭된 경우
def root_function():
    try:
        result = math.sqrt(eval(fst_dp.get()))
        fst_dp.set(str(result))
    except:
        fst_dp.set("Error")

# 'MC' 버튼이 클릭된 경우
def memory_clear():
    snd_dp.set('')

# 'MR' 버튼이 클릭된 경우
def memory_recall():
    if snd_dp.get() != '':
        fst_dp.set(snd_dp.get())

# 'M+' 버튼이 클릭된 경우
def memory_addition():
    if snd_dp.get() != '':
        result = float(snd_dp.get()) + eval(fst_dp.get())
        snd_dp.set(str(result))
    else:
        result = eval(fst_dp.get())
        snd_dp.set(str(result))

# 'M-' 버튼이 클릭된 경우
def memory_subtraction():
    if snd_dp.get() != '':
        result = float(snd_dp.get()) - eval(fst_dp.get())
        snd_dp.set(str(result))
    else:
        result = eval(fst_dp.get())

# '%' 버튼이 클릭된 경우
def percentage_function():
    if fst_dp.get() != '':
        fst_dp.set(str(float(eval(fst_dp.get()) / 100)))

# 'CE' 버튼이 클릭된 경우
def clear_entry():
    # 수식에 +,-,*,/ 기호가 포함되어있는지 확인하기
    if '+' in fst_dp.get() or '-' in fst_dp.get() or '*' in fst_dp.get() or '/' in fst_dp.get():
        # 마지막 연산자 이전의 수식만 남게 하기
        fst_dp.set(fst_dp.get()[:max(fst_dp.get().rfind('+'), fst_dp.get().rfind('-'), fst_dp.get().rfind('*'), fst_dp.get().rfind('/'))])
    else:
        # 연산자가 없다면 전체 수식 삭제하기
        fst_dp.set('') 

# 'ON/C' 버튼이 클릭된 경우
def reset():
    fst_dp.set('0')
    snd_dp.set('0')

# OFF 버튼을 누른 경우
def exit():
    window.quit()

# 호출되는 함수
def click(a):
    if a in "0123456789":
        all_clear()
    if a == "=":
        equal_function()
    elif a == '√':
        root_function()
    elif a == 'MC':
        memory_clear()
    elif a == 'MR':
        memory_recall()
    elif a == 'M+':
        memory_addition()
    elif a == 'M-':
        memory_subtraction()
    elif a == '%':
        percentage_function()
    elif a == 'CE':
        clear_entry()
    elif a == 'OFF':
        exit()
    elif a == 'ON/C':
        reset()
    else:
        # 나머지 버튼 클릭 시 입력된 값을 첫 번째 줄에 나오게 하기
        fst_dp.set(fst_dp.get() + a)

# 버튼표시
row_index = 2  # 버튼 행 위치
col_index = 0  # 버튼 열 위치
for button_text in button_list:
    # 각각의 버튼 클릭 시 나오는 함수 정의
    def process(t=button_text):
        click(t)
    # 버튼생성 설정하기 
    Button(window, text=button_text, width=10, command=process).grid(row=row_index, column=col_index)
    col_index += 1
    # 5개의 버튼이 한 줄이 될 수 있도록 구성하기 
    if col_index > 4:
        row_index += 1
        col_index = 0

window.mainloop()