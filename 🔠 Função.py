#Função

def valor_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.20
    #Como você está calculando o valor do imposto obviamente você quer fazer algo com ele, então no final da função você pode usar a ferramenta "Return"
    #Essa ferramenta vai lhe voltar alguma informação
    return imposto

#O "valor" nessa função é o parâmetro, ou seja, o imposto precisa de um parâmetro para ser aplicado, nesse caso, é o valor:
#Não se precisa especificar uma variável para isso, pois a itenção é que possamos chamar essa função e usála a qualquer momento e com qualquer valor

Produto_1 = 2500
Produto_2 = 3500
Imposto_Produto_1 = valor_imposto(Produto_1)
Imposto_Produto_2 = valor_imposto(Produto_2)
print(Imposto_Produto_1)
print(Imposto_Produto_2)

#Lembrando que existem funções que NÃO precisam de um parâmetro (uma informação externa) pra funcionar

#Também não é necessário por o "Return"
#Pois, têm funções que não precisam retornar uma resposta e sim apenas realizar uma função
#Sempre que você tem uma informação dentro da função que você vai precisar usar fora da função você vai precisar usar o return
#Como por exemplo uma função que mande um e-mail, ela não precisa voltar nenhuma informação
