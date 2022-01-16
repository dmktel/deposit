per_cent = {'ТКБ':5.6, 'СКБ':5.9, 'ВТБ':4.28, 'СБЕР':4.0}
money = int(input("Введите сумму: ")) # input deposit value
deposit = list(per_cent.values()) # dict values to list conversion
deposit[0] = int(deposit[0] * money / 100) # year deposit calculation
deposit[1] = int(deposit[1] * money / 100)
deposit[2] = int(deposit[2] * money / 100)
deposit[3] = int(deposit[3] * money / 100)
print(deposit) # output deposit list with new elements
print("Максимальная сумма, которую вы можете заработать —", max(deposit)) # output max value in deposit list