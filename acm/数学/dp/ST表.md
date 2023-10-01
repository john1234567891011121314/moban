# 用途

解决RMQ（区间最大最小值查询）问题

更准确说，是可重贡献问题

即某个数重复计数不会影响最后的结果，常见的还有区间GCD等

# code

```c++
//注意初值
log = 20
f[M][N]//表示以第N个数为起点，长度为2^j区间中的最大值
logn[N]
void init()
{
    logn[1] = 0;
    logn[2] = 1;
    for(int i = 3; i < N; ++i)
    {
        logn[i] = logn[i / 2] + 1;
    }
    for(int j = 1; j <= log; ++j)
    {
        for(int i = 1; i + (1 << j) - 1 <= n; ++i)
        {
            f[j][i] = max(f[j-1][i], f[j - 1][i + (1 << (j - 1))]);
        }
    }
}
int query(int x, int y)
{
    int s = logn[y - x + 1];
    return max(f[s][x], f[s][y - (1 << s) + 1]);
}
```

