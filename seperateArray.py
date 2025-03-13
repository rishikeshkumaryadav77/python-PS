arr = [1,2,[3,4],[5,[6,7]]]
def seperateArray(arr):
    res = []
    for i in arr:
        if type(i) == list:
            res.extend(seperateArray(i))
            # print(res)
        else:
            res.append(i)
    return res
print(seperateArray(arr))