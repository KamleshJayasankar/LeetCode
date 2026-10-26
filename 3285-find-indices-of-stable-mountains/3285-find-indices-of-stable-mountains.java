class Solution {
    public List<Integer> stableMountains(int[] height, int threshold) {
        List<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < height.length - 1; i++) {
            int prv = height[i];
            if (prv > threshold) {
                ans.add(i + 1);
            }
        }
        
        return ans;
    }
}