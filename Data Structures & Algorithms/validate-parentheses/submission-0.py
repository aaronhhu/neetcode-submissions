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
                    if st.pop(i) == "(":
                        continue
                case "]":
                    if st.pop(i) == "[":
                        continue
                case "}":
                    if st.pop(i) == "{":
                        continue
