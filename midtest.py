# def find_integer_with_most_divisors(input_list):
#     result_list =[]
#     for item in input_list:
#         counter = 0
#         for i in range(1, item):
#             if item % i == 0:
#                 counter += 1
#         result_list.append(counter)
#     maximum = result_list[0]
#
#     for i in range(len(result_list)):
#         if result_list[i] > maximum:
#             maximum = result_list[i]
#             index_max = result_list.index(maximum)
#
#     return input_list[index_max]
#
#
# input_list = [8, 12, 18, 6]
# print(find_integer_with_most_divisors(input_list))





n=int(input('please enter an integer between 1 and 9999: '))
list_yekan = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
list_dahgan = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
list_dahta = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
list_sad = ["hundred", "thousand"]
n = str(n)
list_maked = []
for item in n:
    list_maked.append(item)
for i in range(len(list_maked)):
    num = int(list_maked[i])
    list_maked[i] = list_yekan