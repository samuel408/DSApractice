class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        dictionary = defaultdict(int)
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        current = 0
        print ( dictionary)

        holder = set(nums)
        for i in nums:
            holder.remove(i)
            dictionary[i] -= 1

            if i not in holder and dictionary[i]!= 0 :#if that was the only number in the set return that number
                # answer.append(i)
                holder.add(i)
                # dictionary[i] += 1
            if len(holder) == 1 and dictionary[i] > 1:
                    answer.append((i*dictionary[i]))
                    continue

                
            answer.append(reduce(mul, holder, 1))
            holder.add(i)
            dictionary[i] += 1

        return answer

        

            

