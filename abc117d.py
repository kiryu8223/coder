MAX_DIGIT = 40

n, k = map(int, input().split())
an = list(map(int, input().split()))

digit = [1 << i for i in range(MAX_DIGIT)]#1,2,4,8,...
#<<は左シフト演算子　ビットを左にシフト

sum_d = [[0] * 2 for _ in range(MAX_DIGIT)]
#[0]*2=[0,0] [0,0]がMAX_DIGIT個生成

for ai in an:
    for i in range(MAX_DIGIT):
        d = (ai >> i) & 1 #ビットAND
        sum_d[i][d] += digit[i]
#anにおいて、各桁（1,2,2^2,2^3,...)に1がいくつあるか
print(sum_d)
sum_max = [0] * MAX_DIGIT #[0,0,0,...,0(MAX_DIGIT個)]
sum_max[0] = max(sum_d[0]) #行列の最初に

for i in range(MAX_DIGIT - 1):
    sum_max[i + 1] = sum_max[i] + max(sum_d[i + 1])


dp = [-1] * MAX_DIGIT
dp[0] = sum_d[0][0 if (k & 1) == 1 else 1]

for i in range(MAX_DIGIT - 1):
    d = k >> (i + 1) & 1
    if d == 0:    # i+1 bit目が1のsum + 今までの最大
        dp[i + 1] = sum_d[i + 1][1] + dp[i]
    if d == 1:    # (i+1 bit目が0のsum + 今までの最大) or (i+1 bit目が1のsum + i bitまで任意)
        dp[i + 1] = max(sum_d[i + 1][0] + dp[i], sum_d[i + 1][1] + sum_max[i])
print(dp[-1])

#ビット演算について、下サイト参照
#https://www.javadrive.jp/python/num/index4.html
