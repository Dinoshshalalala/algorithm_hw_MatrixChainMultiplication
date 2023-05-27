import sys
import random
import time
import matplotlib.pyplot as plt

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
    return m[0][n-1]

# p 陣列 長度
def input_n(n):
    # p列表 
    p = []    
    # 使用者輸入n+1個數
    for i in range(n+1):
        input_num = random.randint ( 1 , 20 )
        p.append(input_num)      
    print("p =", p)
    return p

# 畫兩時間函式圖
def plot(listname, string, n_value):
    plt.cla()      
    # 創建折線圖
    plt.plot(n_value, listname)
    # 添加標題和軸標籤
    plt.title(string +'   relationships with Time and n')
    plt.xlabel('n=')
    plt.ylabel('Time')    
    # 顯示圖表
    #plt.show()
    plt.savefig(string + '.png')


n_value1 = []
n_value2 = []
dpTime_list = []
bruteTime_list = []
# main
def main():
    # dp
    print("dp data!!!")    
    for i in range(1, 16, 1):
        x = input_n(i)
        n_value1.append(i)
        start1 = time.perf_counter()
        matrix_chain_order_dp(x)
        end1 = time.perf_counter()
        dpTime_list.append(end1-start1)
        print("finish  n = ", i)
        print("time = ", end1-start1)        
    print("--------------------------------------------------")
            
    # brute
    print("brute data!!!")
    for i in range(1, 16, 1):
        x = input_n(i)
        n_value2.append(i)
        start1 = time.perf_counter()
        z = len(x) - 1
        matrix_chain_order_brute(x, 1, z)
        end1 = time.perf_counter()
        bruteTime_list.append(end1-start1)
        print("finish  n = ", i)
        print("time = ", end1-start1)

#---------------------exe------------------------
# exe
main()
plot(dpTime_list, "dp", n_value1)
plot(bruteTime_list, "brute", n_value2)








