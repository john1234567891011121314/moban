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
template <std::uint32_t P> struct MontgomeryModInt32 {
public:
    using i32 = std::int32_t;
    using u32 = std::uint32_t;
    using i64 = std::int64_t;
    using u64 = std::uint64_t;
 
private:
    u32 v;
 
    static constexpr u32 get_r() {
        u32 iv = P;
 
        for (u32 i = 0; i != 4; ++i)
            iv *= 2U - P * iv;
 
        return -iv;
    }
 
    static constexpr u32 r = get_r(), r2 = -u64(P) % P;
 
    static_assert((P & 1) == 1);
    static_assert(-r * P == 1);
    static_assert(P < (1 << 30));
 
public:
    static constexpr u32 pow_mod(u32 x, u64 y) {
        if ((y %= P - 1) < 0)
            y += P - 1;
 
        u32 res = 1;
 
        for (; y != 0; y >>= 1, x = u64(x) * x % P)
            if (y & 1)
                res = u64(res) * x % P;
 
        return res;
    }
 
    static constexpr u32 get_pr() {
        u32 tmp[32] = {}, cnt = 0;
        const u64 phi = P - 1;
        u64 m = phi;
 
        for (u64 i = 2; i * i <= m; ++i) {
            if (m % i == 0) {
                tmp[cnt++] = i;
 
                while (m % i == 0)
                    m /= i;
            }
        }
 
        if (m > 1)
            tmp[cnt++] = m;
 
        for (u64 res = 2; res <= phi; ++res) {
            bool flag = true;
 
            for (u32 i = 0; i != cnt && flag; ++i)
                flag &= pow_mod(res, phi / tmp[i]) != 1;
 
            if (flag)
                return res;
        }
 
        return 0;
    }
 
    MontgomeryModInt32() = default;
    ~MontgomeryModInt32() = default;
    constexpr MontgomeryModInt32(u32 v) : v(reduce(u64(v) * r2)) {}
    constexpr MontgomeryModInt32(const MontgomeryModInt32 &rhs) : v(rhs.v) {}
    static constexpr u32 reduce(u64 x) {
        return x + (u64(u32(x) * r) * P) >> 32;
    }
    static constexpr u32 norm(u32 x) {
        return x - (P & -(x >= P));
    }
    constexpr u32 get() const {
        u32 res = reduce(v) - P;
        return res + (P & -(res >> 31));
    }
    explicit constexpr operator u32() const {
        return get();
    }
    explicit constexpr operator i32() const {
        return i32(get());
    }
    constexpr MontgomeryModInt32 &operator=(const MontgomeryModInt32 &rhs) {
        return v = rhs.v, *this;
    }
    constexpr MontgomeryModInt32 operator-() const {
        MontgomeryModInt32 res;
        return res.v = (P << 1 & -(v != 0)) - v, res;
    }
    constexpr MontgomeryModInt32 inv() const {
        return pow(-1);
    }
    constexpr MontgomeryModInt32 &operator+=(const MontgomeryModInt32 &rhs) {
        return v += rhs.v - (P << 1), v += P << 1 & -(v >> 31), *this;
    }
    constexpr MontgomeryModInt32 &operator-=(const MontgomeryModInt32 &rhs) {
        return v -= rhs.v, v += P << 1 & -(v >> 31), *this;
    }
    constexpr MontgomeryModInt32 &operator*=(const MontgomeryModInt32 &rhs) {
        return v = reduce(u64(v) * rhs.v), *this;
    }
    constexpr MontgomeryModInt32 &operator/=(const MontgomeryModInt32 &rhs) {
        return this->operator*=(rhs.inv());
    }
    friend MontgomeryModInt32 operator+(const MontgomeryModInt32 &lhs,
                                        const MontgomeryModInt32 &rhs) {
        return MontgomeryModInt32(lhs) += rhs;
    }
    friend MontgomeryModInt32 operator-(const MontgomeryModInt32 &lhs,
                                        const MontgomeryModInt32 &rhs) {
        return MontgomeryModInt32(lhs) -= rhs;
    }
    friend MontgomeryModInt32 operator*(const MontgomeryModInt32 &lhs,
                                        const MontgomeryModInt32 &rhs) {
        return MontgomeryModInt32(lhs) *= rhs;
    }
    friend MontgomeryModInt32 operator/(const MontgomeryModInt32 &lhs,
                                        const MontgomeryModInt32 &rhs) {
        return MontgomeryModInt32(lhs) /= rhs;
    }
    friend bool operator==(const MontgomeryModInt32 &lhs, const MontgomeryModInt32 &rhs) {
        return norm(lhs.v) == norm(rhs.v);
    }
    friend bool operator!=(const MontgomeryModInt32 &lhs, const MontgomeryModInt32 &rhs) {
        return norm(lhs.v) != norm(rhs.v);
    }
    friend std::istream &operator>>(std::istream &is, MontgomeryModInt32 &rhs) {
        return is >> rhs.v, rhs.v = reduce(u64(rhs.v) * r2), is;
    }
    friend std::ostream &operator<<(std::ostream &os, const MontgomeryModInt32 &rhs) {
        return os << rhs.get();
    }
    constexpr MontgomeryModInt32 pow(i64 y) const {
        if ((y %= P - 1) < 0)
            y += P - 1; // phi(P) = P - 1, assume P is a prime number
 
        MontgomeryModInt32 res(1), x(*this);
 
        for (; y != 0; y >>= 1, x *= x)
            if (y & 1)
                res *= x;
 
        return res;
    }
};
```

