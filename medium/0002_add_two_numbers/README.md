# 2. Add Two Numbers

## 📝 Task

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in **reverse order**, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. :contentReference[oaicite:0]{index=0}

---

## 📌 Examples

### Example 1

**Input**
```text
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output**
```text
[7,0,8]
```

**Explanation**

```text
342 + 465 = 807
```

---

### Example 2

**Input**
```text
l1 = [0]
l2 = [0]
```

**Output**
```text
[0]
```

---

### Example 3

**Input**
```text
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```

**Output**
```text
[8,9,9,9,0,0,0,1]
```

---

## 💡 Idea

The linked lists already store digits in reverse order, so the addition can be performed exactly like the manual "column addition" algorithm.

For every pair of nodes:

1. Take the current digits.
2. Add them together with the carry from the previous digit.
3. Store the last digit of the sum.
4. Pass the carry to the next iteration.

The process continues until both lists and the carry are exhausted.

---

## ✅ Complexity

- **Time:** `O(n)`
- **Space:** `O(1)` *(excluding the output list)*

---

## 🛠️ Topics

- Linked List
- Math
- Simulation