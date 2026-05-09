# Extração de contratos e convênios - Ceará Transparente
Projeto que realiza consulta e a coleta de dados automatizada de contratos e convênios do Estado do Ceará utilizando Python entre 01/01/2025 à 31/12/2025.

## Tecnologias utilizadas:
- Python 3
- Pandas (Para tratamento de dados)
- Requests (Para consumo da API)

## Como funciona:
Percorre as páginas da API, fazendo paginação automática utilizando `while` e com pausas aleatórias com a biblioteca `random` para simular comportamento humano. Os dados coletados são salvos de forma incremental em um arquivo CSV.
