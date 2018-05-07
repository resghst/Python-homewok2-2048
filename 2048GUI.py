import Tkinter as tk

window = tk.Tk()
window.title('2048')
window.geometry('540x540')

context = []
color = ['#EEE4DA', '#eee4da', '#ede0c8', '#f2b179',
         '#f59563', '#f67c5f', '#f65e3b', '#edcf72',
         '#edcc61', '#edc850', '#edc53f', '#edc22e']
for i in range(16):
    k = tk.Label(window,
        text = '0', bg = '#EEE4DA',
        font=('Arial', 20), width = 8, height = 4
    )
    context.append(k)
    context[i].grid(column=i/4, row=i%4, padx=5, pady=5)



window.mainloop()

