# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        finaL = [] 
        finaL.append(pairs.copy())
        if len(pairs) == 0:
            return pairs
        for i in range(1, len(pairs)):
            j = i - 1
            curr = pairs[i]
            while j >= 0 and pairs[j].key > curr.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = curr
            finaL.append(pairs.copy())
        return finaL
        
#cpylist = pairs ! a new list just a new name with the addy to the same list
    