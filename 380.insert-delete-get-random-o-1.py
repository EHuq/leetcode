#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.num_list = []
        self.num_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.num_dict:
            return False
        self.num_dict[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_dict:
            return False
        last_elem = self.num_list[-1]
        index_rm = self.num_dict[val]
        self.num_list[index_rm] = last_elem
        self.num_dict[last_elem] = index_rm
        del self.num_dict[val]
        self.num_list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

