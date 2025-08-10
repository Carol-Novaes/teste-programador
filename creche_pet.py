API_KEY = "api_key=live_rZUTqzFVhxtQ8m5I0Y7KKZCCgYUYiNwOj2Xh0z3z1WboQFjHrvWXy0gc4p5PjPhK"  
BASE_URL = "https://api.thedogapi.com/v1"

import requests

cachorros = []

def mostrar_menu():
    print("\n  --- Creche para Pets --- ")
    print("| 1. Cadastrar Cachorro    |")
    print("| 2. Editar Cachorro       |")
    print("| 3. Visualizar Cachorro   |")
    print("| 4. Deletar Cachorro      |")
    print("| 5. Listar Cachorros      |")
    print("| 6. Fechar                |")   

# Cadastrar Cachorro
def cadastrar_cachorro():
    print("\n--- Cadastro de Cachorro ---")

    nome = input("Nome do cachorro: ")
    
    # Obter raças disponíveis da API
    headers = {'x-api-key': API_KEY}
    response = requests.get(f"{BASE_URL}/breeds", headers=headers)
    racas = [raca['name'] for raca in response.json()]
    
    print("--- Raças disponíveis: ---")
    for i, raca in enumerate(racas, 1):
        print(f"{i}. {raca}")    
    
    while True:
        try:
            indice_raca = int(input("Número da raça: ")) - 1
            if 0 <= indice_raca < len(racas):
                raca = racas[indice_raca]
                break
            else:
                print("Número inválido!⚠️")
        except ValueError:
            print("Digite um número válido!")
    
    idade = input("Idade do cachorro: ")

    dono = input("Nome do dono: ")
    
    cachorro = {
        'nome': nome,
        'raca': raca,
        'idade': idade,
        'dono': dono
    }
    
    cachorros.append(cachorro)
    print("\nCachorro cadastrado com sucesso!🌟") 

# Editar um cachorro
def editar_cachorro():
    listar_cachorros()
    if not cachorros: 
        return
    
    try:
        indice = int(input("\nNúmero do cachorro para editar: ")) - 1
        if 0 <= indice < len(cachorros):
            cachorro = cachorros[indice]
            print("\n--- Editando cachorro: ---")
            print(f"1. Nome: {cachorro['nome']}")
            print(f"2. Raça: {cachorro['raca']}")
            print(f"3. Idade: {cachorro['idade']}")
            print(f"4. Dono: {cachorro['dono']}")
            
            campo = input("\nQual campo deseja editar (1-4)? ")
            
            if campo == "1":
                cachorro['nome'] = input("Novo nome: ")
            elif campo == "2":
                headers = {'x-api-key': API_KEY}
                response = requests.get(f"{BASE_URL}/breeds", headers=headers)
                racas = [raca['name'] for raca in response.json()]
                
                print("Raças disponíveis:")
                for i, raca in enumerate(racas, 1):
                    print(f"{i}. {raca}")
                
                novo_indice = int(input("\nNúmero da nova raça: ")) - 1
                cachorro['raca'] = racas[novo_indice]
            elif campo == "3":
                cachorro['idade'] = input("\nNova idade: ")
            elif campo == "4":
                cachorro['dono'] = input("\nNovo dono: ")
            else:
                print("Opção inválida!⚠️")
            
            print("\nCachorro atualizado com sucesso!🌟")
        else:
            print("Número inválido!⚠️")
    except ValueError:
        print("Digite um número válido!")      

# Visualizar Cachorro
def visualizar_cachorro():
    listar_cachorros()
    if not cachorros: 
        return
    
    try:
        indice = int(input("\nNúmero do cachorro para visualizar: ")) - 1
        if 0 <= indice < len(cachorros):
            cachorro = cachorros[indice]
            print("\n--- Informações do Cachorro ---")
            print(f"Nome: {cachorro['nome']}")
            print(f"Raça: {cachorro['raca']}")
            print(f"Idade: {cachorro['idade']}")
            print(f"Dono: {cachorro['dono']}")
        else:
            print("Número inválido!⚠️")
    except ValueError:
        print("Digite um número válido!")

# Deletar Cachorro
def deletar_cachorro():
    listar_cachorros()
    if not cachorros: 
        return
    
    try:
        indice = int(input("\nNúmero do cachorro para deletar: ")) - 1
        if 0 <= indice < len(cachorros):
            cachorro = cachorros.pop(indice)
            print(f"\nCachorro {cachorro['nome']} removido com sucesso!🌟")
        else:
            print("Número inválido!⚠️")
    except ValueError:
        print("Digite um número válido!")       


# Listar Cachorros
def listar_cachorros():
    print("\n--- Lista de Cachorros ---")
    if not cachorros: 
        print("Nenhum cachorro cadastrado.⚠️")
        return
    
    for i, cachorro in enumerate(cachorros, 1):
        print(f"{i}. {cachorro['nome']} - {cachorro['raca']}") 

# MENU
def main():
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            cadastrar_cachorro()
        elif opcao == "2":
            editar_cachorro()
        elif opcao == "3":
            visualizar_cachorro()
        elif opcao == "4":
            deletar_cachorro()
        elif opcao == "5":
            listar_cachorros()
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()    