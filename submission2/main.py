import sys

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 3:
        return

    try:
        a1 = float(data[0])
        r = float(data[1])
        n = int(float(data[2]))  # accept numeric tokens like "5.0"
    except ValueError:
        return

    if n <= 0:
        return

    terms = []
    term = a1
    for k in range(n):
        # keep integer formatting when appropriate
        if isinstance(term, float) and term.is_integer():
            terms.append(str(int(term)))
        else:
            terms.append(str(term))
        term *= r

    print(" ".join(terms))

if __name__ == "__main__":
    main()
