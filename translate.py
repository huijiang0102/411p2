import pandas as pd
import numpy as np
import re

while True:
    df_result = pd.DataFrame({'A' : []})
    command = input("Type the your SQL and press Enter.")
    if len(command) < 1:  # check prevents a crash when indexing to 1st character
       continue
    sqlList = [] #Create the list to store the SQL
    sqlList = command.split()
    fileList = sqlList[3].split(',') #Retrieve one or more filename

    #FROM: Get the outer join of several tables or the content of one single file
    if len(fileList)== 1:
        fileName = fileList[0] + '.csv'
        df_result = pd.read_csv(fileName)
    else:
        for i in range(len(fileList)):
            fileName = fileList[i] + '.csv'
            df1 = pd.read_csv(fileName)
            if df_result.empty:
                df_result = df1
                continue
            else:
                df_result = pd.merge(df1, df_result, how='outer')

    #WHERE: Deal with the conditions
    a = 'a = b and c > d or c > e'
    if any(re.findall(r'and|or|not', a, re.IGNORECASE)):
        # When there are boolean conditions
        if a.find('and'):
            andList = []
            andList = a.split('and')
            print(andList)
        elif a.find('or'):
            orList = a.split('or')
            print(len(orList))
        elif a.find('not'):
            notList = a.split('not')
            print(len(notList))
    else:
        # When there is no boolean conditions, see if it has LIKE or any > < = <= >=
        if any(re.findall(r'like', a, re.IGNORECASE)):
            # Find the key word with LIKE
            userinput = "%123%"
            str = 'a123b12345454'
            userinput = userinput.replace('%', '(.+?)')
            if re.findall(userinput, str):
                print("bingo")  # If matching successfully, then do something(ex: retrieve the matching data

        else: # Find the > < = <= >= and return the expected data


    #SELECT: Get the column(attributes) from file
    attList = sqlList[1].split(',')
    print(df_result[attList])