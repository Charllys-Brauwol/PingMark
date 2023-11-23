import speedtest
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def mainVelocidade():
    repeticoes = int(input("Digite a quantidade de repetições do teste: "))
    i = 0

    repeticoes_list = list(range(1, repeticoes + 1))
    download_speeds = []  # Lista para armazenar velocidades de download
    upload_speeds = []    # Lista para armazenar velocidades de upload

    while i < repeticoes: 
        i += 1
        try:
            st = speedtest.Speedtest()

            velocidade_download = st.download() / 1_000_000  # Convertendo para megabits por segundo
            velocidade_upload = st.upload() / 1_000_000  # Convertendo para megabits por segundo

            download_speeds.append(velocidade_download)
            upload_speeds.append(velocidade_upload)
            
            print(f"Repetição {i} - Download: {velocidade_download:.2f} Mbps, Upload: {velocidade_upload:.2f} Mbps")

        except Exception as e:
            print(f"Erro: {e}")

    # Gráfico para as repetições individuais
    plt.figure(figsize=(10, 6))
    plt.plot(repeticoes_list, download_speeds, marker='o', label='Download Speed', color='b')
    plt.plot(repeticoes_list, upload_speeds, marker='o', label='Upload Speed', color='g')
    plt.xlabel('Repetições')
    plt.ylabel('Velocidade (Mbps)')
    plt.title('Velocidades de Download e Upload por Repetição')
    plt.grid(True)
    plt.legend()
    plt.savefig('repeticoes_grafico.png')  # Salva o gráfico como uma imagem
    plt.show()

    # Gráfico para as médias
    plt.figure(figsize=(8, 6))
    avg_download = np.mean(download_speeds)
    avg_upload = np.mean(upload_speeds)
    plt.bar(['Download', 'Upload'], [avg_download, avg_upload], color=['b', 'g'])
    plt.ylabel('Média de Velocidade (Mbps)')
    plt.title('Média das Velocidades de Download e Upload')
    plt.savefig('medias_grafico.png')  # Salva o gráfico como uma imagem
    plt.show()

    # Tabela de dados
    dados_tabela = list(zip(repeticoes_list, download_speeds, upload_speeds))
    tabela = tabulate(dados_tabela, headers=['Repetição', 'Download (Mbps)', 'Upload (Mbps)'], tablefmt='grid')

    # Salvar tabela como imagem
    plt.figure(figsize=(12, 6))
    plt.axis('off')
    plt.table(cellText=dados_tabela, colLabels=['Repetição', 'Download (Mbps)', 'Upload (Mbps)'], loc='center')
    plt.savefig('tabela_dados.png')  # Salva a tabela como uma imagem
    plt.show()

    print("\nTabela de Dados:")
    print(tabela)

if __name__ == "__main__":
    mainVelocidade()
