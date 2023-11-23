import subprocess
import matplotlib.pyplot as plt

def maintracer():
    # Solicita que o usuário insira o destino (endereço IP ou nome de domínio)
    dest = input("Digite o endereço ou site para fazer o traceroute: ")
    repeticoes = int(input("Digite a quantidade de repetições do teste: "))
    
    for i in range(1, repeticoes + 1):
        cmd = ["tracert", dest]
        traceroute_output = []

        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
            
            for line in process.stdout:
                line = line.strip()
                traceroute_output.append(line)
            
            process.wait()

            # Cria uma figura com as informações do traceroute e organiza no estilo justificado
            plt.figure(figsize=(14, len(traceroute_output) / 4))
            plt.axis('off')
            text = '\n'.join(traceroute_output)
            plt.text(0.1, 0.9, text, ha='left', va='top', fontsize=10)
            plt.title(f"Traceroute para {dest} (Repetição {i})", fontsize=14)

            # Salva a imagem
            plt.savefig(f'traceroute_{i}.png', bbox_inches='tight')
            plt.show()

        except subprocess.CalledProcessError as e:
            print("Erro ao executar o traceroute:", e)

if __name__ == "__main__":
    maintracer()