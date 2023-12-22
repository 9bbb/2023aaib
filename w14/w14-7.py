#set用法
s = [1,2,3,4]#1.大括號
print(s)

s = set( (1,3,5,7) )#2.用set()放想放的用元括號
print(s)

s = set( [1,2,4,3] )# 同上 用方括號
print(s)
s = set( 'Hwllo' )#同1 可放字串
print(s)

#用  .add()    .remove()
s.add(100)
print(s)
s.remove('H')
print(s)