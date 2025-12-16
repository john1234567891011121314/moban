## bascic
```c++
namespace BasicT{
	mt19937 mtrandom(std::chrono::system_clock::now().time_since_epoch().count());
	template<typename T>T getRandom(T l,T r){return uniform_int_distribution<T>(l,r)(mtrandom);}
	template<typename T>T gcd(T a,T b){return b==0?a:gcd(b,a%b);}
	ll qmul(ll a,ll b){ll r=0;while(b){if(b&1)r=(r+a)%mod;b>>=1;a=(a+a)%mod;}return r;}
	ll qpow(ll a,ll n){ll r=1;while(n){if(n&1)r=(r*a)%mod;n>>=1;a=(a*a)%mod;}return r;}
	ll qpow(ll a,ll n,ll p){ll r=1;while(n){if(n&1)r=(r*a)%p;n>>=1;a=(a*a)%p;}return r;}
}
```

```c++
// 上取整
ll ceilDiv(ll n, ll m)
{
    if (n >= 0)
    {
        return (n + m - 1) / m;
    }
    else
    {
        return n / m;
    }
}
// 下取整
ll floorDiv(ll n, ll m)
{
    if (n >= 0)
    {
        return n / m;
    }
    else
    {
        return (n - m + 1) / m;
    }
}
// 赋值
template <class T>
void chmax(T& a, T b)
{
    if (a < b)
    {
        a = b;
    }
}
// 开方
ll sqrt(ll n)
{
    ll s = std::sqrt(n);
    while (s * s > n)
    {
        s--;
    }
    while ((s + 1) * (s + 1) <= n)
    {
        s++;
    }
    return s;
}
// log
int logi(int a, int b)
{
    int t = 0;
    ll v = 1;
    while (v < b)
    {
        v *= a;
        t++;
    }
    return t;
}

int llog(int a, int b)
{
    if (a <= b)
    {
        int l = logi(a, b);
        return (l == 0 ? 0 : std::__lg(2 * l - 1));
    }
    int l = logi(b, a + 1) - 1;
    assert(l > 0);
    return -std::__lg(l);
}
```



