class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        occurence = dict()

        for domain in cpdomains:
            num , dom = domain.split()
            l = dom.split(".")
            st = ""
            for i in range(len(l)):
                if i > 0:
                    st = st[st.index(".") + 1:]
                else:
                    st = dom
                
                if st in occurence:
                    occurence[st] += int(num)
                else:
                    occurence[st] = int(num)
        result = []
        for key in occurence:
            result.append(f"{occurence[key]} {key}")
        return result

