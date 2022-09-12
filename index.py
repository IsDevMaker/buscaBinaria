
vetor = [0, 10, 20, 30, 40, 50, 60, 70]


def pesquisa_binaria(vetor, valor):
    left, right = 0, len(vetor) - 1
    while left <= right:
        meio = (left+right)//2
        if vetor[meio] == valor:
            return meio
        elif vetor[meio] > valor:
            right = meio - 1
        else:
            left = meio + 1
    return -1


for value in range(3):
    value = int(input('digite seu valor:'))
    resultado_valor = pesquisa_binaria(vetor,value)
    
    

    if resultado_valor == -1:
          
            print(f'pesquisa falhou{pesquisa_binaria(vetor, value)}')
        
    else:
         print(f'pesquisa foi um sucesso: {pesquisa_binaria(vetor, value)} ')
        
        
    



