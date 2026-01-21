def lcs_length(str1, str2):
    """
    Returns the length of the longest common subsequence.
    """
    m, n = len(str1), len(str2)

    # Create a 2D table to store results
    # dp[i][j] = LCS length of str1[0...i-1] and str2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match: add 1 to previous diagonal
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Characters don't match: take max of top or left
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(str1, str2):
    """
    Returns the actual longest common subsequence string.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual LCS string
    lcs = []
    i, j = m, n

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            # This character is part of LCS
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # Move up
            i -= 1
        else:
            # Move left
            j -= 1

    # LCS was built backwards, so reverse it
    return ''.join(reversed(lcs))


def print_dp_table(str1, str2):
    """
    Print the DP table for visualization.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Print table
    print("\n    ", end="")
    for char in str2:
        print(f"{char:3}", end="")
    print()

    for i in range(m + 1):
        if i == 0:
            print("  ", end="")
        else:
            print(f"{str1[i - 1]:2}", end="")
        for j in range(n + 1):
            print(f"{dp[i][j]:3}", end="")
        print()


print_dp_table("ABFDRRWDESTFSDERW", "WERTFDPRTPRESAWE")

# Test with our example
str1 = "ABFDRRWDESTFSDERW"
str2 = "WERTFDPRTPRESAWE"

print(f"String 1: {str1}")
print(f"String 2: {str2}")
print(f"LCS Length: {lcs_length(str1, str2)}")
print(f"LCS String: {lcs_string(str1, str2)}")


def print_dp_table_with_arrows(str1, str2):
    """
    Print the DP table with arrows showing the path taken.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    arrows = [['' for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the table and track arrows
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match: diagonal arrow
                dp[i][j] = dp[i - 1][j - 1] + 1
                arrows[i][j] = '↖'  # diagonal
            else:
                # Take max from top or left
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    arrows[i][j] = '↑'  # from top
                else:
                    dp[i][j] = dp[i][j - 1]
                    arrows[i][j] = '←'  # from left

    # Print header
    print("\n       ", end="")
    for char in str2:
        print(f"  {char}  ", end="")
    print()

    # Print table with arrows
    for i in range(m + 1):
        if i == 0:
            print("   ", end="")
        else:
            print(f" {str1[i - 1]} ", end="")

        for j in range(n + 1):
            if i == 0 or j == 0:
                print(f" {dp[i][j]:2}  ", end="")
            else:
                print(f" {dp[i][j]:2}{arrows[i][j]}", end="")
        print()

    return dp, arrows


def print_lcs_path(str1, str2):
    """
    Print the DP table and highlight the LCS path.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    arrows = [['' for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                arrows[i][j] = '↖'
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    arrows[i][j] = '↑'
                else:
                    dp[i][j] = dp[i][j - 1]
                    arrows[i][j] = '←'

    # Find the LCS path
    path = set()
    i, j = m, n
    while i > 0 and j > 0:
        path.add((i, j))
        if arrows[i][j] == '↖':
            i -= 1
            j -= 1
        elif arrows[i][j] == '↑':
            i -= 1
        else:
            j -= 1

    # Print header
    print("\n       ", end="")
    for char in str2:
        print(f"  {char}  ", end="")
    print()

    # Print table with highlighted path
    for i in range(m + 1):
        if i == 0:
            print("   ", end="")
        else:
            print(f" {str1[i - 1]} ", end="")

        for j in range(n + 1):
            if i == 0 or j == 0:
                print(f" {dp[i][j]:2}  ", end="")
            else:
                # Highlight cells in the LCS path
                if (i, j) in path:
                    print(f"[{dp[i][j]:2}{arrows[i][j]}]", end="")
                else:
                    print(f" {dp[i][j]:2}{arrows[i][j]} ", end="")
        print()


# Test the functions
str1 = "ABFDRRWDESTFSDERW"
str2 = "WERTFDPRTPRESAWE"

print("=" * 60)
print(f"String 1: {str1}")
print(f"String 2: {str2}")
print("=" * 60)

print("\n1. DP Table with Arrows:")
print("   ↖ = Characters match (diagonal)")
print("   ↑ = Take value from above")
print("   ← = Take value from left")
print("-" * 60)
print_dp_table_with_arrows(str1, str2)

print("\n" + "=" * 60)
print("\n2. DP Table with LCS Path Highlighted [in brackets]:")
print("-" * 60)
print_lcs_path(str1, str2)

print("\n" + "=" * 60)