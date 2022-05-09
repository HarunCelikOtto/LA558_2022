from operator import index
from pickle import TRUE
import string
import pandas as pd

#Import file
df = pd.read_excel("TestData.xlsx")
df2 = pd.read_excel("TestData_One.xlsx")
df1 = pd.read_excel("blanktest.xlsx", sheet_name="All1")

#Column heads replace blankspace with '_'
df.columns = df.columns.str.replace(" ", "_")
df1.columns = df1.columns.str.replace(" ", "_")

#Function to add data from old file to new excel file
def add_data():
    #Defining data values from an external excel file
    StartDayExtract = df1["Start_Date"].astype("string")
    EndDayExtract = df1["End_Date"]
    LocationNameExtract = df1["Location_Name"]
    LocationTypeExtract = df1["Location_Type"]
    LocationExtraExtract = df1["Location_Extra"]
    DiseaseTypeExtract = df1["Disease_Type"]
    ReportedCasesExtract = df1["Reported_Cases"]
    DeathsExtract = df1["Deaths"]
    LongitudeExtract = df1["Longitude"]
    LatitudeExtract = df1["Latitude"]
    
    df.insert(0, "Start_Date_Calc", StartDayExtract, allow_duplicates=False)
    df.insert(1, "End_Date_Calc", EndDayExtract, allow_duplicates=False)
    df.insert(8, "Location_Name", LocationNameExtract, allow_duplicates=False)
    df.insert(9, "Location_Extra", LocationExtraExtract, allow_duplicates=False)
    df.insert(10, "Location_Type", LocationTypeExtract, allow_duplicates=False)
    df.insert(11, "Disease_Type", DiseaseTypeExtract, allow_duplicates=False)
    df.insert(12, "Reported_Cases", ReportedCasesExtract, allow_duplicates=False)
    df.insert(13, "Deaths", DeathsExtract, allow_duplicates=False)
    df.insert(14, "Longitude", LongitudeExtract, allow_duplicates=False)
    df.insert(15, "Latitude", LatitudeExtract, allow_duplicates=False)
add_data()

#Save for next function to work
df.to_excel("TestData_One.xlsx", index=False)

#Function to parse the dates
list_length = len(df2["Start_Date_Calc"])
def parse_dates():
    total_start_date = df2.loc[start_pos, "Start_Date_Calc"]
    total_end_date = df2.loc[start_pos, "End_Date_Calc"]
    def add_start_dates():
        df2.loc[start_pos, "Start_Year"] = start_year
        df2.loc[start_pos, "Start_Month"] = start_month 
        df2.loc[start_pos, "Start_Day"] = start_day
    def add_end_dates():
        df2.loc[start_pos, "End_Year"] = end_year 
        df2.loc[start_pos, "End_Month"] = end_month 
        df2.loc[start_pos, "End_Day"] = end_day

    if pd.isna(total_start_date) != True:
        total_start_date = total_start_date.replace(".", "")
        start_day = pd.to_numeric(total_start_date[0:2])  
        start_month = pd.to_numeric(total_start_date[2:4])
        start_year = pd.to_numeric(total_start_date[4:8])
        add_start_dates()

    if pd.isna(total_end_date) != True:
        total_end_date = total_end_date.replace(".", "")
        end_day = pd.to_numeric(total_end_date[0:2])
        end_month = pd.to_numeric(total_end_date[2:4])
        end_year = pd.to_numeric(total_end_date[4:8])
        add_end_dates()
        

#Automating Loop to iterate through each column
for start_pos in range(0, list_length):
    parse_dates()
    start_pos += 1

#FILE SAVE
df2.to_excel("TestData_Final.xlsx", index=False)
print("Save Complete")