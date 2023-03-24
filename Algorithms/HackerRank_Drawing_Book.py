

def solve(n, p):
    from_front = p//2
    from_back = (n-p)//2 if n % 2 else (n-p+1)//2
    return min(from_front, from_back)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)