"""
EXERCÍCIO 06 — GERENCIADOR DE TAREFAS

ENUNCIADO:
Desenvolva um gerenciador de tarefas que permita cadastrar, listar,
concluir e remover tarefas. Cada tarefa deverá possuir descrição,
prioridade e status de conclusão.
"""

tarefas = []


def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ").strip()

    if not descricao:
        print("A descrição não pode ficar vazia.")
        return

    prioridade = input("Prioridade (baixa, média ou alta): ").strip().lower()

    if prioridade not in ("baixa", "média", "alta"):
        print("Prioridade inválida.")
        return

    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "prioridade": prioridade,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("Tarefa cadastrada.")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"

        print(
            f'\nID: {tarefa["id"]}'
            f'\nDescrição: {tarefa["descricao"]}'
            f'\nPrioridade: {tarefa["prioridade"]}'
            f'\nStatus: {status}'
        )


def concluir_tarefa():
    listar_tarefas()

    try:
        identificador = int(input("\nID da tarefa: "))

        for tarefa in tarefas:
            if tarefa["id"] == identificador:
                tarefa["concluida"] = True
                print("Tarefa concluída.")
                return

        print("Tarefa não encontrada.")

    except ValueError:
        print("Digite um ID válido.")


def remover_tarefa():
    listar_tarefas()

    try:
        identificador = int(input("\nID da tarefa: "))

        for tarefa in tarefas:
            if tarefa["id"] == identificador:
                tarefas.remove(tarefa)
                print("Tarefa removida.")
                return

        print("Tarefa não encontrada.")

    except ValueError:
        print("Digite um ID válido.")


def main():
    while True:
        print("\n========== GERENCIADOR DE TAREFAS ==========")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()