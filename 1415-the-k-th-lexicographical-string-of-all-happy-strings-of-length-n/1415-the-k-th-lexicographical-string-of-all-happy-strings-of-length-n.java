class Solution {
    private int count = 0;
    private String result = "";

    public String getHappyString(int n, int k) {
        backtrack(n, k, new StringBuilder());
        return result;
    }

    private boolean backtrack(int n, int k, StringBuilder sb) {
        if (sb.length() == n) {
            count++;
            if (count == k) {
                result = sb.toString();
                return true; 
            }
            return false;
        }
        for (char c = 'a'; c <= 'c'; c++) {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == c) {
                continue;
            }
            
            sb.append(c);
            
            if (backtrack(n, k, sb)) {
                return true;
            }
            
            sb.deleteCharAt(sb.length() - 1);
        }
        
        return false;
    }
}