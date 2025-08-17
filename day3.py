def findDuplicateValue (nums):
    
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
    
print(findDuplicateValue ([ 1, 3, 4, 2,5,2]))