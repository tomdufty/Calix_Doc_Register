import time
import datetime
import pywintypes
import os
import main as main
import win32file
import win32con
import win32security

def get_time():
  now_seconds = time.time()
  now_pytime = pywintypes.Time(now_seconds)
  now_datetime = datetime.datetime(
    year=now_pytime.year,
    month=now_pytime.month,
    day=now_pytime.day,
    hour=now_pytime.hour,
    minute=now_pytime.minute,
    second=now_pytime.second)
  return  now_datetime


def get_user(FILENAME):
  try:
    sd = win32security.GetFileSecurity(FILENAME, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorOwner()
    name, domain, type = win32security.LookupAccountSid(None, owner_sid)
  except:
    print('failed')
  return name

ACTIONS = {
  1 : "Created",
  2 : "Deleted",
  3 : "Updated",
  4 : "Renamed from something",
  5 : "Renamed to something"
}
# Thanks to Claudio Grondi for the correct set of numbers
FILE_LIST_DIRECTORY = 0x0001

path_to_watch = "C:/Users/tomdu/Desktop"
def start_monitor():
  hDir = win32file.CreateFile (
    path_to_watch,
    FILE_LIST_DIRECTORY,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
  )
  while 1:
      #
      # ReadDirectoryChangesW takes a previously-created
      # handle to a directory, a buffer size for results,
      # a flag to indicate whether to watch subtrees and
      # a filter of what changes to notify.
      #
      # NB Tim Juchcinski reports that he needed to up
      # the buffer size to be sure of picking up all
      # events when a large number of files were
      # deleted at once.
      #
      results = win32file.ReadDirectoryChangesW (
        hDir,
        1024,
        True,
        win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
        win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
        win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
        win32con.FILE_NOTIFY_CHANGE_SIZE |
        win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
        win32con.FILE_NOTIFY_CHANGE_SECURITY,
        None,
        None
      )
      print (ACTIONS)
      for action, file in results:
          full_filename = os.path.join (path_to_watch, file)
          print (full_filename, ACTIONS.get(action, "Unknown"))
          if ACTIONS.get(action, "Unknown") == "Created":
              main.add_to_regsiter(full_filename)
          elif ACTIONS.get(action, "Unknown") == "Deleted":
              main.remove_from_register(full_filename)
          elif ACTIONS.get(action, "Unknown") == "Updated":
              print(os.stat(full_filename).st_atime)
              main.log_update(full_filename, get_time(), get_user(full_filename))