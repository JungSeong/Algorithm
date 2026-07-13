class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for tok in tokens :
            if tok not in ['+', '-', '*', '/'] :
                st.append(int(tok))
            else :
                num2 = st.pop()
                num1 = st.pop()

                if tok == '+' :
                    st.append(num1 + num2)
                elif tok == '-' :
                    st.append(num1 - num2)
                elif tok == '*' :
                    st.append(num1 * num2)
                else :
                    st.append(int(num1/num2))
        return st[-1]