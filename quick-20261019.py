"""Scratch module."""

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def clamp(value, low, high):
    return max(low, min(value, high))

if __name__ == "__main__":
    print(list(chunks(range(9), 9)))

# quick sketch
