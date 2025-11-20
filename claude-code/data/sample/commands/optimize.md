Analyze and optimize performance of $ARGUMENTS:

## Performance Optimization Process

1. **Profile current performance**
   - Identify bottlenecks
   - Measure current metrics
   - Understand constraints

2. **Analyze code** in $ARGUMENTS
   - Check algorithmic complexity
   - Review data structure choices
   - Look for common anti-patterns

3. **Recommend optimizations**
   - Prioritize by impact
   - Consider implementation cost
   - Note any trade-offs

## Performance Analysis

### Current Performance
- **Execution time:** [X ms/s]
- **Memory usage:** [X MB]
- **Throughput:** [X operations/second]

### Bottlenecks Identified

#### 1. [Bottleneck Name] - Impact: [High/Medium/Low]

**Location:** `file.py:42-56`

**Current Code:**
```python
# Slow implementation
```

**Analysis:**
- Time complexity: O(n²)
- Issue: Nested loops causing quadratic growth
- Performance: 5000ms for 1000 items

**Optimized Code:**
```python
# Fast implementation
```

**Improvement:**
- Time complexity: O(n)
- Performance: 50ms for 1000 items (100x faster)
- Trade-off: Uses O(n) extra memory for hash map

**Benchmark:**
```
Before: 5000ms
After:  50ms
Speedup: 100x
```

---

### Optimization Recommendations

#### High Priority (Biggest Impact)

**1. Replace Linear Search with Hash Lookup**
```python
# Before: O(n) lookup in list
if item in my_list:
    process(item)

# After: O(1) lookup in set
my_set = set(my_list)
if item in my_set:
    process(item)
```
**Expected improvement:** 10-100x faster for large lists

**2. Use Generator Instead of List**
```python
# Before: Creates full list in memory
results = [process(item) for item in huge_dataset]

# After: Lazy evaluation with generator
results = (process(item) for item in huge_dataset)
```
**Expected improvement:** 90% less memory

**3. Add Caching for Repeated Calculations**
```python
# Before: Recalculates every time
def expensive_function(n):
    return sum(i**2 for i in range(n))

# After: Cache results
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(n):
    return sum(i**2 for i in range(n))
```
**Expected improvement:** Instant for cached inputs

---

#### Medium Priority (Good Improvements)

**4. Batch Database Operations**
```python
# Before: N queries
for item in items:
    db.insert(item)

# After: 1 batch query
db.batch_insert(items)
```
**Expected improvement:** 5-10x faster

**5. Use Appropriate Data Structure**
```python
# Before: List for frequent lookups
my_list.index(item)  # O(n)

# After: Dict for key-value pairs
my_dict[key]  # O(1)
```

---

#### Low Priority (Minor Gains)

**6. Avoid String Concatenation in Loops**
```python
# Before
result = ""
for s in strings:
    result += s

# After
result = "".join(strings)
```

---

## Performance Metrics Summary

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Execution Time | Xms | Yms | Z% faster |
| Memory Usage | XMB | YMB | Z% less |
| Throughput | X/s | Y/s | Z% more |

---

## Implementation Plan

### Phase 1: Quick Wins (1-2 hours)
- [ ] [Optimization 1]
- [ ] [Optimization 2]

### Phase 2: Significant Improvements (1-2 days)
- [ ] [Optimization 3]
- [ ] [Optimization 4]

### Phase 3: Architectural Changes (1-2 weeks)
- [ ] [Major optimization]

---

## Trade-offs & Considerations

### Memory vs Speed
- Some optimizations use more memory for faster execution
- Consider if memory is a constraint

### Readability vs Performance
- Don't sacrifice clarity for marginal gains
- Optimize hot paths, keep others readable

### Premature Optimization
- Profile first, optimize later
- Focus on real bottlenecks, not theoretical ones

---

## Verification Plan

After implementing optimizations:

1. **Run benchmarks** to verify improvement
2. **Run tests** to ensure correctness
3. **Monitor in production** for real-world impact
4. **Profile again** to find next bottleneck

---

## Profiling Code

To verify optimizations, use:

```python
# Time measurement
import timeit
time = timeit.timeit(lambda: your_function(), number=1000)

# Memory profiling
import tracemalloc
tracemalloc.start()
your_function()
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory: {peak / 1024 / 1024:.2f}MB")
```

---

**Remember:** Real optimization requires measurement. Always profile before and after!
