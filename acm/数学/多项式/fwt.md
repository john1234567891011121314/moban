## 前置

我们定义 $\times$ 是多项式对应系数相乘，* 作为多项式卷积

 其中 $\bigoplus$是二元位运算符，即 与$(\&)$，或$(|)$，异或$(\wedge)$

我们记对数组 $A$ 进行快速沃尔什变换后得到的结果为$FWT[A]$ 。

那么 FWT 核心思想就是：

我们需要一个新序列$C$，由序列$A$ 和序列$B$经过某运算规则得到，即 $C = A \cdot B$；

我们先正向得到 $FWT[A], FWT[B]]$，再根据 $FWT[C]=FWT[A]  \times FWT[B]$在 $O(n)$ 的时间复杂度内求出 $FWT[C]$；

然后逆向运算得到原序列 $C$。时间复杂度为 $O(n \log n)$

## 用途

用于下标位运算卷积问题

## 或运算

注意到，
$$
i|k=k,j|k=k \Rightarrow (i|j)|k = k
$$
于是构造如下式子
$$
FWT[A](i) = A' = \sum_{i=i|j}A_{j}
$$

### 性质

$$
1. ~~FWT[A+B] = FWT[A] + FWT[B]
$$

$FWT$是$A$序列的一个线性组合
$$
2. ~~ FWT[A] =  \begin{cases}
merge(FWT[A_0] ,FWT[A_0] +FWT[A_1] )~~,~~ n>1 \\
A ~~,~~n =0
\end{cases}
$$
$A_0$是$A$的左半部分，$A_1$是$A$的右半部分。对于$A_0$中的任意下标$i$，都可以在$A_1$中找到在二进制下除最高位以外都相同的下标$j$。

由于最高位不同，右半部分不会对最半部分产生贡献，$FWT[A]_0=FWT[A_0]$

同理可得，$FWT[A]_1=FWT[A_0]+FWT[A_1]$
$$
3. ~~ FWT[A|B] = FWT[A] \times FWT[B]
$$
展开即可证明

### 逆运算

$$
IFWT[A] =  \begin{cases}
merge(IFWT[A_0] ,IFWT[A_1] -IFWT[A_0] )~~,~~ n>1 \\
A ~~,~~n =0
\end{cases}
$$

## 与运算

同或运算

## 异或运算

fwt式子略有不同
$$
FWT[A](i)=\sum_{d(i \& j) ~~mod 2 ~~ \equiv ~~0}A_j-\sum_{d(i \& j) ~~mod 2 ~~ \equiv ~~1}A_j
$$
其中$d(x)$表示$x$在二进制下的1的个数

性质与或运算相同

## Code

### 数组版本

```c++
inline void in() //防止污染原数组
{
    for(int i = 0; i < n; ++ i)
        a[i] = A[i], b[i] = B[i];
}

inline void get()
{
    for(int i = 0; i < n; ++ i)
        a[i] = a[i] * b[i] % mod;
}

inline void out()
{
    for(int i = 0; i < n; ++ i)
        printf("%lld%s", (a[i] % mod + mod) % mod, i == (n - 1) ? "\n" : " ");
}


inline void OR(ll *f, int x = 1)//前半部分 f[i + j], 后半部分 f[i + j + k]
{
    for(int o = 2; o <= n; o <<= 1)
        for(int i = 0, k = o >> 1; i < n; i += o)
            for(int j = 0; j < k; ++ j)
                f[i + j + k] = (f[i + j] * x + f[i + j + k] + (x == 1 ? 0 : mod)) % mod;

}

inline void AND(ll *f, int x = 1)//前半部分 f[i + j],后半部分 f[i + j + k]
{
    for(int o = 2; o <= n; o <<= 1)
        for(int i = 0, k = o >> 1; i < n; i += o)
            for(int j = 0; j < k; ++ j)
                f[i + j] = (f[i + j] + f[i + j + k] * x + (x == 1 ? 0 : mod)) % mod;

}

inline void XOR(ll *f, int x = 1)//前半部分 f[i + j],后半部分 f[i + j + k]
{
    for(int o = 2; o <= n; o <<= 1)
        for(int i = 0, k = o >> 1; i < n; i += o)
            for(int j = 0; j < k; ++ j) {
                int X = f[i + j], Y = f[i + j + k];
                f[i + j] = (X + Y) % mod;
                f[i + j + k] = (X - Y % mod + mod) % mod;
                if(x != 1) {
                    f[i + j] = f[i + j] * inv2 % mod;
                    f[i + j + k] = f[i + j + k] * inv2 % mod;
                }
            }
}

int main()
{
    scanf("%d", &m);
    n = 1 << m;
    for(int i = 0; i < n; ++ i)
        scanf("%lld", &A[i]);
    for(int i = 0; i < n; ++ i)
        scanf("%lld", &B[i]);
    in(), OR(a), OR(b), get(), OR(a, -1), out();
    in(), AND(a), AND(b), get(), AND(a, -1), out();
    in(), XOR(a), XOR(b), get(), XOR(a, -1), out();
    return 0;
}
```



### Vector版本

```c++

struct FWT {
    void add(int &x, int y) {
        (x += y) >= P && (x -= P);
    }
    void sub(int &x, int y) {
        (x -= y) < 0 && (x += P);
    }
    
    int extend(int n) {
        int N = 1;
        for (; N < n; N <<= 1);
        return N;
    }
    void FWTor( vector<int> &a, bool rev) {
        int n = a.size();
        for (int l = 2, m = 1; l <= n; l <<= 1, m <<= 1) {
            for (int j = 0; j < n; j += l) for (int i = 0; i < m; i++) {
                if (!rev) add(a[i + j + m], a[i + j]);
                else sub(a[i + j + m], a[i + j]);
            }
        }
    }
    void FWTand( vector<int> &a, bool rev) {
        int n = a.size();
        for (int l = 2, m = 1; l <= n; l <<= 1, m <<= 1) {
            for (int j = 0; j < n; j += l) for (int i = 0; i < m; i++) {
                if (!rev) add(a[i + j], a[i + j + m]);
                else sub(a[i + j], a[i + j + m]);
            }
        }
    }
    void FWTxor( vector<int> &a, bool rev) {
        int n = a.size(), inv2 = (P + 1) >> 1;
        for (int l = 2, m = 1; l <= n; l <<= 1, m <<= 1) {
            for (int j = 0; j < n; j += l) for (int i = 0; i < m; i++) {
                int x = a[i + j], y = a[i + j + m];
                if (!rev) {
                    a[i + j] = (x + y) % P;
                    a[i + j + m] = (x - y + P) % P;
                } else {
                    a[i + j] = 1LL * (x + y) * inv2 % P;
                    a[i + j + m] = 1LL * (x - y + P) * inv2 % P;
                }
            }
        }
    }
    vector<int> Or(vector<int> a1, vector<int> a2) {
        int n = max(a1.size(), a2.size()), N = extend(n);
        a1.resize(N), FWTor(a1, false);
        a2.resize(N), FWTor(a2, false);
        vector<int> A(N);
        for (int i = 0; i < N; i++) A[i] = 1LL * a1[i] * a2[i] % P;
        FWTor(A, true);
        return A;
    }
    vector<int> And(vector<int> a1, vector<int> a2) {
        int n =  max(a1.size(), a2.size()), N = extend(n);
        a1.resize(N), FWTand(a1, false);
        a2.resize(N), FWTand(a2, false);
        vector<int> A(N);
        for (int i = 0; i < N; i++) A[i] = 1LL * a1[i] * a2[i] % P;
        FWTand(A, true);
        return A;
    }
     vector<int> Xor(vector<int> a1, vector<int> a2) {
        int n = max(a1.size(), a2.size()), N = extend(n);
        a1.resize(N), FWTxor(a1, false);
        a2.resize(N), FWTxor(a2, false);
        vector<int> A(N);
        for (int i = 0; i < N; i++) A[i] = 1LL * a1[i] * a2[i] % P;
        FWTxor(A, true);
        return A;
    }
} fwt;

//main部分
    scanf("%d", &m);
    n = 1 << m;
    vector<int> a1(n), a2(n);
    for (int i = 0; i < n; i++) scanf("%d", &a1[i]);
    for (int i = 0; i < n; i++) scanf("%d", &a2[i]);
    vector<int> A;
    A = fwt.Or(a1, a2);
    for (int i = 0; i < n; i++) {
        printf("%d%c", A[i], " \n"[i == n - 1]);
    }
    A = fwt.And(a1, a2);
    for (int i = 0; i < n; i++) {
        printf("%d%c", A[i], " \n"[i == n - 1]);
    }
    A = fwt.Xor(a1, a2);
    for (int i = 0; i < n; i++) {
        printf("%d%c", A[i], " \n"[i == n - 1]);
    }
```

