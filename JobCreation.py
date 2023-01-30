import pandas as pd
from extracted_csv import extracted_csv
from internal_jobs import internal_job_creation
from contract_jobs import sub_contract_jobs
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/createjob')
def createjob():
    path = request.args.get('path')
    sheet = request.args.get('sheet')

    #read excel file and preprocess
    xls = pd.ExcelFile(path)
    data = pd.read_excel(xls, sheet)

    cust_name = data.columns[0]
    
    data.columns=data.iloc[7]
    print(data.columns)
    data = data[1:]

    #extract only useful columns from data
    extracted_data = extracted_csv(data)

    #split monthwise dataframes
    MAY = extracted_data[extracted_data["Month"].str.contains("MAY")]
    JUN = extracted_data[extracted_data["Month"].str.contains("JUN")]
    JUL = extracted_data[extracted_data["Month"].str.contains("JUL")]
    AUG = extracted_data[extracted_data["Month"].str.contains("AUG")]
    SEP = extracted_data[extracted_data["Month"].str.contains("SEP")]
    OCT = extracted_data[extracted_data["Month"].str.contains("OCT")]
    NOV = extracted_data[extracted_data["Month"].str.contains("NOV")]
    DEC = extracted_data[extracted_data["Month"].str.contains("DEC")]
    JAN = extracted_data[extracted_data["Month"].str.contains("JAN")]
    FEB = extracted_data[extracted_data["Month"].str.contains("FEB")]
    MAR = extracted_data[extracted_data["Month"].str.contains("MAR")]
    APR = extracted_data[extracted_data["Month"].str.contains("APR")]

    internal_jobs_json = internal_job_creation(MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, JAN, FEB, MAR, APR)

    contract_jobs_json = sub_contract_jobs(MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, JAN, FEB, MAR, APR)

    response = { 'customer_name': cust_name, 'internal_jobs' : internal_jobs_json, 'contract_jobs': contract_jobs_json }

    response = json.dumps(response)

    return response

if __name__ == "__main__":
    app.run()