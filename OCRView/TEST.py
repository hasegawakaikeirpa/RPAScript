import pandas as pd

F_stack = "#"
L_stack = "借"
List = [F_stack, L_stack]
dfList = []
dfList.append(List)
df = pd.DataFrame(dfList, columns=["変更前", "変更後"])
print(df)
