def permute(string):
    def backtrack(path, used):
        if len(path) == len(string):  # Base case: permutation is complete
            permutations.append("".join(path))
            
        for i in range(len(string)):
            if used[i]:  # Skip used characters
                continue
            used[i] = True
            path.append(string[i])  # Add character to permutation
            backtrack(path, used)   # Recurse
            path.pop()  # Backtrack
            used[i] = False  # Undo usage

    permutations = []
    backtrack([], [False] * len(string))                                                                                                                                                                                                     
    return permutations

# Example usage:
print(permute("ABC"))