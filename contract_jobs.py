import pandas as pd
import json

def sub_contract_jobs(MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, JAN, FEB, MAR, APR):

    contract_jobs = {"May": {"task category": [], "task service": [], "date": [] }, "Jun": {"task category": [], "task service": [], "date": [] }, 'Jul': {"task category": [], "task service": [], "date": []},
    "Aug": {"task category": [], "task service": [], "date": [] }, "Sep": {"task category": [], "task service": [], "date": [] }, "Oct" : {"task category": [], "task service": [], "date": [] },
    "Nov": {"task category": [], "task service": [], "date": [] }, "Dec": {"task category": [], "task service": [], "date": [] },
    "Jan": {"task category": [], "task service": [], "date": [] }, "Feb": {"task category": [], "task service": [], "date": [] },
    "Mar": {"task category": [], "task service": [], "date": [] }, "Apr": {"task category": [], "task service": [], "date": [] }} 

    sub_jobs = MAY[MAY['Type']=='SUB']
    sub_jobs = sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['MAY 31'] * len(sub_jobs['category'].to_list())
    

    if len(sub_jobs) != 0 :
        contract_jobs["May"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["May"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["May"]["date"].extend(date_scheduled)
    else:
        contract_jobs['May'] = 'no jobs scheduled'

    
    sub_jobs = JUN[JUN['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['JUN 30'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Jun"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Jun"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Jun"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Jun'] = 'no jobs scheduled'

    sub_jobs = JUL[JUL['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['JUL 31'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Jul"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Jul"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Jul"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Jul'] = 'no jobs scheduled'

    sub_jobs = AUG[AUG['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['AUG 31'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Aug"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Aug"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Aug"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Aug'] = 'no jobs scheduled'

    sub_jobs = SEP[SEP['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['SEP 30'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Sep"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Sep"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Sep"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Sep'] = 'no jobs scheduled'

    
    sub_jobs = OCT[OCT['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['OCT 31'] * len(sub_jobs['category'].to_list())
    if len(sub_jobs) != 0 :
        contract_jobs["Oct"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Oct"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Oct"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Oct'] = 'no jobs scheduled'

    sub_jobs = NOV[NOV['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['NOV 30'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Nov"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Nov"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Nov"]["date"].extend(date_scheduled)
    else:
        contract_jobs['NOV'] = 'no jobs scheduled'

    sub_jobs = DEC[DEC['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['DEC 31'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Dec"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Dec"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Dec"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Dec'] = 'no jobs scheduled'

    sub_jobs = JAN[JAN['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()

    if len(sub_jobs) != 0 :
        contract_jobs["Jan"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Jan"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Jan"]["date"].extend(date_scheduled)
        date_scheduled = ['JAN 31'] * len(sub_jobs['category'].to_list())
    else:
        contract_jobs['Jan'] = 'no jobs scheduled'

    sub_jobs = FEB[FEB['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['FEB 28'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Feb"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Feb"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Feb"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Feb'] = 'no jobs scheduled'

    sub_jobs = MAR[MAR['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['MAR 30'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Mar"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Mar"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Mar"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Mar'] = 'no jobs scheduled'

    sub_jobs = APR[APR['Type']=='SUB']
    sub_jobs.groupby(['category'])['service'].apply(lambda x: ','.join(x)).reset_index()
    date_scheduled = ['APR 30'] * len(sub_jobs['category'].to_list())

    if len(sub_jobs) != 0 :
        contract_jobs["Apr"]["task category"].extend(sub_jobs['category'].to_list())
        contract_jobs["Apr"]["task service"].extend(sub_jobs['service'].to_list())
        contract_jobs["Apr"]["date"].extend(date_scheduled)
    else:
        contract_jobs['Apr'] = 'no jobs scheduled'


    #print(dict(contract_jobs))

    #contract_jobs = jsonpickle.encode(contract_jobs)
    
    #contract_jobs ={'contract_jobs': contract_jobs}
    contract_jobs = json.dumps(contract_jobs)

    return contract_jobs
