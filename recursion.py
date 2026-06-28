def show(n):
#    if(n == 0):  #base case
        return
#    print(n)
#    show(n-1)
#    print("end")
#show(5)


#returns n!
def fact(n):
#    if(n == 0 or n == 1):
        return 1
#    else:
        return n * fact(n - 1)
    

#print(fact(4))



#write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
     if(n == 0):
          return 0
     return calc_sum(n - 1)+ n

sum = calc_sum(10)
print(sum)



#write a recursive function to print all element in a list
def print_list(list, idx = 0):
       if(idx == len(list)):
              return
       print(list[idx])
       print_list(list, idx + 1)

nums = [4, 5, 3, 2, 7, 9, 8]

print_list(nums)
