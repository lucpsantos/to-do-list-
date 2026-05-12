lista_de_tarefas = []

while True:
  print ("\n ======== Lista de Tarefas =========")
  print ("1 - Adicionar Tarefas")
  print ("2 - Listar Tarefas")
  print ("3 - Remover Tarefas")
  print ("4 - Sair")

  opcao_menu = input("Selecione a opção desejada: ").strip()

  if opcao_menu == "1":
    tarefa_adicionada = input('Escreva a tarefa a ser adicionada em sua lista: ')
    lista_de_tarefas.append(tarefa_adicionada)

  elif opcao_menu == "2":
        if len(lista_de_tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(lista_de_tarefas, start=1):
                print(f"{i}. {tarefa}") 

  elif opcao_menu == "3": 
      tarefa_removida = input("Digite a tarefa que deseja remover: ")

      if tarefa_removida in lista_de_tarefas:
          lista_de_tarefas.remove(tarefa_removida)
          print("Tarefa removida com sucesso!")
      else:
          print("Tarefa inválida. Essa tarefa não está na lista.") #caso não esteja na lista

  elif opcao_menu == "4":
    print("Saindo do programa")
    break

  else:
    print("Opção Inválida.")