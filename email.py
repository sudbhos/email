import csv
import os.path
from datetime import datetime
from tabulate import tabulate
from comman_data.maling_parameter import recepients_email
from comman_data.formation_email import *

new_date=datetime.astimezone().strftime('%y-%m-%d %H:%M:%S %Z')
cur_date=datetime.now()
receiver=recepients_email

def set_email(id,file_path):
    global html
    if os.path.exists():
        with open(file_path) as input_file:
            reader=csv.reader(input_file)
            data=list(reader)
            html="""<html>
            <head>
            <style>
            table ,th,td {{bordar:1px solid black; border-collapse:collapse; text-align:center}}
            tr,td{{text-align center}}
            </style>
            </head><body>Need to enter the required details or email formate in this </body></html>"""
        html=html.format(table=tabulate(data,headers='firstrow',tablefmt='html')) +str(new_date)
        header="""<p>Greeting..<br> Details</br></p>"""
        subject=f"Welcome,{text}(str(new_date))"
        html_file=header+html
        file_to_Attache="c/myfolder/demo.txt"
        mail_reporting(subject,html_file,file_to_Attache,receiver)
