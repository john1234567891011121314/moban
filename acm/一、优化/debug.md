## debug
```c++
void debug(const std::string &file, i32 line, const std::string &name, const auto &value) {
	std::cerr << file << ":" << line << " | " << name << " = " << value << std::endl;
}

template <class T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &v) {
	os << "[ ";
	for (const T &vi : v) {
		os << vi << ", ";
	}
	return os << "]";
}
```

