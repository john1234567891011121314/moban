```c++
ll exgcd(ll a, ll b, ll &x, ll &y)
{
	if(!b)
	{
		x = 1;
		y = 0;
		return a;
	}
	ll d = exgcd(b, a % b, x, y);
	ll z = x; x = y; y = z - y * (a / b);
	return d;
} 
```

