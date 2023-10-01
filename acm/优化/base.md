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

