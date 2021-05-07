# LiteCache: Redis-based JSON cache

### A very very small wrapper for making calls to JSON APIs. Limited to simple get requests and APIs that return JSON by default.

```python
import service

url = "https://pokeapi.co/api/v2/pokemon/1"
resp1 = service.retrieve(url)  # retrieved remotely if not yet cached
resp2 = service.retrieve(url)  # identical, retrieved locally since result is now cached
```

