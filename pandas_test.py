import pandas as pd
import datetime

# Assumes the date format is something like 4/2001; adjust as necessary
date_format = '%m/%Y'

patient_start_dates: dict[str, datetime.datetime] = dict() 
# List to store "rows" of output data
# Each item is a tuple with a patient id and a span (start date and end date)
patient_spans: list[list] = []

# Read input file into Pandas dataframe (convert month_year data to datetime for ordering)
df = pd.read_csv('test_data.csv', parse_dates=['month_year'], date_format=date_format)

# Group by patient ID
grouped = df.groupby('patient_id')
for id, group in grouped:
    # Sort each group by ascending dates
    ordered_group = group.sort_values(by=['month_year'], ascending=True)
    if len(ordered_group)%2 == 1:
        raise Exception(f'Patient with id {id} has an odd number of dates')
    # For each consecutive set of dates, create a new "span" row for the current Id 
    for row_index, row in ordered_group.iterrows():
        #print(f"{name}  {row['month_year']}")
        if id in patient_start_dates:
            start_date = patient_start_dates[id]
            del patient_start_dates[id]
            patient_spans.append([id, start_date.strftime(date_format), row['month_year'].strftime(date_format)])
        else:
            patient_start_dates[id] = row['month_year']

# Data has been processed, can now create output
df_out = pd.DataFrame(patient_spans, columns=['patient_id', 'start_date', 'end_date'])
print(df_out)
#df_out.to_csv('processed_data.csv', index=False)  


exit(0)

# Everything below here was for testing
mydataset = {
    'patient_ids': ["1", "2", "1", "1", "4", "3", "3"],
    'month_year': ["1/2002", "2/2012", "1/2001", "1/2011", "4/2004", "3/2003", "3/2013"]
}

myvar = pd.DataFrame(mydataset)
myvar['month_year'] = pd.to_datetime(myvar['month_year'], format='%m/%Y')

# print(myvar)
# print(myvar.info())

min_sorted_df = df.sort_values(by=['patient_id'], ascending=True)
min_sorted_df = min_sorted_df.groupby('patient_id')['month_year'].min()

max_sorted_df = df.sort_values(by=['patient_id'], ascending=True)
max_sorted_df = max_sorted_df.groupby('patient_id')['month_year'].max()



print(min_sorted_df)
print(max_sorted_df)
print(df)
merged = pd.merge(min_sorted_df, max_sorted_df, how='left', on='patient_id')
print(merged)
#print(df.info())