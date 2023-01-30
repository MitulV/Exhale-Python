import pandas as pd

def extracted_csv(data):
    categoryList = []
    serviceList = []
    hoursList = []
    TypeLIst = []
    monthList = []

    for i in range(0,len(data)):
        category = data.iloc[i]['CATEGORY']
        categoryList.append(category)
        service = data.iloc[i]['SERVICE']
        serviceList.append(service)
        hours = data.iloc[i]['HOURS/VISIT']
        hoursList.append(hours)
        job_type = data.iloc[i]['INTERNAL/SUB']
        TypeLIst.append(job_type)
        
        jobfrequency = []

        for j in range(1,21):
            if data.iloc[i,j] == 'x':
                month = data.columns[j]
                jobfrequency.append(month)
        monthList.append(str(jobfrequency))

    dataex= {
        'category':categoryList,
        'service' :serviceList,
        'Hours':hoursList,
        'Type' : TypeLIst,
        'Month':monthList}

    extracted_data = pd.DataFrame(dataex)

    return extracted_data
