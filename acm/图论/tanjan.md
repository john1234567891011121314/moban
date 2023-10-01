# 有向图

将任意有向图转化为强连通，需要$\max(p,q)$条有向边，其中$p$和$q$表示零入度点和零出度点的个数

注意重边

```c++
//有向图tanjan
namespace tanjan
{
	vector<int>G[N];
	int st[N], ins[N], c[N];	//ins表示已经找到的点中不在环上的点，标记为1 
	int dfn[N], low[N];
	vector<int>scc[N];
	int ind = 0, top = 0, cnt = 0;
	void add(int x, int y){G[x].push_back(y);}
	void tanjan(int x)
	{
		dfn[x] = low[x] = ++ind;
		st[++top] = x, ins[x] = 1;
		for(auto y:G[x])
		{
			if(!dfn[y])
			{
				tanjan(y);
				low[x] = min(low[x], low[y]);
			}
			else if(ins[y])
			{
				low[x] = min(low[x], dfn[y]);
			}
		}
		if(low[x] == dfn[x])
		{
			cnt++;
			int y;
			do{
				y = st[top--]; ins[y] = 0;
				c[y] = cnt; scc[cnt].push_back(y);
			}while(x != y);
		}
	}
	
	void solve(int n)
	{
		for(int i = 1; i <= n; ++i)
		{
			if(!dfn[i]) tanjan(i);
		}
	} 
	
	vector<int>G_c[N];
	void add_c(int x, int y){ G_c[x].push_back(y);}
	
	void get(int n)	//缩点
	{
		for(int x = 1; x <= n; ++x)
		{
			for(auto y:G[x])
			{
				if(c[x] == c[y])continue;
				add_c(c[x],c[y]);
			}
		}
	 } 
} 
using tanjan::add;
void solve()
{
	int n,m;cin>>n>>m;
	for(int i=1;i<=m;++i)
	{
		int x,y;cin>>x>>y;
		add(x,y); 
	}
	tanjan::solve(n);
}
```

## 无向图

### 求割边 / 桥， 边双

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

### 求割点 ， 点双

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

