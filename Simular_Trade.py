
#Indicador Moving Averange by Leonardo Macedo Freire
from Moving_Averange_Signals import Moving_Averange_Signals

from Momentum import Momentum


#---------------------------------Simular Trade------------------------------------------------

def Simular_Trade(df,Indicador,medias,medias2,Parametro_AM,Parametro2_AM,AMCD,mediaTrigger,ParametroTrigger,momentum,momentumParametro):

    Comprar=0
    Vender=0
    Preco_Compra=0
    Preco_Venda=0
    Estado='Inicio'
    Lucro=0
    Porcentagens=[]
    Compra_Inicial='Vazio'
    j=0
    outlinears=0
    print(len(df))
    for i in range(0,len(df)):    
    
        #------------------------------------Operações de trade--------------------------------
        if (Vender==1 and Estado!='Venda' ):
            
            Preco_Venda=df['Open'].loc[i]
            if(Estado!='Inicio'):                
                Lucro+=Preco_Venda-Preco_Compra
                Porcentagens.append(Preco_Venda/Preco_Compra*100)
                if(Preco_Venda-Preco_Compra<0):
                    outlinears+=1
                    
                

            Estado='Venda'
            print('-------{}------------'.format(i))
            print('V')
            print(Preco_Venda)
            print(outlinears)
            print(Preco_Venda-Preco_Compra)
            #print(Porcentagens[j])
            #j+=1
           
                
                    
                    
        else:
            if(Comprar==1 and Estado!='Compra'):
                Preco_Compra=df['Open'].loc[i]

                if(Estado!='Inicio'):
                   Lucro+=Preco_Venda-Preco_Compra
                if(Compra_Inicial=='Vazio'):
                    Compra_Inicial=Preco_Compra
                if(Preco_Venda-Preco_Compra<0):
                    outlinears+=1
                    
                Estado='Compra'
                print('-------{}------------'.format(i))
                print('C')
                print(Preco_Compra)
                print(outlinears)
                print(Preco_Venda-Preco_Compra)
                
        
        #Capta os signais de compra e venda dados pelas averange rules
        Comprar, Vender = Moving_Averange_Signals(df,i,Parametro_AM,Parametro2_AM,Indicador,medias, medias2,AMCD,mediaTrigger,ParametroTrigger)
        momentum.append(Momentum(df,i,momentumParametro))
        
    return Preco_Venda, Lucro, Compra_Inicial, Porcentagens, outlinears
