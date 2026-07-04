class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        answer = ['/']
        alnum = []
        path += "/"

        for i in range(len(path)) :
            if i == 0 and path[i] == '/' : # 처음 '/'로 이미 시작하는 경우
                continue
            if len(alnum) == 0 and answer[-1] == '/' and path[i] == '/' : # '//' 처럼 연속되는 경우
                continue
            if len(alnum) != 0 and path[i] == '/':
                name = ''.join(alnum)
                alnum = []

                if name == '.':
                    continue
                elif name == '..':
                    if len(answer) > 1:
                        if answer[-1] == '/':
                            answer.pop()
                        while len(answer) > 1 and answer[-1] != '/':
                            answer.pop()
                    continue
                else:
                    answer.append(name)
                    answer.append('/')
                    continue

            alnum.append(path[i])
            print(answer)
            print(alnum)

        if alnum :
            answer.append(''.join(alnum))

        if len(answer) > 1 and answer[-1] == '/':
            answer.pop()

        return ''.join(answer)            