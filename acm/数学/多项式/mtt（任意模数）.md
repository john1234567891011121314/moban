## FFT

```c++
//luoguP4245 【模板】MTT 
#include<cstdio>
#include<cmath>
#include<algorithm>
const int N = 4e5 + 10, M = 32767;
const double pi = acos(-1.0);
typedef long long LL;

int read() {
    char ch = getchar(); int f = 1, x = 0;
    for(;ch < '0' || ch > '9'; ch = getchar()) if(ch == '-') f = -1;
    for(;ch >= '0' && ch <= '9'; ch = getchar()) x = (x << 1) + (x << 3) - '0' + ch;
    return x * f;
}
struct cp {
    double r, i;
    cp(double _r = 0, double _i = 0) : r(_r), i(_i) {}
    cp operator * (const cp &a) {return cp(r * a.r - i * a.i, r * a.i + i * a.r);}
    cp operator + (const cp &a) {return cp(r + a.r, i + a.i);}
    cp operator - (const cp &a) {return cp(r - a.r, i - a.i);}
}w[N], nw[N], da[N], db[N];

cp conj(cp a) {return cp(a.r, -a.i);}

int L, n, m, a[N], b[N], c[N], R[N], P=1e9+7;

void Pre() {
    int x = 0; for(L = 1; (L <<= 1) <= n + m; ++x) ;
    for(int i = 1;i < L; ++i) R[i] = (R[i >> 1] >> 1) | (i & 1) << x;
    for(int i = 0;i < L; ++i) w[i] = cp(cos(2 * pi * i / L), sin(2 * pi * i / L));
}

void FFT(cp *F) {
    for(int i = 0;i < L; ++i) if(i < R[i]) std::swap(F[i], F[R[i]]);
    for(int i = 2, d = L >> 1;i <= L; i <<= 1, d >>= 1) 
        for(int j = 0;j < L; j += i) {
            cp *l = F + j, *r = F + j + (i >> 1), *p = w, tp;
            for(int k = 0;k < (i >> 1); ++k, ++l, ++r, p += d) 
                tp = *r * *p, *r = *l - tp, *l = *l + tp;
        }
}
void Mul(int *A, int *B, int *C) {
    for(int i = 0;i < L; ++i) (A[i] += P) %= P, (B[i] += P) %= P;
    static cp a[N], b[N], Da[N], Db[N], Dc[N], Dd[N];
    for(int i = 0;i < L; ++i) a[i] = cp(A[i] & M, A[i] >> 15);
    for(int i = 0;i < L; ++i) b[i] = cp(B[i] & M, B[i] >> 15);
    FFT(a); FFT(b);
    for(int i = 0;i < L; ++i) {
        int j = (L - i) & (L - 1); static cp da, db, dc, dd;
        da = (a[i] + conj(a[j])) * cp(0.5, 0);
        db = (a[i] - conj(a[j])) * cp(0, -0.5);
        dc = (b[i] + conj(b[j])) * cp(0.5, 0);
        dd = (b[i] - conj(b[j])) * cp(0, -0.5);
        Da[j] = da * dc; Db[j] = da * dd; Dc[j] = db * dc; Dd[j] = db * dd; //顺便区间反转，方便等会直接用DFT代替IDFT 
    }
    for(int i = 0;i < L; ++i) a[i] = Da[i] + Db[i] * cp(0, 1);
    for(int i = 0;i < L; ++i) b[i] = Dc[i] + Dd[i] * cp(0, 1);
    FFT(a); FFT(b);
    for(int i = 0;i < L; ++i) {
        int da = (LL) (a[i].r / L + 0.5) % P; //直接取实部和虚部 
        int db = (LL) (a[i].i / L + 0.5) % P;
        int dc = (LL) (b[i].r / L + 0.5) % P;
        int dd = (LL) (b[i].i / L + 0.5) % P;
        C[i] = (da + ((LL)(db + dc) << 15) + ((LL)dd << 30)) % P; 
    }
}
int main() {
    n = read(); m = read(); 
	P = read();
    for(int i = 0;i <= n; ++i) a[i] = read();
    for(int j = 0;j <= m; ++j) b[j] = read();
    Pre(); Mul(a, b, c); 
    for(int i = 0;i <= n + m; ++i) printf("%d ", (c[i] + P) % P); puts("");
    return 0;
}
```

## 三模数

```c++
#include <algorithm>
#include <cstdio>
#include <cstring>
int mod;
int qpow(int base, int p, const int mod)
{
	int res;
	for (res = 1; p; p >>= 1, base = static_cast<long long> (base) * base % mod) if (p & 1) res = static_cast<long long> (res) * base % mod;
	return res;
}
int inv(int x, const int mod) { return qpow(x, mod - 2, mod); }


const int mod1 = 998244353, mod2 = 1004535809, mod3 = 469762049, G = 3;

const long long mod_1_2 = 1ll * mod1 * mod2;

const int inv_1 = inv(mod1, mod2), inv_2 = inv(mod_1_2 % mod3, mod3);

struct Int {
	int A, B, C;
	Int() { }
	Int(int __num) : A(__num), B(__num), C(__num) { }
	Int(int __A, int __B, int __C) : A(__A), B(__B), C(__C) { }
	
	static inline Int reduce(const Int &x) {
		return Int(x.A + (x.A >> 31 & mod1), x.B + (x.B >> 31 & mod2), x.C + (x.C >> 31 & mod3));
	}
	inline friend Int operator + (const Int &lhs, const Int &rhs) {
		return reduce(Int(lhs.A + rhs.A - mod1, lhs.B + rhs.B - mod2, lhs.C + rhs.C - mod3));
	}
	inline friend Int operator - (const Int &lhs, const Int &rhs) {
		return reduce(Int(lhs.A - rhs.A, lhs.B - rhs.B, lhs.C - rhs.C));
	}
	inline friend Int operator * (const Int &lhs, const Int &rhs) {
		return Int(static_cast<long long> (lhs.A) * rhs.A % mod1, static_cast<long long> (lhs.B) * rhs.B % mod2, static_cast<long long> (lhs.C) * rhs.C % mod3);
	}
	
	inline int get() {
		long long x = 1ll * (B - A + mod2) % mod2 * inv_1 % mod2 * mod1 + A;
		return (1ll * (C - x % mod3 + mod3) % mod3 * inv_2 % mod3 * (mod_1_2 % mod) % mod + x) % mod;
	}
} ;

#define maxn 131072

namespace Poly {
#define N (maxn << 1)
	int lim, s, rev[N];
	Int Wn[N | 1];
	inline void init(int n) {
		s = -1, lim = 1; while (lim < n) lim <<= 1, ++s;
		for (register int i = 1; i < lim; ++i) rev[i] = rev[i >> 1] >> 1 | (i & 1) << s;
		const Int t(qpow(G, (mod1 - 1) / lim, mod1), qpow(G, (mod2 - 1) / lim, mod2), qpow(G, (mod3 - 1) / lim, mod3));
		*Wn = Int(1); for (register Int *i = Wn; i != Wn + lim; ++i) *(i + 1) = *i * t;
	}
	inline void NTT(Int *A, const int op = 1) {
		for (register int i = 1; i < lim; ++i) if (i < rev[i]) std::swap(A[i], A[rev[i]]);
		for (register int mid = 1; mid < lim; mid <<= 1) {
			const int t = lim / mid >> 1;
			for (register int i = 0; i < lim; i += mid << 1) {
				for (register int j = 0; j < mid; ++j) {
					const Int W = op ? Wn[t * j] : Wn[lim - t * j];
					const Int X = A[i + j], Y = A[i + j + mid] * W;
					A[i + j] = X + Y, A[i + j + mid] = X - Y;
				}
			}
		}
		if (!op) {
			const Int ilim(inv(lim, mod1), inv(lim, mod2), inv(lim, mod3));
			for (register Int *i = A; i != A + lim; ++i) *i = (*i) * ilim;
		}
	}
#undef N
}

int n, m;
Int A[maxn << 1], B[maxn << 1];
int main() {
	scanf("%d%d%d", &n, &m, &mod); ++n, ++m;
	for (int i = 0, x; i < n; ++i) scanf("%d", &x), A[i] = Int(x % mod);
	for (int i = 0, x; i < m; ++i) scanf("%d", &x), B[i] = Int(x % mod);
	
	Poly::init(n + m);
	Poly::NTT(A), Poly::NTT(B);
	
	for (int i = 0; i < Poly::lim; ++i) A[i] = A[i] * B[i];
	
	Poly::NTT(A, 0);
	
	for (int i = 0; i < n + m - 1; ++i) {
		printf("%d", A[i].get());
		putchar(i == n + m - 2 ? '\n' : ' ');
	}
	return 0;
}
```

