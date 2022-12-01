def delete(list_, index=None):
    if index == None:
        index = len(list_) - 1
    list_1 = list_[:index] + list_[index + 1:]
    return list_1

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
