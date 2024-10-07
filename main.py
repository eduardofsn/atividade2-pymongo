import pymongo
from pyfiglet import figlet_format
client = pymongo.MongoClient('mongodb+srv://root:mongo282624@pymongo.qropk.mongodb.net/?retryWrites=true&w=majority&appName=pymongo')

db = client.get_database('mercado_lvire')
collection = db.usuarios
collectionVendedor = db.vendedor
collectionProdutos = db.produtos
while True:
    print(figlet_format("Mercado Livre", font= "standard"))
    print("|--------------------|")
    print("|1. (CRUD) Usuários  |")
    print("|2. (CRUD) Vendedor  |")
    print("|3. (CRUD) Produtos  |")
    print("|0. Sair             |")
    print("|--------------------|")
    ch = int(input("Digite sua escolha: "))

    # CRUD Produtos
    def produtos():
        while True:
            print("|--------------------|")
            print("|1. Criar produto    |")
            print("|2. Deletar produto  |")
            print("|3. Exibir produto   |")
            print("|4. Editar produto   |")
            print("|0. Sair             |")
            print("|--------------------|")

            ch = int(input("Digite sua escolha: "))

            if ch == 1:
                p_id = input("Digite o id do produto: ")
                p_name = input("Digite o nome do produto: ")
                p_qualidade = int(input("Digite a qualidade do produto (0-100): "))
                p_marca = input("Digite a marca do produto: ")
                p_preco = int(input("Digite o preço do produto: "))
                record = {"_id": p_id, "name": p_name, "qualidade": p_qualidade, "marca": p_marca, "preco": p_preco}
                collectionProdutos.insert_one(record)
                print("Produto adicionado com sucesso!")

            if ch == 2:
                p_id = input("Digite o id do produto: ")
                query = {"produtos": p_id}
                collectionProdutos.delete_one(query)
                print("Produto deletado com sucesso!")

            if ch == 3:
                p_id = input("Digite o id do produto: ")
                query = {"_id": p_id}
                print(collectionProdutos.find_one(query))


            if ch == 4:
                p_id = input("Digite o id do vendedor: ")
                query = {"_id": p_id}
                present_data = collectionProdutos.find_one(query)
                key = input("Digite a chave a ser alterada: ")
                value = input("Digite o novo valor: ")
                new_data = {'$set': {key: value}}
                collectionProdutos.update_one(present_data, new_data)
                print("Produto editado com sucesso!")

            if ch == 0:
                break

   # CRUD Vendedor
    def vendedor():
        while True:
            print("|--------------------|")
            print("|1. Criar vendedor   |")
            print("|2. Deletar vendedor |")
            print("|3. Exibir vendedor  |")
            print("|4. Editar vendedor  |")
            print("|0. Sair             |")
            print("|--------------------|")

            ch = int(input("Digite sua escolha: "))

            if ch == 1:
                v_id = input("Digite o id do vendedor: ")
                v_name = input("Digite o nome do vendedor: ")
                v_email = input("Digite o email do vendedor: ")
                v_reputacao = input("Digite a reputação em números do vendedor: ")
                v_cnpj = input("Digite o CNPJ do vendedor: ")
                record = {"_id": v_id, "name": v_name, "email": v_email, "reputacao": v_reputacao, "cnpj": v_cnpj}
                collectionVendedor.insert_one(record)
                print("Vendedor adicionado com sucesso!")

            if ch == 2:
                v_id = input("Digite o id do vendedor: ")
                query = {"_id": v_id}
                collectionVendedor.delete_one(query)
                print("Vendedor deletado com sucesso!")

            if ch == 3:
                v_id = input("Digite o id do vendedor: ")
                query = {"_id": v_id}
                print(collectionVendedor.find_one(query))


            if ch == 4:
                v_id = input("Digite o id do vendedor: ")
                query = {"_id": v_id}
                present_data = collectionVendedor.find_one(query)
                key = input("Digite a chave a ser alterada: ")
                value = input("Digite o novo valor: ")
                new_data = {'$set': {key: value}}
                collectionVendedor.update_one(present_data, new_data)
                print("Vendedor editado com sucesso!")

            if ch == 0:
                break

    # CRUD Usuário
    def usuarios():
        while True:
            print("|--------------------|")
            print("|1. Criar usuário    |")
            print("|2. Deletar usuário  |")
            print("|3. Exibir usuário   |")
            print("|4. Editar usuário   |")
            print("|0. Sair             |")
            print("|--------------------|")

            ch = int(input("Digite sua escolha: "))
            if ch == 1:
                u_id = input("Digite o id do usuário: ")
                u_name = input("Digite o nome do usuário: ")
                u_email = input("Digite o email do usuário: ")
                u_senha = input("Digite a senha do usuário: ")
                u_cpf = input("Digite o CPF do usuário: ")
                record = {"_id": u_id, "name": u_name, "email": u_email, "password": u_senha, "cpf": u_cpf}
                collection.insert_one(record)
                print("Usuário adicionado com sucesso!")
    
            if ch == 2:
                u_id = input("Digite o id do usuário: ")
                query = {"_id": u_id}
                collection.delete_one(query)
                print("Usuário deletado com sucesso!")
            

            if ch == 3:
                u_id = input("Digite o id do usuário: ")
                query = {"_id": u_id}
                print(collection.find_one(query))
                
            if ch == 4:
                u_id = input("Digite o id do usuário: ")
                query = {"_id": u_id}
                present_data = collection.find_one(query)
                key = input("Digite a chave a ser alterada: ")
                value = input("Digite o novo valor: ")
                new_data = {'$set': {key: value}}
                collection.update_one(present_data, new_data)
                print("Usuário editado com sucesso!")

            if ch == 0:
                break

    if ch == 1:
        usuarios()

    
    if ch == 2:
        vendedor()


    if ch == 3:
        produtos()


    if ch == 0:
        exit("Desenvolvido por: Eduardo Namiuti")
    
