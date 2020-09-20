
#Will be used for displaying our chart in the end
import matplotlib.pyplot as plt
#Our main library for plotting
from mpl_finance import candlestick_ohlc

#-----------------------------Plot-------------------------------
def Gerar_Grafico(df,medias,medias2,Indicador,AMCD,mediaTrigger,momentum):

    plt.figure(1)
    ax=plt.subplot(311)
    
    candlestick_ohlc(ax,df.values,width=1,colorup='g',colordown='r')

    ax.xaxis_date()
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_title('Bitcoin/USD', color='white')
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='white')

    plt.scatter(df['Date'].values, medias, label='linear')
    if (Indicador=='Averanges_Crossover_Ruler' or Indicador=='AMCD'):
        plt.scatter(df['Date'].values, medias2, color='y', label='linear')


    #----------------------------------------


    bx=plt.subplot(312)
    bx.xaxis_date()
    bx.plot(df['Date'].values,momentum,color='r')
    bx.grid(True)
    bx.set_axisbelow(True)
    bx.set_title('Momentum', color='white')
    bx.set_facecolor('black')
    bx.figure.set_facecolor('#121212')
    bx.tick_params(axis='x', colors='black')
    bx.tick_params(axis='y', colors='white')

    x=[]
    for i in range(0, len(df)):
        x.append(0)
        
    bx.scatter(df['Date'].values, x, color='b')


    #------------------------------


    

    bx=plt.subplot(313)
    bx.xaxis_date()
    bx.plot(df['Date'].values,AMCD,color='r')
    bx.grid(True)
    bx.set_axisbelow(True)
    bx.set_title('AMCD', color='white')
    bx.set_facecolor('black')
    bx.figure.set_facecolor('#121212')
    bx.tick_params(axis='x', colors='white')
    bx.tick_params(axis='y', colors='white')

    x=[]
    for i in range(0, len(df)):
        x.append(0)
        
    bx.scatter(df['Date'].values, x, color='b')
    bx.scatter(df['Date'].values, mediaTrigger, color='g')
        


    plt.show()



