## 树状数组（1-index）
```c++
#include <vector>
#include <cassert>

template <typename T>
class BIT
{
private:
    int n = 0;         // 声明时初始化
    std::vector<T> a;
    int maxStep = 0;    // 声明时初始化

public:
    // 标记为 explicit 防止隐式转换
    explicit BIT(int size = 0) 
        : n(size),       // 初始化列表
          maxStep(0)     // 初始化列表
    { 
        init(size); 
    }

    void init(int _n)
    {
        this->n = _n;
        a.assign(n + 1, T());
        
        // 正确计算最大步长
        maxStep = 1;
        while (maxStep * 2 <= n) 
            maxStep <<= 1;
    }

    void add(int x, T v)
    {
        assert(x > 0 && x <= n);
        while (x <= n)
        {
            a[x] += v;
            x += x & (-x);
        }
    }

    T sum(int x)
    {
        assert(x >= 0 && x <= n);
        auto ans = T();
        while (x)
        {
            ans += a[x];
            x -= x & (-x);
        }
        return ans;
    }

    T rangeSum(int l, int r) 
    { 
        assert(1 <= l && l <= r && r <= n);
        return sum(r) - sum(l - 1); 
    }

    int kth(T k)
    {
        assert(k > T());
        int x = 0;
        for (int step = maxStep; step; step >>= 1)
        {
            if (x + step <= n && k > a[x + step])
            {
                k -= a[x + step];
                x += step;
            }
        }
        return x + 1;
    }
};
```

```c++
template <typename T>
class BIT_2D
{
   private:
    int n = 0;                         // 行数
    int m = 0;                         // 列数
    std::vector<std::vector<T>> data;  // 二维数据存储

   public:
    // 默认构造函数
    BIT_2D() = default;

    // 带参数的显式构造函数
    explicit BIT_2D(int rows, int cols) { init(rows, cols); }

    // 初始化二维树状数组
    void init(int rows, int cols)
    {
        assert(rows > 0 && cols > 0);
        n = rows;
        m = cols;
        // 分配 (n+1) x (m+1) 的矩阵，使用1-indexed
        data.assign(n + 1, std::vector<T>(m + 1, T()));
    }

    // 在位置 (x, y) 添加值 v
    void add(int x, int y, T v)
    {
        assert(1 <= x && x <= n && 1 <= y && y <= m);
        for (int i = x; i <= n; i += i & -i)
        {
            for (int j = y; j <= m; j += j & -j)
            {
                data[i][j] += v;
            }
        }
    }

    // 查询左上角 (1,1) 到 (x,y) 的子矩阵和
    T sum(int x, int y)
    {
        assert(0 <= x && x <= n && 0 <= y && y <= m);
        T res = T();
        for (int i = x; i > 0; i -= i & -i)
        {
            for (int j = y; j > 0; j -= j & -j)
            {
                res += data[i][j];
            }
        }
        return res;
    }

    // 查询子矩阵 [x1, y1] 到 [x2, y2] 的和
    T rangeSum(int x1, int y1, int x2, int y2)
    {
        assert(1 <= x1 && x1 <= x2 && x2 <= n);
        assert(1 <= y1 && y1 <= y2 && y2 <= m);
        return sum(x2, y2) - sum(x1 - 1, y2) - sum(x2, y1 - 1) +
               sum(x1 - 1, y1 - 1);
    }

    // 获取指定位置的值（通过两次差分）
    T get(int x, int y)
    {
        assert(1 <= x && x <= n && 1 <= y && y <= m);
        return rangeSum(x, y, x, y);
    }

    // 设置指定位置的值（先减去旧值，再加上新值）
    void set(int x, int y, T v)
    {
        T current = get(x, y);
        add(x, y, v - current);
    }

    // 打印树状数组内容（调试用）
    void print() const
    {
        std::cout << "2D BIT (" << n << "x" << m << "):\n";
        for (int i = 1; i <= n; ++i)
        {
            for (int j = 1; j <= m; ++j)
            {
                std::cout << data[i][j] << "\t";
            }
            std::cout << "\n";
        }
    }
};
```





