#This program finds the number of all palindromic substrings.
#It also outputs the the longest palindromic substring(s) in a given string as parameter.
#Program considers a single character as palindromic to itself
# Time complexity on average: O(N^2)
# Space complexity: O(N)

def palin(word):
    N = len(word)
    ans = 0
    longest=["0"]
    for center in range(2*N - 1):
        left = center // 2
        right = left + center % 2
        #print(left,right)
        while left >= 0 and right < N and word[left] == word[right]:
            long=((word[left:right+1]))
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
            
    print("Number of palindromic substrings: ",ans)
    print("Logest palindromic substring(s): ",longest)

palin("babab")
