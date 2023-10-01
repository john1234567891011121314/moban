# FFT

## 前置知识

### 复数

#### 性质

$$
性质一· ~~~\omega^{2k}_{2n} = \omega^{k}_{n}\\
性质二· ~~~\omega^{k+\frac{n}{2}}_{2n} = - \omega^{k}_{n}
$$



## 用法

多项式乘法，卷积

## 原理

一个n次多项式可以有两种表示方法，点值表示法和系数表示法

在用系数表示法的前提下，即朴素写法，我们需要$\Theta(n^2)$的时间来完成

在点值表示下，可以仅$\Theta(n)$的时间完成

因此我们考虑如何将点值表示与系数表示进行快速转换

不妨记
$$
A(x) = \sum_{i=0}^{n-1}a_ix^i
$$


在这里，我们可以令高次项$a_i=0$从而使n变大

考虑
$$
A(x) = (a_0+a_2 x^2 + \cdots  + a_{n-2}x^{n-2} ) + x(a_1 +a_3 x^2 + \cdots +  a_{n-1}x^{n-1})
$$
令
$$
A1(x) =(a_0+a_2 x + ……  a_{n-2}x^{ \frac{n-2}{2} } )\\
A2(x) = (a_1+a_3 x + ……   a_{n-1}x^{ \frac{n-2}{2}})
$$
于是有
$$
A(X) = A1(x^2) + A2(x^2)
$$
带入单位根$(0\leq k \leq \frac{n}{2} -1 )$得

左半部分
$$
A(\omega^k_n) = A1(\omega^{2k}_n)+\omega^{k}_n*A2(\omega^{k}_\frac{n}{2})\\
=A1(\omega^{k}_\frac{n}{2}) + \omega^{k}_n*A2(\omega^{2k}_n)(折半引理，性质1)\\
$$
右半部分
$$
A(\omega^{k+\frac{n}{2}}_n) = A1(\omega^{2k+n}_n)+\omega^{k+\frac{n}{2}}_n * A2(\omega^{2k+n}_n)
$$
运算得
$$
A(\omega^{k+\frac{n}{2}}_n) = A1(\omega^{k}_{\frac{n}{2}}) - \omega^{k}_n * A2(\omega^{k}_{\frac{n}{2}})
$$
则问题为求$A1(x)与A2(x)$，总体时间复杂度为$T(n) = 2T(\frac{n}{2})+O(n) = O(nlogn)$,即实现了FFT转换

## 代码

```c++
N 应该5倍大小
const db PI=acos(-1);
n = A的最高次数
m = B的最高次数    
Lim = 1， L = 0; 

int R[N];
struct Complex
{
    double x, y;
    Complex (double x = 0, double y = 0) : x(x), y(y) { }
}a[N], b[N];
Complex operator * (Complex J, Complex Q) {
    //模长相乘，幅度相加
    return Complex(J.x * Q.x - J.y * Q.y, J.x * Q.y + 			J.y * Q.x);
}
Complex operator - (Complex J, Complex Q) {
    return Complex(J.x - Q.x, J.y - Q.y);
}
Complex operator + (Complex J, Complex Q) {
    return Complex(J.x + Q.x, J.y + Q.y);
}
//for (int i = 0; i <= Lim; ++ i) {
    //换成二进制序列
    //R[i] = (R[i >> 1] >> 1) | ((i & 1) << (L - 1));
    // 在原序列中 i 与 i/2 的关系是 ： i可以看做是i/2的二进制上的每一位左移一位得来
    // 那么在反转后的数组中就需要右移一位，同时特殊处理一下奇数
//}

inline void FFT(Complex *J, double type)//1 转点值，-1 转系数
{
    for(int i = 0; i < Lim; ++ i) {
        if(i < R[i]) swap(J[i], J[R[i]]);
        //i小于R[i]时才交换，防止同一个元素交换两次，回到它原来的位置。
    }
    //从底层往上合并
    for(int mid = 1; mid < Lim; mid <<= 1) {//待合并区间长度的一半，最开始是两个长度为1的序列合并,mid = 1;
        Complex wn(cos(PI / mid), type * sin(PI / mid));//单位根w_n^i;
        for(int len = mid << 1, pos = 0; pos < Lim; pos += len) {
        //for(int pos = 0; pos < Lim; pos += (mid << 1)) {
            //len是区间的长度，pos是当前的位置,也就是合并到了哪一位
            Complex w(1, 0);//幂,一直乘，得到平方，三次方...
            for(int k = 0; k < mid; ++ k, w = w * wn) {
                //只扫左半部分，得到右半部分的答案,w 为 w_n^k
                Complex x = J[pos + k];//左半部分
                Complex y = w * J[pos + mid + k];//右半部分
                J[pos + k] = x + y;//蝴蝶变换
                J[pos + mid + k] = x - y;
            }
        }
    }
    if(type == 1) return ;
    for(int i = 0; i <= Lim; ++ i)
        a[i].x /= Lim, a[i].y /= Lim;
}
cin>>n>>m;
for(int i=0;i<=n;++i)cin>>a[i].x;
for(int j=0;j<=m;++j)cin>>a[j].y;
while(Lim < n + m) Lim <<= 1, L ++ ;
for (int i = 0; i < Lim; ++ i) {
    //换成二进制序列
    R[i] = (R[i >> 1] >> 1) | ((i & 1) << (L - 1));
}
FFT(a, 1);
for (int i = 0; i <= Lim; ++ i) 
    //对应项相乘，O(n)得到点值表示的多项式的解C，利用逆变换完成插值得到答案C的点值表示
    	a[i] = a[i] * a[i];
FFT(a, -1);
```

