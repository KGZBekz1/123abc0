# 1, 2, 3. Функция пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    # Внешний цикл проходит по всем элементам
    for i in range(n):
        swapped = False
        # Внутренний цикл сравнивает каждый элемент с его соседним
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Если текущий элемент больше следующего, меняем их местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если во внутреннем цикле не было обменов, значит массив уже отсортирован
        if not swapped:
            break
    return arr


# Применение функции пузырьковой сортировки
unsorted_list = [7, 4, 5, 2, 7]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)


# 4, 5, 6. Функция двоичного поиска
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Если элемент найден
        if arr[mid] == target:
            return f"Элемент {target} найден на индексе {mid}"
        elif arr[mid] < target:
            # Игнорируем левую половину
            low = mid + 1
        else:
            # Игнорируем правую половину
            high = mid - 1

    return f"Элемент {target} не найден"


# Применение функции бинарного поиска
element_to_search = 5
search_result = binary_search(sorted_list, element_to_search)
print(search_result)
