# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

#n = int(input("Введите число монет: ")) 

#k = 0
#for i in range(n):
    #v = int(input())
    #if v == 1:
        #k += 1
#print(k if k < n/2 else n-k)

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

#a, b = map(int, input().split())
#res = []
#for i in range(a + b):
    #if i == (a * i - b)**0.5:
        #res.append(i)
#print(*res if len(res) == 2 else res + res)



# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

#n = int(input())
#i = 0
#while 2 ** i <= n:
    #print(2 ** i)
#i += 1