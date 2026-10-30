class Solution {
    public int minSteps(String s, String t) {
         int[] carr = new int[26]; 
        for (int i = 0;i<s.length();i++) {
            carr[s.charAt(i) - 'a']++;
        }
        for (int i = 0;i<t.length();i++) {
            carr[t.charAt(i) - 'a']--;
        }
        int steps = 0;
        for (int c:carr) {
            if (c > 0) {
                steps += c;
            }
        }
        return steps;
    }
}