class Solution {
    public int numberOfBeams(String[] bank) {
        int totalBeams = 0;
        int prevDevices = 0;
        
        for (String row : bank) {
            int currentDevices = 0;
            
            for (int i = 0; i < row.length(); i++) {
                if (row.charAt(i) == '1') {
                    currentDevices++;
                }
            }
            
            if (currentDevices > 0) {
                totalBeams += prevDevices * currentDevices;
                prevDevices = currentDevices;
            }
        }
        
        return totalBeams;
    }
}