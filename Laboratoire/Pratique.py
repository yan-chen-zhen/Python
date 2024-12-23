#1 質數
from turtle import rt

from flask.scaffold import F

def is_prime(n:int):
    # 如果 n 小於等於 1 或是偶數，則 n 不是質數
    if n <= 1 or n % 2 == 0:
        return False
    # 從 3 開始，每次加 2，檢查 n 是否能被 3, 5, 7, ... 整除
    for i in range(3, int(n**0.5) + 1, 2):
        # 如果 n 能被 i 整除，則 n 不是質數
        if n % i == 0:
            return False
    # 如果沒有找到能整除 n 的數字，則 n 是質數
    return True
# 測試範例
print(is_prime(2))  # True，2 是質數
print(is_prime(4))  # False，4 不是質數
print(is_prime(17))  # True，17 是質數


#2 費氏數列
def fibonacci(n):
    # 如果 n 小於等於 0，回傳空列表
    if n <= 0:
        return []
    # 如果 n 等於 1，回傳 [0]
    elif n == 1:
        return [0]
    # 如果 n 等於 2，回傳 [0, 1]
    elif n == 2:
        return [0, 1]
    # 初始化費式數列的前兩個數字
    fib_sequence = [0, 1]
    # 產生前 n 個費式數列
    # 從 2 開始，因為前兩個數字已經初始化了
    # _i 是一個不需要使用的變數 (類 C)
    for _i in range(2, n):
        # 新的數字是前兩個數字的和
        # -1 是最後一個數字，-2 是倒數第二個數字
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    # 回傳前 n 個費式數列
    return fib_sequence[:n]
# 測試範例
print(fibonacci(6))  # [0, 1, 1, 2, 3, 5]
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

string = "Hello, World!"
string_reversed = ""
for i in range(len(string) - 1, -1, -1):
    print(string[i], end="")
    # string_reversed += string[i] # 字串相加
    # print(string_reversed)
print(string_reversed)


#3 完全平方數
n = 17
# if (n ** 0.5) % 1 == 0:
#     print(f"{n} 是一個完全平方數")
# else:
#     print(f"{n} 不是一個完全平方數")

def list_square_integers(n):
    #
    if n < 1:
        return []
    # 儲存完全平方數的陣列
    square_integers = []
    # 檢查 1, 2, 3, ..., n 是否是完全平方數
    for i in range(1, n + 1):
        # 如果 i 是完全平方數
        # i ** 0.5 = 開根號, % 1 = 取餘數
        if (i**0.5) % 1 == 0:
            # 如果是完全平方數，就加入陣列
            square_integers.append(i)
    return square_integers
print(list_square_integers(20))  # [1, 4, 9, 16]


# #4 質因數分解
from multiprocessing.spawn import is_forking


def prime_factors(n):
#     # 儲存質因數的陣列
    factors = []
#     # 從 2 開始，檢查 n 是否能被 2, 3, 4, ... 整除
    for i in range(2, n + 1):
#         # 如果 i 是質數，且能被 n 整除
        if is_prime(i) and n % i == 0:
#             # 如果是質因數，就加入陣列
            factors.append(i)
    return factors

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
    
    
#完美數
def is_perfect_number(n):
    if n <= 0:
        return False
    sum_of_factors = 0
    for i in range(1, n):
        if n % i == 0:
                sum_of_factors += i
        return sum_of_factors == n
    
    print(is_perfect_number(6)) 
    print(is_perfect_number(28))
    print(is_perfect_number(12))  
    
    
# 阿姆斯壯數
def is_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == n

print(is_armstrong_number(153))
print(is_armstrong_number(9474))
print(is_armstrong_number(123))


# 自動冪數
def is_automorphic_number(n):
    square = n ** 2
    str_n = str(n)
    str_square = str(square)
    return str_square.endswith(str_n)

n = int(input("請輸入一個數字 n: "))

automorphic_numbers = []
for i in range(n):
    if is_automorphic_number(i):
        automorphic_numbers.append(i)

print(f"小於 {n} 的所有自動冪數: {automorphic_numbers}")


# 雙數反轉
def is_palindromic_number(n):
    str_n = str(n)
    return str_n == str_n[::-1]

n = int(input("請輸入一個數字 n: "))

palindromic_numbers = []
for i in range(10,n):
    if is_palindromic_number(i):
        palindromic_numbers.append(i)

print(f"小於 {n} 的所有雙數反轉數: {palindromic_numbers}")


# 數字累加等於給定值
def is_sum_of_digits_equal_to(n, target_sum):
    sum_of_digits = sum(int(digit) for digit in str(n))
    return sum_of_digits == target_sum

n = int(input("請輸入一個數字 n: "))
target_sum = int(input("請輸入目標和 target_sum: "))

matching_numbers = []
for i in range(n):
    if is_sum_of_digits_equal_to(i, target_sum):
        matching_numbers.append(i)

print(f"小於 {n} 的所有數字，其數字累加和等於 {target_sum} 的數字: {matching_numbers}")


# 卡布列克數
def is_kaprekar_number(n):
    square = n ** 2
    str_square = str(square)
    for i in range(1, len(str_square)):
        left_part = str_square[:i]
        right_part = str_square[i:]
        if int(right_part) != 0 and int(left_part) + int(right_part) == n:
            return True
    return False

n = int(input("請輸入一個數字 n: "))

kaprekar_numbers = []
for i in range(n):
    if is_kaprekar_number(i):
        kaprekar_numbers.append(i)

print(f"小於 {n} 的所有卡布列克數: {kaprekar_numbers}")