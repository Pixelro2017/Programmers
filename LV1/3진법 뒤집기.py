import string


def solution(n):
    answer = 0
    tmp = string.digits+string.ascii_lowercase
    def convert(num, base):
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]
    thr = convert(n, 3)
    thr = thr[::-1]

    answer = int(thr, 3)

    
    return answer
