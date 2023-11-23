import subprocess
import re
import matplotlib.pyplot as plt

def mainPing():
    dest = input("Digite o endereço IP de destino: ")
    tamanho_pct = input("Digite o tamanho do pacote (em bytes): ")
    quant_ips = input("Digite a quantidade de pings: ")
    repeticoes = int(input("Digite a quantidade de repetições do teste: "))
    i = 0

    ping_times = []

    while i < repeticoes:
        i += 1
        cmd = ["ping", "-n", quant_ips, "-l", tamanho_pct, dest]

        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
            times = []

            for line in process.stdout:
                print(line.strip())

                # Verifica se a linha contém informações de tempo
                if "tempo" in line.lower():
                    # Usa expressão regular para encontrar o tempo de ping
                    match = re.search(r"tempo[=<]([\d.]+)ms", line.lower())
                    if match:
                        time_str = match.group(1)
                        times.append(float(time_str))

            process.wait()

            # Adiciona a lista de tempos ao longo das repetições
            ping_times.append(times)

        except subprocess.CalledProcessError as e:
            print("Erro ao executar o ping:", e)

    # Gera gráfico de linhas para cada repetição
    plt.figure(figsize=(12, 8))
    for rep, times in enumerate(ping_times, start=1):
        plt.plot(times, label=f'Repetição {rep}')

    plt.title(f"Variação do Tempo de Ping para {dest}")
    plt.xlabel("Número de Pings")
    plt.ylabel("Tempo (ms)")
    plt.legend()
    plt.show()

    # Calcula as médias para cada repetição
    mean_times = [sum(times) / len(times) for times in ping_times]

    # Gera gráfico de barras para as médias
    plt.figure(figsize=(12, 8))
    plt.bar(range(1, repeticoes + 1), mean_times, color='blue', alpha=0.7)
    plt.title(f"Média do Tempo de Ping para {dest}")
    plt.xlabel("Número de Repetições")
    plt.ylabel("Tempo Médio (ms)")
    plt.show()

if __name__ == "__main__":
    mainPing()
