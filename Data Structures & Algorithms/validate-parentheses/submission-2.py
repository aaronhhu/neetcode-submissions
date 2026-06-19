class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in s:
            match i:
                case "(":
                    st.append(i)
                case "[":
                    st.append(i)
                case "{":
                    st.append(i)
                case ")":
                    if not st or st.pop() != "(":
                        return False
                case "]":
                    if not st or st.pop() != "[":
                        return False
                case "}":
                    if not st or st.pop() != "{":
                        return False

        if st == []:
            return True
        else:
            return False