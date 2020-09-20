


def Momentum(df,Preco_Atual,Parametro):

    momentum=0
    if(Preco_Atual>=Parametro):
        momentum=((df.Close.loc[Preco_Atual]-df.Close.loc[Preco_Atual-Parametro])/df.Close.loc[Preco_Atual-Parametro])*100

    return momentum
        


    
    


    
