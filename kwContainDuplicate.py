def containDuplicate(num) -> bool :
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] == num[j]:
                return True
    return False
def containDuplicateUsingSet(nums) -> bool:
    unique_set = set()
    for x in nums:
        if x in unique_set:
            return True
        unique_set.add(x)
    return False
nums1 = [1, 2, 3, 4]
print(containDuplicate(nums1))

nums2 = [1,2,3,3,4]
print(containDuplicate(nums2))

if __name__== 'main':
    nums1 = [1, 2, 3, 4]
    print(containDuplicate(nums1))

    nums2 = [1,2,3,3,4]
    print(containDuplicate(nums2))

    nums3 = [1,2,4,3,4,5]
    print(containDuplicateUsingSet(nums3))