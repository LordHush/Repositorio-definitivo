# -*- coding: utf-8 -*-
"""projeto1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bKjdygxzZ9yJ29hqm_0XVHqtbnXcaZli
"""







print("Terminal de operacoes hHh alterei aqui\n")
print("Adicionei aqui\n")
print("kkkk ssss")
contas=[]
def listar_contas():
  if contas:
    for  conta in contas:

      print(f"Numero da conta {conta['numero']} saldo {conta['saldo']:.2f}R$")
  else:
    print("Ainda nao foi criada nenhuma conta \n")


def criar_conta():
    existe=0
    dados_conta=dict()
    num=input("Digite o numero da conta:\n")
    dados_conta["numero"]=num
    for conta in contas:
        if conta["numero"] == dados_conta["numero"]:
          print("Essa conta ja existe, tente novamente!\n")

          break
    if not existe:
          dados_conta["saldo"]=float(input("digite o saldo:\n"))
          contas.append(dados_conta)
def remover_conta():
    num=input("digite o numero da conta que deseja remover:\n")
    existe=False
    for conta in contas:
      if num in conta.values():
        contas.remove(conta)
        existe=True
        print("Conta removida com sucesso!")
    if not existe:
        print("Conta nao consta no banco de dados")
        return
def creditar():
    entrada=input("Digite o numero da conta que quer adicionar saldo:\n")

    existe=False
    for conta in contas:
      if(conta["numero"] == entrada):
        credito=float(input("Digite o valor do saldo que quer adicionar a sua conta:\n"))
        if credito < 0:

          print("Digite apenas valores positivos \n")
          return
        else:
          soma=conta["saldo"]+credito
          conta["saldo"]=soma
          existe=True
          print(f"Foi adicionado {soma}R$ a sua conta bancaria\n")
    if not existe:
        print("Essa conta nao consta no banco de dados\n")

def debitar():
    entrada=input("Digite o numero da conta que quer debitar o saldo:")
    existe=False
    for conta in contas:
        if(conta["numero"] == entrada):
              credito=float(input("Digite o valor do saldo que quer debitar da sua conta:"))
              if credito > conta["saldo"]:

                    print("Voce nao tem saldo suficiente para realizar este saque\n")
                    return
              elif credito < 0:
                print("Digite apenas valores positivos\n")
              else:
                sub=conta["saldo"]-credito
                conta["saldo"]=sub
                existe=True
                print(f"Foi debitado -{credito}R$ da sua conta bancaria, saldo disponivel {conta['saldo']}")
    if not existe:
        print("Essa conta nao consta no banco de dados\n")
def transferir():
     entrada=input("qual o número da sua conta?:\n")
     verificador=0
     for consulta_conta in contas:
        if entrada in consulta_conta["numero"]:
            verificador=1
            destino=input("digite a conta que deseja transferir:\n")



            for consulta_conta_destino in contas:
                if destino in consulta_conta_destino["numero"]:
                    verificador=1
                    valor=float(input("digite o valor que quer transferir:\n"))

                    if valor > consulta_conta["saldo"]:
                        print("Você não possui saldo suficiente para realizar a transferência\n")
                        break
                    elif valor <= 0:
                        print("Sao permitidas transfencias de valores acima de 0R$ apenas\n")
                        break
                    else:


                       consulta_conta_destino["saldo"]=valor+consulta_conta_destino["saldo"]
                       consulta_conta["saldo"]=consulta_conta["saldo"]-valor
                       print("Operacao realizada com sucesso.\n")
                       break
     if verificador==0:
        print("Essa conta nao existe no banco de dados\n")


while True:

  print("digite 0-finalizar operacoes\n")
  print("digite 1-criar uma conta\n")
  print("digite 2-remover a conta\n")
  print("digite 3-listar as contas criadas\n")
  print("digite 4-lancar credito na conta\n")
  print("digite 5-debitar saldo da sua conta\n")
  print("digite 6-transfeir\n")
  entrada=input("Qual operacao deseja realizar?:\n")
  if entrada == '0':
    print("Servico finalizado.")
    break
  elif entrada == '1':
    criar_conta()
  elif entrada== "2":
    remover_conta()
  elif entrada == '3':
    listar_contas()
  elif entrada=="4":
    creditar()
  elif entrada == "5":
    debitar()
  elif entrada == '6':
    transferir()

  else:
      print("Operacao Invalida\n")

