import requests
import pandas as pd
import time
import random
import os

url = "https://api-dados-abertos.cearatransparente.ce.gov.br/transparencia/contratos/convenios?page=1&data_assinatura_inicio=01%2F01%2F2025&data_assinatura_fim=31%2F12%2F2025"
nome_arquivo = "convenios_2025.csv"
data_inicio = "01/01/2025"
data_fim = "31/12/2025"
pagina = 1

while True:
    parametros = {
        "page": pagina,
        "data_assinatura_inicio": data_inicio,
        "data_assinatura_fim": data_fim
    }
    try:
        response = requests.get(url, params=parametros)
        response.raise_for_status()
        data = response.json()
        
        lista_convenios = data.get('data', [])

        if not lista_convenios:
            print("Processo finalizado: Nenhum dado encontrado.")
            break

        df_pagina = pd.DataFrame(lista_convenios)
        
        precisa_cabecalho = not os.path.exists(nome_arquivo)
        
        df_pagina.to_csv(
            nome_arquivo, 
            mode='a', 
            index=False, 
            header=precisa_cabecalho, 
            encoding="utf-8-sig"
        )

        print(f"Página {pagina} salva com sucesso.")
        
        pagina += 1
        time.sleep(random.uniform(1.0, 3.5))

    except Exception as e:
        print(f"Ocorreu um erro na página {pagina}: {e}")
        break

print(f"Arquivo final gerado: {nome_arquivo}")

