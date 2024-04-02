#ejemplo 1
def example1(S):
   n = len(S)
   total= 0
   for j in range(n):
       total +=S[j]
       return total

#len 1 paso
#total 1 paso
#bucle for  total +=S[j] 1 paso * n veces
#return 1 paso

#suamr pasos 3 pasoso + n
#tiempo(n)= f(n)= n+3


#ejemplo 2

##len 1 paso
#total 1 paso
#bucle for  total +=S[j] 1 paso * n/2 veces
#return 1 paso

#suamr pasos 3 pasoso + n/2
#tiempo(n)= f(n)= n/2  +3

#ejemplo 3

#n(n+1)/2

#ejemplo 4

#n+n= 2n
