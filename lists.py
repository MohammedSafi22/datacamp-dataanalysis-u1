friends = ["Ali", "Sara", "Omar", "Lina"]
print(friends[0])
print(friends[-1])
print(len(friends))
print(friends[1:3])
print(friends[:2])
print(friends[2:])
print(friends[::-1])

friends[0] = "Ahmed"
friends[1:3] = ["X", "Y"]
print(friends)

friends = friends + ["Noor"]
del friends[1]
print(friends)


#important
nums = [5, 2, 9, 1]
print(len(nums))
print(sum(nums))
print(max(nums))
print(min(nums))

print(sorted(nums))

nums.append((7))
print(nums)

nums.insert(1, 100)
print(nums)

nums.remove(100)
print(nums)

last = nums.pop()
print(last, nums)

#)Nested Lists(
house = [["hallway", 11.25],
["kitchen", 18.0],
["living room", 20.0]]
print(house[1]) 
print(house[1][1]) 
print(house[-1][0]) 

#Copying
a = [1, 2, 3]
b = a 
b[0] = 99
print(a)
c = [1, 2, 3]
d = c.copy()
d[0] = 99
print(c) 

#example 1 (area)
house = [["hallway", 11.25],
["kitchen", 18.0],
["living room", 20.0],
["bedroom", 10.75],
["bathroom", 9.50]]
total = house[0][1] + house[1][1] + house[2][1] + house[3][1] + house[4][1]
print(f"Total area: {total} m²")
print(f"Largest room: {house[2][0]}")

#stds avg
scores = [88, 92, 79, 65, 95, 70]
average = sum(scores) / len(scores)
top3 = sorted(scores, reverse=True)[:3]
best = max(scores)
best_position = scores.index(best)
above_avg_count = len([s for s in scores if s > average])
print(f"Average: {average}")
print(f"Top 3: {top3}")
print(f"Best score {best} is at index {best_position}")
print(f"Students above average: {above_avg_count}")