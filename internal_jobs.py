import pandas as pd
import json

def internal_job_creation(MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, JAN, FEB, MAR, APR):

    total_hours = 0

    internal_jobs = {"MAY": {"task category": [], "task service": [], "date": [], "hours": [] }, "JUN": {"task category": [], "task service": [], "date": [], "hours": [] }, 'JUL': {"task category": [], "task service": [], "date": [], "hours": []},
    "AUG": {"task category": [], "task service": [], "date": [], "hours": [] }, "SEP": {"task category": [], "task service": [], "date": [], "hours": [] }, "OCT" : {"task category": [], "task service": [], "date": [], "hours": [] },
    "NOV": {"task category": [], "task service": [], "date": [], "hours": [] }, "DEC": {"task category": [], "task service": [], "date": [], "hours": [] },
    "JAN": {"task category": [], "task service": [], "date": [], "hours": [] }, "FEB": {"task category": [], "task service": [], "date": [], "hours": []},
    "MAR": {"task category": [], "task service": [], "date": [], "hours": [] }, "APR": {"task category": [], "task service": [], "date": [], "hours": [] }}
    
    internal_jobs = dict(internal_jobs)
    print(type(internal_jobs))

    landscape_presence = 'False'
    poolservice_presence = 'False'

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
        day_1 = ['MAY 30'] * ((len(task_service)) // 2)
        day_2 = ['MAY 31'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
       #internal_jobs['May'] = {'task_category': task_category.to_list(), 'task_service': task_service.to_list(), 'date': date_scheduled}
        internal_jobs["MAY"]["task category"].extend(task_category.to_list())
        internal_jobs["MAY"]["task service"].extend(task_service.to_list())
        internal_jobs["MAY"]["date"].extend(date_scheduled)
        internal_jobs["MAY"]["hours"].extend(task_hour)


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
        day_1 = ['JUN 29'] * ((len(task_service)) // 2)
        day_2 = ['JUN 30'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        #internal_jobs['Jun'] = {'task_category': task_category.to_list(), 'task_service': task_service.to_list(), 'date': date_scheduled}
        internal_jobs["JUN"]["task category"].extend(task_category.to_list())
        internal_jobs["JUN"]["task service"].extend(task_service.to_list())
        internal_jobs["JUN"]["date"].extend(date_scheduled)
        internal_jobs["JUN"]["hours"].extend(task_hour)


    JUL['Hours'] = [float(i) for i in JUL['Hours']]
    h = (JUL[JUL['Type']=='INTERNAL']['Hours']).sum()
    
    print(h)
    print(JUL)
    print(JUL[JUL['Type']=='INTERNAL']['category'])
    print(type(task_category.to_list()))

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
        day_1 = ['JUL 30'] * ((len(task_service)) // 2)
        day_2 = ['JUL 31'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2



    if len(task_category) != 0:
        internal_jobs['JUL']['task category'].extend(task_category.to_list())
        internal_jobs['JUL']['task service'].extend(task_service.to_list())
        internal_jobs["JUL"]["hours"].extend(task_hour)
        internal_jobs['JUL']['date'].extend(date_scheduled)

    
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
        day_1 = ['AUG 30'] * ((len(task_service)) // 2)
        day_2 = ['AUG 31'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["AUG"]["task category"].extend(task_category.to_list())
        internal_jobs["AUG"]["task service"].extend(task_service.to_list())
        internal_jobs["AUG"]["hours"].extend(task_hour)
        internal_jobs["AUG"]["date"].extend(date_scheduled)


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
        day_1 = ['SEP 29'] * ((len(task_service)) // 2)
        day_2 = ['SEP 30'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["SEP"]["task category"].extend(task_category.to_list())
        internal_jobs["SEP"]["task service"].extend(task_service.to_list())
        internal_jobs["SEP"]["hours"].extend(task_hour)
        internal_jobs["SEP"]["date"].extend(date_scheduled)


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
        day_1 = ['OCT 30'] * ((len(task_service)) // 2)
        day_2 = ['OCT 31'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["OCT"]["task category"].extend(task_category.to_list())
        internal_jobs["OCT"]["task service"].extend(task_service.to_list())
        internal_jobs["OCT"]["hours"].extend(task_hour)
        internal_jobs["OCT"]["date"].extend(date_scheduled)



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
        day_1 = ['NOV 29'] * ((len(task_service)) // 2)
        day_2 = ['NOV 30'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["NOV"]["task category"].extend(task_category.to_list())
        internal_jobs["NOV"]["task service"].extend(task_service.to_list())
        internal_jobs["NOV"]["hours"].extend(task_hour)
        internal_jobs["NOV"]["date"].extend(date_scheduled)


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
        day_1 = ['DEC 30'] * ((len(task_service)) // 2)
        day_2 = ['DEC 31'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["DEC"]["task category"].extend(task_category.to_list())
        internal_jobs["DEC"]["task service"].extend(task_service.to_list())
        internal_jobs["DEC"]["hours"].extend(task_hour)
        internal_jobs["DEC"]["date"].extend(date_scheduled)


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
        day_1 = ['JAN 30'] * ((len(task_service)) // 2)
        day_2 = ['JAN 31'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["JAN"]["task category"].extend(task_category.to_list())
        internal_jobs["JAN"]["task service"].extend(task_service.to_list())
        internal_jobs["JAN"]["hours"].extend(task_hour)
        internal_jobs["JAN"]["date"].extend(date_scheduled)


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
        day_1 = ['FEB 27'] * ((len(task_service)) // 2)
        day_2 = ['FEB 28'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["FEB"]["task category"].extend(task_category.to_list())
        internal_jobs["FEB"]["task service"].extend(task_service.to_list())
        internal_jobs["FEB"]["hours"].extend(task_hour)
        internal_jobs["FEB"]["date"].extend(date_scheduled)


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
        day_1 = ['MAR 30'] * ((len(task_service)) // 2)
        day_2 = ['MAR 31'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["MAR"]["task category"].extend(task_category.to_list())
        internal_jobs["MAR"]["task service"].extend(task_service.to_list())
        internal_jobs["MAR"]["hours"].extend(task_hour)
        internal_jobs["MAR"]["date"].extend(date_scheduled)
  

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
        day_1 = ['APR 29'] * ((len(task_service)) // 2)
        day_2 = ['APR 30'] * ((len(task_service)) - ((len(task_service)) // 2))
        date_scheduled = day_1 + day_2

    if len(task_category) != 0:
        internal_jobs["APR"]["task category"].extend(task_category.to_list())
        internal_jobs["APR"]["task service"].extend(task_service.to_list())
        internal_jobs["APR"]["hours"].extend(task_hour)
        internal_jobs["APR"]["date"].extend(date_scheduled)


    internal_jobs = dict(internal_jobs)
    
    if 'Landscaping + Lawn Care' in json.dumps(internal_jobs):

        for key, value in internal_jobs.items():
           
            value['task category'].extend(['Landscaping + Lawn Care'])
            value['task service'].extend(['landscaping'])
            value['hours'].extend([2])
            value['date'].extend([f'{key} ' + '30'])
    
    if 'Pool' in internal_jobs:

        for key, value in internal_jobs.items():
           
            value['task category'].extend(['Pool'])
            value['task service'].extend(['Pool cleaning & maintenance'])
            value['hours'].extend([2])
            value['date'].extend([f'{key} ' + '30'])

    '''
    for key, value in internal_jobs.items():
            
            print(key)
            if len(list(value['task category'])) > 0:

                value['task category'].extend(['','','',''])
                value['task service'].extend(['Was work completed or is additional work needed ?','Notice time you spent and any product', 'Anything new discovered or mentioned by member', 'Add pre and post photos'])
                value['hours'].extend([0, 0, 0, 0])
                value['date'].extend([f'{key} ' + '30', f'{key} ' + '30', f'{key} ' + '30', f'{key} ' + '30'])
    '''

    #internal_jobs = {'internal jobs': internal_jobs}
    #internal_jobs = jsonpickle.encode(jsonpickle)

    internal_jobs = json.dumps(internal_jobs)

    return internal_jobs
