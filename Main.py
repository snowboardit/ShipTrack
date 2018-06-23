"""
 ShipTrack by Max Lareau
 - Easily track packages from different carriers in an easy to read format

 Main Class
"""

# Import packages
from tkinter import *
from tkinter.ttk import *

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('PO', 'From', 'Status', 'Carrier', 'Tracking #')
        tv.heading("#0", text='Job', anchor='w')
        tv.column("#0", anchor="w", width=75)
        tv.heading('PO', text='PO')
        tv.column('PO', anchor='center', width=100)
        tv.heading('From',text='From')
        tv.column('From',anchor='center', width=100)
        tv.heading('Status', text='Status')
        tv.column('Status', anchor='center', width=200)
        tv.heading('Carrier', text='Carrier')
        tv.column('Carrier', anchor='center', width=100)
        tv.heading('Tracking #', text='Tracking #')
        tv.column('Tracking #', anchor='center', width=100)
        tv.grid(sticky=(N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text='AL-2010',
                             values=('1035661','Liberty','EST DELIV 6/25','UPS','1Z8974520362114785'))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()