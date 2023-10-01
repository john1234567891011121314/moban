## 状态转换

### 题意

每一位数字$a_i$在$-m\leq a_i\leq m$之间，同时任意长度大于等于2的子段和非负，问这样的序列有多少个

### 分析

很不好考虑的一个问题。

关键在于状态的选择。题目要求的是任意大于2的字段和都非负，我们如果考虑最后一位放什么的话比较难处理，主要在于我们没办法保证我们选择的第$i$个数满足$a_i+a_{i-1}+a_{i-2} \geq 0$，但是仔细考虑的话可以发现我们可以将最后一位放什么的状态改成后缀最小的子段的状态，这样我们就可以转移了。

考虑最小后缀的状态，因为任意长度为2的子段和都大于等于0，于是这个最小后缀的范围也在$-m \leq suf\leq m$之间。

如果当前最小后缀小于零，那么只有一种情况，即前面一位放的是正数，同时这一位放的是等于这个最小后缀的负数，这样才可以满足条件。

如果当前最小后缀大于等于0，那么就有两种情况，一种是前一位放的数要大于等于当前位，或者说前一位的最小后缀要大于等于当前位的数，或者前一位虽然要小于当前位，但是是负数，那么当前位可以放一个正数使其与前一位相加等于最小后缀，形式化的说，应该是下面这个样子。
$$
dp[i][j]= \begin{cases}
            \sum_{0 \leq k \leq m}dp[i-1][k] +\sum_{j-m \leq k < 0}dp[i-1][k] ,  & \text{if $j \geq 0$} \\
            \sum_{-j \leq k \leq m}dp[i-1][k] , & \text{if $j < 0$} \\
        \end{cases}
$$
稍作整理，我们就得到
$$
dp[i][j]= \begin{cases}
            \sum_{j-m \leq k \leq m}dp[i-1][k]  ,  & \text{if $j \geq 0$} \\
            \sum_{-j \leq k \leq m}dp[i-1][k] , & \text{if $j < 0$} \\
        \end{cases}
$$
然后处理一下后缀就可$O(n^2)$完成。

## 题目

23杭电多校第六场1008

### 题意

$Alice$和$Bob$在做游戏。

一开始他们有一个序列，每次他们都可以选择一个位置$pos$，如果第一位到$pos$的和大于等于$pos+1$到最后一位的前缀和，那么我们就把$pos$后面的给截去，只留下前面的部分，否则我们留下后面的。

这个游戏显然有必胜必败策略，于是$Alice$和$Bob$希望自己赢的时候留下的数字尽可能大，不然就尽可能小。

### 分析

在不考虑额外的限制条件的情况下，我们可以轻易写出$O(n^3)$的$sg$函数

```c++
void dfs(int l, int r)
{
    if(vis[l][r]) return;
    vis[l][r] = 1;
    vector<bool>v(r - l + 10, 0);
    for(int k = l; k < r; ++k)
    {
        if(pre[k] - pre[l - 1] >= pre[r] - pre[l - 1])
        {
            dfs(l, k);
            v[sg[l][k]] = 1;
        }
        else
        {
            dfs(k + 1, r);
            v[sg[k + 1][r]] = 1;
		}
    }
    for(int i = 0; i < r - l + 10; ++i)
    {
        if(!vis[i])
        {
            sg[l][r] = i;
            return ;
		}
	}
}
```

现在我们要记录最后剩下的值，那么有一个比较巧妙的方法是我们将必胜态记录为大于0的状态，必败态记录为小于0的状态，那么当前这个状态就必须取后继状态的最小值，当前状态是必胜仅当后继状态有一个小于0，当前必败，仅当后继都大于0。

然后状态的绝对值我们就可以记为当前状态到最后状态的留下的值，仔细思考，这样是符合逻辑的，当前必胜，那么我们就挑一个最小的数，这样取负之后就是当前状态的答案，当前必败，我们就取一个最小的正数，同样符合条件。

然后我们就写出了一个区间$dp$一样的东西。

```c++
for(int i = 1; i <= n; ++i) dp[i][i] = -a[i];
for(int L = 2; L <= n; ++L)
{
    for(int l = 1; l + L - 1 <= n; ++l)
    {
        int r = l + L - 1;
        ll tmp = LINF;
        for(int k = l; k < r; ++k)
        {
            if(pre[k] - pre[l - 1] >= pre[r] - pre[l - 1])
            {
                tmp = min(tmp, dp[l][k]);
            }
            else
            {
                tmp = min(tmp, dp[k + 1][r]);
			}
        }
        dp[l][r] = -tmp;
	}
}
```

仔细考察我们写出来的东西，我们可以发现如果没有$if$语句，那么就是一个全部取$\min$的情况，似乎是比较典型的单调栈优化的过程，接下来仔细分析是否可以用单调栈优化。

我们考虑对每个点开两个单调栈，一个单调栈表示当前区间长度为$L$的情况下，所有作为左端点的有效决策，另一个就是作为右端点的有效决策。

我们发现当$p$是保留左端点的一个决策，当且仅当$pre[p] - pre[l - 1] \geq pre[r] - pre[p]$，稍作整理既得$2*pre[p] \geq pre[r] + pre[l - 1]$，在这个式子里，$l$是不变的，$r$是增大的，因此$p$的值越小，越容易不在有效取值范围内，我们考虑将$p$从小到大排一排，那么后面的一些$p$仍然可以作为我们的一个决策，然后我们希望这个决策带来的值越小越好，因此我们将对应的$dp$值也从小到大排，每一次新加入的决策就在最后面。也就是说，下标越大，值越小，越是我们想要的值，那么这个过程我们就可以拿单调栈维护。

保留右端点同理。

于是我们就有如下的代码

```c++
int n;
ll dp[3010][3010];
int a[3010];
ll pre[3010];
deque<int> top[3010],top2[3010];
void add(int l,int r)
{
	if(pre[r - 1] - pre[l - 1] >= a[r])
	{
		while(!top[l].empty())
		{
			int p = top[l].front();
			if(2 * pre[p] >= pre[l - 1] + pre[r])
			{
				break;
			}
			top[l].pop_front();
		}
		while(!top[l].empty())
		{
			int p = top[l].back();
			if(dp[l][p] < dp[l][r - 1])
			{
				break;
			}
			top[l].pop_back();
		}
		top[l].push_back(r - 1);
		//最优决策为 top[l].front() 
	}
	if(a[l] < pre[r] - pre[l])
	{
		while(!top2[r].empty())
		{
			int p = top2[r].back();
			if(2 * pre[p] < pre[l - 1] + pre[r])
			{
				break;
			}
			top2[r].pop_back();
		}
		while(!top2[r].empty())
		{
			int p = top2[r].front();
			if(dp[p + 1][r] < dp[l + 1][r])
			{
				break;
			}
			top2[r].pop_front();
		}
		top2[r].push_front(l);
		//最优决策为 top2[r].back() 
	}
}
ll query(int l, int r)
{
	ll w = LINF;
	if(!top[l].empty())
	{
		w = min(w, dp[l][top[l].front()]);
	}
	if(!top2[r].empty())
	{
		w = min(w, dp[top2[r].back() + 1][r]); 
	}
	return w;
}
void solve(int cas)
{
	cin >> n;
	for(int i = 1; i <= n; ++i)
	{
		cin>>a[i];
		dp[i][i]=-a[i];
		pre[i]=pre[i-1]+a[i];
		top[i].clear();
		top2[i].clear();
	}
	for(int len = 2; len <= n; ++len)
	{
		for(int l = 1; l + len - 1 <= n; ++l)
		{
			int r = l + len - 1;
			add(l, r);
			dp[l][r] = -query(l, r);
		}
	}
	if(dp[1][n] >= 0)
		cout << "Alice " << dp[1][n] << '\n';
	else 
		cout << "Bob " << -dp[1][n] << '\n';
}
```

