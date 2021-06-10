def noTwoSlash(url: str) -> str:
    arr = list(url)
    print(''.join(arr))

    for i in range(0, len(arr)):

        if len(arr) and (arr[i - 1] == '/') and (arr[i] == '/'):
            del arr[i]
            arr = noTwoSlash(arr)

    return []

    # print("finish")
    # return []


print(noTwoSlash("/page1///page2////page3/test.html"))
