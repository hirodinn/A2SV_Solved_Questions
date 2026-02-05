class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        least = 0
        for st in list1:
            if st in list2:
                if not result:
                    result.append(st)
                    least = list1.index(st) + list2.index(st)
                else:
                    if list1.index(st) + list2.index(st) < least :
                        result = [st]
                        least = list1.index(st) + list2.index(st)
                    elif list1.index(st) + list2.index(st) == least:
                        result.append(st)
        return result


        
