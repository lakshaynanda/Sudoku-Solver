from tkinter import *
from tkinter import messagebox
master = Tk()
master.title('Sudoku')
e = [[0 for x in range(9)]for y in range(9)]
matrix = [[0 for x in range(9)]for y in range(9)]
SIZE = 9


def close_window():
    if messagebox.askyesno('Verify', 'Really quit?'):
        master.destroy()


def number_unassigned(row, col):
    num_unassign = 0
    for i in range(0, SIZE):
        for j in range(9):
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a


def is_safe(n, r, c):
    for i in range(9):
        if matrix[r][i] == n:
            return False
    for i in range(9):
        if matrix[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if matrix[i][j] == n:
                return False
    return True


def solve_sudoku():
    row = 0
    col = 0
    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    for i in range(1, 10):
        if is_safe(i, row, col):
            matrix[row][col] = i
            if solve_sudoku():
                return True
            matrix[row][col] = 0
    return False


def show_entry_fields():
    for i in range(9):
        for j in range(9):
            matrix[i][j] = int(e[i][j].get())
    if solve_sudoku()==True:
        messagebox.showinfo("Success!","Sudoku solved successfully")
        for i in range(9):
            for j in range(9):
                e[i][j].delete(0,END)
                e[i][j].insert(0,matrix[i][j])
                if((i>=0 and i<=2 and ((j>=0 and j<=2) or (j>=6 and j<=8))) or (i>=6 and i<=8 and((j>=0 and j<=2) or (j>=6 and j<=8))) or (i>=3 and i<=5 and j>=3 and j<=5) ):
                    e[i][j].config(bg='#C2FCCF',bd=0.1,highlightcolor='black',justify=CENTER)
                else:
                    e[i][j].config(bg='#8AFCA3',bd=0.1,highlightcolor='black',justify=CENTER)
    elif solve_sudoku()==False:
        messagebox.showinfo("Error!","Sudoku not solvable...")
        master.destroy()

for i in range(9):
    for j in range(9):
        e[i][j]=Entry(master,width=4)
        e[i][j].grid(row=i,column=j,sticky='NSEW')
        e[i][j].insert(0,0)
        if((i>=0 and i<=2 and ((j>=0 and j<=2) or (j>=6 and j<=8))) or (i>=6 and i<=8 and((j>=0 and j<=2) or (j>=6 and j<=8))) or (i>=3 and i<=5 and j>=3 and j<=5) ):
            e[i][j].config(bg='#97EAFF',bd=0.1,highlightcolor='black',justify=CENTER)
        else:
            e[i][j].config(bg='#BFF2FF',bd=0.1,highlightcolor='black',justify=CENTER) 
    Button(master,relief=FLAT,text='Submit',command=show_entry_fields,bg='#CFCFCF',foreground='black',highlightbackground='#3E4149',width=10,height=1).grid(row=9,column=3,pady=2,columnspan=3)
    Button(master,relief=FLAT,text='Exit',command=close_window,bg='#CFCFCF',foreground='black',highlightbackground='#3E4149',width=10,height=1).grid(row=10,column=3,pady=2,columnspan=3)
mainloop() 