## 蒙哥马利约减

# 看不懂

通常我们计算$xy \mod n$，我们需要$x*y-\lfloor \frac{x*y}{n} \rfloor  $

蒙哥马利模乘约减的思路是通过变换，将需要取模的数控制到很小的范围，最需要最多一次减法完成取模运算。通过选择除数为2的幂次，从而通过移位加快速度。

在竞赛范围(模数为正奇数)内，我们认为以下式子总会成立
$$
RR' \equiv 1 (\mod N)\\
RR' - NN' = 1\\
RR' - NN' \equiv 1 (\mod R) \\
-NN' \equiv 1 (\mod R) \\
0 < R' <N\\
0 <N'<R
$$
如果我们需要计算约减形式，即对于$T$我们想要求$TR'$
$$
T=T(RR'-NN')=TRR-TNN'\\
TR'=\frac{T+TNN'}{R}
$$
记$m=TN'$
$$
TR' \mod N \\
=\frac{T+mN}{R} \mod N \\
=\frac{T+(\lfloor \frac{T}{R} \rfloor R +(T\mod R))NN'}{R} \mod N \\
=\frac{T+(T\mod R)NN'}{R} +\lfloor \frac{T}{R} \rfloor NN' \mod N \\
=\frac{T+(T\mod R)NN'}{R}  \mod N \\
$$

## 个人想法？

利用$exgcd$求$RR'-NN'=1$中的$R',N'$

约简的话，对于数$x$，计算$m = xN'(\mod R)$

```c++
template <std::uint32_t P>struct MontInt {
	using u32 = std::uint32_t;
	using u64 = std::uint64_t;
	u32 v;
	static constexpr u32 get_r() {
		u32 iv = P;
 
        for (u32 i = 0; i != 4; ++i)
            iv *= 2U - P * iv;
 
        return -iv;
	}
    static constexpr u32 r = get_r(), r2 = -u64(P) % P;//限定词不能省 
    
	MontInt() = default;
    ~MontInt() = default;
    MontInt(u32 v) : v(reduce(u64(v) * r2)) {}
    MontInt(const MontInt &rhs) : v(rhs.v) {}
    
    u32 reduce(u64 x) {
        return x + (u64(u32(x) * r) * P) >> 32;
    }
    
    u32 norm(u32 x) {
        return x - (P & -(x >= P));
    }
    u32 get() {
        u32 res = reduce(v) - P;
        return res + (P & -(res >> 31));
    }
    
    
    MontInt operator-() const {
        MontInt res;
        return res.v = (P << 1 & -(v != 0)) - v, res;
    }
    MontInt inv() const {
        return pow(-1);
    }
    MontInt &operator=(const MontInt &rhs) {
        return v = rhs.v, *this;
    }
    MontInt &operator+=(const MontInt &rhs) {
        return v += rhs.v - (P << 1), v += P << 1 & -(v >> 31), *this;
    }
    MontInt &operator-=(const MontInt &rhs) {
        return v -= rhs.v, v += P << 1 & -(v >> 31), *this;
    }
    MontInt &operator*=(const MontInt &rhs) {
        return v = reduce(u64(v) * rhs.v), *this;
    }
    MontInt &operator/=(const MontInt &rhs) {
        return this->operator*=(rhs.inv());
    }
    friend MontInt operator+(const MontInt &lhs,
                                        const MontInt &rhs) {
        return MontInt(lhs) += rhs;
    }
    friend MontInt operator-(const MontInt &lhs,
                                        const MontInt &rhs) {
        return MontInt(lhs) -= rhs;
    }
    friend MontInt operator*(const MontInt &lhs,
                                        const MontInt &rhs) {
        return MontInt(lhs) *= rhs;
    }
    friend MontInt operator/(const MontInt &lhs,
                                        const MontInt &rhs) {
        return MontInt(lhs) /= rhs;
    }
    friend bool operator==(const MontInt &lhs, const MontInt &rhs) {
        return norm(lhs.v) == norm(rhs.v);
    }
    friend bool operator!=(const MontInt &lhs, const MontInt &rhs) {
        return norm(lhs.v) != norm(rhs.v);
    }
    constexpr MontInt pow(ll y) const {
        if ((y %= P - 1) < 0)
            y += P - 1; // phi(P) = P - 1, assume P is a prime number
 
        MontInt res(1), x(*this);
 
        for (; y != 0; y >>= 1, x *= x)
            if (y & 1)
                res *= x;
 
        return res;
    }
};
auto ans = MontInt<998244353>(i);
cout << ans.inv().get() << '\n';
```



```c++
// Barrett
struct ModInt {
  static unsigned M;
  static unsigned long long NEG_INV_M;
  static void setM(unsigned m) { M = m; NEG_INV_M = -1ULL / M; }
  unsigned x;
  ModInt() : x(0U) {}
  ModInt(unsigned x_) : x(x_ % M) {}
  ModInt(unsigned long long x_) : x(x_ % M) {}
  ModInt(int x_) : x(((x_ %= static_cast<int>(M)) < 0) ? (x_ + static_cast<int>(M)) : x_) {}
  ModInt(long long x_) : x(((x_ %= static_cast<long long>(M)) < 0) ? (x_ + static_cast<long long>(M)) : x_) {}
  ModInt &operator+=(const ModInt &a) { x = ((x += a.x) >= M) ? (x - M) : x; return *this; }
  ModInt &operator-=(const ModInt &a) { x = ((x -= a.x) >= M) ? (x + M) : x; return *this; }
  ModInt &operator*=(const ModInt &a) {
    const unsigned long long y = static_cast<unsigned long long>(x) * a.x;
    const unsigned long long q = static_cast<unsigned long long>((static_cast<unsigned __int128>(NEG_INV_M) * y) >> 64);
    const unsigned long long r = y - M * q;
    x = r - M * (r >= M);
    return *this;
  }
  ModInt &operator/=(const ModInt &a) { return (*this *= a.inv()); }
  ModInt pow(long long e) const {
    if (e < 0) return inv().pow(-e);
    ModInt a = *this, b = 1U; for (; e; e >>= 1) { if (e & 1) b *= a; a *= a; } return b;
  }
  ModInt inv() const {
    unsigned a = M, b = x; int y = 0, z = 1;
    for (; b; ) { const unsigned q = a / b; const unsigned c = a - q * b; a = b; b = c; const int w = y - static_cast<int>(q) * z; y = z; z = w; }
    assert(a == 1U); return ModInt(y);
  }
  ModInt operator+() const { return *this; }
  ModInt operator-() const { ModInt a; a.x = x ? (M - x) : 0U; return a; }
  ModInt operator+(const ModInt &a) const { return (ModInt(*this) += a); }
  ModInt operator-(const ModInt &a) const { return (ModInt(*this) -= a); }
  ModInt operator*(const ModInt &a) const { return (ModInt(*this) *= a); }
  ModInt operator/(const ModInt &a) const { return (ModInt(*this) /= a); }
  template <class T> friend ModInt operator+(T a, const ModInt &b) { return (ModInt(a) += b); }
  template <class T> friend ModInt operator-(T a, const ModInt &b) { return (ModInt(a) -= b); }
  template <class T> friend ModInt operator*(T a, const ModInt &b) { return (ModInt(a) *= b); }
  template <class T> friend ModInt operator/(T a, const ModInt &b) { return (ModInt(a) /= b); }
  explicit operator bool() const { return x; }
  bool operator==(const ModInt &a) const { return (x == a.x); }
  bool operator!=(const ModInt &a) const { return (x != a.x); }
  friend std::ostream &operator<<(std::ostream &os, const ModInt &a) { return os << a.x; }
};
unsigned ModInt::M;
unsigned long long ModInt::NEG_INV_M;
// !!!Use ModInt::setM!!!
////////////////////////////////////////////////////////////////////////////////

using Mint = ModInt;

int main() {
  Mint A, B, X0, Y0, X1, Y1;
  int N, M;
  for (; ~scanf("%u%u%u%u%u%u%d%d", &A.x, &B.x, &X0.x, &Y0.x, &X1.x, &Y1.x, &N, &M); ) {
    Mint::setM(M);
    Mint ans = 0;
    Mint x2 = X0, x1 = X1;
    Mint y2 = Y0, y1 = Y1;
    for (int n = 2; n <= N; ++n) {
      const Mint x = A * x1 + x2 * y1;
      const Mint y = B * y1 + y2 * x1;
      ans += x;
      x2 = x1; x1 = x;
      y2 = y1; y1 = y;
    }
    printf("%u\n", ans.x);
  }
  return 0;
}
```

