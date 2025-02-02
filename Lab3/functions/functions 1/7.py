def spy_game(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] and nums[i] == "3": return True
    return False

x = list(input())

print(spy_game(x))