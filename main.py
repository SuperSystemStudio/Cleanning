import configparser
import os
import sys
config.read("path.ini")
config=configparser.ConfigParser()
config = open("./path.ini"，"r")
if config.read() == "":
  config.add_section("path")
  for root in os.walk("C:\Users\Lenovo\AppData\Local\kingsoft\WPS Cloud Files\userdata\qing\filecache"):
    if root != ".3172735" or root != "configbackup":
      config.set("path","WPS","C:\Users\Lenovo\AppData\Local\kingsoft\WPS Cloud Files\userdata\qing\filecache"+root)
if sys.argv[1] == "clean":
  for a in config.sections("path")
    for i in config.get("path", a)
  os.removedirs(i)
