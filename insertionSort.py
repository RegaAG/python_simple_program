# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key


L = [45, 103, 12, 8, 3, 26, 82, 38]
print("Sebelum di insertion sort : ")
print(L)
insertionSort(L)
print("Sesudah di insertion sort : ")
print(L)