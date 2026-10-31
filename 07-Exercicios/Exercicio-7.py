"""
EXERCÍCIO 07 — SISTEMA DE VOTAÇÃO

ENUNCIADO:
Crie um sistema de votação com três candidatos e a opção de voto
em branco. O programa deverá registrar os votos, calcular o total,
apresentar a porcentagem de cada candidato e identificar o vencedor.
Também deverá reconhecer situações de empate.
"""

def apresentar_resultado(votos):
    total = sum(votos.values())

    if total == 0:
        print("Nenhum voto foi registrado.")
        return

    print("\n========== RESULTADO ==========")

    for candidato, quantidade in votos.items():
        porcentagem = quantidade / total * 100
        print(f"{candidato}: {quantidade} votos ({porcentagem:.2f}%)")

    votos_candidatos = {
        nome: quantidade
        for nome, quantidade in votos.items()
        if nome != "Branco"
    }

    maior_votacao = max(votos_candidatos.values())

    vencedores = [
        nome for nome, quantidade in votos_candidatos.items()
        if quantidade == maior_votacao
    ]

    if len(vencedores) == 1:
        print(f"\nVencedor: {vencedores[0]}")
    else:
        print(f"\nEmpate entre: {', '.join(vencedores)}")

    print(f"Total de votos: {total}")


def main():
    candidatos = {
        "1": "Candidato A",
        "2": "Candidato B",
        "3": "Candidato C",
        "4": "Branco"
    }

    votos = {nome: 0 for nome in candidatos.values()}

    while True:
        print("\n========== ELEIÇÃO ==========")

        for numero, candidato in candidatos.items():
            print(f"{numero} - {candidato}")

        print("0 - Encerrar votação")

        opcao = input("Seu voto: ")

        if opcao == "0":
            break

        if opcao in candidatos:
            votos[candidatos[opcao]] += 1
            print("Voto registrado.")
        else:
            print("Opção inválida.")

    apresentar_resultado(votos)


if __name__ == "__main__":
    main()