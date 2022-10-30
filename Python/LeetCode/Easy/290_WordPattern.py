class Solution:
  def wordPattern(self, pattern: str, str: str) -> bool:
    t = str.split()
    return [*map(pattern.index, pattern)] == [*map(t.index, t)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern(pattern , s))
