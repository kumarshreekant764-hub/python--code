#function definition
def clac_sum(a, b): #parameter
    sum = a + b
#    print(sum)
    return sum

clac_sum(5, 9) #function call ; arguments



def print_hello():
#    print("Hello World")

#print_hello()



#average of 3 numbers
#def clac_avg(a, b, c):
    sum = a+b+c
    avg = sum/3
#    print(avg)
    return avg

#clac_avg(98, 97, 87)



# built-in function  
print("shreekant", end=" ")   #print function
print("patel")



#waf to print the lenghth of a list . (list is the parameter)
cities = ["delhi", "gurgaon", "patna", "noida", "mumbai", "chennai"]
nums = [4, 56, 78, 34, 56, 34, 25, 45, 67]

def print_len(list):
    print(len(list))

#print_len(cities)
#print_len(nums)


#waf to print the element of a list in a singlr line . (list is the parameter)

city = ["delhi", "gurgaon", "patna", "noida", "mumbai", "chennai"]
num = [4, 56, 78, 34, 56, 34, 25, 45, 67]

def print_list(list):
    for item in list:
        print(item, end= " ")


#print_list(city)
#print_list(num)


#waf to find the factorial of n . (n is the parameter)

def cal_fact(n):
      fact = 1
      for i in range(1, n+1):
          fact*=i
          print(fact)
      

cal_fact(5) 



#waf to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 94
    print(usd_val, "usd =", inr_val, "inr")

converter(5)