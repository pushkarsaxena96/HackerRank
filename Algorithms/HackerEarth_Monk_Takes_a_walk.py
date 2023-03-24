def vowels(n, a) :
    count=0
    for i in range(len(a)) :
        if a[i] in ['a','e','i','o','u','A','E','I','O','U'] :
            count += 1

    return count
    

n = int(input())
for i in range(n) :
    a = str(input())
    result = vowels(n, a)
    print(result)
