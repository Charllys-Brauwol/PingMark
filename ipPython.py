from scapy.all import ARP, Ether, srp
import matplotlib.pyplot as plt
from tabulate import tabulate

def scan_ip_range(ip_prefix):
    try:
        ip = f"{ip_prefix}.0/24"
        arp = ARP(pdst=ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        result = srp(packet, timeout=3, verbose=0)[0]

        ips_ativos = set()
        for sent, received in result:
            ips_ativos.add(received.psrc)

        return list(ips_ativos)

    except Exception as e:
        print(f"Erro: {e}")
        return []

def mainScan():
    ip_prefix = input("Digite os primeiros três octetos do endereço IP (exemplo: 192.168.3): ")
     
    ips_ativos = scan_ip_range(ip_prefix)

    if ips_ativos:
        # Imprime os IPs ativos
        print("\nIPs em uso na rede:")
        for ip in sorted(ips_ativos):
            print(f"IP: {ip} está ativo.")

        # Cria uma tabela usando matplotlib e salva a imagem
        table_data = [["IPs Ativos"]] + [[ip] for ip in sorted(ips_ativos)]
        plt.axis('off')
        plt.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.2]*len(table_data[0]))
        plt.title("IPs Ativos na Rede", fontsize=14)
        plt.savefig('ips_ativos.png', bbox_inches='tight')
        plt.show()
    else:
        print("\nNenhum dispositivo encontrado na faixa de IP informada.")
    print("\n")

if __name__ == "__main__":
    mainScan()
