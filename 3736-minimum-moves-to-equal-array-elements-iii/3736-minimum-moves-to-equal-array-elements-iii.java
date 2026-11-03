class Solution {
    public int minMoves(int[] nums) {
        int maxElement = Integer.MIN_VALUE;
        for(int i = 0; i < nums.length; i++){
            maxElement = Math.max(maxElement,nums[i]);
        }
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            count += Math.abs(maxElement-nums[i]);
        }
        return count;
    }
}