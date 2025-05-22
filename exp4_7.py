import tkinter as tk #注释待补全，相关函数见书P141-144
def f1():
    id = v.get()
    sx = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
    y = int(id[6:10])
    index = (y-4) % 12
    s = sx[index]
    label3['text'] = "您的生肖为：" + s
root = tk.Tk()
root.title("查生肖")
root.geometry('360x150')
v = tk.StringVar()
v.set("")
label1 = tk.Label(root, text="身份证号码：")
text1 = tk.Entry(root, textvariable=v, width=30)
label2 = tk.Label(root, text="结果")
button1 = tk.Button(root, text="识别", command=f1)
label3 = tk.Label(root, text="", height=5, width=50, bg='white', anchor='nw', justify='left')
label1.grid(row=0, column=0)
text1.grid(row=0, column=1)
label2.grid(row=1, column=0)
button1.grid(row=0, column=2)
label3.grid(row=2, column=0, columnspan=3)
root.mainloop()