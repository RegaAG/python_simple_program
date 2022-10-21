def bubble_sort(list1):
    for i in range(0, len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j] > list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1


L = [45, 103, 12, 8, 3, 26, 82, 38]
print("Sebelum di insertion sort : ", L)
print("Sesudah di insertion sort : ", bubble_sort(L))