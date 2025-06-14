def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in [9, 10]:
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False

    return True


def validar_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calc_digito(cnpj, pesos):
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1

    dig1 = calc_digito(cnpj[:12], pesos1)
    dig2 = calc_digito(cnpj[:12] + dig1, pesos2)

    return cnpj.endswith(dig1 + dig2)


def main():
    print("Validador de CPF e CNPJ")
    entrada = input("Digite um CPF ou CNPJ: ")

    if len(entrada.replace(".", "").replace("-", "").replace("/", "")) <= 11:
        valido = validar_cpf(entrada)
        tipo = "CPF"
    else:
        valido = validar_cnpj(entrada)
        tipo = "CNPJ"

    if valido:
        print(f"{tipo} válido! ")
    else:
        print(f"{tipo} inválido.")


if __name__ == "__main__":
    main()
