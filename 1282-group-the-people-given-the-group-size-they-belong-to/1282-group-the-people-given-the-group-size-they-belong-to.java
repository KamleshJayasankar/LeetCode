import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        List<List<Integer>> result = new ArrayList<>();
        Map<Integer, List<Integer>> buckets = new HashMap<>();

        for (int i = 0; i < groupSizes.length; i++) {
            int size = groupSizes[i];
            
            buckets.putIfAbsent(size, new ArrayList<>());
            List<Integer> currentGroup = buckets.get(size);
            currentGroup.add(i);

            if (currentGroup.size() == size) {
                result.add(currentGroup);
                buckets.remove(size);
            }
        }

        return result;
    }
}