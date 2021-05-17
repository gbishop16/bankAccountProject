# automatically display running time of a cell

# output results of multiple statements in one cell
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = “all”
# load libraries
from multiprocessing import freeze_support
from multiprocessing import Pool
from functools import partial
import threading
import pandas as pd
from time import sleep
import timeit

# define a function that goes through the file and tries to find the account with maximum money
def check_account(file):





# mutithreading version
def func_thread(file, out):
    out.append(check_account(file))
x_ls =list(range(num_max))
thread_list = []
results = []
for x in x_ls:
 thread = threading.Thread(target=func_thread, args=(x, results))
 thread_list.append(thread)
for thread in thread_list:
 thread.start()
for thread in thread_list:
 thread.join()


 #check the multithreading autotime
 print sec(timeit.Timer())
