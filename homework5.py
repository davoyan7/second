# July 9
# Homework 5


# TASK 1
"""Ներմուծեմ երկու թիվ,համակարգը 
տպի True, եթեառաջինը խիստ մեծ է 
երկրորդից,False եթե առաջինը խիստ 
փոքր է"""

x = 5
y = 6

print(x > y)

# TASK 2
"""
Ներմուծեմ մեկ թիվ եւհամակարգը 
տպի դրաքառակուսի արմատը(չօգտագործել
 mathգրադարանը)
"""

b = 4
print(int(b**0.5))

# TASK 3
"""
Ներմուծեմ մեկ թիվ եւհամակարգը տպի True,
եթե թիվըերկուսի բաժանվող է։ 
ՀակառակդեպքումտպիFalse։
"""
num = 6
# num = input('Please enter your number')
print(6 % 2 == 0)

# TASK 4
"""
Ներմուծեմ մեկ integer թիվ եւհամակարգը 
տպի True, եթե թիվը[11, 24] միջակայքում 
չէ։ՀակառակդեպքումտպիFalse։
"""

intNum = 12
# intNum = int(input("Please enter number"))
print(intNum not in range(11, 24+1))

# TASK 5
"""
Ներմուծեմ 4-ի բաժանվող թիվ, 
համակարգըտպի այդ թիվը բազմապատկված 
4-ով եւբաժանված 4-ի (տպի ամբողջ մասը 
միայն)։Չօգտագործել որեւէ թվաբանական
(Arithmetical) գործողություն։
"""
x = int(input('Enter a number divisible by 4: '))
print((x << 2) >> 2)

# TASK 6
"""
Ներմուծեմ թիվ, եթե թվի երրորդ
բիթը 1 է՝ տպի True, հակառակ
դեպքում՝False։
• Ներմուծեմ 2 թիվ։ Թվերը փոխեմ
տեղերով առանց երրորդ
փոփոխականօգտագործելու։
"""

# Varuzh jan, es improvize em arel, gitem case er kan vor orinak 0b a, bayc hetagayum kshtkem

x = 60

x3 = int(bin(x)[-4])
x2 = int(bin(x)[-3])
x1 = int(bin(x)[-2])
x0 = int(bin(x)[-1])
print(bin(x))
print(f"Zero index: {x0} First index: {x1} Second index: {x2} Third: {x3}")
print(x3 == 1)
####################################

# TASK 7

"""
Ներմուծեմ 2 թիվ։ Թվերը փոխեմ
տեղերով առանց երրորդ
փոփոխականօգտագործելու։

"""
x, y = 5, 6
print(f"x is {x}, y is {y}")
y, x = x, y
print(f"x is {x}, y is {y}")
