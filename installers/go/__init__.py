import go_installer
from go_installer import Installer
import subprocess
import time

install = Installer()

while True:
    banner = """
  ____         ___           _        _ _           
 / ___| ___   |_ _|_ __  ___| |_ __ _| | | ___ _ __ 
| |  _ / _ \   | || '_ \/ __| __/ _` | | |/ _ \ '__|
| |_| | (_) |  | || | | \__ \ || (_| | | |  __/ |   
 \____|\___/  |___|_| |_|___/\__\__,_|_|_|\___|_|


1. Baixa e instala a versão mais recente.
2. Baixa e instala a versão especificada.
3. Limpa a última instalação do Go e instala a mais recente. 
    """
    print(banner)

    userOption = input("Digite uma opção: ")

    match userOption:
        case "1":
            subprocess.run(["clear"])
            print(f"O sistema irá instalar o Golang versão {install.go_version} em 2 segundos.")
            time.sleep(2)
            install.check_installation()
            break
        case "2":
            subprocess.run(["clear"])
            specific_version = input("Digite o número da versão (exe: 1.18, 1.20): ")
            print(f"Instalando a versão {specific_version} especificada.")
            # restante do código aqui
        case "3":
            subprocess.run(["clear"])
            print("Limpando a versão atual.... Essa ação requere privilégios elevados.")
            subprocess.run(["rm","-rf","__pycache__"])
            # restante do código aqui
        case _:
            subprocess.run(["clear"])
            print("Esta opção não existe. Saindo do instalador.")
            break
