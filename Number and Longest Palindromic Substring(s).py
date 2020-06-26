def palin():
    S="babaa"
    N = len(S)
    ans = 0
    longest=["0"]
    for center in range(2*N - 1):
        left = center // 2
        right = left + center % 2
        print(left,right)
        while left >= 0 and right < N and S[left] == S[right]:
            long=((S[left:right+1]))
            if len(long)>len(longest[0]):
                longest.append(long)
                longest.pop(0)
            elif len(long)==len(longest[-1]):
                longest.append(long)
            else:
                longest=longest        
            ans += 1
            left -= 1
            right += 1
    for string in longest:
        if len(string)<len(max(longest, key=len)):
            longest.remove(string)
            
    print(ans)
    print(longest)

palin()
