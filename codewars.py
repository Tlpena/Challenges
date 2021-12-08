# def square_digits(num):
#     ret = ""
#     for n in str(num):
#         ret += str(int(n) ** 2)
#     return int(ret)
#
#
# print(square_digits(9119))
#
#
# pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#
#
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])
#
#
# print(DNA_strand("ATATAGG"))
#
# def narcissistic(num):
#     return num == sum([int(x) ** len(str(num)) for x in str(num)])
#
#
# print(narcissistic(153))

# def descending_order(num):
#     return int("".join(sorted(str(num), reverse=True)))
#
#
# print(descending_order(145897134))

# def persistence(x):
#     pcount = 0
#     while x >= 10:
#         y = x
#         z = 1
#         while y != 0:
#             z = z * (y % 10)
#             y = y // 10
#         x = z
#         pcount += 1
#     return pcount
#
#
# print(persistence(999)

# def solution(number):
#     total_sum = 0
#     for i in range(number):
#         if (i % 3 == 0 or i % 5 == 0):
#             total_sum = total_sum + i
#     return total_sum
#
# return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
#
#
# print(solution(10))

# def to_jaden_case(string):
#     s = ' '.join(word[0].upper() + word[1:] for word in string.split())
#     return s
#
#
# print(to_jaden_case("yo dawg what is up"))

# def find_short(s):
#     length = [len(x) for x in s.split()]
#     return min(length)
#
#
# find_short("he is never going back he is dead")

# def array_diff(a, b):
#     return [x for x in a if x not in b]
#
#
# print(array_diff([1, 2, 2, 2, 3], [2]))

# def create_phone_number(n):
#     f = "".join(map(str, n[0:3]))
#     s = "".join(map(str, n[3:6]))
#     t = "".join(map(str, n[6:10]))
#     return '({}) {}-{}'.format(f, s, t)
#
#
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# def avg(*num):
#     total_sum = 0
#     for t in num:
#         total_sum = total_sum + t
#     avg = total_sum / len(num)
#     return avg
#
#
#
# print(avg(1, 3, 4, 5, 2))
# from string import punctuation
#
#
# def pig_it(string):
#     s = ' '.join(word[1:] + word[0] + "ay" if word not in punctuation else word for word in string.split())
#     return s
#
#
# print(pig_it("Hello all I am the man !"))

# def digital_root(n):
#     x = str(n)
#     while len(x) != 0 and len(x) != 1:
#         r = 0
#         for i in range(len(x)):
#             r = r + int(x[i])
#         x = str(r)
#     return r
#
# return n if n < 10 else digital_root(sum(map(int,str(n))))
#
#
# print(digital_root(942))

# def move_zeros(array):
#     for n in sorted(array):
#         if n == 0:
#             array.pop(n)
#     return array
#
#
#
# print(move_zeros([False, 1, 1, 0, 1, 2, 0, 0, 2, 3]))

# def song_decoder(song):
#     return ' '.join(song.replace('WUB', ' ').split())
#
#
#
# print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
# def tribonacci(signature, n):
#     res = signature[:n]
#     for i in range(n - 3):
#         res.append(sum(res[-3:]))
#     return res
#
#
# print(tribonacci([0, 0, 1], 10))

# def cakes(recipe, available):
#     return min(available.get(k, 0) // recipe[k] for k in recipe)
#
#
# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# print(cakes(recipe, available))

# def scramble(s1, s2):
#     for letter in set(s2):
#         if s1.count(letter) < s2.count(letter):
#             return False
#     return True
#
#
# print(scramble('katas', 'steak'))
#
# def summation(num):
#     sum = 0
#     for n in range(1, num + 1):
#         sum += n
#     return sum
#
# print(summation(8))

# def last_digit(n1, n2):
#     return pow(n1, n2, 10)
#
#
# print(last_digit(4, 4))

# def high_and_low(numbers):
#     nums = sorted(numbers.split(), key=int)
#     return '{} {}'.format(nums[-1], nums[0])
#
#
# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
#
# def two_oldest_ages(ages):
#     return sorted(ages)[-2:]
#
#
# print(two_oldest_ages([1, 5, 87, 45, 8, 8]))

# def solve(s):
#     return s[::-1]
#
#
# print(solve("our code"))

# def get_count(input_string):
#     num_vowels = 0
#     for v in input_string:
#         if v in "aeiou":
#             num_vowels = num_vowels + 1
#
#     return num_vowels
#
#
# print(get_count("abracadabraeeekhwjbefoiaweu"))
#
# def filter_list(l):
#     new_list = []
#     for n in l:
#         if type(n) == int:
#             new_list.append(n)
#     return new_list
#
#
# print(filter_list([1,2,'aasf','1','123',123]))

# def is_triangle_number(number):
#     summ, n = 0, 1
#     if type(number) != int:
#         pass
#     else:
#         while summ <= number:
#             summ = summ + n
#             if summ == number:
#                 return True
#             n += 1
#     return False
#
#
# print(is_triangle_number(6))
# def solve(arr):
#     return sorted(arr, key=lambda x: (-arr.count(x), x))
#
#
# print(solve([2,3,5,3,7,9,5,3,7]))

# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     if len(cc) > 4:
#         return '#' * (len(cc) - 4) + cc[-4:]
#
#
# print(maskify("4556364607935616"))

# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 != 0:
#             return i
#
#
# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

# def spin_words(sentence):
#     returned_string = []
#     new_sentence = sentence.split(' ')
#     for word in new_sentence:
#         if len(word) >= 5:
#             returned_string.append(word[::-1])
#         else:
#             returned_string.append(word)
#
#     return ' '.join(returned_string)
#
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
#
#
# print(spin_words("Hello my name is Thatcher and I am really intoxicated"))
#
# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))
#
#
# print(order("is2 Thi1s T4est 3a"))

# def is_valid_walk(walk):
#     if len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
#         return True
#     else:
#         return False
#
#
# print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))

# def iq_test(numbers):
#     numbers = [int(i) % 2 for i in numbers.split()]
#     if numbers.count(0) > 1:
#         return numbers.index(1) + 1
#     else:
#         return numbers.index(0) + 1
#
#
# print(iq_test("2 4 6 8 10 11"))
#
# def get_middle(s):
#     x = len(s)
#     if x % 2 == 0:
#         return s[(x // 2) - 1: (x // 2) + 1]
#     else:
#         return s[x // 2]
#
#
# print(get_middle("test"))
# print(get_middle("testing"))

# def friend(x):
#     # friends = []
#     # for name in x:
#     #     if len(name) == 4:
#     #         friends.append(name)
#     # return friends
#
#     return [name for name in x if len(name) == 4]
#
#
# print(friend(["Ryan", "Kieran", "Mark"]))

# def count_smileys(arr):
#     # new_faces = []
#     # for face in arr:
#     #     if face in ':D:-D:~D;D;-D;~D:-):):~);~);-);)':
#     #         new_faces.append(face)
#     # return len(new_faces)
#
#
# print(count_smileys([':)', ':(', ':D', ':O', ':;']))

# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
#
#
# print(duplicate_encode("Success"))
#
# def sort_array(source_array):
#     odds = iter(sorted(el for el in source_array if el % 2))
#     return [next(odds) if el % 2 else el for el in source_array]
#
#
# print(sort_array([5, 3, 2, 8, 1, 4]))

# def solution(n):
#     roman_numerals = {1000: 'M',
#                       900: 'CM',
#                       500: 'D',
#                       400: 'CD',
#                       100: 'C',
#                       90: 'XC',
#                       50: 'L',
#                       40: 'XL',
#                       10: 'X',
#                       9: 'IX',
#                       5: 'V',
#                       4: 'IV',
#                       1: 'I'
#                       }
#     roman_string = ''
#     for key in sorted(roman_numerals.keys(), reverse=True):
#         while n >= key:
#             roman_string += roman_numerals[key]
#             n -= key
#     return roman_string
#
#
# print((solution(540)))
#
# def queue_time(customers, n):
#     l = [0] * n
#     for i in customers:
#         l[l.index(min(l))] += i
#     return max(l)
#
#
# print(queue_time([], 1))
#
# def find_missing_letter(chars):
#     n = 0
#     while ord(chars[n]) == ord(chars[n+1]) - 1:
#         n += 1
#     return chr(1+ord(chars[n]))
#
#
# print(find_missing_letter(['O', 'Q', 'R', 'S']))
#
# def number(bus_stops):
#     people = 0
#     for items in bus_stops:
#         people += items[0]
#         people -= items[1]
#
#     return people
#
#
# print((number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]])))
# def find_outlier(integers):
#     odd_numbers = []
#     even_numbers = []
#     for item in integers:
#         if item % 2 == 0:
#             even_numbers.append(item)
#         else:
#             odd_numbers.append(item)
#     if len(even_numbers) < len(odd_numbers):
#         return even_numbers[0]
#     else:
#         return odd_numbers[0]
#
#     odds = [x for x in int if x%2!=0]
#     evens= [x for x in int if x%2==0]
#     return odds[0] if len(odds)<len(evens) else evens[0]
#
#
# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
#
# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
#     return -1
#
#
# print(find_even_index([20, 10, 30, 10, 10, 15, 35]))

# def diamond(n):
#     if n > 0 and n % 2 == 1:
#         diamond = ""
#         for i in range(n):
#             diamond += " " * abs(int(n/2) - i)
#             diamond += "*" * (n - abs((n-1) - 2 * i))
#             diamond += "\n"
#         return diamond
#     else:
#         return None
#
# print(diamond(5))
def wave(people):
    new_words = []
    for i, c in enumerate(people):
        if c not in " ":
            new_words.append(people[:i] + c.upper() + people[i + 1:])

    return new_words



print(wave("two words"))

