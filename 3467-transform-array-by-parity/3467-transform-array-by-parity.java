class Solution {
    public int[] transformArray(int[] nums) {
        int zeroCount = 0;

        for (int num : nums) {
            if (num % 2 == 0) {
                zeroCount++;
            }
        }

        for (int i = 0; i < nums.length; i++) {
            nums[i] = (i < zeroCount) ? 0 : 1;
        }

        return nums;
    }
}