

#----------------------Moving Averange Signals---------------------------


def Moving_Averange(Dados,Preco_Atual,Quant_Media):

    
    if (Preco_Atual>=(Quant_Media-1)):
        
        Soma=0

        elementos=Preco_Atual-(Quant_Media-1)

        
        #print(list(range(Preco_Atual,elementos-1,-1)))
        
        for i in range(Preco_Atual,elementos-1,-1):

            Soma=Soma+Dados['Close'].loc[i]
            

        return Soma/Quant_Media

        
    else:
        return 8000
    
def Moving_Averange2(AMCD,Quant_Media):

    
    if ((len(AMCD)-1)>=(Quant_Media-1)):
        
        Soma=0

        elementos=(len(AMCD)-1)-(Quant_Media-1)

        
        #print(list(range(Preco_Atual,elementos-1,-1)))
        
        for i in range((len(AMCD)-1),elementos-1,-1):

            Soma=Soma+AMCD[i]
            

        return Soma/Quant_Media

        
    else:
        return 0

    

def Moving_Averange_Signals(df,i,Parametro_AM,Parametro2_AM,Indicador,medias, medias2,AMCD,mediaTrigger,ParametroTrigger):

    
    

    medias.append(Moving_Averange(df,i,Parametro_AM))
    medias2.append(Moving_Averange(df,i,Parametro2_AM))
    AMCD.append(medias[len(medias)-1]-medias2[len(medias)-1])
    mediaTrigger.append(Moving_Averange2(AMCD,ParametroTrigger))
    Comprar=0
    Vender=0

    if Indicador=='Crossover_Ruler':
        if(i>=Parametro_AM-1):
            #Sinal para comprar
            if(df['Close'].loc[i]>medias[i]):
                Comprar=1
                Vender=0
                #print('SC')
                #print(df['Close'].loc[i])
            else:
                 #Sinal para vender
                 if(df['Close'].loc[i]<medias[i]):
                     Vender=1
                     Comprar=0
                     #print('SV')
                     #print(df['Close'].loc[i])
                     
    if Indicador=='Averange_Ruler':
        if(i>Parametro_AM-1):
            #Sinal para comprar
            if(medias[i-1]<medias[i]):
                Comprar=1
                Vender=0
                #print('SC')
                #print(df['Close'].loc[i])
            else:
                 #Sinal para vender
                 if(medias[i-1]>medias[i]):
                     Vender=1
                     Comprar=0
                     #print('SV')
                     #print(df['Close'].loc[i])
                     
    if Indicador=='Averanges_Crossover_Ruler':
        if(i>=Parametro2_AM-1):
            #Sinal para comprar
            if(medias[i]>medias2[i]):
                Comprar=1
                Vender=0
                #print('SC')
                #print(df['Close'].loc[i])
            else:
                 #Sinal para vender
                 if(medias[i]<medias2[i]):
                     Vender=1
                     Comprar=0
                     #print('SV')
                     #print(df['Close'].loc[i])
    if Indicador=='AMCD':
        if(i>=Parametro2_AM-1):
            #Sinal para comprar
            if(mediaTrigger[i]<AMCD[i]):
                Comprar=1
                Vender=0
                #print('SC')
                #print(df['Close'].loc[i])
            else:
                 #Sinal para vender
                 if(mediaTrigger[i]>AMCD[i]):
                     Vender=1
                     Comprar=0
                     #print('SV')
                     #print(df['Close'].loc[i])

    return Comprar,Vender



 
              
                  
            
              
    
        

    


        

    

    
