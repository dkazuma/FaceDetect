import pandas as pd

data = {
    'roti': [3,2,0,1],
    'cola': [0,3,7,2],
    'tisu': [5,1,1,8]
}
transaksi = pd.DataFrame(data,index=['Ani','Budi','Citra','David'])
#print(transaksi.loc['Citra'])
df = pd.read_csv(r'E:\Job\Python\transaksi.csv', index_col=0)
#new_colums = df.columns.values
#new_colums[0] = 'nama'
#df.columns = new_colums
#df = df.set_index('nama')
print(df)
print(__name__)