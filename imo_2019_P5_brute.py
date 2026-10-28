import itertools

def flip_game(s: str) -> tuple[str, int]:
    # 1. Count the number of 'H's in the string
    k = s.count('H')
    
    # Convert string to list for in-place modifications
    chars = list(s)
    n = len(chars)
    
    # 2. Set the starting index (1-indexed 'k' means index k-1 in Python)
    idx = k - 1
    
    # 3. Process the simulation until all characters turn to 'T'
    # (Or until the index falls out of bounds)
    flipctr = 0
    while 'H' in chars:
        if idx < 0 or idx >= n:
            break
            
        if chars[idx] == 'H':
            chars[idx] = 'T'   # Flip H to T
            idx -= 1           # Move to k-1th character (left)
        else:
            chars[idx] = 'H'   # Flip T to H
            idx += 1           # Move to k+1th character (right)
        flipctr += 1
            
    return "".join(chars), flipctr

# --- Test Cases ---
if __name__ == "__main__":
    for n in range(1,7):
        # n = 2  # Length of strings to test
        # print(f"Generating all {2**n} combinations for n = {n}:\n")
        # print(f"{'Input':<{n + 2}} | {'Final':<{n + 2}} | {'Flips':<6} | {'Terminated All T'}")
        # print("-" * (n + n + 25))
        tot_flips = 0

        for p in itertools.product('HT', repeat=n):
            input_str = "".join(p)
            final_result, flipctr = flip_game(input_str)
            tot_flips += flipctr
            terminated = "Yes" if 'H' not in final_result else "No (Out of bounds)"
            # print(f"{input_str:<{n + 2}} | {final_result:<{n + 2}} | {flipctr:<6} | {terminated}")
        print(n, "=>", tot_flips, (2**n), tot_flips/(2**n))

#S(n) = 2*S(n-1) + n*2^(n-1)
# =>(2**n)*A(n) = 2*(2**(n-1))*A(n-1) + n*2**(n-1)
# => 2*A(n) = 2*A(n-1) + n
# => A(n) = A(n-1) + n/2
