import sqlite3 as db
from os import stat
import sys
from main_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5


#global variables
FEILDS_LIST = ['discipline','size','project','seqno','ver','desc','auth']
DISCIPLINE_CODES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z']
DISCIPLINE_LIST = ['Architechtural','Process','Civil','Engineering Administration','Electrical','Finance/Accounting',
                   'General','Health, Safety and Environmental','Instrumentation and Control', 'Building', 'Manuals',
                   'Mechanical','Procurement','Piping','Quality Assurance/Control','MDR Documentation','Structrual',
                   '','','Vendor','','Client','','']

#main variables
trackfile_loc = 'C/Users/HP/AppData/Local/CDM'
tracked_dir_list = []


#define overwriting class for main window - inherits QTMain window
class CDMMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        QtWidgets.QMainWindow.__init__(self, *args)

    def projectChanged(self):
        print("Received")

    def addProject(self):

        project_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        tracked_dir_list.append(project_path)
        print("project added")

    def projectChanged(self):
        populate_form()

    def updateFile(self):
        #open dialogue box -confrim overwriting of file
        print("renaming file")

### this section defines general functions

#open trackfile in install directory
def read_trackfile():
    print('reading trackfile')
    trackfile = db.connect(trackfile_loc)
    query = 'SELECT * FROM DIRECTORY_LIST'
    result = trackfile.execute(query).fetchall()
    for i in trackfile:
        tracked_dir_list.append()

def write_trackfile():
    print('writing trackfile')

#open sqlite and read document register
def read_doc_register(tracked_dir):
    print('reading document register')
    query = 'SELECT * FROM REGISTER'
    try:                            #attempt to connect to document register
        connection = db.connect(tracked_dir)
        result = connection.execute(query)

        #do someting with result
        populate_tree(result)

    except:
        print('failed to connect to document register')

    connection.close()

def create_doc_register(dir):
    print('new document register created')
    connection = db.connect(dir)
    create_table_query = 'CREATE TABLE RESGISTER'
    create_field_query = 'WITH RESISTER ADD %,%,%,%,%,%,%,%,%,%,%' # incorrect syntax to be fixed!
    connection.execute(create_table_query)
    connection.execute(create_field_query,FEILDS_LIST)
    connection.close()

# prepoluate tree
def populate_tree():
    print('populating filee tree')

def populate_form():
    print('popoulating form')


def add_tracked_file():
    print('new file tracked')


if __name__ == "__main__":
    # run main code
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = CDMMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
