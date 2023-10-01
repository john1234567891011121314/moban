## 解决和点对有关的问题

这类问题多数类似于「给定一个长度为 n 的序列，统计有一些特性的点对 $(i,j)$的数量/找到一对点$ (i,j) $使得一些函数的值最大」。

CDQ 分治解决这类问题的算法流程如下：

1. 找到这个序列的中点 $mid$；
2. 将所有点对$(i,j)$划分为 3 类：
   1. $1\le i,j\le mid$
   2. $mid+1\le i,j\le r$
   3. $1\le i\le mid, mid+1 \le j \le r$
3. 将 $(1,n)$这个序列拆成两个序列 $(1,mid)$和 $(mid+1,n)$。此时第一类点对和第三类点对都在这两个序列之中；
4. 递归地处理这两类点对；
5. 设法处理第二类点对。

## 题目

$$
f_0=1\\
f_i=\sum_{j=1}^{i}f_{i-j}g_j
$$

考虑如何计算左区间对右区间的贡献即可。

```c++
void work(poly &g, int l, int r, int n) 
{
	if(l == r)
	{
		return ;
	}
	int mid = (l + r) >> 1;
	
	work(g, l, mid, n);
	
	poly r1(mid - l + 1, 0), r2(r - l + 1, 0);
	for(int i = l; i <= mid; ++i)
	{
		r1[i - l] = f[i];
	}
	for(int i = 0; i < r - l + 1; ++i)
	{
		r2[i] = g[i];
	}
	poly res = poly_mul(r1, r2);
	for(int i = mid - l + 1; i < min((int)res.size(), r - l + 1); ++i)
	{
		
		f[i + l] += res[i];
		if(f[i + l] > mod) f[i + l] -= mod;
		
	}
	work(g, mid + 1, r, n); 
}
```

传参数的时候注意$g$传引用值，不然会惨遭$TLE$