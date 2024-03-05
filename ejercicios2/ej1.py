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
