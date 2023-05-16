import re
import pandas as pd

data = {
    'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Sally Lee', 'Bob Johnson', 'Jane Smith', 'Lily Lee'],
    'Email': ['johndoe@gmail.com', 'janesmith@hotmail.com', 'bobjohnson@gmail.com', 'sally_lee@yahoo.com', 'bobjohnson@gmail.com', 'janesmith@hotmail.com', 'lily_lee@gmail.com']
}
df = pd.DataFrame(data)

b=[]
 #使用正则表达式过滤非法格式的电子邮件
for i in range(len(df)):
    pattern = r'^[a-z]+@gmail\.com$'
    if re.match(pattern, df["Email"][i]):
        print(str(i)+" "+df["Name"][i]+" "+df["Email"][i])
