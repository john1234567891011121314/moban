## dp优化
### 基本概念

按照状态维度和决策点维度，我们可以将$dp$分为$1D/1D$和$2D/2D$。

### 1D/1D

形如
$$
f(i) = \min \{g(j) + w(i, j)\}
$$
的式子，通常称为$1D/1D$

$\min$ 和 $\max$ 在这里不做区分

#### $w(i,j)$为一次函数

通常使用单调队列优化
$$
dp[i] = \min \{ dp[j] + b[j] \} + a[i] \\
 = \min \{ ds[j] \} + a[i] , j \in [L[i], R[i]]
$$
如果$L[i], R[i]$都是单调的，那么可以有单调队列优化，否则只能考虑线段树等结构。

**问题**

有一个包括 $n$ 个正整数的序列，第 $i$ 个整数为 $E_i$ ，给定一个整数 $k$ ，找这样的子序列，如果子序列中的数在原序列中连续，则连续长度不能超过 $k$ 。对于子序列求和，问所有子序列中最大的和是多少？

**解答**
$$
dp[i] = \max \{ dp[j - 1] - sum[j] \} + sum[i] , i - j <= k
$$

#### w(i, j)是x*y

$$
dp[i] = \min \{ dp[j] - a[i] * d[j] \}
$$

这种时候没有办法分离变量

这个时候我们可以先去掉$\min$然后变换主元。

那么有
$$
dp[j] = dp[i] + a[i] * d[j]
$$
不妨让$(d[j], dp[j])$作为点在平面上，那么原问题就可以转换为经过这些点的斜率为$a[i]$的直线的截距最小。

![img](./汇总.assets/1.svg)

如果没有单调性或者其他条件，那么$dp$优化只能做到这一步，接下来就是进一步探讨。

对于其他类型，有
$$
dp[i]= \min \{ a[i] * x[j] + b[i]  * y[j] \} + w[i]
\\
\frac{dp[i]}{a[i]} = x[j] + \frac{b[i]}{a[i]} * y[j] + \frac{w[i]}{a[i]}
\\
x[j] = -\frac{b[i]}{a[i]} * y[j] + \frac{dp[i] - w[i]}{a[i]}
$$

##### 如果$a$，$d$都是单调不减的

这个时候，新加入的点一定在凸包右侧，因此直接维护凸包就行

另外，斜率单调不减，最优决策一定是单调不减的。

只要维护单调队列，保证队首是当前的最优决策即可。

**问题**

打印有$n$个字的文章，一次可以一口气打印若干个文字，如果当前打印的文字为$[l, r]$区间的文字，那么需要支付$(\sum_{i = l}^r c[i])^2 + M $的代价

求最小所需支付代价

**解答**

套路的，我们将式子写出来得到
$$
dp[i] = \min \{ dp[j] + (s[i] - s[j]) ^ 2 \} + M
$$
整理得到
$$
dp[j] + s[j] ^ 2 = (2 * s[i]) * s[j] + (dp[i] - s[i] ^ 2 - M)
$$
因此每次相当于插入$(s[j], dp[j] + s[j] ^ 2)$

斜率为$2 * s[i]$

符合之前的单调性，因此使用队列进行维护

```c++
vector<int> dp(n + 1);
vector<int> c(n + 1), s(n + 1);
auto check_min = [&](int p1, int p2, int k) -> bool
{
    return (dp[p1] + s[p1] * s[p1]) - (dp[p2] + s[p2] * s[p2]) <= k * (s[p1] - s[p2]);
};
auto k1_le_k2 = [&](int p1, int p2, int p3) -> bool
{
    int x1 = s[p1] - s[p2], x2 = s[p1] - s[p3];
    int y1 = (dp[p1] + s[p1] * s[p1]) - (dp[p2] + s[p2] * s[p2]), y2 = (dp[p1] + s[p1] * s[p1]) - (dp[p3] + s[p3] * s[p3]);
    return x1 * y2 <= x2 * y1;
};
for(int i = 1; i <= n; ++i)
{
    cin >> c[i];
    s[i] = s[i - 1] + c[i];
}
int head = 1, tail = 1;
st[tail] = 0; // dp[0]
for(int i = 1; i <= n; ++i)
{
    while(head < tail && check_min(st[head + 1], st[head], 2 * s[i])) head++;
    int j = st[head];
    dp[i] = dp[j] + (s[i] - s[j]) * (s[i] - s[j]) + m;
    while(head < tail && k1_le_k2(st[tail - 1], st[tail], i)) tail--;
    st[++tail] = i;
}
cout << dp[n] << '\n';
```

##### 如果$a$，$d$都是单调不减的

反着维护就行

##### a不单调d单调



