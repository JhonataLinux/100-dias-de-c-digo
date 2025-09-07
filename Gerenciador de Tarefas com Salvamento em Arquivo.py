tarefas = []
finalizada = []
print("Gerenciador de Tarefas")



while True:
     print("1 - Adicionar tarefa: ")
     print("2 - Listar tarefas")
     print("3 - Concluir tarefa")
     print("4 - Sair do programa")

     description =input("Deseja adicionar tarefa?")
     if description not in ("1", "2", "3", "4"):
         print("Opção inválida!")

     elif description == "1":
            descricao = input("Digite a descrição da tarefa: ")
            agendamento =input("Digite a data do agendamento:")
            tarefas.append({"descricao": descricao, "agendamento": agendamento })
            print("Tarefa adicionada com sucesso!")

     elif description == "2":
         for i, c in enumerate(tarefas, start=1):
             print(f"{i} → {c['descricao']} {c['agendamento']}")
     elif description == "3":
        for i, v in enumerate(tarefas, start=1):
            print(f"{i} → {v['descricao']} {v['agendamento']}")
            done = input("Qual tarefa foi finalizada? ")
            finalizada.append(done)
            print("Parabéns, tarefa concluída!")
     elif description == "4":
         print("Saindo...")
         break

print("tarefas em aberto")
print(tarefas)
print(finalizada)




