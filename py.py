import array
from copy import copy,deepcopy

a= array.array("i",[1,2,3,4])

for i in a:
    print(i,end=" ")

list_one = [1,2,3]
list_two = [4,5,6]

added_list = [x+y for (x,y) in zip(list_one,list_two)]

print(added_list)

little_complex_added_list = [x+y for x in list_one for y in list_two]

print(little_complex_added_list)

list = [[10,20,30],[40,50,60],[70,80,90]]

shallow_copied_list = copy(list)

shallow_copied_list[0].append(0)

shallow_copied_list[0][0]=1

print(list)



def fibonnaci(n):
    p=0
    q=1
    while p<n:
        print(p)
        p,q=q,p+q


def fib(n):
   p, q = 0, 1
   while(p < n):
       print(p)
       p, q = q, p + q

fib(10)


fibonnaci(10)



# import pandas as pd
#
# pandas_dict = {"column1":pd.Series([1,2,3,None],index=["a","b","c","d"])}
#
# df = pd.DataFrame(pandas_dict)
#
# df.index.name=None
# print(df)
# # class A:
# #     def __init__(self,a_name):
# #         self.a_name=a_name
# #
# # class B(A):
# #     def __init__(self,b_name,a_name):
# #         self.b_name=b_name
# #
# #         A.__init__(self,a_name)
# #
# # class C(B):
# #     def __init__(self,c_name,b_name,a_name):
# #         self.c_name=c_name
# #
# #         B.__init__(self,b_name,a_name)
# #
# #     def display_names(self):
# #         print(f"a_name:{self.a_name}, b_name:{self.b_name}, c_name:{self.c_name}")
# #
# # obj1 = C("third_name","second_name","first_name")
# # obj1.display_names()
# # print(obj1.a_name)
#
