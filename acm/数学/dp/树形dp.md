### 题意

给定一棵树，你需要给树上每一个点赋**不同**的值，每个节点$u$的贡献$f[u]$是$mex_{v\in son_u} \{f[v] \}$，一颗树的贡献是所有节点的贡献，求这棵树的最大贡献

### 分析

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

### 题意

给定一棵树，每条边都有权值，每个点也都有权值。一个点$i$有一个修改代价$c[i]$，表示点$i$从权值$a$变成权值$b$需要$c_i*|a-b|$。

现在要求对于边$(u,v)$，都满足$min(w[u],w[v]) \leq w(u,v) \leq max(w[u],w[v])$，求最小修改代价

## 分析

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

