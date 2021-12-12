import tkinter as tk
from tkcalendar import DateEntry
import datetime
from API import API

def main():
    window = tk.Tk()
    window.geometry('300x250')
    window.title('Twitter Analysis')
    window.configure(bg='blue')

    uname_frame = tk.Frame(window)
    uname_frame.pack(anchor='center', expand=True)
    
    date_frame = tk.Frame(window)
    date_frame.pack(anchor='center', expand=True)

    label_name = tk.Label(uname_frame, text='Username @', bg='blue', fg='white')
    label_name.pack(side='left')
    
    uname = tk.StringVar()
    entry = tk.Entry(uname_frame, textvariable=uname)
    entry.pack(side='left')
    #entry.bind("<Return>", on_change) 

    label_date = tk.Label(date_frame, text="Tweet Sejak Tanggal", bg='blue', fg='white')
    label_date.pack(side='left')

    cal = DateEntry(date_frame,selectmode='day')
    cal.pack(side='left')

    but_frame = tk.Frame(window)
    but_frame.pack(anchor='center', expand=True)

    
    def submit():
        username = entry.get()
        datepicked = cal.get()
        new = API(username, datepicked)
        new.run()


    b_search = tk.Button(but_frame, text='Search', command=submit)
    b_search.pack()

    window.mainloop()

if __name__ == "__main__":
    main()