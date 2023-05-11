from motionchart.motionchart import MotionChart, MotionChartDemo
import pandas as pd
import numpy as np
import datetime
erp_raw=pd.read_csv("data/ERP.csv")
hpi_raw=pd.read_csv("data/House_Price_Index.csv")
rate_raw=pd.read_excel("data/SA4_Time_Series.xls",sheet_name="Time Series")

state_cols = ['Time','NSW','VIC','QLD','SA','WA','TAS','NT','ACT']
rate_cols = ['State','Time','Unemployment Rate']

#ERP_by state and gender
erp = erp_raw.iloc[:,[0,19,20,21,22,23,24,25,26]]
erp.columns = state_cols

#House Price Index
hpi_raw.columns = state_cols

#SA4 Time Series - October 2016
rate = rate_raw.iloc[:,[0,1,3]]
rate.columns = rate_cols
erp_reform = pd.melt(erp, id_vars=['Time'],value_vars=['NSW','VIC','QLD','SA','WA','TAS','NT','ACT'],var_name='State')
erp_reform.rename(columns = {'value':'Population'}, inplace = True)
hpi_reform = pd.melt(hpi_raw, id_vars=['Time'],value_vars=['NSW','VIC','QLD','SA','WA','TAS','NT','ACT'],var_name='State')
hpi_reform.rename(columns = {'value':'House price index'}, inplace = True)
merge = pd.merge(erp_reform,hpi_reform,on=['Time','State'])
merge['Time'] = pd.to_datetime(merge['Time'])#Change only this column
rate['Time'] = pd.to_datetime(rate['Time'])
output = pd.merge(merge,rate,on=['Time','State'])
output['Time'] = output['Time'].apply(lambda x: datetime.datetime.strftime(x, '%d/%m/%y')) #Run only,otherwise have to restart
mChart = MotionChart(df = output, key='Time', x='Unemployment Rate', y='House price index', xscale='linear', yscale='linear',
                     size='Population', color='State', category='State')
mChart.to_notebook()