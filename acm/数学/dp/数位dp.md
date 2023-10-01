# 一些说明

**pos**为当前在第几位

**lead** 前导零标记 1表示需要判前导零

如果当前位是0直接跳过，$dfs(pos+1)$

**limit** 限制标记 1表示前面已经取到最高位 

不妨计当前最高位为$res$

则下一位的$limit$为$p[i]==res \&\& limit$

$x \space | \space \exists v \in subtree\left( u \right), x$

### code

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
//最高位在0c
ll pre(string s)
{
	dfs();
}
```

