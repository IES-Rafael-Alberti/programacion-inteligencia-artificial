# Chuleta: Contenedores C++ STL

## vector<T>

```cpp
#include <vector>

std::vector<T> v;

// Construcción
std::vector<int> v;              // vacío
std::vector<int> v(5);           // 5 elementos (0)
std::vector<int> v(5, 10);      // 5 elementos con valor 10
std::vector<int> v = {1, 2, 3};  // inicializado

// Acceso
v[i]                // sin проверка
v.at(i)             // с проверкой bounds
v.front()           // primer elemento
v.back()            // último elemento
v.data()           // puntero al array interno

// Modificadores
v.push_back(x);     // añadir al final
v.pop_back();      // quitar último
v.insert(it, x);   // insertar en posición
v.erase(it);      // borrar en posición
v.clear();        // vaciar todo
v.resize(n);      // cambiar tamaño
v.resize(n, val); // cambiar tamaño con valor
v.reserve(n);    // reservar capacidad
v.shrink_to_fit();// reducir capacidad

// Tamaño
v.size();         // número de elementos
v.empty();        // está vacío?
v.capacity();     // capacidad actual

// Iteradores
v.begin(); v.end();
v.rbegin(); v.rend();

// Algoritmos
std::sort(v.begin(), v.end());
std::find(v.begin(), v.end(), x);
std::reverse(v.begin(), v.end());
```

---

## unordered_map<T, U>

```cpp
#include <unordered_map>

std::unordered_map<std::string, int> mp;

// Acceso
mp["clave"] = valor;      // insertar/actualizar
mp.at("clave");          // obtener (si existe)
mp["clave"];            // obtener (crea si no existe)

// Busca
mp.find("clave") != mp.end()  // existe?
mp.count("clave");            // 0 o 1
mp.contains("clave");        // existe? (C++20)

// Modificadores
mp.insert({"clave", valor});
mp.insert(std::make_pair("clave", valor));
mp.emplace("clave", valor);    // konstruir in-place
mp.erase("clave");            // borrar
mp.clear();                // vaciar

// Tamaño
mp.size();
mp.empty();

// Iteradores
for (auto& [k, v] : mp) { }  // C++17

// Rapidez
// O(1) promedio para busca, insert, erase
// No ordenado

```

---

## map<T, U> (ordenado)

```cpp
#include <map>

std::map<std::string, int> mp;

// Mismos métodos que unordered_map
// + Ordered by key

// Métodos adicionales
mp.lower_bound(key);  // primer >= key
mp.upper_bound(key);  // primer > key
mp.equal_range(key); // par de iteradores

// O(log n) para operaciones
```

---

## set<T>

```cpp
#include <set>

std::set<int> s;

s.insert(x);         // insertar
s.erase(x);          // borrar
s.find(x);           // buscar
s.count(x);          // 0 o 1
s.contains(x);      // existe? (C++20)

// Iteradores
for (auto it = s.begin(); it != s.end(); ++it)

// size, empty, clear
```

---

## deque<T>

```cpp
#include <deque>

std::deque<int> dq;

dq.push_front(x);   // añadir al inicio
dq.push_back(x);    // añadir al final
dq.pop_front();     // quitar del inicio
dq.pop_back();     // quitar del final
dq[i]; dq.at(i);   // acceso aleatorio
```

---

## list<T> (lista doblemente enlazada)

```cpp
#include <list>

std::list<int> lst;

lst.push_front(x);
lst.push_back(x);
lst.pop_front();
lst.pop_back();
lst.insert(it, x);
lst.erase(it);
lst.remove(x);           //borra todos los x
lst.unique();            //borra duplicados adyacentes
lst.sort();
lst.mergeotro lst);

//双向迭代器
lst.begin(); lst.end();
lst.rbegin(); lst.rend();
```

---

## stack<T>

```cpp
#include <stack>

std::stack<int> st;
st.push(x);     // poner
st.top();       // ver cima
st.pop();       // quitar (no retorna)
st.empty();
st.size();
```

---

## queue<T>

```cpp
#include <queue>

std::queue<int> q;
q.push(x);      // encolar
q.front();      // ver frente
q.back();       // ver atrás
q.pop();        // desencolar
q.empty();
q.size();
```

---

## priority_queue<T>

```cpp
#include <queue>

std::priority_queue<int> pq;     // max-heap por defecto
std::priority_queue<int, std::vector<int>, std::greater<int>> pq; // min-heap

pq.push(x);
pq.top();
pq.pop();
```

---

## pair<T, U>

```cpp
#include <utility>

std::pair<int, std::string> p = {1, "hola"};
p.first;
p.second;

// Funciones de utilidad
std::make_pair(1, "hola");
std::tie(a, std::ignore) = p;  // descompresión
```

---

## array<T, N>

```cpp
#include <array>

std::array<int, 4> arr = {1, 2, 3, 4};
arr.size();
arr.fill(x);
arr.begin(); arr.end();
arr[i]; arr.at(i);