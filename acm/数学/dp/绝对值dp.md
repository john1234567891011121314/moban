### 前置

涉及绝对值的$dp$，往往需要在朴素解法上再优化一下，常见套路是将绝对值拆开求最大值

### 题目

给定两个序列$a$，$b$，定义一个区间为$[l, r]$，其长度为$r - l + 1$，贡献为$\mid b_l - a_r \mid + \mid a_l - b_r \mid$

现在可以选择一些不相交的区间使得总长度恰好为k，贡献最大，求最大贡献。

### 分析

将绝对值拆开我们得到4个式子，在朴素情况下我们有$O(nk^2)$，于是我们考虑进一步优化。

将绝对值拆开后，我们相当于同时维护4个式子，同时将这个点对后面的点的影响消除了。将$dp$状态写成表格，然后注意到我们的状态转移是在一条斜线上，或者说在对角线上，然后将$i-j$作为一个新的状态去转移即可。

```c++
void solve(int cas)
{
	int n, k; cin >> n >> k;
	vector<vector<ll>>dp(n + 2, vector<ll>(k + 1, 0));
	vector<ll>mx1(n + 2, -LINF);
	vector<ll>mx2(n + 2, -LINF);
	vector<ll>mx3(n + 2, -LINF);
	vector<ll>mx4(n + 2, -LINF);
	vector<int>a(n + 1);
	vector<int>b(n + 1);
	for(int i = 1; i <= n; ++i) cin >> a[i];
	for(int j = 1; j <= n; ++j) cin >> b[j];

	
	for(int i = 1; i <= n + 1; ++i)
	{
		
		for(int j = 0; j <= min(i, k); ++j)
		{
			dp[i][j] = dp[i - 1][j];
			int p = i - j;

			dp[i][j] = max(dp[i][j], mx1[p] + b[i - 1] - a[i - 1]);
			dp[i][j] = max(dp[i][j], mx2[p] + b[i - 1] + a[i - 1]);
			dp[i][j] = max(dp[i][j], mx3[p] - b[i - 1] - a[i - 1]);
			dp[i][j] = max(dp[i][j], mx4[p] - b[i - 1] + a[i - 1]);

			
		}
		for(int j = 0; j <= min(i, k); ++j)
		{
			int p = i - j;
			mx1[p] = max(mx1[p], dp[i][j] + b[i] - a[i]);
			mx2[p] = max(mx2[p], dp[i][j] - b[i] - a[i]);
			mx3[p] = max(mx3[p], dp[i][j] + b[i] + a[i]);
			mx4[p] = max(mx4[p], dp[i][j] - b[i] + a[i]);
			
		}
	}
	cout << dp[n + 1][k] << '\n';
}
```

