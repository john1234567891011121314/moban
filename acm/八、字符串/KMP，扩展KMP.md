## KMP，扩展KMP
```c++
void get_nxt(string &s) // 从1开始
{
    int n = s.size();
    nxt[1] = 0;
    for(int i = 2, j = 0; i < n; ++i)
    {
        while(j > 0 && s[i] != s[j + 1]) j = nxt[j];
        if(s[i] == s[j + 1]) j++;
        nxt[i] = j;
    }
}
```

```c++
void get_f(string &s, string &t)
{
    int m = t.size();
    int n = s.size();
    for(int i = 1, j =0; i < m; ++i)
    {
        while(j > 0 && (j == n - 1 || t[i] != s[j + 1])) j = nxt[j];
        if(t[i] == s[j + 1]) j++;
        f[i] = j;
    
    }
}
```

### border理论

我们定义一个字符串$s$的$border$为，当一个子串既是这个字符串的前缀，又是这个字符串的后缀，那么这个子串就是$border$

#### 定理1

如果有一个$border$ $k$的长度超过字符串$s$的一半，那么$s$有一个周期$|s| - |k|$

 ![0](./汇总.assets/1-1749092190903-1.png)

如图所示，红线表示$border$，这时有一部分重合，那么重合部分，是$k$的一个$border$，因此有$s[1 - (|s| - |k|)] = s[(|s| - |k| +  1)  - 2 * (|s| - |k|)]$，于是我们可以得到这个周期是$|s|-|k|$​，当然也可以选择末尾的字符，论述方式一样。

#### 推论1

如果字符串$s$有一个周期$T$，那么必然存在一个$border$，长度为$|s|-|T|$

根据$border$的定义，显然可得

这里的周期指的是$s[i+T]=s[i],i+T<=|s|$​

#### 推论2

字符串$s$的最小正周期为$|s|-|v|$，其中$v$表示$s$的最大$border$

#### 定理2

如果$p,q$是周期，那么$\gcd(p,q)$​也是周期

较为显然，不证

#### 定理3

字符串$s$所有长度不小于$|s|$一半的$border$构成一个等差数列

设$u$是字符串最大的$border$，另一个不小于一半的$border$为$v$

由定理12可知，$\gcd(|s|-|v|, |s| - |u|)$是一个周期，因此有$gcd(|s|-|v|, |s|-|u|) \leq |s| - |v|$，易知等号恒成立，可以推出$|s|-|u|$是$|s|-|v|$的倍数，因此长度构成等差数列

#### 定理4

对于字符串 $u,v$,如果 $|u|=|v|=n$，我们则定义 $PS(u,v)=\{k|Pre(u,k)=Suf(v,k)\}$。

此外的定义是 $LargePS(u,v)=\{k|Pre(u,k)=Suf(v,k),⌈\frac{n}{2}⌉≤k≤n\}$。

那么有：$LargePS(u,v)$ 中的元素可以构成一个等差数列。



不妨假设 $|LargePS(u,v)|>2$|，取出 $p=maxLargePS(u,v)$。

此时对于任意的 $x∈LargePS(u,v)∖ \{p \}$，都有 $Pre(p,x) = pre(u, x) = suf(v, x) = suf(p, x)$，于是有$pre(p, x) \in border(p)$

因此，我们可以得到 $LargePS(u,v)=\{|p|\} ∪ \{|b|~|b∈Border(p),|b|≥⌈\frac{n}{2}⌉\}$。由于 $⌈\frac{p}{2}⌉≤⌈\frac{n}{2}⌉$，我们即可结合引理之一得到证明。



接下来我们可以开始构造，以下有两种构造思路

- 递归构造

  $largePS(s, s) => large(pre(s, \lfloor{\frac{n}{2}}\rfloor), suf(s, \lfloor\frac{n}{2}\rfloor)) => large(pre(s, \lfloor{\frac{n}{4}}\rfloor), suf(s, \lfloor\frac{n}{4}\rfloor))$

- 长度划分

  划分为$[1, 2) \cup [2, 4) \cup \dots \cup [2^{k - 1}, 2 ^{k}) \cup [2^k, n)$

  对于$[2^k,n)$，有$2^k \geq \lceil\frac{n}{2} \rceil$，显然可以构成

  否则对于$[2^i, 2^{i + 1})$，考虑$LargePS(pre(s, 2^{i + 1} - 1), suf(s, 2 ^ {i + 1} - 1))$由之前证明，也可以构成等差数列



给定字符串，求$p$前缀和$q$前缀的最长公共$border$

本质是在求这两个点在$fail$树上的$lca$，模拟重链剖分的形式即可

```c++
string s; cin >> s;
int n = s.size();
s = "~" + s;
vector<int> nxt(n + 1);
for(int i = 2, j = 0; i <= n; ++i)
{
    while(j > 0 && s[i] != s[j + 1]) j = nxt[j];
    if(s[i] == s[j + 1]) j++;
    nxt[i] = j;
}
int q; cin >> q;
while(q--)
{
    int x, y; cin >> x >> y;
    x = nxt[x], y = nxt[y];
    while(x && y && x != y)
    {
        if(x < y) swap(x, y);
        if(nxt[x] > (x / 2))
        {
            int d = x - nxt[x];
            if(x % d == y % d) break;
            x = nxt[x % d + d];
        }
        else x = nxt[x];
    }
    cout << min(x, y) << '\n';
}
```

### 在线维护border集合

```c++
for(int i = 2, j = 0; i <= n; ++i)
{
    cin >> s[i] >> a[i] >> b[i];
    s[i] = (s[i] + las) % n;
    while(j > 0 && s[i] != s[j + 1]) j = nxt[j];
    if(s[i] == s[j + 1]) j++;
    nxt[i] = j;

    if(s[i] == s[nxt[i - 1] + 1]) anc[i - 1] = anc[nxt[i - 1]];
    else anc[i - 1] = nxt[i - 1];

    for(int k = i - 1; k; )//此时的border集合，sum记录
    {
        if(s[k + 1] == s[i])
        {
            k = anc[k];
        }
        else 
        {
            sum -= b[i - k];//sum记录
            k = nxt[k];
        }
    }
    if(s[i] == s[1]) 
    {
        sum += b[i];//sum记录
    }
    las += sum * a[i];
    cout << las << '\n';
}
```

```c++
for(int i = 2, j = 0; i <= n; ++i)
{
    cin >> s[i] >> a[i] >> b[i];
    s[i] = (s[i] + las) % n;
    while(j > 0 && s[i] != s[j + 1]) 
    {
        sum -= b[i - j];//sum记录
        e[i].push_back(j);
        j = nxt[j];
    }
    
    if(s[i] == s[j + 1]) j++;
    nxt[i] = j;
    
    
    for(auto x : e[nxt[i]]) 
    {
        sum -= b[i - x];//sum记录
        e[i].push_back(x);
    }
    if(s[i] == s[1]) 
    {
        sum += b[i];//sum记录
    }
    las += sum * a[i];
    cout << las << '\n';
}
```



### 前缀函数

 $\pi[i]$最长$s$的真前缀和真后缀$(最后一位是s[i])$匹配的长度
$$
\pi[0]=0;
\pi[i]=\max_{k = 0\cdots i}\{ s[0\cdots k - 1]=s[i - (k - 1) \cdots i]  \}
$$


```c++
vector<int> prefix_function(string s) {
  int n = (int)s.length();
  vector<int> pi(n, 0);
  for (int i = 1; i < n; i++) {
    int j = pi[i - 1];
    while (j > 0 && s[i] != s[j]) j = pi[j - 1];
    if (s[i] == s[j]) j++;
    pi[i] = j;
  }
  return pi;
}
```

### 查找$s$在$t$中的所有出现

```c++
vector<int> find_occurrences(string text, string pattern) {
  string cur = pattern + '#' + text;
  int sz1 = text.size(), sz2 = pattern.size();
  vector<int> v;
  vector<int> lps = prefix_function(cur);
  for (int i = sz2 + 1; i <= sz1 + sz2; i++) {
    if (lps[i] == sz2)
      v.push_back(i - 2 * sz2);
  }
  return v;
}
```

### 自动机

让我们重新回到通过一个分隔符将两个字符串拼接的新字符串。对于字符串 $s$ 和 $t$我们计算 $s + \# + t$的前缀函数。显然，因为 $\#$是一个分隔符，前缀函数值永远不会超过 $|s|$。因此我们只需要存储字符串 $s + \#$ 和其对应的前缀函数值，之后就可以动态计算对于之后所有字符的前缀函数值：

$ \underbrace{s_0 ~ s_1 ~ \dots ~ s_{n-1} ~ \#}_{\text{need to store}} ~ \underbrace{t_0 ~ t_1 ~ \dots ~ t_{m-1}}_{\text{do not need to store}} $

实际上在这种情况下，知道 $t$ 的下一个字符 $c$以及之前位置的前缀函数值便足以计算下一个位置的前缀函数值，而不需要用到任何其它 ![t](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符和对应的前缀函数值。

换句话说，我们可以构造一个 **自动机**（一个有限状态机）：其状态为当前的前缀函数值，而从一个状态到另一个状态的转移则由下一个字符确定。

因此，即使没有字符串 $t$，我们同样可以应用构造转移表的算法构造一个转移表 $( \text { old } \pi , c ) \rightarrow \text { new } _ { - } \pi$：

该自动机在什么时候有用呢？首先，记得大部分时候我们为了一个目的使用字符串 $s + \# + t$的前缀函数：寻找字符串$s$在字符串 $t$中的所有出现。

因此使用该自动机的最直接的好处是 **加速计算字符串 $s + \# + t$ 的前缀函数**。

通过构建 $s + \#$ 的自动机，我们不再需要存储字符串 $s$ 以及其对应的前缀函数值。所有转移已经在表中计算过了。

但除此以外，还有第二个不那么直接的应用。我们可以在字符串 $t$ 是 **某些通过一些规则构造的巨型字符串** 时，使用该自动机加速计算。Gray 字符串，或者一个由一些短的输入串的递归组合所构造的字符串都是这种例子。

出于完整性考虑，我们来解决这样一个问题：给定一个数 $k \le 10^5$，以及一个长度 $\le 10^5$ 的字符串 $s$，我们需要计算 $s$ 在第 $k$ 个 Gray 字符串中的出现次数。回想起 Gray 字符串以下述方式定义：

$\begin{aligned} g_1 &= \mathtt{a}\\ g_2 &= \mathtt{aba}\\ g_3 &= \mathtt{abacaba}\\ g_4 &= \mathtt{abacabadabacaba} \end{aligned}$

由于其天文数字般的长度，在这种情况下即使构造字符串 $t$ 都是不可能的：第 $k$ 个 Gray 字符串有 $2^k - 1$ 个字符。然而我们可以在仅仅知道开头若干前缀函数值的情况下，有效计算该字符串末尾的前缀函数值。

除了自动机之外，我们同时需要计算值 $G[i][j]$：在从状态 $j$ 开始处理 $g_i$ 后的自动机的状态，以及值 $K[i][j]$：当从状态 $j$ 开始处理 $g_i$ 后，$s$ 在 $g_i$ 中的出现次数。实际上 $K[i][j]$ 为在执行操作时前缀函数取值为 $|s|$ 的次数。易得问题的答案为 $K[k][0]$。

我们该如何计算这些值呢？首先根据定义，初始条件为 $G[0][j] = j$ 以及 $K[0][j] = 0$。之后所有值可以通过先前的值以及使用自动机计算得到。为了对某个 $i$ 计算相应值，回想起字符串 $g_i$ 由 $g_{i - 1}$，字母表中第 $i$个字符，以及 $g_{i - 1}$ 三者拼接而成。因此自动机会途径下列状态：

$\begin{gathered} \text{mid} = \text{aut}[G[i - 1][j]][i] \\ G[i][j] = G[i - 1][\text{mid}] \end{gathered} $

$K[i][j]$ 的值同样可被简单计算。

$K[i][j] = K[i - 1][j] + [\text{mid} == |s|] + K[i - 1][\text{mid}] $

其中 $[\cdot]$ 当其中表达式取值为真时值为 $1$，否则为 $0$。综上，我们已经可以解决关于 Gray 字符串的问题，以及一大类与之类似的问题。举例来说，应用同样的方法可以解决下列问题：给定一个字符串 $s$以及一些模式 $t_i$，其中每个模式以下列方式给出：该模式由普通字符组成，当中可能以 $t_{k}^{\text{cnt}}$的形式递归插入先前的字符串，也即在该位置我们必须插入字符串 $t_k^{cnt}$ 次。以下是这些模式的一个例子：

$\begin{aligned} t_1 &= \mathtt{abdeca} \\ t_2 &= \mathtt{abc} + t_1^{30} + \mathtt{abd} \\ t_3 &= t_2^{50} + t_1^{100} \\ t_4 &= t_2^{10} + t_3^{100} \end{aligned} $

递归代入会使字符串长度爆炸式增长，他们的长度甚至可以达到 $100^{100}$ 的数量级。而我们必须找到字符串 $s$ 在每个字符串中的出现次数。

该问题同样可通过构造前缀函数的自动机解决。同之前一样，我们利用先前计算过的结果对每个模式计算其转移然后相应统计答案即可。

```c++
void compute_automaton(string s, vector<vector<int>>& aut) {
  s += '#';
  int n = s.size();
  vector<int> pi = prefix_function(s);
  aut.assign(n, vector<int>(26));
  for (int i = 0; i < n; i++) {
    for (int c = 0; c < 26; c++) {
      if (i > 0 && 'a' + c != s[i])
        aut[i][c] = aut[pi[i - 1]][c];
      else
        aut[i][c] = i + ('a' + c == s[i]);
    }
  }
}
```

### z函数

$z[i]$表示$s$和$s[i,n-1]$的最长公共前缀

```c++
vector<int> z_function(string s) {
  int n = (int)s.length();
  vector<int> z(n,0);
  for (int i = 1, l = 0, r = 0; i < n; ++i) {
    if (i <= r && z[i - l] < r - i + 1) {
      z[i] = z[i - l];
    } else {
      z[i] = max(0, r - i + 1);
      while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
    }
    if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
  }
  return z;
}
```

