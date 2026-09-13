class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] result = new int[n];

        int lessCount = 0;
        int equalCount = 0;
        for (int num : nums) {
            if (num < pivot) {
                lessCount++;
            } else if (num == pivot) {
                equalCount++;
            }
        }
        
        int left = 0;
        int mid = lessCount;
        int right = lessCount + equalCount;
        
        for (int num : nums) {
            if (num < pivot) {
                result[left++] = num;
            } else if (num == pivot) {
                result[mid++] = num;
            } else {
                result[right++] = num;
            }
        }
        
        return result;
    }
}