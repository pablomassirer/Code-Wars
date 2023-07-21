def count_positives_sum_negatives(arr):
    positive = len([x for x in arr if x > 0])
    negative = sum([x for x in arr if x < 0])
    return [positive, negative] if len(arr) else []


result = count_positives_sum_negatives(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
result2 = count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0])
result3 = count_positives_sum_negatives([])
print(result, result2, result3, sep="\n")
