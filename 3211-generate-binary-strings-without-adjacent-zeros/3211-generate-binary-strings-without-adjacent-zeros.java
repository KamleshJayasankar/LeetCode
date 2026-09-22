import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> validStrings(int n) {
        List<String> result = new ArrayList<>();
        generate(result, new StringBuilder(), n);
        return result;
    }
    
    private void generate(List<String> result, StringBuilder sb, int n) {
        if (sb.length() == n) {
            result.add(sb.toString());
            return;
        }
        
        int len = sb.length();
        
        sb.append('1');
        generate(result, sb, n);
        sb.setLength(len); 
        
        if (len == 0 || sb.charAt(len - 1) == '1') {
            sb.append('0');
            generate(result, sb, n);
            sb.setLength(len); 
        }
    }
}