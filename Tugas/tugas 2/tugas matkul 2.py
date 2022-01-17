def twice(function): 
    return lambda x: function(function(x)) 


def f(x): 
  	return x + 3 
g = twice(f)

#print(g(7))

'''
my_list = [1,2,3,4,5]
sum = 0
for x in my_list:
        sum+= x
        print(sum)

print(sum)

'''
my_list = [1,2,3,4,5]


def muul():
    sum = 0
    for x in my_list:
        sum = sum + ( x ** 2)
    print(sum)
        
muul()

def konversiCtoF(a):
    konversiCtoF = lambda a : (a * 9/5) + 32
    return konversiCtoF



def namea():
    return list(map(konversiCtoF(a), my_list))

print(namea())
