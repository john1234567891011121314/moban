## 2-sat
分为几种情况考虑

### 若$x_i = a$，则$x_j = b$

建边 $(x_{i, a}, x_{j, b}), (x_{j, b \oplus 1}, x_{i, a \oplus 1})$​

$addClause(x_i, a, x_j, b)$

### $x_i=a$ 与 $x_j=b$​ 至少满足一个

建边$(x_{i, a\oplus 1},x_{{j,b}}), (x_{j, b\oplus 1}, x_{i, a})$​

$addClause(x_i, a \oplus 1, x_j, b)$

### 一定满足$x_i=a$

建边$(x_{i,a \oplus 1}, x_{i, a})$​

$addClause(x_i, a \oplus 1, x_i, a)$

### code

```c++
// 1~n
struct TwoSat
{
    int n;
    std::vector<std::vector<int>> e;
    std::vector<bool> ans;
    TwoSat(int n) : n(n), e(2 * n + 2), ans(n + 1) {}
    void addClause(int u, bool f, int v, bool g)
    {
        e[2 * u + f].push_back(2 * v + g);
        e[2 * v + !g].push_back(2 * u + !f);
    }
    bool satisfiable()
    {
        std::vector<int> id(2 * n + 2, -1), dfn(2 * n + 2, -1),
            low(2 * n + 2, -1);
        std::vector<int> stk;
        int now = 0, cnt = 0;
        std::function<void(int)> tarjan = [&](int u)
        {
            stk.push_back(u);
            dfn[u] = low[u] = ++now;
            for (auto v : e[u])
            {
                if (dfn[v] == -1)
                {
                    tarjan(v);
                    low[u] = std::min(low[u], low[v]);
                }
                else if (id[v] == -1)
                {
                    low[u] = std::min(low[u], dfn[v]);
                }
            }
            if (dfn[u] == low[u])
            {
                int v;
                ++cnt;
                do
                {
                    v = stk.back();
                    stk.pop_back();
                    id[v] = cnt;
                } while (v != u);
            }
        };
        for (int i = 1; i <= 2 * n; ++i)
            if (dfn[i] == -1) tarjan(i);
        for (int i = 1; i <= n; ++i)
        {
            if (id[2 * i] == id[2 * i + 1]) return false;
            ans[i] = id[2 * i] > id[2 * i + 1];
        }
        return true;
    }
    std::vector<bool> answer() { return ans; }
};

void solve()
{
    int n, m;
    std::cin >> n >> m;
    TwoSat g(n);
    for (int i = 1; i <= m; ++i)
    {
        int p1, a, p2, b;
        std::cin >> p1 >> a >> p2 >> b;
        g.addClause(p1, a ^ 1, p2, b);
    }
    if (g.satisfiable())
    {
        std::cout << "POSSIBLE\n";
        auto Ans = g.answer();
        for (int i = 1; i <= n; ++i)
            if (Ans[i])
                std::cout << 1 << ' ';
            else
                std::cout << 0 << ' ';
    }
    else
    {
        std::cout << "IMPOSSIBLE\n";
    }
}
```



