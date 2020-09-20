
#____________________________________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------------------------------
#---------------        BACKTESTING             ------------------------        BACKTESTING             -----------------------------
#---------------       Money's Machine          ------------------------       Money's Machine          -----------------------------
#--------------- Leonardo Macedo Freire 2020/05 ------------------------ Leonardo Macedo Freire 2020/05 -----------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________________________________



from Tratar_Dados import Tratar_Dados
from Tratar_Dados import Tratar_Dados2

from Gerar_Grafico import Gerar_Grafico

from Simular_Trade import Simular_Trade





#------------------Simulação Trade ----------------------------------
#'2019-01-01','2020-05-14'
#'2019-05-01','2020-05-14'
#df=Tratar_Dados('BTCUSD_d.csv','2018-05-01','2020-05-14')
df=Tratar_Dados2('BTCUSD_1h_2020_marco_dia10.csv')

medias=[]
medias2=[]
AMCD=[]
mediaTrigger=[]
momentum=[]
momentumParametro=15
Parametro_AM=5
Parametro2_AM=20
ParametroTrigger=15
#Indicador='Averanges_Crossover_Ruler'
#Indicador='Averange_Ruler'
#Indicador='Crossover_Ruler'
Indicador='AMCD'

Preco_Venda,Lucro,Compra_Inicial, Porcentagens, outlinears = Simular_Trade(df,Indicador,medias,medias2,Parametro_AM,Parametro2_AM,AMCD,mediaTrigger,ParametroTrigger,momentum,momentumParametro)

Porcentagem_Lucro=Lucro/Compra_Inicial*100
Porcentagem_Comprar_Segurar=Preco_Venda/Compra_Inicial*100

print('-----------Valores de Avalição da Simulação--------')
print('                                                   ')

Valor_Final=Compra_Inicial
for i in range(0,len(Porcentagens)):    
    Valor_Final= Porcentagens[i]/100*Valor_Final
    #print(Porcentagens[i]/100)
    #print(Valor_Final)

Porcentagem_Valor_Final=Valor_Final/Compra_Inicial*100

print('Compra Inicial={}'.format(Compra_Inicial))

print('Preço de Venda (Porcentagem) ={} ({})'.format(Preco_Venda,Porcentagem_Comprar_Segurar))

print('Valor Final com Trade(Porcentagem) ={} ({})'.format(Valor_Final,Porcentagem_Valor_Final))

print('Lucro de Avaliação da Estrategia(Porcentagem)= {} ({})'.format(Lucro,Porcentagem_Lucro))

print('Porcentagens Compra/Venda={}'.format(Porcentagens))

print('Outlinears ={}'.format(outlinears))

Gerar_Grafico(df,medias,medias2,Indicador,AMCD,mediaTrigger,momentum)
















