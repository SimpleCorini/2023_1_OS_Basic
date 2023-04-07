from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def myFunc():
    messagebox.shwoinfo("강아지 버튼", "강아지가 커엽죠?")

## 메인 코드 부분 ##
window = Tk()

photo = PhotoImage(file = "gif/dog2.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()
