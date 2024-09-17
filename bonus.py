# bonus
def rome_to_int(roman):
    rome_nums={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    res=0
    prev=0

    for i in roman[::-1]:
        a=rome_nums[i]
        if a>=prev:
            res+=a
        else:
            res-=a
        prev=a

    return res
romans=input().upper()
print(rome_to_int(romans))



# bonus2
# a=int(input())
# b=int(input())
# a1=[]
# b1=[]
# i=2
# while i<=a:
#     if a%i==0:
#         a1.append(i)
#     i+=1
# j=2
# while j<=b:
#     if b%j==0:
#         b1.append(j)
#     j+=1
# new=[]
# for l in a1:
#     if l in b1:
#         new.append(l)
# def maxim(a:list):
#     mx=-999999999999999999999999
#     for i in a:
#         i=int(i)
#         if i>mx:
#             mx=i
#     return mx
# print(maxim(new))
