# Case Engenheiro de Dados - Nestlé

---

# 1. Objetivos
### Este case tem como finalidade testar as habilidades técnicas voltadas para um Engenheiro de Dados através de processo ETL e Análise de Dados.

## 1.1 Participantes
- Guilherme Martins Serafim

---

# 2. Repositório
### CASE ENGENHEIRO DE DADOS.pptx
- Arquivo PowerPoint com o escopo e definição do Case.

### Diretório - Foto
- Contém o logo da Nestlé, que foi utilizado no Jupyter Notebook.

### Diretório - Dados
1. Diretório - Originais:
   - Contém os arquivos .CSV originais antes dos tratamentos.
      - **BaseCargos.csv** 
         - Cargo,
         - Nível,
         - Contratação,
         - Área,
         - COD Área,
         - COD Nível,
         - Quadro,
         - Bonus.
      - **BaseCEP.csv**
         - CEP,
         - Estado,
         - Região.
      - **BaseNível.csv**
         - Nível,
         - Descrição Nível,
         - Tempo no Nível,
         - Plano de Saúde,
         - Plano Odontológico,
         - Setor Responsável,
         - Plano de Carreira.
      - **BaseClientes.csv**
         - Cliente,
         - Valor Contrato Anual,
         - Quantidade de Serviços,
         - Cargo Responsável,
         - CEP,
         - Data Início Contrato,
         - Nível de Importancia.
      - **BaseFuncionarios.csv**
         - ID RH,
         - RG,
         - CPF,
         - Ramal,
         - Estado Civil,
         - Nome Completo,
         - Login,
         - Data de Nascimento,
         - CEP,
         - Data de Contratacao,
         - Data de Demissao,
         - Dias Uteis Trabalhados Ano Orcamentario,
         - Salario Base,
         - Impostos,
         - Beneficios,
         - VT,
         - VR,
         - Cargo,
         - Bandeira,
         - Codigos,
         - Quantidade de Acessos,
         - Ferias Acumuladas,
         - Ferias Remuneradas,
         - Horas Extras,
         - Valores Adicionais,
         - ID de Pessoal,
         - ID da area.
     - **BasePQ.csv**
         - ID RH,
         - RG,
         - CPF,
         - Ramal,
         - Estado Civil,
         - Nome Completo,
         - Login,
         - Data de Nascimento,
         - CEP,
         - Data de Contratacao,
         - Data de Demissao,
         - Dias Uteis Trabalhados Ano Orcamentario,
         - Salario Base,
         - Impostos,
         - Beneficios,
         - VT,
         - VR,
         - Cargo,
         - Bandeira,
         - Codigos,
         - Quantidade de Acessos,
         - Ferias Acumuladas,
         - Ferias Remuneradas,
         - Horas Extras,
         - Valores Adicionais,
         - ID de Pessoal,
         - ID da area,
         - OP,
         - 010,
         - Operações,
         - JAJ,
         - 0,
         - J,
         - 1,
         - I,
         - Estagiário,
         - JA,
         - Nível,
         - Área,
         - COD Área,
         - COD Nível,
         - Quadro,
         - Bonus,
         - Contratacao,
         - Descrição Nível,
         - Tempo no Nível,
         - Plano de Saúde,
         - Plano Odontológico,
         - Setor Responsável,
         - Plano de Carreira.
---
2. Diretório - Ajustados:
   - Contém os arquivos .CSV após o tratamento de linhas, colunas, separadores e encoding.
      - BaseCargos.csv
      - BaseCEP.csv
      - BaseClientes.csv
      - BaseFuncionarios.csv
      - BaseNível.csv
      - BasePQ.csv
---
3. Diretório - Finalizados
   - Contém os arquivos após ser feito o **MERGE** das bases, pronto para a realização das análises.
      - BaseClientes.csv
      - BasePQ.csv
---
### Diretório - Notebook
1. funcoes.py
   - Arquivo Python com as funções que foram desenvolvidas:
      - **verificaDataframe:** Função que recebe um DataFrame e retorna:
        - Quantidade de linhas, 
        - Quantidade de Colunas, 
        - Quantidade de duplicados,
        - Quantidade de Nulos.
      - **juntaLinhas:** Função que recebe um DataFrame e uma coluna:
        - Essa função tem como intuito tratar dados que estão quebrados em duas linhas. Ela separa a linha (par) e a linha (impar) em listas, ajusta o nome das colunas e no final concatena em um DataFrame.
      - **ajusteColunas:** Função que recebe um DataFrame:
        - Essa função tem como intuito tratas as colunas que estão deslocadas. É feito um looping para filtrar as colunas que possuem nulos, e a partir delas é criado um DataFrame. Nele é utilizado o método **SHIFT** do **PANDAS**, onde é possível mover os dados pelas colunas. No final é gerado um novo DataFrame com as colunas ajustadas.
      - **ajustaData:** Função que recebe um DataFrame:
        - Essa função tem como intuito tratas as datas do formato **GENERAL** (Númerico) para o tipo **DATE**. Ela foi desenvolvida a partir da biblioteca Datetime do Python. Ela faz um looping pelas colunas do DataFrame, e ao encontrar alguma Coluna que contenha *DATA* no nome, é feito a conversão. Ela retorna o DataFrame de entrada com as colunas de data ajustadas.

---
2. **1_TratamentoBases.ipynb**
   - Arquivo Notebook desenvolvido para a leitura dos arquivos, tratamento dos separadores, ajustes nas linhas e colunas.
3. **2_MergeDados.ipynb**
   - Arquivo Notebook desenvolvido para realização do MERGE das bases.
4. **3_AnaliseClientes.ipynb**
   - Arquivo Notebook com as análises do arquivo final, Base Clientes.
5. **3_AnalisePQ.ipynb**
   - Arquivo Notebook com as análises do arquivo final, Base PQ.
