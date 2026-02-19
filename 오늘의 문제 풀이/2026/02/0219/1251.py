import sys
input = sys.stdin.readline

word = input().rstrip()
word_list = []
idx1, idx2 = 0, 0

for i in range(len(word)-2) :
    for j in range(i+1, len(word)-1) :
        idx1, idx2 = i, j
        answer = ''.join(reversed(word[:idx1+1])) + ''.join(reversed(word[idx1+1:idx2+1])) + ''.join(reversed(word[idx2+1:]))
        word_list.append(answer)

print(min(word_list))