import platform
import sys

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename

def ask_folder():
  root = Tk()
  root.withdraw()
  root.wm_attributes('-topmost', 1)
  folder = askdirectory(parent=root)
  root.update()

  return folder if bool(folder) else None