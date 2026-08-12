# Pipeline de Dados — Python e Orientação a Objetos

## Objetivo

Construir um pipeline de dados (Extract → Transform → Load) em Python puro, unindo dados de duas fontes diferentes — arquivos **JSON** e **CSV** — através de um *join*, e evoluir esse pipeline de um script procedural para uma versão organizada em **funções** e, por fim, em **classes (orientação a objetos)**.

## Por que este projeto

Depois de construir um pipeline completo no projeto [streaming-data-warehouse](https://github.com/Thiagomvbs/streaming-data-warehouse) (OLTP → ETL → DW, containerizado com Docker), o objetivo aqui foi diferente: não construir algo novo do zero, e sim **aprofundar a qualidade do código** por trás de qualquer pipeline — legibilidade, reutilização e manutenção, que são o que diferencia um script pontual de um pipeline pronto para produção.

## O que o pipeline faz

1. **Extract**: lê dados brutos de duas fontes distintas — um arquivo **JSON** e um arquivo **CSV** (`data_raw/`)
2. **Transform**: trata e padroniza os dados de cada fonte, e realiza um **join** entre elas, unindo as informações num único conjunto de dados consistente
3. **Load**: grava o resultado final processado em `data_processed/`

## O que este projeto demonstra

- Leitura e parsing de dados em formatos diferentes (JSON e CSV) sem bibliotecas de alto nível
- Extração, transformação (incluindo *join* entre fontes) e gravação de dados
- Evolução de código procedural para funções, e de funções para classes
- Encapsulamento do pipeline em classes, aplicando orientação a objetos a um caso real de ETL

## Stack

- Python (biblioteca padrão)

## Estrutura do Projeto

```
├── README.md
├── data_raw/        # dados brutos de entrada (JSON e CSV)
├── data_processed/  # dado final, já unido e tratado
├── notebooks/        # exploração e validação incremental da lógica
└── scripts/          # pipeline final, organizado em classes (POO)
```
## Próximos Passos

- Aplicar os aprendizados de POO na refatoração do projeto streaming-data-warehouse
