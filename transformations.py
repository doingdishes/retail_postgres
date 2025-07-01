import pandas as pd

'''
first, we define where the excel file is
next, we read the file. by default it reads the first sheet, but this can be modified
finally, we save the df to csv
'''

excel_file = 'path to xlsx'

df = pd.read_excel(excel_file, engine='openpyxl')

csv_file = 'path to save the csv to'

df.to_csv(csv_file, index=False) #index determines if it will right the leftmost label of the dataframe to the csv file


