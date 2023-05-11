import pandas
import datetime
import math
from motionchart.motionchart import MotionChart
#read data
population=pandas.read_csv("data/ERP.csv")
hourseprice=pandas.read_csv("data/House_Price_Index.csv")
sa4=pandas.read_excel("data/SA4_Time_Series.xls",sheet_name="Time Series")
#clean data
sa4.drop(columns="Employment Rate (15-64)",inplace=True)
sa4.drop(columns="Participation Rate (15+)",inplace=True)
#rename columns
sa4.columns=["State","date","unemployment"]
rename_h=["date","NSW","VIC","QLD","SA","WA","TAS","NT","ACT"]
hourseprice.columns=rename_h
#melt data
hourseprice=hourseprice.melt(id_vars=["date"],value_vars=["NSW","VIC","QLD","SA","WA","TAS","NT","ACT"],var_name="State")
population=population.loc[:,["Unnamed: 0","Estimated Resident Population ;  Persons ;  Victoria ;","Estimated Resident Population ;  Persons ;  Queensland ;","Estimated Resident Population ;  Persons ;  South Australia ;","Estimated Resident Population ;  Persons ;  Western Australia ;","Estimated Resident Population ;  Persons ;  Tasmania ;","Estimated Resident Population ;  Persons ;  Northern Territory ;","Estimated Resident Population ;  Persons ;  Australian Capital Territory ;"]]
population.columns=["date","VIC","QLS","SA","WA","TAS","NT","ACT"]
population=pandas.melt(population,
    id_vars=["date"],
    value_vars=["VIC","QLS","SA","WA","TAS","NT","ACT"],
    var_name="State",
    value_name="population"
)
#to datetime
#test
population["date"]=pandas.to_datetime(population["date"],format="%d-%b-%y")
sa4["date"]=pandas.to_datetime(sa4["date"],format="%y-%m-%d")
hourseprice["date"]=pandas.to_datetime(hourseprice["date"],format="%d-%b-%y")
#merge data
total=pandas.merge(population,hourseprice,on=["date","State"])
final = pandas.merge(total, sa4, on=['date', 'State'])
mChart = MotionChart(df=final, key='date', x='population', y='value', xscale='linear', yscale='linear', size='unemployment', color='State')
mChart.to_notebook()