```c++
const ll base1=1331,base2=311,mod1=1e9+7,mod2=1000000000000002493;
inline ll ksc(ull x,ull y ,ll p){return (x*y-(ull)((ld)x/p*y)*p+p)%p;}
map<pair<ull,ull>,int>h;
ull hash[N];
void Hash()
{
	hash[0]=(ull)1;
	for(int i=1;i<N-10;++i)hash[i]=ksc(hash[i-1],base1,mod1);
}
```

```c++
namespace Hash
{
    const ull base1 = 1331, base2 = 31;
    const ull mod1 = 1e9 + 7, mod2 = 1000000000000002493ll;
    ull p;
    inline ll ksc(ull x,ull y ,ll p){return (x*y-(ull)((long double)x/p*y)*p+p)%p;}
//  map<pair<ull,ull>,int>h;
    vector<ull> power, h;
    int n;
    void init(string const& s, const ull _p = mod2)
    {
        p = _p;
        n = s.size();
        power.resize(n + 5);
        h.resize(n + 5, 0);
        power[0]=(ull)1;
        for(int i = 1; i < n; ++i)
        {
            power[i]=ksc(power[i-1],base1,p);
        }
        for(int i = 0; i < n; ++i)
        {
            h[i + 1] = (ksc(h[i], base1, p) + s[i]) % p;
        }
    }
    ull get_hash(int l, int r)
    {
        l++, r++;
        ull t = h[r] + p - ksc(h[l - 1], power[r - l + 1], p);
        return (t % p + p) % p;
    }
     
};

using Hash::init;
using Hash::get_hash;
```



```c++
namespace Hash
{
//	const ull base1 = 1331, base2 = 31;
	const ull mod1 = 1000000007, mod2 = 1000000000000002493ll;
	const int hash_cnt = 2;
	vector<ull>p(hash_cnt), base(hash_cnt);
	inline ll ksc(ull x,ull y ,ull p){return (x*y-(ull)((long double)x/p*y)*p+p)%p;}
//	map<pair<ull,ull>,int>h;
	vector<ull> power[hash_cnt], h[hash_cnt];
	int n;
	void init(string const& s)
	{
		base[0] = 233;
		base[1] = 1331;
		p[0] = mod1;
		p[1] = mod2;
		n = s.size();
		for(int j = 0; j < hash_cnt; ++j)
		{
			power[j].resize(n + 5);
			h[j].resize(n + 5, 0);
			power[j][0]=(ull)1;
			for(int i = 1; i <= n; ++i)
			{
				power[j][i]=ksc(power[j][i-1], base[j], p[j]);
			}
			for(int i = 1; i <= n; ++i)
			{
				h[j][i] = (ksc(h[j][i - 1], base[j], p[j]) + s[i - 1]) % p[j];
			}
		}
	}
	vector<ull> get_hash(int l, int r)
	{
		l++, r++;
		vector<ull>ans(hash_cnt);
		for(int j = 0; j < hash_cnt; ++j)
		{
			ll t = h[j][r] + p[j] - ksc(h[j][l - 1], power[j][r - l + 1], p[j]);
			ans[j] = (t % p[j] + p[j]) % p[j];
		}
		return ans;
	}
	
};
using Hash::init;
using Hash::get_hash;
```

