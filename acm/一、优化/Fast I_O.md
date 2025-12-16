## Fast I/O
```c++
namespace FastIOT
{
    const int bsz = 1 << 18;
    char bf[bsz], *head, *tail;
    char gc()
    {
        if (head == tail) tail = (head = bf) + fread(bf, 1, bsz, stdin);
        if (head == tail) return 0;
        return *head++;
    }
    template <typename T>
    void read(T& x)
    {
        T f = 1;
        x = 0;
        char c = gc();
        for (; c > '9' || c < '0'; c = gc())
            if (c == '-') f = -1;
        for (; c <= '9' && c >= '0'; c = gc())
            x = (x << 3) + (x << 1) + (c ^ 48);
        x *= f;
    }
    template <typename T>
    void print(T x)
    {
        if (x < 0) putchar(45), x = -x;
        if (x > 9) print(x / 10);
        putchar(x % 10 + 48);
    }
    template <typename T>
    void println(T x)
    {
        print(x);
        putchar('\n');
    }
}  // namespace FastIOT
using namespace FastIOT;
```

```c++
struct IO {
    char a[1 << 25], b[1 << 25], *s, *t;
    IO() : s(a), t(b) {
        a[std::fread(a, 1, sizeof a, stdin)] = 0;
    }
    ~IO() {
        std::fwrite(b, 1, t - b, stdout);
    }
    IO &operator>>(std::uint64_t &x);
    IO &operator>>(std::int64_t &x);
    IO &operator>>(std::int32_t &x);
    IO &operator>>(std::uint32_t &x) {
        x = 0;
 
        while (*s < '0' || *s > '9')
            ++s;
 
        while (*s >= '0' && *s <= '9')
            x = x * 10 + *s++ - '0';
 
        return *this;
    }
    IO &operator<<(const char *tmp) {
        return std::fwrite(tmp, 1, std::strlen(tmp), stdout), *this;
    }
    IO &operator<<(char x) {
        return *t++ = x, *this;
    }
    IO &operator<<(std::int32_t x);
    IO &operator<<(std::uint64_t x);
    IO &operator<<(std::int64_t x);
    IO &operator<<(std::uint32_t x) {
        static char c[16], *i;
        i = c;
 
        if (x == 0) {
            *t++ = '0';
        } else {
            while (x != 0) {
                std::uint32_t y = x / 10;
                *i++ = x - y * 10 + '0', x = y;
            }
 
            while (i != c)
                *t++ = *--i;
        }
 
        return *this;
    }
} io;
io >> a
io << a
    
```



