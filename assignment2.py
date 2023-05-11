import pandas
import datetime
import math
import os
import matplotlib.pyplot as plt
#read data
path=os.getcwd()
postion=path+"\\homework\\data\\IFC_Investment\\"
Industry=pandas.read_csv(postion+"IFC_Investment_By_Industry_-_Annual_Summary.csv")
Product=pandas.read_csv(postion+"IFC_Investment_By_Product_-_Annual_Summary.csv")
Region=pandas.read_csv(postion+"IFC_Investment_By_Region_-__Annual_Summary.csv")
# merge data
year='FiscalYear'
Industry=Industry.rename(columns={Industry.columns[0]:year},inplace=False)
Product=Product.rename(columns={Product.columns[0]:year},inplace=False)
Region=Region.rename(columns={Region.columns[0]:year},inplace=False)
total=pandas.merge(Industry,Product,on=year)
final = pandas.merge(total, Region,on=year)
plt.plot(final[year], final[final.columns[9]])
# 添加标签和标题
plt.xlabel('year')
plt.ylabel(final.columns[9])

# 显示图表
plt.show()


