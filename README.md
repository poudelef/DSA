# DSA Target Summer 2027

## Hashmap

```
h = {} 
h[key] = value # write - adds or overwrites
h[key]         # Read - crashes if key missing
key in h       # Check - True/False

h[key] = h.get(key,0) + 1 # counting pattern 

defaultdict(int)    # auto 0 for new keys
defaultdict(list)   # auto [] for new keys

h.setdefault("a", 0)    # "a" not in h -> Create h["a"] = 0
h.setdefault("a", 99)   # "a" already in h -> does Nothing, keeps old value

h.setdefault("a", []).append(1)   # creates "a":[] then appends 1 → {"a":[1]}
h.setdefault("a", []).append(2)   # "a" exists, just appends    → {"a":[1,2]}

```
