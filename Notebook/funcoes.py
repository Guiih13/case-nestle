import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('bmh')

def verificaDataframe(df):
    
    rows = df.shape[0]
    columns = df.shape[1]
    
    duplicados = df.duplicated().sum()
    nulos = df.isna().sum()
    
    print(f'O DataFrame tem {rows} linhas.')
    print(f'O DataFrame tem {columns} colunas.')
    print(f'O DataFrame tem {duplicados} duplicados.')
    print(f'O DataFrame tem nulo:')
    print(nulos)

def juntaLinhas(df, coluna):
    
    # Lista com os DataFrame pares
    lista_index_df1 = []
    
    for i in df[df[coluna].isna()].index:
        if i % 2 == 0:
            lista_index_df1.append(i)
    
    # Filtrando as linhas e as colunas 
    df1 = df.iloc[lista_index_df1, :3]
    
    # Exclui os registros do DataFrame
    df.drop(lista_index_df1, inplace=True)
    
    # Resetando o Index
    df1.reset_index(drop=True, inplace=True)
    
    # Lista com os DataFrame impares
    lista_index_df2 = []
    
    for i in df[df[coluna].isna()].index:
        if i % 2 != 0:
            lista_index_df2.append(i)
     
    # Filtra as linhas
    df2 = df.loc[lista_index_df2]
    
    # Exclui os registros do DataFrame
    df.drop(lista_index_df2, inplace=True)

    # Dicionário de colunas
    dic_colunas = {
    'Cliente':'Cargo Responsável',
    'Valor Contrato Anual':'CEP',
    'Quantidade de Serviços':'Data Início Contrato',
    'Cargo Responsável':'Nivel de Importancia'}
    
    # Drop colunas que não serão utilizadas
    df2.drop(columns=['CEP', 'Data Início Contrato', 'Nivel de Importancia'], inplace=True)
    
    # Renomeando as colunas
    df2.rename(columns=dic_colunas, inplace=True)
    df2.reset_index(inplace=True, drop=True)
    
    # Gera DataFrame final
    dfFinal = pd.concat([df1, df2], axis=1)
            
    return dfFinal

def ajusteColunas(Clientes):

    lista_colunas = []
    auxClientes = pd.DataFrame()

    # Filtrando só a coluna que tem nulo
    for i,j in Clientes.isna().sum().items():
        if j > 0 and i != 'toDrop':
            lista_colunas.append(i)

    for coluna in lista_colunas:  

        # Salvando as linhas que serão ajustadas
        ajustesLinhas = Clientes[Clientes[coluna].isna()]

        # Verificando a coluna que tem nulo
        for i, j in Clientes[Clientes[coluna].isna()].isna().sum().items():
            if j > 0:
                auxColuna = i

        for i,j in enumerate(Clientes.columns):
            if j == auxColuna:
                numAuxColuna = i

        # Armazenando a primeira coluna
        ajustesLinhasColuna = ajustesLinhas.iloc[:,:numAuxColuna]

        # Voltando uma coluna para os campos
        ajustesLinhas = ajustesLinhas.loc[ajustesLinhas.index, auxColuna:].shift(-1, axis=1)#.drop(columns='toDrop')

        # Concatenando os dois arquivos
        ajusteFinal = pd.concat([ajustesLinhasColuna, ajustesLinhas], axis=1)

        auxClientes = pd.concat([auxClientes, ajusteFinal])

    return auxClientes

def ajustaData(df):
    
    varData = 693596
    print(f'Data de 01/01/0001 até 01/01/1900: Dias: {varData} - Data: {datetime.fromordinal(varData)}')
    
    for i in df.columns:
        if i.find('Data') >= 0:
            df[i] = df[i].apply(lambda x: datetime.strftime(datetime.fromordinal(int(x) + varData), '%Y-%m-%d')  
                                if pd.isna(x)==False 
                                else 0)
        
    return df