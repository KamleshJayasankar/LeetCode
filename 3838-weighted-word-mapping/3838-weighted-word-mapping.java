class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder result = new StringBuilder();
        
        for (String word : words) {
            int currentWeight = 0;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                currentWeight += weights[c - 'a'];
            }
            
            int modValue = currentWeight % 26;
            char mappedChar = (char) ('z' - modValue);
            
            result.append(mappedChar);
        }
        
        return result.toString();
    }
}