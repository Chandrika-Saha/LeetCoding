class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

         
        nums_dict = dict(sorted(nums_dict.items(), key= lambda item: item[1], reverse=True))

        print(nums_dict) 

        return list(nums_dict.keys())[0:k]

        # nums_dict = {}

        # for num in nums:
        #     nums_dict[num] = nums_dict.get(num, 0) + 1

        # freq = [[] for n in range(len(nums) + 1)]
        # for key, value in nums_dict.items():
        #     freq[value].append(key)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
        0, 1, 2
        1, 2, 3
        3, 2, 1
        # num_list = []
        # freq_list = [0] * (len(nums) + 1)
        # print(freq_list)

        # for num in nums:
        #     if num in num_list:
        #         num_list.append(num)

        # for num in nums:
        #     freq_list[num] += 1

        # print(freq_list)

        # res = []
        # temp = freq_list.copy()
        # for i in range(k):
        #     maximum = max(freq_list)
        #     print(maximum)
        #     res.append(temp.index(maximum))
        #     freq_list.remove(maximum)
            
        # print(temp)

        # return res


        