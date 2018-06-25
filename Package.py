"""
 ShipTrack by Max Lareau
 - Easily track packages from different carriers in an easy to read format

 Package Class
 - Provides structure for each package being tracked by ShipTrack
 - Each package will have the following attributes:
    - Job
    - PO
    - From
    - Date Ordered
    - Carrier
    - Tracking #
"""

class Package:

    job = ""
    PO = ""
    frm = ""
    dateOrdered = ""
    carrier = ""
    tracking = ""

    def __init__(self, job, PO, frm, dateOrdered, carrier, tracking):
        self.job = job
        self.PO = PO
        self.frm = frm
        self.dateOrdered = dateOrdered
        self.carrier = carrier
        self.tracking = tracking
