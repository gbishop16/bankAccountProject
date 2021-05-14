# automatically display running time of a cell
%reload_ext autotime
# output results of multiple statements in one cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = “all”
# load libraries
from multiprocessing import freeze_support
from multiprocessing import Pool
from functools import partial
import threading
import pandas as pd
from time import sleep

# define a function that goes through the file and tries to find the account with maximum money
def check_account(file):
