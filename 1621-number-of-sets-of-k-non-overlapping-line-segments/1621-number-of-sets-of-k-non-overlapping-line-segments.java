class Solution {
    public int numberOfSets(int n, int k) {
        int MOD = 1_000_000_007;

        int total = n + k - 1;
        int choose = 2 * k;

        if (choose > total) return 0;

        int[] dp = new int[choose + 1];
        dp[0] = 1;

        for (int i = 1; i <= total; i++) {
            for (int j = Math.min(i, choose); j > 0; j--) {
                dp[j] = (dp[j] + dp[j - 1]) % MOD;
            }
        }

        return dp[choose];
    }
}