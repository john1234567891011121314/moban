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

