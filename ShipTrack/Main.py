"""
 ShipTrack by Max Lareau
 - Easily track packages from different carriers in an easy to read format

 Main Class
"""

# Import packages
import tkinter as tk
import Package as package


# Main class
class Main(tk.Tk):

    shipments = []
    carrierslist = ["UPS", "FX", "ABF", "ADP"]

    def newshipmentpopup(self):
        popup = tk.Tk()
        popup.wm_title("New Shipment")
        popup.geometry("500x500")

        

        pk = package

        jobEntry = tk.StringVar()
        poEntry = tk.StringVar()
        fromEntry = tk.StringVar()
        dateEntry = tk.StringVar()
        trackingEntry = tk.StringVar()

        titlelabel = tk.Label(popup, text="Enter info into all fields, then press 'Add'")

        joblabel = tk.Label(popup, text="Job: ")
        entry1 = tk.Entry(popup, textvariable=jobEntry, justify="left")

        polabel = tk.Label(popup, text="PO: ")
        entry2 = tk.Entry(popup, textvariable=poEntry, justify="left")

        fromlabel = tk.Label(popup, text="From: ")
        entry3 = tk.Entry(popup, textvariable=fromEntry, justify="left")

        dateorderedlabel = tk.Label(popup, text="Date Ordered: ")
        entry4 = tk.Entry(popup, textvariable=dateEntry, justify="left")

        carrierlabel = tk.Label(popup, text="Carrier: ")
        entry5 = tk.Listbox(popup, selectmode="SINGLE")
        entry5.insert(0, self.carrierslist[0])
        entry5.insert(1, self.carrierslist[1])
        entry5.insert(2, self.carrierslist[2])
        entry5.insert(3, self.carrierslist[3])

        trackinglabel = tk.Label(popup, text="Tracking #: ")
        entry6 = tk.Entry(popup, textvariable=trackingEntry, justify="left")

        # Define setvalues method
        def setvalues():
            newPackage = pk.Package(str(jobEntry.get()),
                                str(poEntry.get()),
                                str(fromEntry.get()),
                                str(dateEntry.get()),
                                entry5.get('active'),
                                str(trackingEntry.get()))
            self.shipments.append(newPackage)

            popup.destroy()


        # Set values for new package
        donebutton = tk.Button(popup, text="Add", command=lambda: setvalues())

        # Grid placement
        titlelabel.grid(column=0, row=0, rowspan=2, sticky="nsew")

        joblabel.grid(column=0, row=1, sticky="nsew")
        entry1.grid(column=1, row=1, sticky="nsew")

        polabel.grid(column=0, row=2, sticky="nsew")
        entry2.grid(column=1, row=2, sticky="nsew")

        fromlabel.grid(column=0, row=3, sticky="nsew")
        entry3.grid(column=1, row=3, sticky="nsew")

        dateorderedlabel.grid(column=0, row=4, sticky="nsew")
        entry4.grid(column=1, row=4, sticky="nsew")

        carrierlabel.grid(column=0, row=5, sticky="nsew")
        entry5.grid(column=1, row=5, sticky="nsew")

        trackinglabel.grid(column=0, row=6, sticky="nsew")
        entry6.grid(column=1, row=6, sticky="nsew")

        donebutton.grid(column=0, row=7, rowspan=2, sticky="nsew")


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap
        tk.Tk.wm_title(self, "ShipTrack")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar)
        filemenu.add_command(label="New shipment...", command=lambda: self.newshipmentpopup())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: exit())
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self, menu=menubar)


app = Main()
app.geometry("1280x720")
app.mainloop()
