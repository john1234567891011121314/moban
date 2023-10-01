设一个块大小为$B$，将$a^{0},a^{1},\cdots,a^{B-1}$插入哈希表中，

根据询问查询$b, b * a^{-B}, a^{-2B}\cdots, $

如果$b*a^{-iB}=a^{j}$ 那么$x=iB+j$

实际可以调整块大小加快询问

```c++
ll BSGS(ll a, ll b, ll P) //a^x=b(mod p) return x;
{
	map<ll, ll>mp;
	ll ans = 0, m = ceil(sqrt(P)) + 1, tmp = 1ll;
	for(ll i = 1; i <= m; ++i)
	{
		tmp = tmp * a % P;
		mp[tmp * b % P] = i;
		
	}
	ll res = tmp;
	for(ll i = 1; i <= m; ++i)
	{
		if(mp[res])
		{
			ans = m * i - mp[res];
			return ans;
		}
		res = res * tmp % P;
	}
	return -1;
}
```

## exBSGS

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

using namespace std;

ll BSGS(ll a, ll b, ll P) //a^x=b(mod p) return x;
{
	b %= P, a %= P;
	map<ll, ll>mp;
	ll m = ceil(sqrt(P)) + 1, tmp = 1ll;
	for(ll i = 1; i <= m; ++i)
	{
		tmp = tmp * a % P;
		mp[tmp * b % P] = i;
		
	}
	ll res = tmp;
	for(ll i = 1; i <= m; ++i)
	{
		if(mp.find(res) != mp.end())
		{
			return (m * i - mp[res] + P) % P;
		}
		res = res * tmp % P;
	}
	return -1;
}
ll inv(ll a, ll b)
{
	ll x, y;
	exgcd(a, b, x, y);
	return (x % b + b) % b;
}
ll exBSGS(ll a, ll b, ll P) //a^x=b(mod p) return x;
{
	a %= P;
	b %= P;
	if(b == 1 || P == 1)
	{
		return 0;
	}
	ll g = gcd(a, P), k = 0, na = 1;
	while(g > 1)
	{
		
		if(b % g) return -1;
		k++; b /= g; P /= g; na = na * (a / g) % P;
		if(na == b) return k;
		g = gcd(a, P);
	}
	ll x, y;
	exgcd(na, P, x, y);
	x = (x % P + P) % P; 
	ll f = BSGS(a, b * x % P, P);
	if(f == -1)return -1;
	return f + k;
}
```

奇怪的求，似乎快很多$p≤10^{18}$ 且 $p $不怎么毒瘤能够通过

```c++
#include <bits/stdc++.h>
using namespace std;

// 2023 OneWan
long long qpow(long long a, long long b) {
	long long res = 1;
	while (b) {
		if (b & 1) res = res * a;
		a = a * a;
		b >>= 1;
	}
	return res;
}
long long qpow(long long a, long long b, long long mod) {
    long long res = 1;
    while (b) {
        if (b & 1) {
            res = (__int128) res * a % mod;
        }
        b >>= 1;
        a = (__int128) a * a % mod;
    }
    return res;
}
template<class T> struct Random {
    mt19937 mt;
    Random() : mt(chrono::steady_clock::now().time_since_epoch().count()) {}
    T operator()(T L, T R) {
        uniform_int_distribution<int64_t> dist(L, R);
        return dist(mt);
    }
};
Random<long long> rng;
namespace Miller_Rabin {
    bool Miller_Rabin(const long long& n, const vector<long long>& as) {
        long long d = n - 1;
        while (!(d & 1)) {
            d >>= 1;
        }
        long long e = 1, rev = n - 1;
        for (auto& a : as) {
            if (n <= a) {
                break;
            }
            long long t = d;
            long long y = qpow(a, t, n);
            while (t != n - 1 && y != e && y != rev) {
                y = (__int128) y * y % n;
                t <<= 1;
            }
            if (y != rev && (!(t & 1))) return false;
        }
        return true;
    }
    bool is_prime(const long long& n) {
        if (!(n & 1)) {
            return n == 2;
        }
        if (n <= 1) {
            return false;
        }
        if (n < (1LL << 30)) {
            return Miller_Rabin(n, {2, 7, 61});
        }
        return Miller_Rabin(n, {2, 325, 9375, 28178, 450775, 9780504, 1795265022});
    }
} // Miller_Rabin
namespace Pollard_rho {
    long long solve(long long n) {
        if (!(n & 1)) {
            return 2;
        }
        if (Miller_Rabin::is_prime(n)) {
            return n;
        }
        long long R, one = 1;
        auto f = [&](long long x) {
            return ((__int128) x * x % n + R) % n;
        };
        auto rnd = [&]() {
            return rng(0, n - 3) + 2;
        };
        while (true) {
            long long x, y, ys, q = one;
            R = rnd(), y = rnd();
            long long g = 1;
            int m = 128;
            for (int r = 1 ; g == 1 ; r <<= 1) {
                x = y;
                for (int i = 0 ; i < r ; i++) {
                    y = f(y);
                }
                for (int k = 0 ; g == 1 && k < r ; k += m) {
                    ys = y;
                    for (int i = 0 ; i < m && i < r - k ; i++) {
                        q = (__int128) q * ((x - (y = f(y)) + n) % n) % n;
                    }
                    g = __gcd(q, n);
                }
            }
            if (g == n) {
                do {
                    g = __gcd((x - (ys = f(ys)) + n) % n, n);
                } while (g == 1);
            }
            if (g != n) {
                return g;
            }
        }
        return 0;
    }
    vector<long long> factorize(long long n) {
        if (n <= 1) return {};
        long long p = solve(n);
        if (p == n) return {n};
        auto L = factorize(p);
        auto R = factorize(n / p);
        copy(R.begin(), R.end(), back_inserter(L));
        return L;
    }
    vector<pair<long long, int>> prime_factor(long long n) {
        auto ps = factorize(n);
        sort(ps.begin(), ps.end());
        vector<pair<long long, int>> ret;
        for (auto &e : ps) {
            if (!ret.empty() && ret.back().first == e) {
                ret.back().second++;
            } else {
                ret.emplace_back(e, 1);
            }
        }
        return ret;
    }
    vector<long long> divisors(long long n) {
        auto ps = prime_factor(n);
        int cnt = 1;
        for (auto& [p, t] : ps) cnt *= t + 1;
        vector<long long> ret(cnt, 1);
        cnt = 1;
        for (auto& [p, t] : ps) {
            long long pw = 1;
            for (int i = 1; i <= t; i++) {
                pw *= p;
                for (int j = 0; j < cnt; j++) ret[cnt * i + j] = ret[j] * pw;
            }
            cnt *= t + 1;
        }
        return ret;
    }
} // Pollard_rho
namespace Pohlig_Hellman {
	long long BSGS(long long A, long long B, long long P, long long mod) {
		A %= mod;
		B %= mod;
		if (B == 1) {
			return 0;
		}
		if (A == 0) {
			if (B == 0) {
				return 1;
			}
			return -1;
		}
		long long t = 1;
		int m = sqrt(1.0 * P) + 1;
		long long base = B;
		unordered_map<long long, long long> vis;
		for (int i = 0 ; i < m ; i++) {
			vis[base] = i;
			base = (__int128) base * A % mod;
		}
		base = qpow(A, m, mod);
		long long now = 1;
		for (int i = 1 ; i <= m ; i++) {
			now = (__int128) now * base % mod;
			auto k = vis.find(now);
			if (k != vis.end()) {
				return i * m - k -> second;
			}
		}
		return -1;
	}
	long long getK(long long A, long long B, long long P, long long C, long long phi, long long mod) {
		vector<long long> pi;
		long long temp = 1;
		for (int i = 0 ; i <= C ; i++) {
			pi.emplace_back(temp);
			temp *= P;
		}
		long long k = qpow(A, pi[C - 1], mod);
		long long inv = 0;
		temp = 1;
		for (int i = C - 1 ; i >= 0 ; i--) {
			long long tp = qpow(A, pi[C] - inv, mod);
			long long tx = temp * BSGS(k, qpow((__int128)B * tp % mod, pi[i], mod), P, mod);
			inv += tx;
			temp *= P;
		}
		return inv;
	}
	int getOrg(long long P, long long phi, const vector<pair<long long, int>>& res) {
		for (int k = 2 ; ; k++) {
			bool flag = true;
			for (auto& [x, y] : res) {
				if (qpow(k, phi / x, P) == 1LL) {
					flag = false;
					break;
				}
			}
			if (flag) return k;
		}
	}
	void Exgcd(long long a, long long b, long long& x, long long& y) {
		if (b == 0) {
			x = 1;
			y = 0;
			return;
		}
		Exgcd(b, a % b, y, x);
		y -= a / b * x;
	}
	long long CRT(const vector<long long>& k, const vector<pair<long long, int>>& res) {
		int len = res.size();
		long long M = 1, ans = 0;
		vector<long long> m(len);
		for (int i = 0 ; i < len ; i++) {
			m[i] = qpow(res[i].first, res[i].second);
			M *= m[i];
		}
		for (int i = 0 ; i < len ; i++) {
			long long Mi = M / m[i];
			long long x, y;
			Exgcd(Mi, m[i], x, y);
			ans = (ans + (__int128)Mi * ((x % m[i] + m[i]) % m[i]) * k[i]) % M;
		}
		if (ans < 0) ans += M;
		return ans;
	}
	long long getX(long long B, long long A, long long phi, long long mod, vector<pair<long long, int>>& res) {
		vector<long long> k;
		for (auto& [x, y] : res) {
			long long z = qpow(x, y);
			long long tA = qpow(A, phi / z, mod);
			long long tB = qpow(B, phi / z, mod);
			k.emplace_back(getK(tA, tB, x, y, phi, mod));
		}
		return CRT(k, res);
	}
	long long Solve(long long A, long long B, long long P) {
		if (B == 1LL) {
			return 0LL;
		}
		long long phi = P - 1;
		vector<pair<long long, int>> res = Pollard_rho::prime_factor(phi);
		int rt = getOrg(P, phi, res);
		long long x = getX(A, rt, phi, P, res), y = getX(B, rt, phi, P, res);
		long long a, b;
		if (x == 0LL) {
			if (y == 0LL) {
				return 1LL;
			} else if (y == 1LL) {
				return 0LL;
			}
			return -1LL;
		}
		long long d;
		if (y % (d = __gcd(x, phi))) return -1;
		x /= d;
		phi /= d;
		y /= d;
		Exgcd(x, phi, a, b);
		a = ((__int128)a * y % phi + phi) % phi;
		return a;
	}
} // Pohlig_Hellman

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	long long A, B, P;
	cin >> P >> A >> B;
	long long ans = Pohlig_Hellman::Solve(A, B, P);
	if (ans == -1) {
		cout << "no solution\n";
	} else {
		cout << ans << "\n";
	}
	return 0;
}
```

