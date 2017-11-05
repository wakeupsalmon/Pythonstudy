def human_sort(L):
    # this functions tries to parse out the number in string s
    # starting from index i
    def get_num(s, i):
        num = s[i]
        length = len(s)
        for k in range(i+1,length):
            if (s[k].isdigit()):
                num += s[k]
            else:
                break
        return (int(num))
    
    # string compare function
    def compare(A, B):
        length_A = len(A)
        length_B = len(B)
        i = 0
        while (i <= length_A):
            if (i >= length_B):
                return True
            if (A[i].isdigit() and B[i].isdigit()):
                num_A = get_num(A,i)
                num_B = get_num(B,i)
                if (num_A == num_B):
                    i += 1 
                else:
                    return (num_A > num_B)
            else:
                if (A[i] == B[i]):
                    i += 1
                else:
                    return (ord(A[i]) > ord(B[i]))
        return False

    def merge(a, start1, start2, end):
        index1 = start1
        index2 = start2
        length = end - start1
        aux = [None] * length
        for i in range(length):
            if ((index1 == start2) or
                ((index2 != end) and (compare(a[index1], a[index2])))):
                aux[i] = a[index2]
                index2 += 1
            else:
                aux[i] = a[index1]
                index1 += 1
        for i in range(start1, end):
            a[i] = aux[i - start1]

    def mergeSort(a):
        n = len(a)
        step = 1
        while (step < n):
            for start1 in range(0, n, 2*step):
                start2 = min(start1 + step, n)
                end = min(start1 + 2*step, n)
                merge(a, start1, start2, end)
            step *= 2
        return a

    return (mergeSort(L))


def test():
    # some arrays for testing
    L1 = ["file1","file10","file2"]
    L2 = ["file3aaaaaaaa","aa","file3","file30"]
    L3 = ["213","15","121aa","howd1","howd15","howd2"]
    L4 = ["file1","file3","file10","file2","file20","file11_v1","file11_v10",
    "file11_v2"]
    return
