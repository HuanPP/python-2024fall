def question1(x):
    maxval = x[0]
    minval = x[0]
    sumval = 0
    for i in x:
        if i > maxval:
            maxval = i
        if i < minval:
            minval = i
        sumval += i
    print("Question 1 Results:")
    print(f"最大值是 {maxval}")
    print(f"最小值是 {minval}")
    average = sumval / len(x)
    print(f"总和是 {sumval}")
    print(f"平均值是 {average}")
    print("")

def question2():
    month = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    while True:
        x = int(input("输入一个整数 (1-12): "))
        if 1 <= x <= 12:
            print("Question 2 Result:")
            print("英文单词是 " + month[x])
            print("")
            break
        else:
            print("错误的数字，请重新输入")

def question3(alist, start, end):
    blist = alist[start:end]
    print("Question 3 Result:")
    print(f"子列表是 {blist}")
    print("")
    return blist

from itertools import combinations

def question4(nums):
    result = []
    n = len(nums)
    for r in range(2, n + 1):
        for combo in combinations(nums, r):
            if sum(combo) == 9:
                result.append(combo)
    print("Question 4 Result:")
    print(f"所有和为9的组合: {result}")
    print("")
    return result

def question5(nums):
    unique_nums = list(set(nums))
    print("Question 5 Result:")
    print(f"去重后的列表: {unique_nums}")
    print("")

def question6(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print("Question 6 Result:")
            print(f"目标值 {target} 的索引是 {mid}")
            print("")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Question 6 Result:")
    print("目标值未找到，返回 -1")
    print("")
    return -1

def question7(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Question 7 Result:")
    print(f"冒泡排序后的数组: {arr}")
    print("")
    return arr

def question8(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Question 8 Result:")
    print(f"选择排序后的数组: {arr}")
    print("")
    return arr

def question9(wordlist):
    print("Question 9 Result:")
    for element in wordlist:
        if isinstance(element, list):
            question9(element)
        else:
            print(element, end=", ")
    print("\n")

def question10(wordlist):
    cleaned_list = [item.replace(" ", "") for item in wordlist]
    new_list = [item for item in cleaned_list if item.lower().startswith('a') and item.lower().endswith('c')]
    print("Question 10 Result:")
    print(f"原列表： {cleaned_list}")
    print(f"新列表： {new_list}")
    print("")

import random

def question11():
    unique_random_list = random.sample(range(0, 11), 10)
    print("Question 11 Result:")
    print(f"随机生成的列表: {unique_random_list}")
    print("")

def question12(alist):
    alist.sort()
    n = len(alist)
    sumval = sum(alist[1:n-1])
    average = sumval / (n - 2)
    print("Question 12 Result:")
    print(f"去掉最大和最小值的平均值是 {average}")
    print("")

# Testing each function with sample inputs
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 1]
question1(list1)
question2()
question3(list1, 2, 5)
question4(list1)
question5(list1)
question6(list1, 8)
question7(list1)
question8(list1)
wordlist = [1, 3, 4, "sishu", ["aa", "bb", "cc"], 5, "it"]
question9(wordlist)
tryOnce = ["IT sishu", "alexC", "Ab C ", "egon ", " ticToc ", " Angle ", " aqc"]
question10(tryOnce)
question11()
question12(list1)
