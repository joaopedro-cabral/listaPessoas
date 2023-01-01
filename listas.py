def adicionar_elemento(lista: list, elemento: str) -> bool:
    import re

    regex = r'(^[A-Z]+[\sa-zA-z]+)'

    if re.fullmatch(regex, elemento) is not None:
        lista.append(elemento)
        return True

    '''
    Verifica se o elemento começa com letra maiúscula e possui apenas letras e espaços.
    Se ele passar na verificação, inserir na lista e retornar verdadeiro, caso contrário, retorne falso
    '''

def buscar_elemento(lista: list, elemento: str) -> bool:
    if elemento in lista:
        return True

    '''
    Verifica se um elemento está contido na lista.
    Se estiver, retorne verdadeiro, caso contrário, retorne falso.
    '''

def remover_elemento(lista: list, elemento: str) -> bool:
    if elemento in lista:
        lista.remove(elemento)
        return True

    '''
    Verifica se a lista contém um elemento específico.
    Se ele estiver contido na lista, remover o elemento e
    retornar verdadeiro, caso contrário, retornar falso.
    '''

def limpar_lista(lista: list) -> None:
    lista.clear()

    '''
    Remove todos os elementos da lista.
    Função sem retorno.
    '''

def ordenar_lista(lista: list) -> None:
    lista.sort()

    '''
    Ordena todos os elementos da lista por ordem
    alfabética. A função não possui retorno
    '''

def pegar_quantidade(lista: list) -> int:
    return len(lista)

    '''
    Retorna a quantidade de elementos dentro
    da lista
    '''

def converter_maiusculo(lista: list) -> list:
    lista_maiusculas = []
    for i in lista:
        lista_maiusculas.append(i.upper())
    
    return lista_maiusculas

    '''
    Converte todos os elementos da lista para letra
    maiúscula e os retorna em uma nova lista
    '''

def eliminar_repetidos(lista: list) -> list:
    lista_sem_rep = lista[:]

    for i in lista:
        if lista_sem_rep.count(i) > 1:
            lista_sem_rep.remove(i)

    return lista_sem_rep
           
    '''
    DESAFIO: 0.5 extra
    Remove todos os elementos repetidos na lista
    e retorna uma lista nova
    (não vale utilizar o set)
    '''
