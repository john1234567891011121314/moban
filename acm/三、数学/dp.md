## dp
### 单调栈单调队列

#### 定义

简单来说就是满足单调性的栈和队列

出去条件：下标不在范围或新来的元素会比老元素有优势，老元素出队

栈

```c++
void insert(int x) 
{
    while(!sta.empty() && sta.top() < x)
	{
    	sta.pop();
	}
	sta.push(x);
}


```

```c++
head = 1; tail = 0;
void insert(int x)
{
    while (head <= tail && a[q[tail]] >= a[R[i]]) tail--;
    q[++tail] = R[i];
    while(q[head] < L[i])head++;
}    
```

#### 优化dp

对于形如$f[i]=max_{L[i] \leq j \leq R[i]} (f[j]+w[i])$的式子进行优化

#### 例题

##### 烽火传递

###### 题意

在某两个城市之间有 n 座烽火台，每个烽火台发出信号都有一定的代价。

为了使情报准确传递，在连续 m 个烽火台中至少要有一个发出信号。

###### 数据范围

$1≤m≤n≤2×10^5,0≤a_i≤1000$

###### 分析

首先有$dp$转移式，$dp[i]=min_{i-m+1 \leq j \leq i-1}(dp[j]+a[i])$

然后套板子即可

```c++
	dp[0] = 0;
	int l = 1, r = 0;
	int ans = INF;
	for(int i = 1; i <= n; ++i)
	{
		while(l <= r && dp[sta[r]] >= dp[i - 1])r--;
		sta[++r]=i - 1;
		while(sta[l] < i - m)l++;
		dp[i] = dp[sta[l]] + a[i];
		if(i > n - m)ans=min(ans, dp[i]);
	}
```

##### 修剪草坪

###### 题意

在一年前赢得了小镇的最佳草坪比赛后，FJ 变得很懒，再也没有修剪过草坪。现在，新一轮的最佳草坪比赛又开始了，FJ 希望能够再次夺冠。

然而，FJ 的草坪非常脏乱，因此，FJ 只能够让他的奶牛来完成这项工作。FJ 有 $N$ 只排成一排的奶牛，编号为 1 到 *N*。每只奶牛的效率是不同的，奶牛 *i*的效率为 $E_i$。

靠近的奶牛们很熟悉，如果 FJ 安排超过 *K* 只连续的奶牛，那么这些奶牛就会罢工去开派对。因此，现在 FJ 需要你的帮助，计算 FJ 可以得到的最大效率，并且该方案中没有连续的超过 *K* 只奶牛。

###### 分析

即$k+1$中必有一个不选，然后考虑不选之后的最小效率

同上

```c++
	cin >> n >> k; k++;//区间长度
    for(int i = 1;i <= n; ++i)cin>>a[i];
	dp[0] = 0;
	int l = 1, r = 0;
	ll ans = LINF;
	ll sum = 0;
	for(int i = 1;i <= n; ++i)sum += a[i];
	for(int i = 1;i <= n; ++i)
	{
		while(l <= r && dp[sta[r]] >= dp[i-1])r--;
		sta[++r] = i - 1;
		while(sta[l] < i - k)l++;
		dp[i] = dp[sta[l]] + a[i];
		if(i > n - k)ans = min(ans, dp[i]);
	}
	cout << sum - ans << '\n';
```

##### 绿色草坪

###### 题意

高二数学《绿色通道》总共有 *n* 道题目要抄，编号 $1 \cdots n$，抄第 *i* 题要花 $a_i$ 分钟。小 Y 决定只用不超过 *t* 分钟抄这个，因此必然有空着的题。每道题要么不写，要么抄完，不能写一半。下标连续的一些空题称为一个空题段，它的长度就是所包含的题目数。这样应付自然会引起马老师的愤怒，最长的空题段越长，马老师越生气。
现在，小 Y 想知道他在这 *t* 分钟内写哪些题，才能够尽量减轻马老师的怒火。由于小 Y 很聪明，你只要告诉他最长的空题段至少有多长就可以了，不需输出方案。

###### 数据范围

$0<n≤5×10^4,0<a_i≤3000,0<t≤10^8$

###### 分析

容易发现答案具有单调性，因此不妨二分最长连续空段为$m$，然后跑一次$ dp $，代码与上述相同

##### The Great Wall II

###### 题意

将n个数分成m段，每一段的代价是这一段数的最大值，求$m=1 \cdots n$时的最小代价

###### 分析

朴素写法即枚举前$i$个数，分成$j$段，然后考虑第$j+1$段是从那里开始到$i+1$

考虑优化，我们发现状态可以分为$a_i$作为最后一段贡献或者不是最后一段最大值

我们记$dp[i][j]$为前$i$个数分成$j$段的代价，那么就有$dp[i][j]=min_{ pos \leq p \leq i-1}(dp[p][j-1]+a[i])$，表示$a_i$作为最后一段最大值，然后$pos$表示$a[pos-1] \ge  a[i]$的最大的值，即上一个比$a_i$大的位置的下一位

如果不是最大值，那就有$dp[i][j]=dp[pos-1][j]$，这时将最后一段区间挂到$pos-1$的第$j$段上，那么$a_i$一定不是这一段的代价

首先单调栈维护上一个$pos$的值，$dp[i][j]$不具有单调性，因此我们考虑在为维护$pos$的时候顺便也维护对应的$dp$值，即栈内两个相邻元素的对应的下标的$min ~dp$。





### 期望dp概率dp

#### 期望$dp$

##### 常用公式

$$
E(X)=\sum p(X_i)X_i \\
E(X|D) =\sum p(X_i|D)X_i\\
P(X|D)=\frac{P(XD)}{P(D)} \\
P(A)=\sum P(A|B_i)P(B_i) ,~~~B_i \cap B_j= \emptyset, ~~ \cup B_i=\Omega
$$

**通常我们期望 $dp$是从后往前推，而概率$dp$一般从前往后**

**期望具有线性性**

##### 题目

###### 题意

$n$面的骰子，问每个面都被投出过的期望次数是多少

###### 分析

$dp[i]$表示已经有$i$面被投出过，那么接下来还有$n-i$没有被投出过
$$
dp[i] = \frac{i}{n}dp[i]+\frac{n-i}{n}dp[i+1]+1
$$
稍作整理即可得出递推式

###### 题意

若干个宝箱，宝箱里有东西的概率是$p$，求最后$n$次中至少有$k$个宝箱期望次数

###### 分析

这题$n$，$k$很小，只有$6$

考虑枚举最后$n$位的状态，我们有
$$
dp[z_0z_1z_2z_3z_4z_5]=1+p*dp[1z_0z_1z_2z_3z_4]+(1-p)*dp[0z_0z_1z_2z_3z_4]
$$
然后高斯消元即可

###### 题意

已知牌堆一共有34种类型，每种类型的牌四张

在开局会发给你13张牌，（**保证**每种类型的牌的数量小于等于2)，以此进行游戏

在每一回合，先从牌库抽一张牌，若此时十四张手牌为（7种不同的类型，每种各两张）则算作胜利，结束游戏。否则就从十四张牌中选择一张放入弃牌堆（不放回的意思）

一共T组样例，每次给你起始手牌，询问在**最优策略的情况下**的获胜的期望次数。

###### 分析

首先思考什么是最优策略

如果我当前拿到的牌，我手中已经有了2张，那么我们就直接丢弃这张牌

如果我当前已经有一张，那么我们丢弃另外的只有一张的牌

如果我当前没有，那么直接把这张牌丢了

为什么呢，首先我一开始手上一定有单牌，那么最后我们肯定是和一开始留下的牌进行匹配，不然如果我们先前把某个类型的牌丢了，那么后面我们就不可能再拿这个类型的牌，因为牌库里这种牌的数量已经小于$3$了，比一开始就有的牌抽到的概率低。

于是我们发现每次我只需要关心牌库里还有几张牌，以及我当前有几张单牌。

于是设$dp[i][j]$表示牌库里还有$j$张牌，手上有$i$张单牌，然后到达全匹配的期望次数。

容易发现$dp[1][3]=1$。即当我手上有只有一张单牌，同时牌库里还有三张牌时，我们怎么样都可以抽出一个

和其匹配的牌。

同时我们有转移方程
$$
dp[i][j]=1+\frac{3*i}{j}dp[i-2][j-1]+\frac{j-3*i}{j}dp[i][j-1]
$$
这里$-2$是因为还有一张牌被我们丢了

当$i$等于1时，我们有
$$
dp[i][j]=1+\frac{j-3*i}{j}dp[i][j-1]
$$
这是因为只有我们没抽到想要的牌，我们才需要继续抽

###### 题意

一个长度为$n$的序列，每次操纵随机选取两个下标，然后将这两个下标对应的数进行交换，问$m$次操作后每一位和一开始不同的个数的期望

###### 分析

一道很好的期望题，虽然赛时尝试打表并没有找到什么规律

我们计$f_m$表示操作%$m$次后，$a_0=0$的概率。

因为每一位其实是等价的，我们计算时可以

$E(\sum X_i) =\sum E(X_i)=n*E(X_0)=n*f_m$

其中$E(X_i)$表示第$i$位和一开始一样的期望

因此只需要计算$f_m$即可

首先第$m$次和原来相同，来自于前一次和原来相同，然后操作一次不变，或者前一次和原来不同，但是操作完后回到原位置

原来相同，操作不变，可能是两次交换的下标都是$0$，或者都不是$0$

原来不同，那么只有两种情况回到原位置

$f_m= \frac{1+(n-1)^2}{n^2} f_{m-1} + \frac{2}{n^2} (1-f_{m-1})$

化简得到$f_m=\frac{2}{n^2}+\frac{n-2}{n}f_{m-1}$

然后就可以用矩阵快速幂之类的方法维护了。

#### 随机游走

 首先对于任何一个点的期望经过次数，我们都有

$d(x)$表示点$x$的度
$$
E(X)= \sum_{X \to Y} \frac{E[Y]}{d(Y)}
$$
而每条边经过的期望次数我们可以写成
$$
f(u,v)=\frac{E(u)}{d(u)}+\frac{E(v)}{d(v)}
$$
然后通过高斯消元我们就可以解决问题

#### 树上随机游走

不妨计$f[i]$为从子节点$i$走向父节点的期望步数，我们有


$$
f[u]=\frac{w(u,p_u)+\sum_{v \in son_u} (w(u,v)+f[v]+f[u])}{deg[u]}
$$
化简可得
$$
f[u]=\sum_{(u,v) \in E} w(u,v) + \sum_{v \in son_u}f[v]
$$
当边权都是1时，我们进一步可以得到
$$
f[u]=2*size[u]-1
$$
其中$size[u]$是$u$子树的大小

计$G[x]$为从父节点$f$走向子节点$x$的期望步数
$$
G[x]=\frac{w(p_x,x) + (~ w(p_x,p_{p_x})+ G[p_x]+G[x] ~) + \sum_{v \in son_{f_x},v \neq x } (~w(p_x,v)+f[v] + G[x]) } {deg[p_x]}
$$
化简可得
$$
G[x]=G[p_x] + f[p_u] - f[u]
$$

```c++
//代码存疑需要修改，主要初始值需要斟酌
void dfs1(int u, int p) {
    bool flag = 1;
  	for (auto [v,w] : G[u]) {
    	if (v == p) continue;
        flag = 0;
    	dfs1(v, u);
    	f[u] += f[v] + w;
  	}
    if(flag) f[u] = G[u][0].second; 
}

void dfs2(int u, int p) {
  	for (auto v : G[u]) {
    	if (v == p) continue;
        g[v] = g[u] + f[u] - f[v];
    	dfs2(v, u);
    	
  	}
}
```



### 奇怪dp

#### 状态转换

##### 题意

每一位数字$a_i$在$-m\leq a_i\leq m$之间，同时任意长度大于等于2的子段和非负，问这样的序列有多少个

##### 分析

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

##### 题目

23杭电多校第六场1008

##### 题意

$Alice$和$Bob$在做游戏。

一开始他们有一个序列，每次他们都可以选择一个位置$pos$，如果第一位到$pos$的和大于等于$pos+1$到最后一位的前缀和，那么我们就把$pos$后面的给截去，只留下前面的部分，否则我们留下后面的。

这个游戏显然有必胜必败策略，于是$Alice$和$Bob$希望自己赢的时候留下的数字尽可能大，不然就尽可能小。

##### 分析

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



### 区间dp

#### 题目

##### 题意

你有$n$张牌，每张牌都有类型和等级$(初始等级为1)$，每张牌打出去后都会产生$p^{x-1}*V_i$的收益，其中$x$是这张牌的等级，$i$是这张牌的种类。你可以选择两张相邻且种类相同等级相同的牌，将其合并为一张更高等级的牌，求所有牌打完后的最高收益。

##### 分析

这显然是一道区间$dp$，即我们可以考虑这个区间产生的最大收益是多少。但是仅有这个状态是不够的，因为还有合并的状态，因此我们考虑这个区间只有一张牌的情况，此时任意的合并操作都可以看成两个区间留下一张牌的情况

即设状态为$dp[l][r][x][k]$，表示在$[l,r]$区间保留种类为$k$，等级为$x$的牌。

同时记$dp[l][r][0][0]$，表示这个区间牌都打光的情况。

如果留下来的牌等级为$1$，那么
$$
dp[l][r][1][k]=\max_{l+1 \leq p \leq r-1,a[i]==k} (dp[l][p-1][0][0]+dp[p+1][r][0][0])
$$
同时，$p=l$或$p=r$的情况与之类似

如果留下的牌等级超过$1$，那么一定是合成来的
$$
dp[l][r][x][k]=\max_{l\leq p\leq r-1} (dp[l][p][x-1][k]+dp[p+1][r][x-1][k])
$$
计算这个区间的贡献，只需枚举这个区间最后一张牌是是什么
$$
dp[l][r][0][0]=\max{dp[l][r][x][k]+P^{x-1}*v[k]}
$$

```c++
for(int i=0;i<=n;++i)for(int p=0;p<=n;++p)
        for(int j=0;j<=7;++j)for(int k=0;k<=20;++k)dp[i][p][j][k]=-LINF;
    
    for(int i=1;i<=n;++i)dp[i][i][1][a[i]]=0,dp[i][i][0][0]=v[a[i]];
    for(int len=2;len<=n;++len)
    {
        for(int l=1;l+len-1<=n;++l)
        {
            int r=l+len-1;
            for(int p=l;p<=r;++p)
            {
                if(p!=l&&p!=r)dp[l][r][1][a[p]]=max(dp[l][r][1][a[p]],dp[l][p-1][0][0]+dp[p+1][r][0][0]);
                else if(p==l)dp[l][r][1][a[p]]=max(dp[l][r][1][a[p]],dp[p+1][r][0][0]);
                else if(p==r)dp[l][r][1][a[p]]=max(dp[l][r][1][a[p]],dp[l][p-1][0][0]);
            }
            
            for(int x=2;x<=R;++x)
            {
                for(int k=1;k<=m;++k)
                {
                    for(int p=l;p<r;++p)
                    {
                        dp[l][r][x][k]=max(dp[l][r][x][k],dp[l][p][x-1][k]+dp[p+1][r][x-1][k]);
                    }
                }
                
            }
            
            for(int x=1;x<=R;++x)
            {
                for(int k=1;k<=m;++k)
                {
                    dp[l][r][0][0]=max(dp[l][r][0][0],dp[l][r][x][k]+v[k]*pw[x-1]);
                }
            }
        }
    }
    cout<<dp[1][n][0][0]<<'\n';
```



### 树形dp

#### 题意

给定一棵树，你需要给树上每一个点赋**不同**的值，每个节点$u$的贡献$f[u]$是$mex_{v\in son_u} \{f[v] \}$，一颗树的贡献是所有节点的贡献，求这棵树的最大贡献

#### 分析

首先对于一个节点来说，最大贡献肯定是只有它一个子树的贡献加上它这个子树的大小。

即我们可以假设这个点的所有子节点从零开始赋值，否则这个节点的贡献会减少，同时在儿子节点中只有一个产生贡献，因为$0$只有一个。那么贪心的选择就可以。

```c++
vector<int>G[N];
ll dp[N],s[N]; 
void dfs(int x,int f)
{
	dp[x]=0;
	s[x]=1;
	for(int y:G[x])
	{
		if(y==f)continue;
		dfs(y,x);
		dp[x]=max(dp[x],dp[y]);
		s[x]+=s[y];
	}
	dp[x]+=s[x];
	
}
```

#### 题意P2986 [USACO10MAR] Great Cow Gathering G

Bessie 正在计划一年一度的奶牛大集会，来自全国各地的奶牛将来参加这一次集会。当然，她会选择最方便的地点来举办这次集会。

每个奶牛居住在 *N* 个农场中的一个，这些农场由 $N−1$ 条道路连接，并且从任意一个农场都能够到达另外一个农场。道路 *i* 连接农场 $A_i$ 和 $B_i$，长度为 $Li$。集会可以在 $N$ 个农场中的任意一个举行。另外，每个牛棚中居住着 $C_i $只奶牛。

在选择集会的地点的时候，Bessie 希望最大化方便的程度（也就是最小化不方便程度）。比如选择第 $X$ 个农场作为集会地点，它的不方便程度是其它牛棚中每只奶牛去参加集会所走的路程之和（比如，农场 $i$ 到达农场 $X$ 的距离是 20，那么总路程就是 $C_i×20$。帮助 Bessie 找出最方便的地点来举行大集会。

#### 分析

假设我们选择一号点作为集会点，那么我们可以子树dp一下，记录子树内所有牛到子树的根节点的距离，即$dp[u] = \sum_{v \in son _u} dp[v] + sz[v] * w[u, v]$，$sz[x]$表示以$x$为根的子树的牛的个数。

接下来考虑换根计算每个点作为集会点的代价，有
$$
ans[1] = dp[1]\\ 
ans[v] = 子树内的点到v+子树外的点到u再到v\\
= dp[v] + dp[u] - sz[y] * w[u, v] - dp[y] + (tot - sz[y]) * w[u,v]
$$

```c++
ll c[N];
ll sz[N];
vector<pair<int,ll>> G[N];
ll dp[N], ans[N];
int n;
void dfs(int x, int fa)
{
	sz[x] = c[x];
	for(auto [y, w]:G[x])
	{
		if(y == fa) continue;
		dfs(y, x);
		sz[x] += sz[y];
		dp[x] += w * sz[y] + dp[y];
	}
	// cout << x << ' ' << dp[x] << '\n';
}
void rdfs(int x, int fa)
{
	// cout << x << ' ' << dp[x] << '\n';
	for(auto [y, w]:G[x])
	{
		if(y == fa) continue;
		dp[y] = (sz[1] - sz[y]) * w + dp[x] - sz[y] * w;
		rdfs(y, x);
	}
}
void solve(int cas)
{
	cin >> n;
	for(int i = 1; i <= n; ++i) cin >> c[i];
	for(int i = 1; i < n; ++i)
	{
		int x, y;
		ll z;
		cin >> x >> y >> z;
		G[x].emplace_back(y, z);
		G[y].emplace_back(x, z);
	}
	dfs(1, 0);
	rdfs(1, 0);
	ll Ans = LINF;
	for(int i = 1; i <= n; ++i)Ans = min(Ans, dp[i]);
	cout << Ans << '\n';
} 
```



#### 题意

给定一棵树，每条边都有权值，每个点也都有权值。一个点$i$有一个修改代价$c[i]$，表示点$i$从权值$a$变成权值$b$需要$c_i*|a-b|$。

现在要求对于边$(u,v)$，都满足$min(w[u],w[v]) \leq w(u,v) \leq max(w[u],w[v])$，求最小修改代价

#### 分析

每个点的取值可以认为不会超过这个点的度数+1个，枚举一下可能的取值然后对于相同情况考虑上下界取最小即可

```c++
ll calc(int x,int w)
{
	return c[x]*abs(d[x]-w);
}
void dfs(int x,int f,ll pre)
{
	vector<pair<ll,int> >v;
	ll s=0;
	for(int i=head[x];i;i=nxt[i])
	{
		int y=ver[i];
		if(y==f)continue;
		dfs(y,x,e[i]);
		s+=dp[y][1];
		v.emplace_back(e[i],y);
	}
	v.emplace_back(d[x],0);
	if(x!=1)v.emplace_back(pre,0);
	sort(v.begin(),v.end());
	ll ppre=0;
	for(int i=0;i<v.size();++i)
	{
		int j=i;
		ll tmp=min(dp[v[i].second][1],dp[v[i].second][0]);
		s-=dp[v[i].second][1];
		while(j<(int)v.size()-1&&v[j+1].first==v[i].first)
		{
			j++;
			s-=dp[v[j].second][1];
			tmp+=min(dp[v[j].second][1],dp[v[j].second][0]);
		}
		
		if(pre<=v[i].first||x==1)
		{
			dp[x][1]=min(dp[x][1],calc(x,v[i].first)+ppre+s+tmp);
		}
		if(pre>=v[i].first||x==1)
		{
			dp[x][0]=min(dp[x][0],calc(x,v[i].first)+ppre+s+tmp);
		}
		while(i<j)
		{
			ppre+=dp[v[i].second][0];
			i++;
		} 
		 ppre+=dp[v[i].second][0];
	}
	
}
```

#### 树上背包

##### 题目 P2014 [CTSC1997] 选课

大学里每个学生，为了达到一定的学分，必须从很多课程里选择一些课程来学习，在课程里有些课程必须在某些课程之前学习，如高等数学总是在其它课程之前学习。现在有 $N$ 门功课，每门课有个学分，每门课有一门或没有直接先修课（若课程 $a$ 是课程 $b$ 的先修课即只有学完了课程 $a$，才能学习课程 $b$）。一个学生要从这些课程里选择 $M$ 门课程学习，问他能获得的最大学分是多少？

##### 分析

得到的结构是树形的结构， 可以用临时数组记录合并状态。

```c++
int dp[310][310];
int s[310];
int n, m;
vector<int> G[310];
int up[310];
int ret[310];
void dfs(int x)
{
	dp[x][1] = s[x];
	up[x] = 1;
	for(int y:G[x])
	{
		dfs(y);
		for(int i = 0; i <= up[x] + up[y]; ++i) ret[i] = dp[x][i];

		for(int i = 1; i <= up[x]; ++i)
		{
			for(int j = 0; j <= up[y]; ++j)
			{
				ret[i + j] = max(ret[i + j], dp[x][i] + dp[y][j]);
			}
		}

		up[x] += up[y];
		for(int i = 0; i <= up[x]; ++i) dp[x][i] = ret[i];
	}
	
}
void solve(int cas)
{
	cin >> n >> m;
	m++;
	int root = n + 1;
	for(int i = 1; i <= n; ++i)
	{
		int k;
		cin >> k >> s[i];
		if(k) G[k].push_back(i);
		else G[root].push_back(i);
	}
	dfs(root);
	cout << dp[root][m] << '\n';
} 
```



##### 题目

给定一棵树，可以选择若干组没有公共端点的边，同时还可以往里面加$k$组权值为$p$的边，求选择的边的最大权重。

##### 分析

考虑每个点是否可以向上连边，以及每个点的子树删除恰好$m$个点的最大贡献

于是题目就是求树上背包

```c++

vector<pair<int,ll>>G[maxn]; 
ll dp[maxn][210][2];
ll tmp[210][2];
int sz[maxn];
int n, k;
ll p;
void dfs(int x, int fa)
{
	for(int i = 0; i <= 2 * k; ++i) dp[x][i][0] = dp[x][i][1] = -LINF;
	dp[x][0][1] = 0;
	dp[x][1][0] = 0;
	sz[x] = 1;
	for(auto [y, w]:G[x])
	{
		if(y == fa) continue;
		dfs(y, x);
		for(int i = 0; i <= min(2 * k, sz[x] + sz[y]); ++i)
		{
			tmp[i][0] = -LINF;
			tmp[i][1] = -LINF;
		} 
		for(int i = 0; i <= min(2 * k, sz[x]); ++i)
		{
			for(int j = 0; j <= min(2 * k, sz[y]) && i + j <= min(2 * k, sz[x] + sz[y]); ++j)
			{
				tmp[i + j][1] = max({tmp[i + j][1], dp[x][i][1] + dp[y][j][0], dp[x][i][1] + dp[y][j][1]});
				tmp[i + j][0] = max({tmp[i + j][0], dp[x][i][1] + dp[y][j][1] + w, dp[x][i][0] + dp[y][j][1], dp[x][i][0] + dp[y][j][0]});
				if(i + j < 2 * k)
				{
					tmp[i + j + 1][0] = max({tmp[i + j + 1][0], dp[x][i][1] + dp[y][j][1], dp[x][i][1] + dp[y][j][0]});
				}
				
			}
		}
		sz[x] += sz[y];
		for(int i = 0; i <= min(2 * k, sz[x]); ++i) 
		{
			dp[x][i][0] = tmp[i][0];
			dp[x][i][1] = tmp[i][1];
		}
	}	
	
}
void solve() {
    
	cin >> n >> k >> p;
	for(int i = 1; i < n; ++i)
	{
		int u, v;
		ll w;
		cin >> u >> v >> w;
		G[u].emplace_back(v, w);
		G[v].emplace_back(u, w);
	}
	dfs(1, 0);
	ll ans = 0;
	for(int i = 0; i <= 2 * k; ++i)
	{
		ans = max(ans, (i / 2ll) * p + max(dp[1][i][0], dp[1][i][1]));
	}
	cout << ans << '\n';
} 


```



### 数位dp

#### 一些说明

**pos**为当前在第几位

**lead** 前导零标记 1表示需要判前导零

如果当前位是0直接跳过，$dfs(pos+1)$

**limit** 限制标记 1表示前面已经取到最高位 

不妨计当前最高位为$res$

则下一位的$limit$为$p[i]==res \&\& limit$

$x \space | \space \exists v \in subtree\left( u \right), x$

#### code

```c++
//lead 前导零标记 1表示需要判前导零，当前位是0直接跳过
//limit 限制标记 1表示已经取到最高位 ，当前能取到的 
//pre 记录前几位的数方便状态转移 
// dp初值取-1 
ll dp[N];
//从高位到低位 
ll dfs(int pos, int pre, int st, ... , int lead, int limit)
{
    if(pos > len) return st; //剪枝
	if(dp[pos][pre][st]...[...] != -1 && !limit && !lead) return  dp[pos][pre][st]...[...];
	ll res = 0;	//当前的方案数 
	int up = limit?a[pos]:9;
	for(int i = 0; i <= up; ++i)
	{
		//需要判前导零并且当前位是0 
		if(!i && lead) res += dfs(pos + 1,...,i == res && limit);
		//需要判前导零并且当前位不是0
		else if(i && lead) res +=  dfs(pos + 1,..., 0,i == res && limit);
		else if(其他条件) res += dfs(pos + 1,...,i == res && limit);
	} 
	if(!limit && !lead) dp[pos][pre][st]...[...] = res;
	return res;
}
//最高位在0
ll pre(string s)
{
	dfs();
}
```

#### 题目

对于一个十进制非负整数 $n$，我们可以按照从高位到低位将其写成一个由数位 $0∼9$ 构成的字符串 $S(n)$（不含前导 0）。

称一个仅由 $<$ 和 $>$ 组成的串为关系串。对于一个长度为 $k$ 的关系串 $R=r_1r_2⋯r_k$ 和一个长度为 $k+1$ 的字符串 $S=s_1s_2⋯s_{k+1}$，如果任意 $1≤i≤k$，都有关系 $ri(si,si+1)$ 成立，则称字符串 $S$ 满足关系串 $R$ 的限制。

其中关系 $ri(si,si+1)$ 成立只有两种情况，$ri=<$ 且 $si<si+1$ 或者 $ri=>$ 且 $si>si+1$，比较按照字典序顺序。

现在定义 $f(n,R)$ 表示 $S(n)$ 中有多少个子序列满足关系串 $R$ 的限制。给定 $l,r,R$，求：

$∑_{n=l}^rf(n,R)) \mod998244353$

其中一个字符串的子序列定义为从原字符串中删去若干个（可以不删或删空）字符得到的新字符串。

```c++
int dp[2][N+9][N+9][S];; //是否有前导零，第i个开始任意,已经选了j个，结尾是k 
/*
pos 当前第几位 
sec 已经选择了几位
last 上一位是多少
lead 是否有前导零
limit 是否限制
len r的大小
s 字符串
r 关系限制 
*/ 
string r;
int dfs(int pos, int sec, int last, int lead, int len,const string &r)
{
    int &res = dp[lead][pos][sec][last];
    if(res != -1) return res;
    if(pos >= len)
    {
        if(sec == (int)r.size() + 1) return 1;
        return 0;    
    }
    if(sec == (int)r.size() + 1)
    {
        res = 10ll * dfs(pos + 1, sec, last, lead, len, r) % mod;
        return res;
    }
    
//    int res = 0;
    res = 0;
    for(int i = 0; i <= 9; ++i)
    {
        res += dfs(pos + 1, sec, last, lead && !i, len, r);
        res %= mod;
        if(!i && lead) continue;
        if(sec > 0 && r[sec - 1] == '<' && last >= i) continue;
        if(sec > 0 && r[sec - 1] == '>' && last <= i) continue;
        res +=  dfs(pos + 1, sec + 1, i, 0, len, r);
        res %= mod;
    } 
    return res;
}

int pdp[501][10], ndp[501][10];
int check(const string &s, int n, const string &r, int m)
{
    memset(pdp, 0, sizeof(pdp));

    pdp[0][0] = 1;
    for(int i = 1; i <= n; ++i)
    {
        for(int j = 0; j <= m; ++j)
        {
            for(int k = 0; k < 10; ++k)
            {
                ndp[j][k] = pdp[j][k];
            }
        }
        for(int j = 0; j < m; ++j)
        {
            for(int k = 0; k < 10; ++k)
            {
                if((j == 0) || (r[j - 1] == '<' && k < s[i] - '0') || (r[j - 1] == '>' && k > s[i] - '0'))
                {
                    ndp[j + 1][s[i] - '0'] += pdp[j][k]; 
                    ndp[j + 1][s[i] - '0'] %= mod;
                }
                    
            }
        }
        for(int j = 0; j <= m; ++j)
        {
            for(int k = 0; k < 10; ++k)
            {
                pdp[j][k] = ndp[j][k];
            }
        }

    }
    int ans = 0;
    for(int i = 0; i < 10; ++i)
    {
        ans += pdp[m][i];
        ans %= mod;
    }
    return ans;
}
void init()
{
    memset(dp, -1, sizeof(dp));
}
int pre(const string &s, int len,const string &r)
{

    init();
    int ans = 0;
    int n = s.size();

    
    memset(pdp, 0, sizeof(pdp));
    pdp[0][0] = 1;
    for(int i = 1; i < n; ++i)
    {

        if(i + 1 < n)
        {
            for(int j = 0; j < s[i] - '0'; ++j)
            {
                for(int p = 0; p <= len; ++p)
                {
                    for(int k = 0; k < 10; ++k)
                    {
                        ans += 1ll * pdp[p][k] * dfs(i + 1, p, k, i == 1 && j == 0, s.size(), r) % mod;
                        ans %= mod;
                        if(j == 0 && i == 1) continue;
                        if(i + 1 >= n) continue;
                        if(p > 0 && p < len && r[p - 1] == '<' && k >= j) continue;
                        if(p > 0 && p < len && r[p - 1] == '>' && k <= j) continue;
                        if(p == len) continue;
                        ans += 1ll * pdp[p][k] * dfs(i + 1, p + 1, j, 0, s.size(), r) % mod;
                        ans %= mod;
                    }
                }
                    
            } 
        }
        else 
        {
            for(int j = 0; j < s[i] - '0'; ++j)
            {
                for(int k = 0; k < 10; ++k)
                {
                    ans += pdp[len][k];
                    ans %= mod;
                    if(k == 0 && i == 1) continue;
                    if(r[len - 2] == '<' && k >= j) continue;
                    if(r[len - 2] == '>' && k <= j) continue;
                    ans += pdp[len - 1][k];
                    ans %= mod;
                }
            }
                    
        }

        for(int j = 0; j <= len; ++j)
        {
            for(int k = 0; k < 10; ++k)
            {
                ndp[j][k] = pdp[j][k];
            }
        }
        for(int j = 0; j < len; ++j)
        {
            for(int k = 0; k < 10; ++k)
            {
                if((j == 0) || (r[j - 1] == '<' && k < s[i] - '0') || (r[j - 1] == '>' && k > s[i] - '0'))
                {
                    ndp[j + 1][s[i] - '0'] += pdp[j][k]; 
                    ndp[j + 1][s[i] - '0'] %= mod;
                }
                    
            }
        }

        for(int j = 0; j <= len; ++j)
        {
            for(int k = 0; k < 10; ++k)
            {
                pdp[j][k] = ndp[j][k];
            }
        }
    }
    for(int i = 0; i < 10; ++i)
    {
        ans += pdp[len][i];
        ans %= mod;
    }
    return ans;
}

void solve(int cas) {
    int n, m, len;
    string l; cin >> l; n = l.size();
    l = '~' + l;
    
    string r; cin >> r; m = r.size();
    r = '~' + r;
    
    string R; cin >> R; len = R.size();
    
    int ans = pre(r, len + 1, R) - pre(l, len + 1, R) + check(l, n, R, len + 1);
    ans = (ans % mod + mod) % mod; 
    cout << ans << '\n';
//    cout << r.size() << '\n';
//    cout << "!! " << cnt << ' ' << m * len * 10 * 10 *2 << '\n';
}
```



### min优化

#### 题目

总共$n$个数，要求连续$m$个数，至少取两个的最小代价

#### 分析

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



### ST表

#### 用途

解决RMQ（区间最大最小值查询）问题

更准确说，是可重贡献问题

即某个数重复计数不会影响最后的结果，常见的还有区间GCD等

#### code

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
            f[j][i] = max(f[j -1][i], f[j - 1][i + (1 << (j - 1))]);
        }
    }
}
int query(int x, int y)
{
    int s = logn[y - x + 1];
    return max(f[s][x], f[s][y - (1 << s) + 1]);
}
```

```c++
template <class T, class Op>
struct SparseTable
{
    int n = 0;
    vector<vector<T>> st;
    Op op;

    SparseTable() = default;

    SparseTable(const vector<T>& v, Op _op) : op(_op) { build(v); }

    template <class It>
    SparseTable(It l, It r, Op _op) : op(_op)
    {
        build(vector<T>(l, r));
    }

    void build(const vector<T>& v)
    {
        n = v.size();
        if (n == 0) return;
        int lg = std::__lg(n);
        st.assign(lg + 1, v);
        for (int k = 0; k < lg; k++)
        {
            for (int i = 0; i + (1 << (k + 1)) <= n; i++)
            {
                st[k + 1][i] = op(st[k][i], st[k][i + (1 << k)]);
            }
        }
    }

    T query(int l, int r) const
    {
        int k = std::__lg(r - l + 1);
        return op(st[k][l], st[k][r - (1 << k) + 1]);
    }

    T operator()(int l, int r) const { return query(l, r); }
};

template <class T, class Op>
auto make_sparse_table(const vector<T>& v, Op op)
{
    return SparseTable<T, Op>(v, op);
}

auto st = make_sparse_table(v, [](int a, int b){ return max(a, b); });
```

```c++
template <class T, class Cmp = std::less<T>>
struct ST
{
    const int n;
    const int k;
    std::vector<std::vector<T>> max_table;
    std::vector<std::vector<T>> min_table;
    const Cmp cmp;

    ST(const std::vector<T>& in)
        : n(static_cast<int>(in.size())),
          k(n ? (31 - __builtin_clz(n)) + 1 : 1),
          max_table(k, std::vector<T>(n)),
          min_table(k, std::vector<T>(n)),
          cmp(Cmp())
    {
        init(in);
    }

    void init(const std::vector<T>& in)
    {
        for (int i = 0; i < n; ++i)
        {
            max_table[0][i] = in[i];
            min_table[0][i] = in[i];
        }

        // 构建稀疏表
        for (int i = 0, t = 1; i < k - 1; ++i, t <<= 1)
        {
            const int range_end = n - (t << 1);
            for (int j = 0; j <= range_end; ++j)
            {
                max_table[i + 1][j] =
                    std::max(max_table[i][j], max_table[i][j + t], cmp);
                min_table[i + 1][j] =
                    std::min(min_table[i][j], min_table[i][j + t], cmp);
            }
        }
    }

    T getMax(int l, int r) const
    {
        if (l > r) return numeric_limits<T>::min();
        int lg = __lg(r - l + 1);
        return std::max(max_table[lg][l], max_table[lg][r - (1 << lg) + 1],
                        cmp);
    }

    T getMin(int l, int r) const
    {
        if (l > r) return numeric_limits<T>::max();
        int lg = __lg(r - l + 1);
        return std::min(min_table[lg][l], min_table[lg][r - (1 << lg) + 1],
                        cmp);
    }
};
```



### 绝对值dp

#### 前置

涉及绝对值的$dp$，往往需要在朴素解法上再优化一下，常见套路是将绝对值拆开求最大值

#### 题目

给定两个序列$a$，$b$，定义一个区间为$[l, r]$，其长度为$r - l + 1$，贡献为$\mid b_l - a_r \mid + \mid a_l - b_r \mid$

现在可以选择一些不相交的区间使得总长度恰好为k，贡献最大，求最大贡献。

#### 分析

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

### 同余最短路

一类最短路模型，表示$i$号点向$(i + v[i]) \% m$号点连边权为$w[i]$ 的点。

可以用最短路做，注意初始条件

```c++
for(int i = 1; i <= n; ++i)
{
    for(int j = 0, lim = __gcd(v[i], m); j < lim; ++j)
    {
        for(int k = j, c = 0; c < 2; c += (j == k))
        {
            int p = (k + v[i]) % m;
            dp[p] = min(dp[p], dp[k] + w[i]);
            k = p;
		}
	}
}
//求【l，r】可以表示的数的数量
for(int i = 0; i < m; ++i)
{
    if(r >= dp[i]) ans += max(0ll, (r - dp[i]) / m + 1);
	if(l > dp[i]) ans -= max(0ll, (l - 1 - dp[i]) / m + 1);
}
//求最大不能表示的数
for(int i = 0; i < m; ++i)
{
    ans = max(ans, dp[i] - m);
}

```

应用：完全背包/多重背包优化



### 简单dp

#### 01背包

```c++
for(int i = 1; i <= n; ++i)
{
    for(int j = T; j >= v[i]; --j)
    {
        dp[j] = max(dp[j], dp[j - v[i]] + w[i]);
	}
}
```

在只考虑可不可行的情况下，可以用bitset优化为

```c++
dp[0] = 1;
for(int i = 1; i <= n; ++i)
{
    dp |= (dp << v[i]);
}
```

只考虑是否可行，且物品权重不超过D时有$O(ND)$的如下算法

```c++
int work(vector<ll> a, ll limit, ll C) 
{
    int n = a.size();
    a.insert(a.begin(), 0);
    ll sum = 0, pos = 0;
    
    for(int i = 1; i <= n; ++i)
    {
        if(sum + a[i] <= C) 
        {
            sum += a[i];
            pos++;
        }
        else break;
    }
    
    if(pos == n && sum < C) return 0; // 无解
    vector<vector<ll>> f(n + 1, vector<ll>(2 * limit + 1, 0));
    vector<vector<pair<ll, ll>>> last(n + 1, vector<pair<ll, ll>>(2 * limit + 1, {0, 0}));
    f[pos][sum - C + limit] = pos + 1;
    for(int i = pos + 1; i <= n; ++i)
    {
        for(int j = 1; j <= 2 * limit; ++j)
        {
            if(f[i][j] < f[i - 1][j]) 
            {
                f[i][j] = f[i - 1][j];
                last[i][j] = {i - 1, j};
            }
        }
        for(int j = 1; j <= limit; ++j)
        {
            if(f[i][j + a[i]] < f[i - 1][j]) 
            {
                f[i][j + a[i]] = f[i - 1][j];
                last[i][j + a[i]] = {i - 1, j};
            }
        }
        for(int j = 2 * limit; j >= limit + 1; --j)
        {
            for(int k = f[i - 1][j]; k <= f[i][j] - 1; ++k)
            {
                if(f[i][j - a[k]] < k) 
                {
                    f[i][j - a[k]] = k;
                    last[i][j - a[k]] = {i, j};
                }
            }
        }
    }
    // cerr << "!" << f[n - 1][limit] << '\n';
	if(!f[n][limit]) return 0;

    ans = vector<int>(n + 1, 0);
    for(int i = 1; i <= pos; ++i) ans[i] = 1;
    ll x = n, y = limit;
    while(x > pos)
    {
        auto [prex, prey] = last[x][y];
        if(prex == x - 1 && prey == y - a[x]) ans[x] = 1;
        else if(prex == x) ans[f[x][y]] = 0;
        x = prex, y = prey;
    }
    return 1;
}
```



#### 完全背包

```c++
for(int i = 1; i <= n; ++i)
{
    for(int j = v[i]; j <= T; ++j)
    {
        dp[j] = max(dp[j], dp[j - v[i]] + w[i])
    }
}
```

#### 多人背包

他们一共有 $K $个人，每个人都会背一个包。这些包 的容量是相同的，都是 $V$。可以装进背包里的一共有 $N$ 种物品，每种物品都 有 给定的体积和价值。 在 DD 看来，合理的背包安排方案是这样的： 每个人背包里装的物品的总体积恰等于包的容量。 每个包里的每种物品最多只有一件，但两个不同的包中可以存在相同的物品。 任意两个人，他们包里的物品清单不能完全相同。 在满足以上要求的前提下，所有包里的所有物品的总价值最大是多少呢？

求第k大背包方案，$O(nVK)$

```c++
void solve(int cas)
{
	int k, V, n;
	cin >> k >> V >> n;
	vector<int> v(n + 1), w(n + 1);
	vector<vector<int>> dp(k + 1, vector<int>(V + 1, -INF));
	dp[1][0] = 0;
	vector<int> ret(V + 1);
	for(int i = 1; i <= n; ++i) cin >> v[i] >> w[i];

	for(int i = 1; i <= n; ++i)
	{
		for(int j = V; j >= v[i]; --j)
		{
			for(int a = 1,  b = 1, t = 1; t <= k; ++t)
			{
				if(dp[a][j] >= dp[b][j - v[i]] + w[i])
					ret[t] = dp[a++][j];
				else 
					ret[t] = dp[b++][j - v[i]] + w[i];
			}
			for(int p = 1; p <= k; ++p) dp[p][j] = ret[p];
		}
	}

	int ans = 0;
	for(int i = 1; i <= k; ++i) ans += dp[i][V];
	cout << ans << '\n';

} 
```

#### 分组背包

容量为$V$，物品个数$n$，依次为体积，价值，所属的组别，每组物品至多选一个。

```c++
void solve(int cas)
{
	int V, n; cin >> V >> n;
	vector<vector<pair<int,int>>> a;
	for(int i = 1; i <= n; ++i)
	{
		int x, y, z; cin >> x >> y >> z;
		if(a.size() < z + 1) a.resize(z + 1);
		a[z].push_back({x, y});
	}
	vector<int> dp(V + 1);
	for(auto vec:a)
	{
		for(int j = V; j >= 0; --j)
		{
			for(auto [v, w]:vec)
			{
				if(j >= v)
				{
					dp[j] = max(dp[j], dp[j - v] + w);
				}
			}
		}
	}
	cout << dp[V] << '\n';

} 
```

#### 多重背包

有 $N$种物品和一个容量是 $V$ 的背包。

第 $i$ 种物品最多有 $s_i$件，每件体积是 $vi$，价值是 $wi$。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

```c++
void solve(int cas)
{
	int n, V; cin >> n >> V;
	vector<int> dp(V + 1);
	vector<pair<int,int>> a;
	for(int i = 1; i <= n; ++i)
	{
		int v, w, s;
		cin >> v >> w >> s;
		int p = 1;
		while(s >= p) 
		{
			a.emplace_back(w * p, v * p); 
			s -= p; 
			p <<= 1;
		}
		if(s) a.emplace_back(w * s, v * s);
	}
	for(auto [w, v] : a)
	{
		for(int j = V; j >= v; --j)
		{
			dp[j] = max(dp[j], dp[j - v] + w);
		}
	}
	cout << dp[V] << '\n';
} 

```

#### bitset优化可行性多重背包

```c++
template <int len = 1>
ll work(vector<int>&cnt, int n, int va) 
{
	if(len <= n)
	{
		return work<min(len * 2, maxn)>(cnt, n, va);//注意maxn也是整数
	}
	//下面是正常代码
	bitset<len>dp;
	dp[0] = 1;
	for(auto x:cnt)
	{
		int w = x, val = a[x];
		for(int i = 1; i <= val; i <<= 1)
		{
			if(x * i <= n)dp |= (dp << (x * i));
			val -= i;
		}
		if(val)
		{
			if(x * val <= n)dp |= (dp << (x * val));
		}
	}
    
	ll ans = 0;
	for(int i = n / 2; i >= 0; --i)
	{
		if(dp[i]) return 1ll * i * (s[va] - i);
	}
	return 0;
}
```

#### 多项式优化背包

首先考虑01背包

生成函数为$F(x)=\prod(1+x^{a_i})$

其中$a_i$表示第$i$件物品的体积

考虑$\ln$之后再$\exp$，则有$F(x)=\exp(\ln(1+x^{a_1}) + \cdots + \ln(1 + x^{a_n}))$

其中$\ln(1+x^{a_i})$应用泰勒展开可以得到$x^{a_i} - \frac{x^{2 * a_i}}{2} + \cdots + (-1)^n * \frac{x^{(n + 1) * a_i}}{n + 1}$

可以发现这部分式子是只有$V/a_i$的项是有意义的，利用调和级数优化即可

接下来考虑完全背包

生成函数为$F(x)=\prod(\frac{1}{1-x^{a_i}})$​

同样的，我们有$F(x)=\exp(\ln(\frac{1}{1-x^{a_1}})+\cdots)$

提取一个负号后，和01背包部分做同样操作即可。

多重背包

$b$是个数

$F(x) = \prod (\frac{1-x^{b_i*a_i}}{1-x^{a_i}})$​

然后类似上面做一下就行

附完全背包代码

```c++
for(int i = 1; i <= n; ++i)
{
    int x; cin >> x;
    a[x]++;
}
for(int i = 1; i <= m; ++i)
{
    if(!a[i]) continue;
    for(int j = 1; 1ll * j * i <= m; ++j)
    {
        dp[j * i] += 1ll * a[i] * (Poly::inv[j]) % mod;
        dp[j * i] %= mod;
    }
}
//	for(int i = 1; i <= m; ++i) cout << i << ' ' << dp[i] << '\n';
auto res = Poly::poly_exp(dp, dp.size());
```



### 高位前缀和优化dp

题目为所有子序列出现次数的立方和。

将题目转化为求三个序列恰好相等的方案数

则当$a[i] = a[j] = a[k]$ 时，选择的方案数 $dp[i][j][k]$为$dp$数组的三维前缀和数组$f[i -1][j-1][k-1]+ 1$

维护这个前缀和数组即可

```c++
vector<int> a(n + 1);
    vector f(4, vector<vector<vector<int>>>(n + 1, vector<vector<int>>(n + 1, vector<int>(n + 1))));
    for(int i = 1; i <= n; ++i)
    {
        cin >> a[i];
    }
    for(int i = 1; i <= n; ++i)
    {
        for(int j = 1; j <= n; ++j)
        {
            for(int k = 1; k <= n; ++k)
            {
                if(a[i] == a[j] && a[j] == a[k])
                {
                    f[0][i][j][k] = f[3][i - 1][j - 1][k - 1] + 1;
                    f[0][i][j][k] %= mod;
                }
                f[1][i][j][k] = f[0][i][j][k] + f[1][i][j][k - 1];
                f[1][i][j][k] %= mod;
                f[2][i][j][k] = f[1][i][j][k] + f[2][i][j - 1][k];
                f[2][i][j][k] %= mod;
                f[3][i][j][k] = f[2][i][j][k] + f[3][i - 1][j][k];
                f[3][i][j][k] %= mod;
                
            }
        }
    }
    cout << f[3][n][n][n] << '\n';
```

### SOSdp

sosdp通常用来解决子集问题。

对于$G(S) = \sum_{T \in S} f(T)$，其中求和符号可以为任意的具有结合律的符号。

可以使用子集枚举的方式，此时复杂度为$O(3^n)$。

但是可以发现在枚举子集的过程中，有很多地方我们都重复计算了，对于集合1110来说，集合1000出现了一次，但是在计算1100时，集合1000又出现了一次，这启示我们在枚举子集时有很多计算实质是不需要的。

那么接下来我们如何去考虑改变转移顺序使得我们能够尽量复用我们的计算。

我们令$S(mask) = \set{x | x \subseteq mask}$，我们考虑将其划分为若干个不相交的集合。

然后$S(mask, i) = \set{x| x \subseteq mask ~ \wedge x \bigoplus mask < 2^{i + 1} }$

如果$mask$的$i$是0，那么$S(mask, i) = S(mask, i - 1)$

否则$S(mask,i ) = S(mask, i - 1) \cup S(mask \bigoplus 2 ^ i, i - 1)$

常用写法（子集求和）

```c++
for(int i = 0; i < up; ++i)
	{
		for(int j = 0; j < (1 << up); ++j)
		{
			if(j & (1 << i))
				dp[j] = max(dp[j], dp[j ^ (1 << i)]);
		} 
	}
```

超集求和

```c++
for(int i = 0; i < up; ++i)
{
    for(int j = (1 << up) - 1; ~j; j--)
    {
        if(j & (1 << i))
        {
            sum[j ^ (1 << i)] += sum[j];
        }
	}
}
```

从子集和到权值

```c++
for(int i = n - 1; ~i; --i)
{
    for(int j = 0; j < (1 << n); ++j)
    {
        if(j & (1 << i))
            sum[j] -= sum[j ^ (1 << i)];
	}
}
```

从超集和到权值

```c++
for(int i = n - 1; ~i; --i)
{
    for(int j = (1 << n) - 1; ~j; --j)
    {
        if(j & (1 << i))
        {
            sum[j ^ (1 << i)] += sum[j];
		}
	}
}
```

统计有多少个数与给定数按位与不为0，可以转换为有多少个数是给定数的反的子集（即按位与为0）的情况。

### 动态dp

简而言之，就是通过树剖线段树维护矩阵来进行。

下面给出一个全局平衡二叉树的写法

```c++
// (max, +)矩乘
struct mat
{
    int mp[2][2];
    mat()
    {
        for (int i = 0; i < 2; ++i)
            for (int j = 0; j < 2; ++j)
                mp[i][j] = -INF;
    }
    mat(int a, int b, int c, int d)
    {
        mp[0][0] = a;
        mp[0][1] = b;
        mp[1][0] = c;
        mp[1][1] = d;
    }
    friend mat operator*(const mat &a, const mat &b)
    {
        mat c;
        for (int i = 0; i < 2; ++i)
            for (int j = 0; j < 2; ++j)
                for (int k = 0; k < 2; ++k)
                    c.mp[i][j] = max(c.mp[i][j], a.mp[i][k] + b.mp[k][j]);
        return c;
    }
};
int w[N];
struct Bst
{
    int root;             // 平衡后的根
    int dep[N], son[N], sz[N];
    int tfa[N];
    int ls[N], rs[N];
    int st[N], tp;
    bitset<N> vis;
    int s[N];
    mat val[N], d[N]; // 记录非重儿子的矩阵和所有儿子的转移矩阵信息
    vector<int> G[N];
    void add(int x, int y)
    {
        G[x].push_back(y);
        G[y].push_back(x);
    }

    // 找重儿子
    void dfs(int u, int fa)
    {
        sz[u] = 1;
        for (int v : G[u])
        {
            if (v == fa)
                continue;
            dep[v] = dep[u] + 1;
            dfs(v, u);
            sz[u] += sz[v];
            if (!sz[u] || sz[son[u]] < sz[v])
                son[u] = v;
        }
    }

    void update(int u)
    {
        d[u] = val[u];
        if (ls[u])
            d[u] = d[ls[u]] * d[u];
        if (rs[u])
            d[u] = d[u] * d[rs[u]];
    }
    // 链分治
    int Sbuild(int l, int r)
    {
        if (l > r)
            return 0;
        int mid = lower_bound(s + l, s + r + 1, (s[r] + s[l - 1]) >> 1) - s;
        int lch = Sbuild(l, mid - 1), rch = Sbuild(mid + 1, r);
        ls[st[mid]] = lch, rs[st[mid]] = rch;
        tfa[lch] = tfa[rch] = st[mid];
        update(st[mid]);
        return st[mid];
    }
    // 构建平衡树
    int build(int u)
    {
        for (int pos = u; pos; pos = son[pos])
            vis[pos] = true;
        // 计算轻儿子的贡献
        for (int pos = u; pos; pos = son[pos])
            for (int v : G[pos])
                if (!vis[v])
                {
                    tfa[build(v)] = pos;
                    while (tfa[v] != pos)
                        v = tfa[v];

                    val[pos].mp[0][0] += max(d[v].mp[0][0], d[v].mp[1][0]);
                    val[pos].mp[0][1] = val[pos].mp[0][0];
                    val[pos].mp[1][0] += d[v].mp[0][0];
                }
        // 处理重儿子
        tp = 0;
        for (int pos = u; pos; pos = son[pos])
        {
            st[++tp] = pos; // 把重链取出来
            s[tp] = s[tp - 1] + sz[pos] - sz[son[pos]];
        }
        int ret = Sbuild(1, tp); // 对重链进行单独的SBuild(我猜是Special Build?)
        return ret;              // 返回当前重链的二叉树的根
    }

    void Modify(int u, int v)
    {
        // 更新矩阵
        val[u].mp[1][0] += v - w[u];
        w[u] = v;
        for (int pos = u; pos; pos = tfa[pos])
            if (tfa[pos] && ls[tfa[pos]] != pos && rs[tfa[pos]] != pos)
            {
                mat c1 = d[pos];
                update(pos);
                mat c2 = d[pos];
                val[tfa[pos]].mp[0][0] += max(c2.mp[0][0], c2.mp[1][0]) - max(c1.mp[0][0], c1.mp[1][0]);
                val[tfa[pos]].mp[0][1] = val[tfa[pos]].mp[0][0];
                val[tfa[pos]].mp[1][0] += c2.mp[0][0] - c1.mp[0][0];
            }
            else
                update(pos);
    }

    void work()
    {
        // d[0] = mat(0, 0, -INF, -INF);
        dfs(1, -1);
        root = build(1);
    }

    int query()
    {
        int ret = -INF;
        for (int i = 0; i < 2; ++i)
            for (int j = 0; j < 2; ++j)
                ret = max(ret, d[root].mp[i][j]);

        return max(d[root].mp[0][0], d[root].mp[1][0]);
    }
} bs;

void solve()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i)
    {
        cin >> w[i];
        bs.val[i] = mat(0, 0, w[i], -INF);
    }
    for (int i = 1; i < n; ++i)
    {
        int x, y;
        cin >> x >> y;
        bs.add(x, y);
        // bs.add(y, x);
    }
    bs.work();

    int lastAns = 0;

    while (m--)
    {
        int u, v;
        cin >> u >> v;
        u ^= lastAns;
        bs.Modify(u, v);
        lastAns = bs.query();
        cout << lastAns << '\n';
    }
}
```

### 插入dp



