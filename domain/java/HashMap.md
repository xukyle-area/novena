## Overview

### What is HashMap?

HashMap is a hash table-based implementation of the Map interface in Java. It stores data as key-value pairs and provides **O(1)** average time complexity for basic operations (get, put, remove).

### Class Declaration

```Java
public class HashMap<K,V> 
    extends AbstractMap<K,V>
    implements Map<K,V>, Cloneable, Serializable
```

### Evolution of HashMap Data Structure

| Version            | Data Structure           | Collision Handling                            |
| ------------------ | ------------------------ | --------------------------------------------- |
| **Java 1.2 - 1.7** | Array + Linked List      | Chaining (Linked List only)                   |
| **Java 8+**        | Array + Linked List/Tree | Chaining (List → Tree when threshold reached) |

## Core Data Structure

### High-Level Architecture

```Plain
HashMap = Array of Buckets + Collision Resolution Structure

┌─────────────────────────────────────────────────────────┐
│                    Hash Table (Array)                    │
├────────┬────────┬────────┬────────┬─────────┬───────────┤
│Index 0 │Index 1 │Index 2 │Index 3 │   ...   │  Index n  │
└───┬────┴────┬───┴────┬───┴────┬───┴─────────┴─────┬─────┘
    │         │        │        │                    │
    v         v        v        v                    v
  Node      Node     Tree     null                 Node
    │         │        │                             │
    v         v        │                             v
  Node      null       │                           Node
    │                  │
    v                  │
  null            (Red-Black Tree)
```

### Internal Fields

```Java
public class HashMap<K,V> extends AbstractMap<K,V> 
    implements Map<K,V>, Cloneable, Serializable {
    
    /**
     * The table, initialized on first use, and resized as necessary.
     * Always a power of 2.
     */
    transient Node<K,V>[] table;
    
    /**
     * The number of key-value mappings contained in this map.
     */
    transient int size;
    
    /**
     * The load factor for the hash table.
     */
    final float loadFactor;
    
    /**
     * The next size value at which to resize (capacity * load factor).
     */
    int threshold;
    
    /**
     * The number of times this HashMap has been structurally modified.
     */
    transient int modCount;
    
    // Constants
    static final int DEFAULT_INITIAL_CAPACITY = 1 << 4;    // 16
    static final int MAXIMUM_CAPACITY = 1 << 30;           // 2^30
    static final float DEFAULT_LOAD_FACTOR = 0.75f;
    static final int TREEIFY_THRESHOLD = 8;
    static final int UNTREEIFY_THRESHOLD = 6;
    static final int MIN_TREEIFY_CAPACITY = 64;
}
```

### Node Structure (Entry)

```Java
/**
 * Basic hash bin node, used for most entries.
 */
static class Node<K,V> implements Map.Entry<K,V> {
    final int hash;        // Cached hash code
    final K key;           // The key (immutable)
    V value;               // The value (mutable)
    Node<K,V> next;        // Next node in the chain
    
    Node(int hash, K key, V value, Node<K,V> next) {
        this.hash = hash;
        this.key = key;
        this.value = value;
        this.next = next;
    }
    
    public final K getKey()        { return key; }
    public final V getValue()      { return value; }
    public final String toString() { return key + "=" + value; }
    
    public final int hashCode() {
        return Objects.hashCode(key) ^ Objects.hashCode(value);
    }
    
    public final V setValue(V newValue) {
        V oldValue = value;
        value = newValue;
        return oldValue;
    }
    
    public final boolean equals(Object o) {
        if (o == this)
            return true;
        if (o instanceof Map.Entry) {
            Map.Entry<?,?> e = (Map.Entry<?,?>)o;
            if (Objects.equals(key, e.getKey()) &&
                Objects.equals(value, e.getValue()))
                return true;
        }
        return false;
    }
}
```

## Hash Function & Bucket Selection

### The Hashing Process

```Plain
Step 1: Calculate hashCode()
   key.hashCode() → int hash

Step 2: Apply HashMap's hash function
   hash(key) → int h

Step 3: Calculate bucket index
   (n - 1) & hash → int index
```

### Hash Function Implementation

```Java
/**
 * Computes key.hashCode() and spreads (XORs) higher bits of hash
 * to lower. Because the table uses power-of-two masking, sets of
 * hashes that vary only in bits above the current mask will
 * always collide.
 */
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
```

### Why This Hash Function?

**Problem:** When table size is small (e.g., 16), only the lower 4 bits are used for indexing.

```Plain
Example with capacity = 16:
index = (16 - 1) & hash = 15 & hash = 0000...1111 & hash

This means only the lower 4 bits of hash matter!
```

**Solution:** XOR with upper 16 bits to mix high bits into lower bits.

```Plain
Original hash:     1010 1100 0011 0101 | 1111 0000 1010 1100
Right shift >>> 16: 0000 0000 0000 0000 | 1010 1100 0011 0101
XOR result:        1010 1100 0011 0101 | 0101 1100 1001 1001
                                         ^^^^^^^^^^^^^^^^^
                                         Better distribution!
```

### Bucket Index Calculation

```Java
/**
 * Returns index for hash code h.
 */
static int indexFor(int h, int length) {
    return h & (length - 1);
}

// Why (length - 1) & hash instead of hash % length?
// Because length is always power of 2:
//   16 - 1 = 15 = 0000...01111
//   32 - 1 = 31 = 0000...11111
// Using bitwise AND is much faster than modulo operation!
```

### Visual Example

```Plain
Assume: capacity = 16, hash = 189

Step 1: Calculate index
   hash        = 189 = 0000 0000 0000 0000 0000 0000 1011 1101
   length - 1  = 15  = 0000 0000 0000 0000 0000 0000 0000 1111
   AND result  = 13  = 0000 0000 0000 0000 0000 0000 0000 1101

Result: Element goes into bucket[13]

Hash Table:
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬─────┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │ 13  │14 │15 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──┬──┴───┴───┘
                                                        │
                                                        v
                                                      Node
                                                 (hash=189, key, value)
```

## Collision Handling

### What is a Collision?

A collision occurs when two different keys hash to the same bucket index.

```Plain
Example:
   key1 = "John"  → hash1 = 2589 → index = 2589 & 15 = 13
   key2 = "Jane"  → hash2 = 3101 → index = 3101 & 15 = 13
   
Both keys map to bucket[13] → Collision!
```

### Collision Resolution Methods

HashMap uses **Separate Chaining** with two structures:

1. **Linked List** (default)
2. **Red-Black Tree** (when list becomes too long)

### Method 1: Linked List (Chaining)

```Plain
Bucket Structure with Collisions:

table[13] → Node1 → Node2 → Node3 → null
           (John)  (Jane)  (Jack)

Each node contains:
┌──────────────────────────┐
│ hash: int                │
│ key: K                   │
│ value: V                 │
│ next: Node<K,V>         │
└──────────────────────────┘
```

#### Put Operation with Collision

```Java
// Simplified put() logic
public V put(K key, V value) {
    return putVal(hash(key), key, value, false, true);
}

final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
               boolean evict) {
    Node<K,V>[] tab; Node<K,V> p; int n, i;
    
    // 1. Initialize table if necessary
    if ((tab = table) == null || (n = tab.length) == 0)
        n = (tab = resize()).length;
    
    // 2. Calculate bucket index
    i = (n - 1) & hash;
    
    // 3. If bucket is empty, create new node
    if ((p = tab[i]) == null)
        tab[i] = newNode(hash, key, value, null);
    else {
        // 4. Collision handling
        Node<K,V> e; K k;
        
        // 4a. Check if first node matches
        if (p.hash == hash &&
            ((k = p.key) == key || (key != null && key.equals(k))))
            e = p;
        
        // 4b. If bucket is a tree, use tree insertion
        else if (p instanceof TreeNode)
            e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
        
        // 4c. Traverse linked list
        else {
            for (int binCount = 0; ; ++binCount) {
                if ((e = p.next) == null) {
                    // Add to end of list
                    p.next = newNode(hash, key, value, null);
                    
                    // Convert to tree if list too long
                    if (binCount >= TREEIFY_THRESHOLD - 1)
                        treeifyBin(tab, hash);
                    break;
                }
                // Key already exists
                if (e.hash == hash &&
                    ((k = e.key) == key || (key != null && key.equals(k))))
                    break;
                p = e;
            }
        }
        
        // 5. Update existing value
        if (e != null) {
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);
            return oldValue;
        }
    }
    
    // 6. Increment size and check for resize
    ++modCount;
    if (++size > threshold)
        resize();
    afterNodeInsertion(evict);
    return null;
}
```

#### Get Operation with Collision

```Java
public V get(Object key) {
    Node<K,V> e;
    return (e = getNode(hash(key), key)) == null ? null : e.value;
}

final Node<K,V> getNode(int hash, Object key) {
    Node<K,V>[] tab; Node<K,V> first, e; int n; K k;
    
    // 1. Check if table exists and bucket is not empty
    if ((tab = table) != null && (n = tab.length) > 0 &&
        (first = tab[(n - 1) & hash]) != null) {
        
        // 2. Check first node
        if (first.hash == hash &&
            ((k = first.key) == key || (key != null && key.equals(k))))
            return first;
        
        // 3. Check remaining nodes
        if ((e = first.next) != null) {
            // If tree structure
            if (first instanceof TreeNode)
                return ((TreeNode<K,V>)first).getTreeNode(hash, key);
            
            // Traverse linked list
            do {
                if (e.hash == hash &&
                    ((k = e.key) == key || (key != null && key.equals(k))))
                    return e;
            } while ((e = e.next) != null);
        }
    }
    return null;
}
```

### Collision Example Walkthrough

```Java
HashMap<String, Integer> map = new HashMap<>(4); // capacity = 4

// Assume these keys have colliding hash indices
map.put("key1", 1);  // hash & 3 = 2
map.put("key2", 2);  // hash & 3 = 2 (collision!)
map.put("key3", 3);  // hash & 3 = 2 (collision!)
```

**Visual representation:**

```Plain
Initial State:
┌────┬────┬────┬────┐
│ 0  │ 1  │ 2  │ 3  │
└────┴────┴────┴────┘

After put("key1", 1):
┌────┬────┬────────────┬────┐
│ 0  │ 1  │ 2          │ 3  │
└────┴────┴─┬──────────┴────┘
             │
             v
           Node(key1, 1)

After put("key2", 2):
┌────┬────┬────────────┬────┐
│ 0  │ 1  │ 2          │ 3  │
└────┴────┴─┬──────────┴────┘
             │
             v
           Node(key1, 1) → Node(key2, 2)

After put("key3", 3):
┌────┬────┬────────────┬────┐
│ 0  │ 1  │ 2          │ 3  │
└────┴────┴─┬──────────┴────┘
             │
             v
           Node(key1, 1) → Node(key2, 2) → Node(key3, 3)
```

## Dynamic Resizing

### Why Resize?

As more elements are added, the load factor increases:

```Plain
Load Factor = size / capacity

If load factor exceeds threshold (default 0.75):
  → More collisions
  → Longer chains
  → Worse performance
  → Need to resize!
```

### Resize Trigger

```Java
// Resize when size exceeds threshold
if (++size > threshold)
    resize();

// threshold = capacity × loadFactor
// Example: capacity=16, loadFactor=0.75
//          threshold = 16 × 0.75 = 12
```

### Resize Process

```Java
final Node<K,V>[] resize() {
    Node<K,V>[] oldTab = table;
    int oldCap = (oldTab == null) ? 0 : oldTab.length;
    int oldThr = threshold;
    int newCap, newThr = 0;
    
    if (oldCap > 0) {
        // Check maximum capacity
        if (oldCap >= MAXIMUM_CAPACITY) {
            threshold = Integer.MAX_VALUE;
            return oldTab;
        }
        // Double the capacity
        else if ((newCap = oldCap << 1) < MAXIMUM_CAPACITY &&
                 oldCap >= DEFAULT_INITIAL_CAPACITY)
            newThr = oldThr << 1; // Double threshold
    }
    else if (oldThr > 0)
        newCap = oldThr;
    else {
        // Initialize with defaults
        newCap = DEFAULT_INITIAL_CAPACITY;
        newThr = (int)(DEFAULT_LOAD_FACTOR * DEFAULT_INITIAL_CAPACITY);
    }
    
    if (newThr == 0) {
        float ft = (float)newCap * loadFactor;
        newThr = (newCap < MAXIMUM_CAPACITY && ft < (float)MAXIMUM_CAPACITY ?
                  (int)ft : Integer.MAX_VALUE);
    }
    
    threshold = newThr;
    Node<K,V>[] newTab = (Node<K,V>[])new Node[newCap];
    table = newTab;
    
    // Rehash all existing entries
    if (oldTab != null) {
        for (int j = 0; j < oldCap; ++j) {
            Node<K,V> e;
            if ((e = oldTab[j]) != null) {
                oldTab[j] = null;
                if (e.next == null)
                    // Single node, rehash directly
                    newTab[e.hash & (newCap - 1)] = e;
                else if (e instanceof TreeNode)
                    // Tree node, split tree
                    ((TreeNode<K,V>)e).split(this, newTab, j, oldCap);
                else {
                    // Linked list, preserve order
                    Node<K,V> loHead = null, loTail = null;
                    Node<K,V> hiHead = null, hiTail = null;
                    Node<K,V> next;
                    do {
                        next = e.next;
                        // Check if node stays in same bucket
                        if ((e.hash & oldCap) == 0) {
                            if (loTail == null)
                                loHead = e;
                            else
                                loTail.next = e;
                            loTail = e;
                        }
                        // Node moves to new bucket
                        else {
                            if (hiTail == null)
                                hiHead = e;
                            else
                                hiTail.next = e;
                            hiTail = e;
                        }
                    } while ((e = next) != null);
                    
                    // Place in new table
                    if (loTail != null) {
                        loTail.next = null;
                        newTab[j] = loHead;
                    }
                    if (hiTail != null) {
                        hiTail.next = null;
                        newTab[j + oldCap] = hiHead;
                    }
                }
            }
        }
    }
    return newTab;
}
```

### Resize Example

```Plain
Old Table (capacity = 4):
┌────┬────┬────┬────┐
│ 0  │ 1  │ 2  │ 3  │
└────┴────┴─┬──┴────┘
             │
             v
        Node(hash=2, A) → Node(hash=6, B) → Node(hash=10, C)

Resize to capacity = 8:

Calculate new indices:
  A: hash=2  → 2 & 7 = 2  (stays)
  B: hash=6  → 6 & 7 = 6  (moves to 2+4=6)
  C: hash=10 → 10 & 7 = 2 (stays)

New Table:
┌────┬────┬────┬────┬────┬────┬────┬────┐
│ 0  │ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │
└────┴────┴─┬──┴────┴────┴────┴─┬──┴────┘
             │                    │
             v                    v
        Node(A) → Node(C)      Node(B)
```

### Efficient Rehashing Trick

**Key insight:** When capacity doubles, a node also:

1. Stays in the same bucket, OR
2. Moves to `oldIndex + oldCapacity`

```Plain
Why?
Old index: hash & (oldCap - 1)
New index: hash & (newCap - 1) = hash & (2×oldCap - 1)

Example with oldCap=4, newCap=8:
  hash = 10 = ...1010
  
  Old: 10 & 3 = 1010 & 0011 = 0010 = 2
  New: 10 & 7 = 1010 & 0111 = 0010 = 2 (same)
  
  hash = 14 = ...1110
  
  Old: 14 & 3 = 1110 & 0011 = 0010 = 2
  New: 14 & 7 = 1110 & 0111 = 0110 = 6 (2 + 4)
  
The bit that determines movement is bit at oldCap position!
  if (hash & oldCap) == 0 → stays
  else → moves to index + oldCap
```

## Red-Black Tree Optimization (Java 8+)

### Why Trees?

**Problem with long chains:**

```Plain
Bucket with 10 nodes in linked list:
  get() time = O(n) = O(10) = linear search

Worst case: all keys hash to same bucket
  get() time = O(n) where n = total entries
  → HashMap degrades to linked list!
```

**Solution: Convert to tree when chain is long**

```Plain
Bucket with 10 nodes in Red-Black Tree:
  get() time = O(log n) = O(log 10) ≈ O(3.3)
  → Much better!
```

### Treeification Thresholds

```Java
// Convert list to tree when bin count reaches 8
static final int TREEIFY_THRESHOLD = 8;

// Convert tree back to list when bin count drops to 6
static final int UNTREEIFY_THRESHOLD = 6;

// Minimum table capacity for treeification (prevent premature treeifying)
static final int MIN_TREEIFY_CAPACITY = 64;
```

### TreeNode Structure

```Java
static final class TreeNode<K,V> extends LinkedHashMap.Entry<K,V> {
    TreeNode<K,V> parent;   // Red-Black tree parent
    TreeNode<K,V> left;     // Left child
    TreeNode<K,V> right;    // Right child
    TreeNode<K,V> prev;     // Needed for delete
    boolean red;            // Color (red or black)
    
    TreeNode(int hash, K key, V val, Node<K,V> next) {
        super(hash, key, val, next);
    }
    
    /**
     * Returns root of tree containing this node.
     */
    final TreeNode<K,V> root() {
        for (TreeNode<K,V> r = this, p;;) {
            if ((p = r.parent) == null)
                return r;
            r = p;
        }
    }
}
```

### Tree Structure Visualization

```Plain
Linked List (before treeification):
table[5] → Node → Node → Node → Node → Node → Node → Node → Node → null
          (hash) (hash) (hash) (hash) (hash) (hash) (hash) (hash)
          8 nodes in chain → Triggers treeification!

Red-Black Tree (after treeification):
table[5] → TreeNode (Black, root)
              /          \
    TreeNode (Red)    TreeNode (Red)
       /    \            /      \
  TreeNode TreeNode TreeNode TreeNode
   (Black)  (Black)  (Black)  (Black)

Properties:
  - Balanced binary search tree
  - Search time: O(log n)
  - Self-balancing during insertion/deletion
  - Red-Black tree rules maintained
```

### Treeify Process

```Java
/**
 * Replaces all linked nodes in bin at index for given hash unless
 * table is too small, in which case resizes instead.
 */
final void treeifyBin(Node<K,V>[] tab, int hash) {
    int n, index; Node<K,V> e;
    
    // If table too small, resize instead of treeify
    if (tab == null || (n = tab.length) < MIN_TREEIFY_CAPACITY)
        resize();
    else if ((e = tab[index = (n - 1) & hash]) != null) {
        TreeNode<K,V> hd = null, tl = null;
        
        // Convert all nodes to TreeNodes
        do {
            TreeNode<K,V> p = replacementTreeNode(e, null);
            if (tl == null)
                hd = p;
            else {
                p.prev = tl;
                tl.next = p;
            }
            tl = p;
        } while ((e = e.next) != null);
        
        // Build Red-Black tree
        if ((tab[index] = hd) != null)
            hd.treeify(tab);
    }
}

/**
 * Forms tree of the nodes linked from this node.
 */
final void treeify(Node<K,V>[] tab) {
    TreeNode<K,V> root = null;
    for (TreeNode<K,V> x = this, next; x != null; x = next) {
        next = (TreeNode<K,V>)x.next;
        x.left = x.right = null;
        
        // Set root
        if (root == null) {
            x.parent = null;
            x.red = false;  // Root is always black
            root = x;
        }
        else {
            K k = x.key;
            int h = x.hash;
            Class<?> kc = null;
            
            // Find insertion point
            for (TreeNode<K,V> p = root;;) {
                int dir, ph;
                K pk = p.key;
                
                // Compare hashes
                if ((ph = p.hash) > h)
                    dir = -1;
                else if (ph < h)
                    dir = 1;
                // If hashes equal, compare keys
                else if ((kc == null &&
                          (kc = comparableClassFor(k)) == null) ||
                         (dir = compareComparables(kc, k, pk)) == 0)
                    dir = tieBreakOrder(k, pk);
                
                TreeNode<K,V> xp = p;
                if ((p = (dir <= 0) ? p.left : p.right) == null) {
                    x.parent = xp;
                    if (dir <= 0)
                        xp.left = x;
                    else
                        xp.right = x;
                    // Balance tree after insertion
                    root = balanceInsertion(root, x);
                    break;
                }
            }
        }
    }
    // Ensure root is in first position
    moveRootToFront(tab, root);
}
```

### Tree Search

```Java
/**
 * Calls find for root node.
 */
final TreeNode<K,V> getTreeNode(int h, Object k) {
    return ((parent != null) ? root() : this).find(h, k, null);
}

/**
 * Finds the node starting from root p with the given hash and key.
 */
final TreeNode<K,V> find(int h, Object k, Class<?> kc) {
    TreeNode<K,V> p = this;
    do {
        int ph, dir; K pk;
        TreeNode<K,V> pl = p.left, pr = p.right, q;
        
        // Search left subtree
        if ((ph = p.hash) > h)
            p = pl;
        // Search right subtree
        else if (ph < h)
            p = pr;
        // Found exact match
        else if ((pk = p.key) == k || (k != null && k.equals(pk)))
            return p;
        // One subtree is null
        else if (pl == null)
            p = pr;
        else if (pr == null)
            p = pl;
        // Need to compare keys
        else if ((kc != null ||
                  (kc = comparableClassFor(k)) != null) &&
                 (dir = compareComparables(kc, k, pk)) != 0)
            p = (dir < 0) ? pl : pr;
        // Recursively search right, then left
        else if ((q = pr.find(h, k, kc)) != null)
            return q;
        else
            p = pl;
    } while (p != null);
    return null;
}
```

### Untreeify (Tree to List)

```Java
/**
 * Returns a list of non-TreeNodes replacing those in this bin.
 */
final Node<K,V> untreeify(HashMap<K,V> map) {
    Node<K,V> hd = null, tl = null;
    for (Node<K,V> q = this; q != null; q = q.next) {
        Node<K,V> p = map.replacementNode(q, null);
        if (tl == null)
            hd = p;
        else
            tl.next = p;
        tl = p;
    }
    return hd;
}
```

### When Does Untreeification Occur?

1. During resize, if bin count drops below `UNTREEIFY_THRESHOLD` (6)
2. During removal operations that reduce tree size

```Java
// In resize() method
if (loHead instanceof TreeNode) {
    if (loHead.count() <= UNTREEIFY_THRESHOLD)
        tab[index] = loHead.untreeify(map);
    else {
        tab[index] = loHead;
        if (hiHead != null)
            loHead.treeify(tab);
    }
}
```

## Memory Layout

### Memory Structure Overview

```Plain
HashMap Instance Memory Layout:

┌─────────────────────────────────────┐
│       HashMap Object Header         │  ~12-16 bytes
├─────────────────────────────────────┤
│  table: Node<K,V>[]                 │  8 bytes (reference)
│  size: int                          │  4 bytes
│  modCount: int                      │  4 bytes
│  threshold: int                     │  4 bytes
│  loadFactor: float                  │  4 bytes
│  entrySet: Set                      │  8 bytes (reference)
│  ... other fields                   │  
└─────────────────────────────────────┘
         │
         │ references
         v
┌─────────────────────────────────────┐
│    Node<K,V>[] Array (table)        │  
│    Length = capacity                │  capacity × 8 bytes (references)
├──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬───┤
│0 │1 │2 │3 │4 │5 │6 │7 │8 │9 │10│...│
└──┴──┴──┴──┴──┴──┴─┬┴──┴──┴──┴──┴───┘
                    │
                    v
              ┌─────────────────┐
              │   Node Object   │  ~32-40 bytes each
              ├─────────────────┤
              │ hash: int       │  4 bytes
              │ key: K          │  8 bytes (reference)
              │ value: V        │  8 bytes (reference)
              │ next: Node      │  8 bytes (reference)
              │ object header   │  ~12-16 bytes
              └─────────────────┘
                    │
                    v (if collision)
              ┌─────────────────┐
              │   Node Object   │
              └─────────────────┘
```

### Memory Calculation Example

```Plain
HashMap<String, Integer> with 100 entries, capacity=128, loadFactor=0.75

1. HashMap object:           ~48 bytes
2. Node[] array:            128 × 8 = 1,024 bytes
3. 100 Node objects:        100 × 40 = 4,000 bytes
4. 100 String keys:         ~100 × 60 = 6,000 bytes (average)
5. 100 Integer values:      100 × 16 = 1,600 bytes

Total: ~12,672 bytes ≈ 12.4 KB

Overhead per entry: ~127 bytes (without key/value data)
```

### TreeNode Memory

```Plain
TreeNode is larger than regular Node:

┌─────────────────────────────┐
│   TreeNode Object           │  ~56-64 bytes
├─────────────────────────────┤
│ (inherits from Node)        │
│   hash: int                 │  4 bytes
│   key: K                    │  8 bytes
│   value: V                  │  8 bytes
│   next: Node                │  8 bytes
│ (TreeNode specific)         │
│   parent: TreeNode          │  8 bytes
│   left: TreeNode            │  8 bytes
│   right: TreeNode           │  8 bytes
│   prev: TreeNode            │  8 bytes
│   red: boolean              │  1 byte
│   object header             │  ~12-16 bytes
└─────────────────────────────┘

TreeNode is ~50% larger than Node!
But provides O(log n) search instead of O(n)
```

## Performance Analysis

### Time Complexity

| Operation         | Average Case | Worst Case (before Java 8) | Worst Case (Java 8+) |
| ----------------- | ------------ | -------------------------- | -------------------- |
| **get()**         | O(1)         | O(n)                       | O(log n)             |
| **put()**         | O(1)         | O(n)                       | O(log n)             |
| **remove()**      | O(1)         | O(n)                       | O(log n)             |
| **containsKey()** | O(1)         | O(n)                       | O(log n)             |
| **resize()**      | O(n)         | O(n)                       | O(n)                 |

### Space Complexity

```Plain
Space = O(n + m)

where:
  n = number of entries (size)
  m = number of buckets (capacity)

Actual memory:
  ≈ capacity × 8 bytes (array)
  + size × 40 bytes (nodes)
  + key and value sizes
```

### Load Factor Impact

```Plain
Load Factor = size / capacity

Low Load Factor (e.g., 0.5):
  ✅ Fewer collisions
  ✅ Faster operations
  ❌ More memory waste
  ❌ More frequent resizing (if capacity small)

High Load Factor (e.g., 0.9):
  ✅ Better memory utilization
  ❌ More collisions
  ❌ Slower operations
  ❌ Longer chains

Default 0.75 is a good trade-off!
```

### Performance Comparison

```Java
// Test: 1 million insertions

// Scenario 1: Good hash distribution
HashMap<Integer, String> goodMap = new HashMap<>();
for (int i = 0; i < 1_000_000; i++) {
    goodMap.put(i, "value" + i);
}
// Time: ~200ms, mostly O(1) operations

// Scenario 2: Poor hash distribution (all hash to same bucket)
HashMap<BadHash, String> badMap = new HashMap<>();
for (int i = 0; i < 1_000_000; i++) {
    badMap.put(new BadHash(i), "value" + i);
}
// Before Java 8: ~50,000ms (O(n) operations)
// After Java 8: ~500ms (O(log n) operations with tree)

class BadHash {
    int value;
    BadHash(int v) { this.value = v; }
    
    @Override
    public int hashCode() {
        return 1;  // All instances hash to same value!
    }
}
```

### Optimization Tips

1. **Set initial capacity** if size is known:

```Java
// Avoid multiple resizes
int expectedSize = 1000;
int capacity = (int) (expectedSize / 0.75) + 1;
HashMap<K,V> map = new HashMap<>(capacity);
```

1. **Use good hash functions**:

```Java
// Bad
@Override
public int hashCode() {
    return 1;  // All objects hash to same value
}

// Good
@Override
public int hashCode() {
    return Objects.hash(field1, field2, field3);
}
```

1. **Consider capacity and load factor**:

```Java
// For memory-constrained applications
HashMap<K,V> map = new HashMap<>(16, 0.9f);

// For performance-critical applications
HashMap<K,V> map = new HashMap<>(64, 0.5f);
```

## Implementation Details

### Complete Put Operation Flow

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=NDlhNDYwNmZlNGJjZTgzODc2NjE3MWJkOGYxZTNlMGNfVE00b1JPRWJ5Tnp4YmFuOU5QOWtBUUgweHU3aWRVcnZfVG9rZW46VmhZaWI4c2lYb2VldVJ4b295OWN4YzNLbnNkXzE3NjQ4NzAwNTU6MTc2NDg3MzY1NV9WNA)

### Key Design Decisions

#### 1. Why Power of 2 Capacity?

```Plain
Benefits:
1. Fast modulo operation: hash & (n-1) instead of hash % n
2. Efficient resizing: only need to check one bit
3. Better cache utilization

Example:
  capacity = 16 (2^4)
  index = hash & 15 = hash & 0b1111
  
  Much faster than: index = hash % 16
```

#### 2. Why Load Factor 0.75?

```Plain
Trade-off analysis:

Load Factor 0.5:
  - 50% empty buckets
  - Very few collisions
  - Wastes 50% memory
  
Load Factor 0.75:
  - 25% empty buckets
  - Reasonable collisions
  - Good memory/performance balance
  
Load Factor 1.0:
  - No empty buckets
  - Many collisions
  - Poor performance

0.75 is proven to be optimal through statistical analysis!
```

#### 3. Why Threshold 8 for Treeification?

```Plain
Statistical reasoning (Poisson distribution):

Probability of bin having k nodes:
  P(k) = (e^-0.5 × 0.5^k) / k!

For well-distributed hash:
  P(0) = 0.60653  (60% empty)
  P(1) = 0.30326  (30% one node)
  P(2) = 0.07582  (7.5% two nodes)
  P(8) = 0.00000006  (extremely rare!)

If bin has 8+ nodes, hash function is likely bad
→ Worth converting to tree for O(log n) performance

Threshold 6 for untreeify: provides hysteresis to avoid
frequent conversions when size oscillates around threshold.
```

#### 4. Why XOR with >>> 16 in Hash Function?

```Java
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
Problem: Only lower bits used for small tables
Solution: Mix upper bits into lower bits

Example with capacity=16 (uses lower 4 bits):

Original hash:    
  1101 0110 1010 0011 | 1111 0000 1100 0101
  Upper 16 bits       | Lower 16 bits

After >>> 16:
  0000 0000 0000 0000 | 1101 0110 1010 0011

XOR result:
  1101 0110 1010 0011 | 0010 0110 0110 0110
                        ^^^^^^^^^^^^^^^^^^^^
                        Better distribution!

This simple operation significantly improves hash distribution
with minimal performance cost.
```

## Summary

### Core Data Structures

```Plain
HashMap = Array + Linked List/Tree

Array (table):
  - Size always power of 2
  - Stores references to Node/TreeNode
  - Index = hash & (capacity - 1)

Linked List (default):
  - Used for collision handling
  - Nodes connected via 'next' reference
  - O(n) search time

Red-Black Tree (Java 8+):
  - Used when list length ≥ 8
  - Self-balancing binary search tree
  - O(log n) search time
```

### Key Points

1. **Hashing**: Converts key to array index using hash function
2. **Collisions**: Handled by chaining (list/tree)
3. **Resizing**: Doubles capacity when load exceeds threshold
4. **Treeification**: Converts long chains to trees (Java 8+)
5. **Performance**: O(1) average, O(log n) worst case

### Performance Tips

```Java
// 1. Set initial capacity if size known
HashMap<K,V> map = new HashMap<>(expectedSize * 4/3 + 1);

// 2. Implement good hashCode() and equals()
@Override
public int hashCode() {
    return Objects.hash(field1, field2);
}

// 3. Use immutable keys
// String, Integer are good key types

// 4. Avoid resizing
// Set capacity = expectedSize / loadFactor
```