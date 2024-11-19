list1 = [1,2,3]
list2 = [10,20,30]
add = list(map(lambda x,y: x+y,list1,list2))
diff = list(map(lambda x,y: x-y,list1,list2))

print(f"addition is {add}")
print(f"difference is {diff}")