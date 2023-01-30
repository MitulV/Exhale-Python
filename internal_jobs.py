import pandas as pd
import json

def internal_job_creation(MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, JAN, FEB, MAR, APR):

    total_hours = 0

    internal_jobs = {"May": {"task category": [], "task service": [], "date": [], "hours": [] }, "Jun": {"task category": [], "task service": [], "date": [], "hours": [] }, 'Jul': {"task category": '', "task service": '', "date": [], "hours": ''},
    "Aug": {"task category": [], "task service": [], "date": [], "hours": [] }, "Sep": {"task category": [], "task service": [], "date": [], "hours": [] }, "Oct" : {"task category": [], "task service": [], "date": [], "hours": [] },
    "Nov": {"task category": [], "task service": [], "date": [], "hours": [] }, "Dec": {"task category": [], "task service": [], "date": [], "hours": [] },
    "Jan": {"task category": [], "task service": [], "date": [], "hours": [] }, "Feb": {"task category": [], "task service": [], "date": [], "hours": []},
    "Mar": {"task category": [], "task service": [], "date": [], "hours": [] }, "Apr": {"task category": [], "task service": [], "date": [], "hours": [] }}
    
    internal_jobs = dict(internal_jobs)
    print(type(internal_jobs))

    MAY['Hours'] = [float(i) for i in MAY['Hours']]
    h = (MAY[MAY['Type']=='INTERNAL']['Hours']).sum()

    if(h < 8):
        task_category = MAY[MAY['Type']=='INTERNAL']['category']
        task_service = MAY[MAY['Type']=='INTERNAL']['service'] 
        task_hour = MAY[MAY['Type']=='INTERNAL']['Hours']
        date_scheduled = ['MAY 31'] * len(task_service)

    if(h > 7):
        task_category = MAY[MAY['Type']=='INTERNAL']['category']
        task_service = MAY[MAY['Type']=='INTERNAL']['service']
        task_hour = MAY[MAY['Type']=='INTERNAL']['Hours']
        date_scheduled = ['MAY 29', 'MAY 30'] * int(len(task_service)/2)

    if len(task_category) != 0:
       #internal_jobs['May'] = {'task_category': task_category.to_list(), 'task_service': task_service.to_list(), 'date': date_scheduled}
        internal_jobs["May"]["task category"].extend(task_category.to_list())
        internal_jobs["May"]["task service"].extend(task_service.to_list())
        internal_jobs["May"]["date"].extend(date_scheduled)
        internal_jobs["May"]["hours"].extend(task_hour)
    else:
        internal_jobs['May'] = 'no jobs scheduled'

    JUN['Hours'] = [float(i) for i in JUN['Hours']]
    h = (JUN[JUN['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = JUN[JUN['Type']=='INTERNAL']['category']
        task_service = JUN[JUN['Type']=='INTERNAL']['service'] 
        task_hour = JUN[JUN['Type']=='INTERNAL']['Hours']
        date_scheduled = ['JUN 30'] * len(task_service)
    
    if(h > 7):
        task_category = JUN[JUN['Type']=='INTERNAL']['category']
        task_service = JUN[JUN['Type']=='INTERNAL']['service']
        task_hour = JUN[JUN['Type']=='INTERNAL']['Hours']
        date_scheduled = ['JUN 29', 'JUN 30'] * int(len(task_service)/2)

    if len(task_category) != 0:
        #internal_jobs['Jun'] = {'task_category': task_category.to_list(), 'task_service': task_service.to_list(), 'date': date_scheduled}
        internal_jobs["Jun"]["task category"].extend(task_category.to_list())
        internal_jobs["Jun"]["task service"].extend(task_service.to_list())
        internal_jobs["Jun"]["date"].extend(date_scheduled)
        internal_jobs["Jun"]["hours"].extend(task_hour)
    else:
        internal_jobs['Jun'] = 'no jobs scheduled'

    JUL['Hours'] = [float(i) for i in JUL['Hours']]
    h = (JUL[JUL['Type']=='INTERNAL']['Hours']).sum()
    
    print(h)
    print(JUL)
    print(JUL[JUL['Type']=='INTERNAL']['category'])

    total_hours += h

    if(h < 8):
        print('less than 7')
        task_category = JUL[JUL['Type']=='INTERNAL']['category']
        task_service = JUL[JUL['Type']=='INTERNAL']['service']
        task_hour = JUL[JUL['Type']=='INTERNAL']['Hours']
        date_scheduled = ['JUL 31'] 

    if(h > 7):
        print('grater than 7')
        task_category = JUL[JUL['Type']=='INTERNAL']['category']
        task_service = JUL[JUL['Type']=='INTERNAL']['service']
        task_hour = JUL[JUL['Type']=='INTERNAL']['Hours']
        date_scheduled = ['JUL 30', 'JUl 31'] * int(len(task_service)/2)

    print('JULY TEST DATA:::::::: ', task_category)

    if len(task_category) != 0:
        #internal_jobs['Jul'] = {'task_category': task_category.to_list(), 'task_service': task_service.to_list(), 'date': date_scheduled}
        internal_jobs['Jul']['task category'] = str(task_category.values)
        internal_jobs['Jul']['task service'] = str(task_service.values)
        internal_jobs["Jul"]["hours"] = str(h)
        internal_jobs['Jul']['date'].extend(date_scheduled)
    else:
        internal_jobs['Jul'] = 'no jobs scheduled'
    
    AUG['Hours'] = [float(i) for i in AUG['Hours']]
    h = (AUG[AUG['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = AUG[AUG['Type']=='INTERNAL']['category']
        task_service = AUG[AUG['Type']=='INTERNAL']['service'] 
        task_hour = AUG[AUG['Type']=='INTERNAL']['Hours']
        date_scheduled = ['AUG 31'] * len(task_service)

    if(h > 7):
        task_category = AUG[AUG['Type']=='INTERNAL']['category']
        task_service = AUG[AUG['Type']=='INTERNAL']['service']
        task_hour = AUG[AUG['Type']=='INTERNAL']['Hours']
        date_scheduled = ['AUG 30', 'AUG 31'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Aug"]["task category"].extend(task_category.to_list())
        internal_jobs["Aug"]["task service"].extend(task_service.to_list())
        internal_jobs["Aug"]["hours"].extend(task_hour)
        internal_jobs["Aug"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Aug'] = 'no jobs scheduled'

    SEP['Hours'] = [float(i) for i in SEP['Hours']]
    h = (SEP[SEP['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = SEP[SEP['Type']=='INTERNAL']['category']
        task_service = SEP[SEP['Type']=='INTERNAL']['service'] 
        task_hour = SEP[SEP['Type']=='INTERNAL']['Hours']
        date_scheduled = ['SEP 30'] * len(task_service)

    if(h > 7):
        task_category = SEP[SEP['Type']=='INTERNAL']['category']
        task_service = SEP[SEP['Type']=='INTERNAL']['service']
        task_hour = SEP[SEP['Type']=='INTERNAL']['Hours']
        date_scheduled = ['SEP 29', 'SEP 30'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Sep"]["task category"].extend(task_category.to_list())
        internal_jobs["Sep"]["task service"].extend(task_service.to_list())
        internal_jobs["Sep"]["hours"].extend(task_hour)
        internal_jobs["Sep"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Sep'] = 'no jobs scheduled'

    OCT['Hours'] = [float(i) for i in OCT['Hours']]
    h = (OCT[OCT['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = OCT[OCT['Type']=='INTERNAL']['category']
        task_service = OCT[OCT['Type']=='INTERNAL']['service'] 
        task_hour = OCT[OCT['Type']=='INTERNAL']['Hours']
        date_scheduled = ['OCT 31'] * len(task_service)

    if(h > 7):
        task_category = OCT[OCT['Type']=='INTERNAL']['category']
        task_service = OCT[OCT['Type']=='INTERNAL']['service']
        task_hour = OCT[OCT['Type']=='INTERNAL']['Hours']
        date_scheduled = ['OCT 30', 'OCT 31'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Oct"]["task category"].extend(task_category.to_list())
        internal_jobs["Oct"]["task service"].extend(task_service.to_list())
        internal_jobs["Oct"]["hours"].extend(task_hour)
        internal_jobs["Oct"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Oct'] = 'no jobs scheduled'


    NOV['Hours'] = [float(i) for i in NOV['Hours']]
    h = (NOV[NOV['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = NOV[NOV['Type']=='INTERNAL']['category']
        task_service = NOV[NOV['Type']=='INTERNAL']['service'] 
        task_hour = NOV[NOV['Type']=='INTERNAL']['Hours']
        date_scheduled = ['NOV 30'] * len(task_service)

    if(h > 7):
        task_category = NOV[NOV['Type']=='INTERNAL']['category']
        task_service = NOV[NOV['Type']=='INTERNAL']['service']
        task_hour = NOV[NOV['Type']=='INTERNAL']['Hours']
        date_scheduled = ['NOV 29', 'NOV 30'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Nov"]["task category"].extend(task_category.to_list())
        internal_jobs["Nov"]["task service"].extend(task_service.to_list())
        internal_jobs["Nov"]["hours"].extend(task_hour)
        internal_jobs["Nov"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Nov'] = 'no jobs scheduled'

    DEC['Hours'] = [float(i) for i in DEC['Hours']]
    h = (DEC[DEC['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = DEC[DEC['Type']=='INTERNAL']['category']
        task_service = DEC[DEC['Type']=='INTERNAL']['service'] 
        task_hour = DEC[DEC['Type']=='INTERNAL']['Hours']
        date_scheduled = ['DEC 31'] * len(task_service)

    if(h > 7):
        task_category = DEC[DEC['Type']=='INTERNAL']['category']
        task_service = DEC[DEC['Type']=='INTERNAL']['service']
        task_hour = DEC[DEC['Type']=='INTERNAL']['Hours']
        date_scheduled = ['DEC 30', 'DEC 31'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Dec"]["task category"].extend(task_category.to_list())
        internal_jobs["Dec"]["task service"].extend(task_service.to_list())
        internal_jobs["Dec"]["hours"].extend(task_hour)
        internal_jobs["Dec"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Dec'] = 'no jobs scheduled'

    JAN['Hours'] = [float(i) for i in JAN['Hours']]
    h = (JAN[JAN['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = JAN[JAN['Type']=='INTERNAL']['category']
        task_service = JAN[JAN['Type']=='INTERNAL']['service'] 
        task_hour = JAN[JAN['Type']=='INTERNAL']['Hours']
        date_scheduled = ['JAN 31'] * len(task_service)

    if(h > 7):
        task_category = JAN[JAN['Type']=='INTERNAL']['category']
        task_service = JAN[JAN['Type']=='INTERNAL']['service']
        task_hour = JAN[JAN['Type']=='INTERNAL']['Hours']
        date_scheduled = ['JAN 30', 'JAN 31'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Jan"]["task category"].extend(task_category.to_list())
        internal_jobs["Jan"]["task service"].extend(task_service.to_list())
        internal_jobs["Jan"]["hours"].extend(task_hour)
        internal_jobs["Jan"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Jan'] = 'no jobs scheduled'

    FEB['Hours'] = [float(i) for i in FEB['Hours']]
    h = (FEB[FEB['Type']=='INTERNAL']['Hours']).sum()
    
    total_hours += h



    if(h < 8):
        task_category = FEB[FEB['Type']=='INTERNAL']['category']
        task_service = FEB[FEB['Type']=='INTERNAL']['service'] 
        task_hour = FEB[FEB['Type']=='INTERNAL']['Hours']
        date_scheduled = ['FEB 28'] * len(task_service)

    if(h > 7):
        task_category = FEB[FEB['Type']=='INTERNAL']['category']
        task_service = FEB[FEB['Type']=='INTERNAL']['service']
        task_hour = FEB[FEB['Type']=='INTERNAL']['Hours']
        date_scheduled = ['FEB 27', 'FEB 28'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Feb"]["task category"].extend(task_category.to_list())
        internal_jobs["Feb"]["task service"].extend(task_service.to_list())
        internal_jobs["Feb"]["hours"].extend(task_hour)
        internal_jobs["Feb"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Feb'] = 'no jobs scheduled'

    MAR['Hours'] = [float(i) for i in MAR['Hours']]
    h = (MAR[MAR['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = MAR[MAR['Type']=='INTERNAL']['category']
        task_service  = MAR[MAR['Type']=='INTERNAL']['service'] 
        task_hour = MAR[MAR['Type']=='INTERNAL']['Hours']
        date_scheduled = ['MAR 30'] * len(task_service)

    if(h > 7):
        task_category = MAR[MAR['Type']=='INTERNAL']['category']
        task_service = MAR[MAR['Type']=='INTERNAL']['service']
        task_hour = MAR[MAR['Type']=='INTERNAL']['Hours']
        date_scheduled = ['MAR 29', 'MAR 30'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Mar"]["task category"].extend(task_category.to_list())
        internal_jobs["Mar"]["task service"].extend(task_service.to_list())
        internal_jobs["Mar"]["hours"].extend(task_hour)
        internal_jobs["Mar"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Mar'] = 'no jobs scheduled'

    APR['Hours'] = [float(i) for i in APR['Hours']]
    h = (APR[APR['Type']=='INTERNAL']['Hours']).sum()

    total_hours += h

    if(h < 8):
        task_category = APR[APR['Type']=='INTERNAL']['category']
        task_service = APR[APR['Type']=='INTERNAL']['service'] 
        task_hour = APR[APR['Type']=='INTERNAL']['Hours']
        date_scheduled = ['APR 30'] * len(task_service)

    if(h > 7):
        task_category = APR[APR['Type']=='INTERNAL']['category']
        task_service = APR[APR['Type']=='INTERNAL']['service']
        task_hour = APR[APR['Type']=='INTERNAL']['Hours']
        date_scheduled = ['APR 29', 'APR 30'] * int(len(task_service)/2)

    if len(task_category) != 0:
        internal_jobs["Apr"]["task category"].extend(task_category.to_list())
        internal_jobs["Apr"]["task service"].extend(task_service.to_list())
        internal_jobs["Apr"]["hours"].extend(task_hour)
        internal_jobs["Apr"]["date"].extend(date_scheduled)
    else:
        internal_jobs['Apr'] = 'no jobs scheduled'
    

    #internal_jobs = {'internal jobs': internal_jobs}
    #internal_jobs = jsonpickle.encode(jsonpickle)

    internal_jobs = json.dumps(internal_jobs)

    return internal_jobs