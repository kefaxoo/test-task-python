"""
В N корзинах находятся золотые монеты. Корзины пронумерованы числами от 1 до N. Во всех корзинах, кроме одной, монеты
весят по w граммов. В одной корзине монеты фальшивые и весят w–d граммов. Волшебник берет 1 монету из первой корзины, 2
монеты из второй корзины, и так далее, и, наконец, N-1 монету из (N-1)-й корзины. Из N-й корзины он не берет ничего. Он
взвешивает взятые монеты и сразу указывает на корзину с фальшивыми монетами. Напишите программу, которая сможет
выполнять такое волшебство. Дано: четыре целых числа: N, w, d и P – суммарный вес отобранных монет. Найти номер корзины
с фальшивыми монетами.
"""
from InputLibrary import int_input

def main():
    N = int_input("Enter count of baskets: ")
    w = int_input("Enter weight of real coins: ")
    d = int_input("Enter difference between weight of real and fake coins: ")
    P = int_input("Enter summary weight of coins: ")
    summary_weight = 0
    for i in range(N):
        summary_weight += i * w

    if summary_weight == P:
        print("Basket with fake coins:", N)
    else:
        print("Basket with fake coins:", (P - summary_weight) // d)

if __name__ == "__main__":
    main()