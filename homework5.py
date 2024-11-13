def question1():
    dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33]}

    # 1. 循环输出所有的 key
    for key in dic.keys():
        print("Key:", key)

    # 2. 循环输出所有的 value
    for value in dic.values():
        print("Value:", value)

    # 3. 循环输出所有的 key 和 value
    for key, value in dic.items():
        print(f"Key: {key}, Value: {value}")

    # 4. 添加键值对 'k4': 'v4'
    dic['k4'] = 'v4'
    print("After adding 'k4':", dic)

    # 5. 修改 'k1' 对应的值为 'alex'
    dic['k1'] = 'alex'
    print("After modifying 'k1':", dic)

    # 6. 在 'k3' 对应的值中追加一个元素 44
    dic['k3'].append(44)
    print("After appending 44 to 'k3':", dic)

    # 7. 在 'k3' 对应的值的第 1 个位置插入元素 18
    dic['k3'].insert(0, 18)
    print("After inserting 18 to 'k3':", dic)

    # 8. 删除键值对 'k1': 'v1'
    dic.pop('k1', None)
    print("After deleting 'k1':", dic)

    # 9. 删除键 'k5' 对应的键值对，如果不存在则返回 None
    dic.pop('k5', None)
    print("After attempting to delete 'k5':", dic)

    # 10. 获取 'k2' 对应的值
    print("Value of 'k2':", dic.get('k2'))

    # 11. 获取 'k6' 对应的值，如果不存在则返回 None
    print("Value of 'k6':", dic.get('k6'))


def question2():
    dic2 = {'k1': 'v111', 'a': 'b'}

    # 通过一行代码更新 dic2 为所要求的值
    dic2.update({'k1': 'v1', 'k2': 'v2', 'k3': 'v3'})
    print("Updated dic2:", dic2)


def question3():
    lis = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]

    # 1. 将 'tt' 变成大写
    lis[0][1][2]['k1'][0] = lis[0][1][2]['k1'][0].upper()
    print("After uppercasing 'tt':", lis)

    # 2. 将 3 变成 '100'
    lis[0][1][2]['k1'][1] = '100'
    print("After changing 3 to '100':", lis)

    # 3. 将 '1' 变成 101
    lis[0][1][2]['k1'][2] = 101
    print("After changing '1' to 101:", lis)


def question4():
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 4, 'f': 3, 'g': 3}

    # 1. 计算值的总和与乘积
    total_sum = sum(sample_dict.values())
    total_product = 1
    for value in sample_dict.values():
        total_product *= value
    print("Sum of values:", total_sum)
    print("Product of values:", total_product)

    # 2. 查找最大值和最小值
    max_value = max(sample_dict.values())
    min_value = min(sample_dict.values())
    print("Max value:", max_value)
    print("Min value:", min_value)

    # 3. 查找出现次数最多的值
    from collections import Counter
    most_common_value = Counter(sample_dict.values()).most_common(1)[0][0]
    print("Most frequent value:", most_common_value)

    # 4. 计算值为偶数的键的总和
    even_sum = sum(value for value in sample_dict.values() if value % 2 == 0)
    print("Sum of even values:", even_sum)

    # 5. 删除值小于 3 的键值对
    sample_dict = {k: v for k, v in sample_dict.items() if v >= 3}
    print("After removing values < 3:", sample_dict)

    # 6. 将键值对互换
    inverted_dict = {v: k for k, v in sample_dict.items()}
    print("Inverted dictionary:", inverted_dict)



print("Question 1 results:")
question1()
print("\nQuestion 2 results:")
question2()
print("\nQuestion 3 results:")
question3()
print("\nQuestion 4 results:")
question4()