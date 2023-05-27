import sys
import random

# 暴力算法
def matrix_chain_order_brute(p, i, j):
    if i == j:
        return 0, str(i)
    min_cost = sys.maxsize
    optimal_paren = ""
    for k in range(i, j):
        left_cost, left_paren = matrix_chain_order_brute(p, i, k)
        right_cost, right_paren = matrix_chain_order_brute(p, k+1, j)
        cost = left_cost + right_cost + (p[i-1] * p[k] * p[j])
        if cost < min_cost:
            min_cost = cost
            optimal_paren = f"({left_paren})({right_paren})"
    return min_cost, optimal_paren


# 動態規劃算法
def matrix_chain_order_dp(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i-1][j-1] = sys.maxsize
            for k in range(i, j):
                q = m[i-1][k-1] + m[k][j-1] + (p[i-1] * p[k] * p[j])
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
                    s[i-1][j-1] = k                    
    return m[0][n-1], print_optimal_parens_dp(s, 1, n)

def print_optimal_parens_dp(s, i, j):
    if i == j:
        print(f"{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens_dp(s, i, s[i-1][j-1])
        print_optimal_parens_dp(s, s[i-1][j-1]+1, j)
        print(")", end="")
        
# 輸入 p 陣列長度
def input_n():
    # 輸入 list 長度
    n = int(input("please enter list length: "))    
    # p列表 
    p = []   
    # 使用者輸入n+1個數
    for i in range(n+1):
        input_num = random.randint ( 1 , 20 )
        p.append(input_num)        
    print("p =", p)
    return p , n

#---------------------main---------------------------
print("")


p, n =  input_n()

# brute
print("-----------------brute-------------------")
z = len(p) - 1
brute_min_cost, brute_optimal_paren = matrix_chain_order_brute(p, 1, z)
print(f"Optimal parenthesization: {brute_optimal_paren}")
print(f"Minimum number of scalar multiplications: {brute_min_cost}")

# dp
print("-----------------dp----------------------")
print("Optimal parenthesization: ", end="")
dp_min_cost, dp_optimal_paren = matrix_chain_order_dp(p)
print("")
print(f"Minimum number of scalar multiplications: {dp_min_cost}")




