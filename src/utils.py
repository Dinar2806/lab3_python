def get_digit_at_position(number, position):
    """
    Возвращает цифру на заданной позиции (начиная с 0 для единиц)
    """
    if not isinstance(number, int) or not isinstance(position, int):
        return (int(number) // (10**int(position))) % 10
    if number < 0:
        number = abs(number) # Работаем с абсолютным значением для удобства
    return (number // (10**position)) % 10


def counting_sort_for_radix(arr, exp):
    """
    Вспомогательная сортировка подсчетом для конкретного разряда
    """
    n = len(arr)
    output = [0] * n  # Выходной массив
    count = [0] * 10  # Счетчик для цифр 0-9
    
    # Подсчитываем количество каждой цифры в текущем разряде
    for i in range(n):
        # Получаем цифру текущего разряда
        # Например: число 345, exp=10 → (345 // 10) % 10 = 34 % 10 = 4
        digit = get_digit_at_position(arr[i], exp)
        count[digit] += 1
    
    # Преобразуем count так, чтобы он содержал позиции цифр в выходном массиве
    # Теперь count[i] содержит позицию, где должна находиться цифра i
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Строим выходной массив, обрабатывая исходный массив с конца
    # (это важно для сохранения стабильности)
    for i in range(n - 1, -1, -1):
        digit = get_digit_at_position(arr[i], exp)
        position = count[digit] - 1  # Позиция в выходном массиве (0-based)
        output[position] = arr[i]
        count[digit] -= 1  # Уменьшаем счетчик для следующего элемента с этой цифрой
    
    return output



def insertion_sort(arr):
    """Сортировка вставками - идеальна для маленьких массивов"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def heapify(arr, n, i):



    """
    Преобразование поддерева в max-кучу
    arr - массив
    n - размер кучи
    i - индекс корня поддерева
    """
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок
    
    # Если левый потомок существует и больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Если правый потомок существует и больше текущего наибольшего
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
        # Рекурсивно heapify затронутое поддерево
        heapify(arr, n, largest)


def show_benchmark_results(benchmark_results):
    
    
    # Группируем по алгоритмам
    for algos_name in benchmark_results.keys():
        print(f"\n Алгоритм: {algos_name}")
        print("-" * 60)
        
        # Получаем результаты для этого алгоритма
        algo_results = benchmark_results[algos_name]
        
        # Сортируем массивы по времени (от быстрого к медленному)
        sorted_arrays = sorted(
            [(array_name, time_taken) for array_name, time_taken in algo_results.items()],
            key=lambda x: x[1]
        )
        
        # Вывод с местами для каждого типа массива
        for place, (array_name, time_taken) in enumerate(sorted_arrays, 1):
            
            
            print(f"   {place} {array_name:<25}: {time_taken:.6f} сек")
