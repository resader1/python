a = [10,5,2,4,7]
print(min(a))
print(max(a))
print(sum(a))

a_dict = [
    {"no":1,"name":"홍길동"},
    {"no":5,"name":"유관순"},
    {"no":3,"name":"이순신"},
    {"no":4,"name":"강감찬"},
    {"no":2,"name":"김구"}
]

print(max(a_dict,key=lambda x:x['no']))
print(max(a_dict,key=lambda x:x['name']))

a_dict.sort(key=lambda x:x['no'])
a_dict.sort(key=lambda x:x['no'],reverse=True)
print(a_dict)