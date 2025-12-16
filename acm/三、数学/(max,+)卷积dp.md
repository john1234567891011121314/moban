## (max,+)卷积dp
当式子形如$dp[i]=\max_{j+k=i}(a[j]+b[k])$​时且至少有一个是凸函数

我们可以在$O(n\log n)$​内完成卷积

需要保证b是凸函数

```c++
template <class F>
vector<ll> monotone_maxima(F &f, int h, int w)
{
    vector<ll> ret(h);
    auto sol = [&](auto &&self, int l_i, int r_i, int l_j, int r_j) -> void
    {
        if(l_i > r_i) return ;
        int m_i = (l_i + r_i) / 2; //计算m_i处的最大值以及决策点
        int max_j = l_j;
        ll max_val = -inf;
        for(int j = l_j; j <= r_j; ++j)
        {
            ll v = f(m_i, j);
            if(v > max_val)
            {
                max_j = j;
                max_val = v;
            }
        }
        ret[m_i] = v;
        self(self, l_i, m_i - 1, l_j, max_j);
        self(self, m_i + 1, r_i, max_j, r_j);
            
    }
    sol(sol, 0, h - 1, 0, w - 1);
}
vector<ll> max_plus_convolution(const vector<ll> &a, const vector<ll> &b) {
    int n = (int)a.size(), m = (int)b.size();
    auto f = [&](int i, int j) {
        if (i < j or i - j >= m) {
            return -inf;
        }
        return a[j] + b[i - j];
    };

    return monotone_maxima(f, n + m - 1, n);
}
```

如果n个物品的的质量有D种，在不超过C的情况下的最大价值

我们可以$O(DC\log n + n \ log n) $解决。

首先按照价值v排序，然后对每个重量w，提取出对应的v子序列，构造$[0, v_1, v_1 + v_2, v_1 + v_2 + v_3, \dots]$，然后与背包dp进行max卷积。容易证明，背包dp的结果一定是凸函数。



