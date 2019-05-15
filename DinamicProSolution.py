#-*-coding: utf-8-*-
import matplotlib.pyplot as plt
import operator
import numpy as np
iteration = 0
start_k = 174
# Призводительность цеха 1
def f1(x):
    return (5+(x+40)**(2/3))

# Призводительность цеха 2
def f2(x):
    return (7+(x+30)**(1/2))

# Общая производительность за месяц
def w(k, x):
    return (f1(x)+f2(k-x))

# Остаток производства за месяц
def phi(k,x):
    return (0.7*x+0.94*(k-x))
# Главная функция 
def magic (k):
    global iteration;
    global best_x;
    iteration += 1;
    x_list = [i for i in range (int(k))];
    if (iteration<3):
        next_results_list=[w(k,i)+magic(phi(k,i)) for i in x_list]
    else:
        next_results_list = [w(k,i) for i in x_list]
    best_result=max(next_results_list)
    iteration -= 1
    best_x =next_results_list.index(best_result)
    return best_result

for i in range(3):
    result = magic(start_k)
    if(iteration==0):
           fullresult=int(result)
    iteration+=1
    
print("Total win: ",fullresult)
#Оптимальный выигрыш от управления
#3 этап
print("\n\n3й этап:")
k3_max_1=0.7**2*174;
k3_max_2=0.94**2*174;
k_3 = np.arange(k3_max_1,k3_max_2,5)
xs3_1 = np.arange(0,k3_max_1,5) #85
xs3_2 = np.arange(0,k3_max_2,5) #150
plt.plot(xs_2,w(k3_max_2,xs3_2),xs_1,w(k3_max_1,xs3_1));
plt.xlabel('x')
plt.ylabel('W_3')
plt.title('График функции W_3 (k_3,x_3)')
plt.grid(True)
plt.show()
print("Значения k_3:",k_3)
x_3 = np.arange(85,155,5)
print("Значения x_3:",x_3)
W_3 = w(k_3,x_3)
print("Значения W_3:",W_3)

#2 этап
print("\n\n2й этап:")
k2_max_1=0.7**1*174;
k2_max_2=0.94**1*174;
k_2 = np.arange(k2_max_1,k2_max_2,5)
xs2_1 = np.arange(0,k2_max_1,5) #120
xs2_2 = np.arange(0,k2_max_2,5) #165
plt.plot(xs2_2,w(k2_max_2,xs2_2),xs2_1,w(k2_max_1,xs2_1));
plt.xlabel('x')
plt.ylabel('W_2')
plt.title('График функции W_2 (k_2,x_2)')
plt.grid(True)
plt.show()
print("Значения k_2:",k_2)
x_2 = np.arange(120,165,5)
print("Значения x_2:",x_2)
W_2 = w(k_2,x_2)
print("Значения W_2:",W_2)

#1 этап
print("\n\n1й этап:")
k1_max_1=0.7**0*174;
k1_max_2=0.94**0*174;
k_1 = np.arange(k1_max_1,k1_max_2,5) #174=start_k
xs1_1 = np.arange(0,k1_max_1,5) #121
xs1_2 = np.arange(0,k1_max_2,5) #175
plt.plot(xs1_2,w(k1_max_2,xs1_2),xs1_1,w(k1_max_1,xs1_1));
plt.xlabel('x')
plt.ylabel('W_1')
plt.title('График функции W_1 (k_1,x_1)')
plt.grid(True)
plt.show()
k_1 = 174
print("Значения k_1:",k_1)
x_1 = np.arange(121,175,5)
print("Значения x_1:",x_1)
W_1 = w(k_1,x_1)
print("Значения W_1:",W_1)

