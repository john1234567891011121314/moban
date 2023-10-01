## 题目

总共$n$个数，要求连续$m$个数，至少取两个的最小代价

## 分析

不同于取一个的的情况，似乎没办法转换。因为我们取数时需要考虑前两个取的位置。

因此我们可以这样写$dp[i][j]$，表示第$i$个数取走，上一个取的数是$j$。

于是有转移方程
$$
dp[i][j]=\min_{i-m \le k \le j-1}(dp[j][k])+a[i]
$$
如果$k$的值小于$i-m$，那么就会有一段区间只有$j$而没有其他的。

这样我们的转移时间复杂度是$O(n^2)$的。有一个$n$可以通过取$\min$来优化

考虑到$j$的取值，我们可以将其中一维优化成$O(n*m)$

这样我们的转移方程就可以写成
$$
dp[i][j] = minn[i - j][m - j] + a[i]
$$
其中$j$表示与上一位的差值，$minn[i][j]$表示第$i$位，前一位与当前位差值不超过$m-j$的最小$dp$值

```c++
	//前m个需要特殊考虑
	for(int i = 2; i <= m; ++i)
    {
    	for(int j = i - 1; j; --j)
    	{
    		dp[pos[i]][i - j] = a[i] + a[j];
    		minn[pos[i]][i - j] = min(minn[pos[i]][i - j - 1], dp[pos[i]][i - j]);
		}
	}

    for(int i = m + 1; i <= n; ++i)
    {
    	for(int j = 1; j < m; ++j)
    	{
    		dp[pos[i]][j] = minn[pos[i - j]][m - j] + a[i];
    		minn[pos[i]][j] = min(dp[pos[i]][j], minn[pos[i]][j - 1]);
		}
	}
//当最后m个有两个被选中时，可以作为答案
	ll ans = LINF;
	for(int i = n - m + 1; i <= n; ++i)
	{
		for(int j = i - 1; j >= n - m + 1; --j)
		{
			ans = min(ans, dp[pos[i]][i - j]);
		}
	} 
	cout << ans << '\n';
```

