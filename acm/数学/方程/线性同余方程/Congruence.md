```c++
struct Congruence
{
	ll exgcd(ll a, ll b, ll &x, ll &y)	//扩欧
	{
		if(b == 0){x = 1; y = 0; return a;}
		ll d = exgcd(b, a % b, x, y);
		ll z = x; x = y; y = z - a / b * y;
		return d;
	}

	ll mul(ll a, ll b, ll c)
	{
		if(b < 0)a = -a, b = -b;
		ll res = 0;
		while(b)
		{
			if(b & 1)res = (res + a) % c;
			a = (a + a) % c;
			b >>= 1;
		}
		return res;
	}


	vector<ll>ai,bi;//x mod b = a;
    ll excrt()	//扩展中国剩余定理
    {
    	int n = ai.size();
    	ll x, y, k;
    	ll M = bi[0], ans = ai[0];//第一个方程的特解
    	for(int i = 1; i < n; ++i)
    	{
    		ll a = M, b = bi[i], c = (ai[i] - ans % b + b) % b;
    		ll d = exgcd(a, b, x, y);
    		ll bg = b / d;	//lcm
    		if(c % d != 0)return -1;	//判断无解
    		x = mul(x, c / d, bg);
    		ans += x * M;	//更新前k个方程的答案
    		M *= bg;
    		ans = (ans % M + M) % M;
    	}
    	ans = (ans % M + M) % M;
    	// if(ans == 0)ans = M;	//看情况，可能0是符合题意的也可能不是
    	return ans;
    }
}t;
```

