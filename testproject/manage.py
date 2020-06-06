import os
import sys

from proj.settings import BASE_DIR

sys.path.append(os.path.dirname(BASE_DIR))

from myframe.myframeadmin import run_command

os.environ.setdefault('MYFRAME_SETTINGS_MODULE', 'proj.settings')

run_command(*sys.argv)
