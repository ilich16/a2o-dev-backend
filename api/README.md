# API Reference

## Getting Started

Base URL: At present this app can only be run locally and is no hosted as a base URL. The backend app is hosted at the default, `http://localhost:8000/`.

## Endpoints

### GET /problem-1

Returns a list of the winners and the missing games.

Example: `curl http://localhost:8000/api/v1/problem-1/?input=Junior%0ABuenisimos%203%20Malisimos%200%0ABuenillos%202%20Malillos%201%0ABuenillos%203%20Malisimos%200%0ABuenisimos%203%20Malillos%200%0ABuenisimos%202%20Buenillos%201%0AMalisimos%200%20Buenisimos%203%0AMalillos%201%20Buenillos%202%0AMalisimos%200%20Buenillos%203%0AMalillos%200%20Buenisimos%203%0ABuenillos%201%20Buenisimos%202%0AFIN%0ASenior%0AAbuelos%203%20Abueletes%200%0AAbueletes%202%20Abuelos%201%0AFIN`

```javascript
{
  "result": [
    "Buenisimos 2",
    "EMPATE 0"
  ]
}
```

### GET /problem-2

Returns an integer that describes the number of squares the queen can attack.

Example: `curl http://localhost:8000/api/v1/problem-2/?input=5%203%0A4%203%0A5%205%0A4%202%0A2%203`

```javascript
{
  "result": 10
}
```

### GET /problem-3

Returns the maximum value of f(s) among all the substrings (s) of string t.

Example: `curl http://localhost:8000/api/v1/problem-3/?input=abcabcddd`

```javascript
{
  "result": 9
}
```
