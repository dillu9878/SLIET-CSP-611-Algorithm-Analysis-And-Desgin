def main():
    for _ in range(int(input())):
        (v, e) = map(int, input().split())
        d = {}
        for i in range(e):
            (a, b) = map(int, input().split())
            if a in d:
                d[a].append(b)
            else:
                d[a] = [b]
            if b in d:
                d[b].append(a)
            else:
                d[b] = [a]

        l = list(d.keys())
        l.sort()
        for i in l:
            print(str(i) + '->' + '->'.join(list(map(str, d[i]))))


if __name__ == '__main__':
    main()