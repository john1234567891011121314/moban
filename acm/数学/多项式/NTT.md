# NTT

## 前置知识

原根和单位根具有相似的性质，可以简单认为原根就是模数意义下的单位根

## 用法

用于模数意义下的多项式乘法，卷积

## 代码

#### 数组形式

```c++
const int p = 998244353, G = 3, Gi = 332748118;//G是原根，Gi是G的除法逆元
const int N = 5e5+10;


int n, m;
int res, ans[N];
int limit = 1;//
int L;//二进制的位数
int RR[N];
ll a[N], b[N];


ll qpow(ll a, ll b)
{
    ll res = 1;
    while(b) {
        if(b & 1) res = res * a % p;
        a = a * a % p;
        b >>= 1;
    }
    return res % p;
}

ll inv(ll x) {return qpow(x, p - 2);}

void NTT(ll *A, int type)//1转点值，-1转系数
{
    for(int i = 0; i < limit; ++ i)
        if(i < RR[i])
            swap(A[i], A[RR[i]]);
    for(int mid = 1; mid < limit; mid <<= 1) {//原根代替单位根
        //ll wn = qpow(type == 1 ? G : Gi, (p - 1) / (mid << 1));
        ll wn = qpow(G, (p - 1) / (mid * 2));
        
        for(int len = mid << 1, pos = 0; pos < limit; pos += len) {
            ll w = 1;
            for(int k = 0; k < mid; ++ k, w = (w * wn) % p) {
                int x = A[pos + k], y = w * A[pos + mid + k] % p;
                A[pos + k] = (x + y) % p;
                A[pos + k + mid] = (x - y + p) % p;

            }
        }
    }

    if(type == -1) {
        ll limit_inv = inv(limit);//N的逆元（N是limit, 指的是2的整数幂）
        for (int i = 1; i < limit / 2; i ++)swap(A[i], A[limit - i]);
        for(int i = 0; i < limit; ++ i)
            A[i] = (A[i] * limit_inv) % p;//NTT还是要除以n的，但是这里把除换成逆元了，inv就是n在模p意义下的逆元
    }
}//代码实现上和FFT相差无几
//多项式乘法
void poly_mul(ll *a, ll *b, int deg)
{
    for(limit = 1, L = 0; limit <= deg; limit <<= 1) L ++ ;
    for(int i = 0; i < limit; ++ i) {
        RR[i] = (RR[i >> 1] >> 1) | ((i & 1) << (L - 1));
    }
    NTT(a, 1);
    NTT(b, 1);
    for(int i = 0; i < limit; ++ i) a[i] = a[i] * b[i] % p;
    NTT(a, -1);
}
```



#### vector形式

```c++

namespace Poly
{
    typedef vector<int> poly;
    const int G = 3;
    const int mod = 998244353;
    const int inv_G = qpow(G, mod - 2);
    int RR[N], deer[2][22][N], inv[N];

    void init(const int t) {//预处理出来NTT里需要的w和wn
        for(int p = 1; p <= t; ++ p) {
            int buf1 = qpow(G, (mod - 1) / (1 << p));
            int buf0 = qpow(inv_G, (mod - 1) / (1 << p));
            deer[0][p][0] = deer[1][p][0] = 1;
            for(int i = 1; i < (1 << p); ++ i) {
                deer[0][p][i] = 1ll * deer[0][p][i - 1] * buf0 % mod;//逆
                deer[1][p][i] = 1ll * deer[1][p][i - 1] * buf1 % mod;
            }
        }
        inv[1] = 1;
        for(int i = 2; i <= (1 << t); ++ i)
            inv[i] = 1ll * inv[mod % i] * (mod - mod / i) % mod;
    }

    int NTT_init(int n) {
        int limit = 1, L = 0;
        while(limit < n) limit <<= 1, L ++ ;
        for(int i = 0; i < limit; ++ i)
            RR[i] = (RR[i >> 1] >> 1) | ((i & 1) << (L - 1));
        return limit;
    }

    #define ck(x) (x >= mod ? x - mod : x)

    void NTT(poly &A, int type, int limit) {
        A.resize(limit);
        for(int i = 0; i < limit; ++ i)
            if(i < RR[i])
                swap(A[i], A[RR[i]]);
        for(int mid = 2, j = 1; mid <= limit; mid <<= 1, ++ j) {
            int len = mid >> 1;
            for(int pos = 0; pos < limit; pos += mid) {
                int *wn = deer[type][j];
                for(int i = pos; i < pos + len; ++ i, ++ wn) {
                    int tmp = 1ll * (*wn) * A[i + len] % mod;
                    A[i + len] = ck(A[i] - tmp + mod);
                    A[i] = ck(A[i] + tmp);
                }
            }
        }
        if(type == 0) {
            int inv_limit = qpow(limit, mod - 2);
            for(int i = 0; i < limit; ++ i)
                A[i] = 1ll * A[i] * inv_limit % mod;
        }
    }

    poly poly_mul(poly A, poly B) {
        int deg = A.size() + B.size() - 1;
        int limit = NTT_init(deg);
        poly C(limit);
        NTT(A, 1, limit);
        NTT(B, 1, limit);
        for(int i = 0; i < limit; ++ i)
            C[i] = 1ll * A[i] * B[i] % mod;
        NTT(C, 0, limit);
        C.resize(deg);
        return C;
    }
    
    poly poly_mul(poly A, poly B, int deg) {//多项式乘法
        int limit = NTT_init(deg);
        poly C(limit);
        NTT(A, 1, limit);
        NTT(B, 1, limit);
        for(int i = 0; i < limit; ++ i)
            C[i] = 1ll * A[i] * B[i] % mod;
        NTT(C, 0, limit);
        C.resize(deg);
        return C;
    }
    
}

using Poly::poly;
using Poly::poly_mul;

init(21);
f = poly_mul(f, g);
```

