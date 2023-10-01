```c++
ll sqrtl(ll x)
{
    ll y = sqrt(x);
    while(y * y >= x) y--;
    while(y * y < x) y++;
    return y
}
```

