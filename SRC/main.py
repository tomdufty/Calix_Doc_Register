import main_ui
import sqlite3

#global variables
FEILDS_LIST = ['discipline','size','project','seqno','ver','desc','auth']
DISCIPLINE_CODES = ['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
DISCIPLINE_LIST = ['Architechtural','Process','Civil','Engineering Administration','Electrical','Finance/Accounting',
                   'General','Health, Safety and Environmental','Instrumentation and Control', 'Building', 'Manuals',
                   'Mechanical','Procurement','Piping','Quality Assurance/Control','MDR Documentation','Structrual',
                   '','','Vendor','','Client','','']

#main variables

tracked_dir = []


#open trackfile in install directory
def read_trackfile():
    print('reading trackfile')

#open sqlite and read document register
def read_doc_register(tracked_dir):
    print('reading document register')


def create_doc_register():
    print('new document register created')

# prepoluate tree
def populate_tree():
    print('populating filee tree')

def populate_form():
    print('popoulating form')



def add_tracked_file():
    print('new file tracked')

