import java.util.*;

class Solution {
    public List<String> braceExpansionII(String expression) {
        int[] pos = new int[]{0}; 
        Set<String> resultSet = parse(expression, pos);
        
        List<String> resultList = new ArrayList<>(resultSet);
        Collections.sort(resultList);
        return resultList;
    }

    private Set<String> parse(String s, int[] pos) {
        List<Set<String>> unionSets = new ArrayList<>();
        Set<String> currentSet = new HashSet<>();
        currentSet.add(""); 

        while (pos[0] < s.length()) {
            char c = s.charAt(pos[0]);

            if (c == '{') {
                pos[0]++; 
                Set<String> nestedSet = parse(s, pos);
                currentSet = cartesianProduct(currentSet, nestedSet);
            } else if (c == '}') {
                pos[0]++; 
                break;   
            } else if (c == ',') {
                pos[0]++; 
                unionSets.add(currentSet); 
                
                currentSet = new HashSet<>();
                currentSet.add(""); 
            } else {
                pos[0]++;
                Set<String> literalSet = new HashSet<>();
                literalSet.add(String.valueOf(c));
                currentSet = cartesianProduct(currentSet, literalSet);
            }
        }

        unionSets.add(currentSet);

        Set<String> finalSet = new HashSet<>();
        for (Set<String> set : unionSets) {
            finalSet.addAll(set);
        }
        
        return finalSet;
    }
    private Set<String> cartesianProduct(Set<String> set1, Set<String> set2) {
        Set<String> res = new HashSet<>();
        for (String s1 : set1) {
            for (String s2 : set2) {
                res.add(s1 + s2);
            }
        }
        return res;
    }
}