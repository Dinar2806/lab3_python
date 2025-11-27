import matplotlib
from src.app import full_cycle


def main():
    print("Что вы хотите запустить?:\n"
    "1: Алгоритмы сортировки\n"
    "2: Фибоначчи\n"
    "3: Факториал\n"
    "4: Стек через связный список\n"
    "5: бенчмарк для алгоритмов сортировки\n")

    while(True):
        inp = input()
        print(inp)


if __name__ == "__main__":

    main()