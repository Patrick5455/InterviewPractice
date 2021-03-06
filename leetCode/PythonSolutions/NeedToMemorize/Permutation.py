# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


# Recursion
class SolutionRecursion:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here

        if nums is None:
            return []

        if nums is []:
            return [[]]

        result = []
        self._permute(result, [], sorted(nums))
        return result

    def _permute(self, result, temp, nums):
        if nums == []:
            result.append([temp])
        else:
            for i in range(len(nums)):
                t = temp + [nums[i]]
                # the number of n is decreasing
                n = nums[:i] + nums[i + 1:]
                self._permute(result, t, n)

# Non-Recursion
class SolutionIterative:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if nums is None:
            return []

        if nums:
            return [[]]

        nums = sorted(nums)
        permutation = []
        stack = [-1]
        permutations = []

        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations

if __name__ == '__main__':
    list1 = [1,2,3]
    recurSol = SolutionRecursion()
    res = recurSol.permute(list1)
    print(res)

