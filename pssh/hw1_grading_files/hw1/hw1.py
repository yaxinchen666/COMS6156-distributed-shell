import sys

def sum(l1, l2):
  return [e1 + e2 for e1, e2 in zip(l1, l2)]

if __name__ == "__main__":
  l1 = [int(e) for e in sys.stdin.readline().split()]
  l2 = [int(e) for e in sys.stdin.readline().split()]
  print(sum(l1, l2))
