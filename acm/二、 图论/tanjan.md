## tanjan
### 有向图

将任意有向图转化为强连通，需要$\max(p,q)$条有向边，其中$p$和$q$表示零入度点和零出度点的个数

注意重边

```c++
// 1~n
// 1~n
struct SCC
{
    int n;
    std::vector<std::vector<int>> adj;
    std::vector<std::vector<int>> scc;
    std::vector<int> stk;
    std::vector<int> dfn, low, bel;
    int cur, cnt;

    SCC() {}
    SCC(int n) { init(n); }

    void init(int n)
    {
        this->n = n;
        n++;
        adj.assign(n, {});
        dfn.assign(n, -1);
        low.resize(n);
        bel.assign(n, -1);
        stk.clear();
        cur = cnt = 0;
    }

    void addEdge(int u, int v) { adj[u].push_back(v); }

    void dfs(int x)
    {
        dfn[x] = low[x] = ++cur;
        stk.push_back(x);
        for (auto y : adj[x])
        {
            if (dfn[y] == -1)
            {
                dfs(y);
                low[x] = std::min(low[x], low[y]);
            }
            else if (bel[y] == -1)
            {
                low[x] = std::min(low[x], dfn[y]);
            }
        }
        if (dfn[x] == low[x])
        {
            cnt++;
            int y;
            std::vector<int> tmp;
            do
            {
                y = stk.back();
                bel[y] = cnt;
                stk.pop_back();
                tmp.push_back(y);
            } while (y != x);
            scc.push_back(tmp);
        }
    }

    std::vector<int> work()
    {
        for (int i = 1; i <= n; i++)
        {
            if (dfn[i] == -1)
            {
                dfs(i);
            }
        }
        return bel;
    }

    
};
void solve()
{
	int n, m;
    std::cin >> n >> m;
    SCC g(n);
    std::vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i)
        std::cin >> a[i];
    for (int i = 1; i <= m; ++i)
    {
        int u, v;
        std::cin >> u >> v;
        g.addEdge(u, v);
    }
    auto bel = g.work();
    std::vector<std::vector<int>> G(g.cnt + 1);
    for (int x = 1; x <= n; ++x)
    {
        for (auto y : g.adj[x])
        {
            if (bel[x] == bel[y]) continue;
            G[bel[x]].push_back(bel[y]);
        }
    }
}
```

### 无向图

#### 求割边 / 桥， 边双

```c++
int n, m;
struct ECC
{
	vector<pair<int,int>>e[N];
	int dfn[N], low[N];
	int num;

	vector<vector<int>>ecc;

	int st[N], top;

	void add(int x, int y, int id)
	{
		e[x].emplace_back(y, id << 1);
		e[y].emplace_back(x, id << 1 | 1);
	}
	void tarjan(int x, int in_edge)
	{
		dfn[x] = low[x] = ++num;
		st[++top] = x;
		for(auto [y, i]:e[x])
		{
			if(i == (in_edge ^ 1)) continue;
			if(!dfn[y])
			{
				tarjan(y, i);
				low[x] = min(low[x], low[y]);
			}
			else 
			{
				low[x] = min(low[x], dfn[y]); 
			}
		}
		if(dfn[x] == low[x])
		{
			vector<int>vec;
			do{
				vec.emplace_back(st[top]);
			}while(st[top--] != x);
	
			ecc.emplace_back(vec);
		}
	}

	void solve()
	{
		for(int i = 1; i <= n; ++i)
		{
			if(!dfn[i]) tarjan(i, -1);
		}
		cout << ecc.size() << '\n'; //边双个数
		for(auto vec:ecc)
		{
			cout << vec.size() << ' ';//某一个边双大小
			for(auto x:vec)
			{
				cout << x << ' '; //边双内的点
			}
			cout << '\n';
		}
	}
} e_dcc;



void solve(int cas)
{
	cin >> n >> m;
	for(int i = 1; i <= m; ++i)
	{
		int x, y;
		cin >> x >> y;
		e_dcc.add(x, y, i);
	}	
	
	e_dcc.solve();
} 
```

#### 求割点 ， 点双

```c++
 //割边，桥
int n, m;
struct VCC
{
	vector<int>e[N];
	int dfn[N], low[N];
	int num;

	vector<vector<int>>vcc;

	int st[N], top;

	void add(int x, int y)
	{
		e[x].emplace_back(y);
		e[y].emplace_back(x);
	}
	void tarjan(int x, int fa)
	{
		int son = 0;
		dfn[x] = low[x] = ++num;
		st[++top] = x;
		for(auto y:e[x])
		{
			if(!dfn[y])
			{
				son++;
				tarjan(y, x);
				low[x] = min(low[x], low[y]);
				if(low[y] >= dfn[x])
				{
					vector<int> vec;
					while(st[top + 1] != y)
						vec.emplace_back(st[top--]);
					vec.emplace_back(x);
					vcc.emplace_back(vec);
				}
			}
			else  if(y != fa)
			{
				low[x] = min(low[x], dfn[y]); 
			}
		}
		if(fa == 0 && son == 0) vcc.emplace_back(vector<int>(1, x));
	}

	void solve()
	{
		for(int i = 1; i <= n; ++i)
		{
			if(!dfn[i]) tarjan(i, 0);
		}
		cout << vcc.size() << '\n'; //点双个数
		for(auto vec:vcc)
		{
			cout << vec.size() << ' ';//某一个点双大小
			for(auto x:vec)
			{
				cout << x << ' '; //点双内的点
			}
			cout << '\n';
		}
	}
} v_dcc;



void solve(int cas)
{
	cin >> n >> m;
	for(int i = 1; i <= m; ++i)
	{
		int x, y;
		cin >> x >> y;
		v_dcc.add(x, y);
	}	
	
	v_dcc.solve();

	

} 
```

