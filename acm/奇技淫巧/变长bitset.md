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

