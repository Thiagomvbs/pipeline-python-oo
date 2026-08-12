from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#EXTRACT

dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f"Colunas da Empresa A: {dados_empresaA.nome_colunas}")
print(f"O número de linhas na Empresa A é: {dados_empresaA.qtd_linhas}\n")

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f"Colunas da Empresa B: {dados_empresaB.nome_colunas}")
print(f"O número de linhas na Empresa B é: {dados_empresaB.qtd_linhas}\n")

##TRANSFORM
key_mapping = {'Nome do Item': "Nome do Produto",
               'ClassificaÃ§Ã£o do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Colunas da Empresa Fusão: {dados_fusao.nome_colunas}")
print(f"O número de linhas na Empresa Fusão é: {dados_fusao.qtd_linhas}\n")

##LOAD

dados_fusao.salvando_dados('data_processed/dados_combinados.csv')
print(f"Dados combinados salvos em: data_processed/dados_combinados.csv")
