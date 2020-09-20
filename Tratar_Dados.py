

#This library will convert our dates into the necessary number format
import matplotlib.dates as mdates
#We will use this one to define our desired time span
import datetime as dt
#The module that will load the desired stock data
import pandas_datareader as web
import pandas as pd

#----------------------------Data Manipulation-----------------
def Tratar_Dados(nome_arquivo,comeco,fim):
        
    

    #Loading the data
    df=pd.read_csv(nome_arquivo)
    print(df.head())

    df=df[['Date','Open','High','Low','Close']]
    print(df.head())

    df=df[(df.Date>=comeco)&(df.Date<=fim)]

    print(df.head())
    df=df.reset_index(drop=True)
    
    print(df)

    #Converting date of string to date format
    def converter(data):
        return dt.datetime.strptime(data, '%Y-%m-%d')
        

    df['Date']=df['Date'].apply(converter)

    #Manipulation the Date so it cans plot it
    df['Date']=df['Date'].map(mdates.date2num)
    #print(df.head())

    return df



def Tratar_Dados2(nome_arquivo):
        

    df=pd.read_csv(nome_arquivo)
    print(df.head())

    df=df[['Date','Open','High','Low','Close']]
    #df=df.sort_values(by='Date')
    print(df.head())

    aux=pd.DataFrame(columns=('Date','Open','High','Low','Close'))
    tamanho=len(df)-1
    for i in range(0,len(df)):
        aux.loc[i]=df.loc[tamanho]
        tamanho=tamanho-1

    print(aux)

    #Converting date of string to date format
    def converter(data):
        return dt.datetime.strptime(data,'%Y-%m-%d %I-%p')
        

    aux['Date']=aux['Date'].apply(converter)

    #Manipulation the Date so it cans plot it
    aux['Date']=aux['Date'].map(mdates.date2num)
    #print(df.head())

    return aux



