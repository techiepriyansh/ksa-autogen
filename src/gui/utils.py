import os, sys, re
import platform
from distutils.dir_util import copy_tree

def open_output_folder(folder):
  folder_directory = os.path.abspath(folder)
  if platform.system() == 'Windows':
    os.startfile(folder_directory, 'explore')
  elif platform.system() == 'Linux':
    os.system('xdg-open "' + folder_directory + '"')
  elif platform.system() == 'Darwin':
    os.system('open "' + folder_directory + '"')
  else:
    return False
  return True


def readConfig(pathToBinary, algoFuncs):
  configPath = os.path.join(pathToBinary, "config")

  configFiles = []
  for (dirpath, dirnames, filenames) in os.walk(configPath):
    configFiles.extend(filenames)
    break

  for configFile in configFiles:
    with open(os.path.join(configPath, configFile), "r") as f:
      exec(f.read())

  pat = re.compile(r"[A-Za-z_][A-Za-z0-9_]*_algo")
  for k,v in locals().items():
    if pat.fullmatch(k): algoFuncs[k] = v



def copyStaticFiles(pathToBinary, projectLocation):
  staticPath = os.path.join(pathToBinary, "static")
  copy_tree(staticPath, projectLocation)
