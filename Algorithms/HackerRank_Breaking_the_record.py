# https://www.hackerrank.com/challenges/breaking-best-and-worst-records


def breakingRecords(score):
    # Complete this function
    minr, maxr = score[0], score[0]
    cmin, cmax = 0, 0
    for i in score:
        if i > maxr:
            maxr = i
            cmax += 1
        elif i < minr:
            minr = i
            cmin += 1
    return cmax, cmin

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))