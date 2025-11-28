# "Что вы хотите запустить?:\n"
#     "1: Алгоритмы сортировки\n"
#     "2: Фибоначчи\n"
#     "3: Факториал\n"
#     "4: Стек через связный список\n"
#     "5: бенчмарк для алгоритмов сортировки\n" \
#     "6: Визуализация эффективности алгоритмов сортировки")
from src.sorting.sort_algorithms import *
from src.sorting.benchmark import *
from src.factorial_fibonacci.fibonacci import *
from src.factorial_fibonacci.factorial import *
from src.stack.stack import LinkedList


import time


sorting_alg = {
    "1": bubble_sort,
    "2": quick_sort,
    "3": counting_sort,
    "4": radix_sort,
    "5": bucket_sort,
    "6": heap_sort
}

def app_full_cycle(inp: str):
    match inp:
        case '1':
            """
             Алгоритмы сортировки
            """
            print(f"Вы выбрали {inp}: Алгоритмы сортировки, выберите тип сортировки и режим работы\n")

            print("Алгоритм сортировки:\n"
                  "1: Пузырьковая сортировка\n" \
                  "2: Быстрая сортировка\n" \
                  "3: Сортировка подсчетом\n" \
                  "4: Поразрядная сортировка\n" \
                  "5: Блочная сортировка\n" \
                  "6: Пирамидальная сортировка")
            type_of_sort = input()
            
            print("Режим работы:\n" \
            "1: Готовые пресеты массивов\n" \
            "2: Пользовательский массив")
            mode = input()
            

            if mode == "1":
                print("Выберите пресет массива (чтобы посмотреть список, напишите list)")
                preset = input("Введите ваш пресет: ")
                while preset == "list" and not arrays.keys().__contains__(preset) and not float_arrays.keys().__contains__(preset):
                    if preset != "list":
                        print("Нет такого пресета")
                    arrs = arrays.keys()
                    for i in arrs:
                        print(i)
                    print("----------------\n"
                        "Для bucket_sort:\n" \
                        "----------------")
                    float_arrs = float_arrays.keys()
                    for i in float_arrs:
                        print(i)
                    preset = input()

                match type_of_sort:
                    case "1":
                        array = arrays.get(preset)
                        print(f"Исходный массив: {array}")
                        start = time.perf_counter()
                        print(f"Отсортированный массив: {bubble_sort(array)}")
                        end = time.perf_counter()
                        print(f"Время сортировки: {end - start} секунд")
                        
                    case "2":
                        array = arrays.get(preset)
                        print(f"Исходный массив: {array}")
                        start = time.perf_counter()
                        print(f"Отсортированный массив: {quick_sort(array)}")
                        end = time.perf_counter()
                        print(f"Время сортировки: {end - start} секунд")

                    case "3":
                        array = arrays.get(preset)
                        print(f"Исходный массив: {array}")
                        start = time.perf_counter()
                        print(f"Отсортированный массив: {counting_sort(array)}")
                        end = time.perf_counter()
                        print(f"Время сортировки: {end - start} секунд")

                    case "4":
                        array = arrays.get(preset)
                        print(f"Исходный массив: {array}")
                        start = time.perf_counter()
                        print(f"Отсортированный массив: {radix_sort(array)}")
                        end = time.perf_counter()
                        print(f"Время сортировки: {end - start} секунд")

                    case "5":
                        array = float_arrays.get(preset)
                        bucket = int(input("Укажите размер одного блока: "))
                        print(f"Исходный массив: {array}")
                        start = time.perf_counter()
                        print(f"Отсортированный массив: {bucket_sort(array, bucket)}")
                        end = time.perf_counter()
                        print(f"Время сортировки: {end - start} секунд")

                    case "6":
                        array = arrays.get(preset)
                        print(f"Исходный массив: {array}")
                        start = time.perf_counter()
                        print(f"Отсортированный массив: {heap_sort(array)}")
                        end = time.perf_counter()
                        print(f"Время сортировки: {end - start} секунд")
                    

                    case _:
                        raise ValueError(f"Неизвестная команда {type_of_sort}")

            elif mode == "2":
                pass

            else:
                raise ValueError(f"Неизвестная команда {mode}")
            
            
            



        case '2':
            """
            Фибоначчи
            """
            print(f"Вы выбрали {inp}")
            type_of_fib = input("Выберите тип подсчета числа с номером n в ряду фибоначчи:\n" \
            "1: Стандартный\n" \
            "2: Рекурсивный\n")

            if type_of_fib == "1":
                n = input("Ваше число n: ")
                print(fibo(int(n)))
            elif type_of_fib == "2":
                n = input("Ваше число n: ")
                print(fibo_recursive(int(n)))
            else:
                raise ValueError(f"Неизвестная команда {type_of_fib}")
            
            

        case '3':
            """
            Факториал
            """
            print(f"Вы выбрали {inp}")
            type_of_fac = input("Выберите тип подсчета факториала числа n:\n" \
            "1: Стандартный\n" \
            "2: Рекурсивный\n")

            if type_of_fac == "1":
                n = input("Ваше число n: ")
                print(factorial(int(n)))
            elif type_of_fac == "2":
                n = input("Ваше число n: ")
                print(factorial_recursive(int(n)))
            else:
                raise ValueError(f"Неизвестная команда {type_of_fib}")

        case '4':
            """
            Стек через связный список
            """
            print(f"Вы выбрали {input}")

            print("Выберите операцию над стеком:\n" \
                "1: push\t" \
                "2: pop\t" \
                "3: peek\t" \
                "4: is empty\t" \
                "5: length\t" \
                "6: min\t" \
                "7: print elements\n" \
                "info: Показать это сообщение снова")
            
            stack = LinkedList()

            while (True):
                
                action = input("Stack playground >>> ")
                match action:
                    case "1":
                        """push"""
                        try:
                            num = int(input("Помещяемый элемент (целое число):"))
                            stack.push(num)
                        except Exception:
                            print("Вводите целое число")
                        
                        
                    case "2":
                        """pop"""
                        print(stack.pop())
                    case "3":
                        """peek"""
                        print(stack.peek())
                    case "4":
                        """is_empty"""
                        print(stack.is_empty())
                    case "5":
                        """length"""
                        print(stack.__len__())
                    case "6":
                        """min"""
                        print(stack.min())
                    case "7":
                        """print elements"""
                        print(stack.print_elements())
                    case "info":
                        print("Выберите операцию над стеком:" \
                        "1: push\t" \
                        "2: pop\t" \
                        "3: peek\t" \
                        "4: is empty\t" \
                        "5: length\t" \
                        "6: min\t" \
                        "7: print elements\n" \
                        "info: Показать это сообщение снова")
                    case "exit":
                        break
                        
                    case _:
                        print(f"Несуществующая команда {action}")


        case '5':
            """
            бенчмарк для алгоритмов сортировки
            """
            print(f"Вы выбрали {input}")
            print(show_benchmark_results(benchmark))


        case '6':
            """
            Визуализация эффективности алгоритмов сортировки
            """
            print(f"Вы выбрали {input}")
            print("Пока не работает(")

        case _:
            raise ValueError(f"Неизвестная команда {input}")
