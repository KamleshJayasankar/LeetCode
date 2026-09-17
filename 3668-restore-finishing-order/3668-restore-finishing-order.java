class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {
        boolean[] isFriend = new boolean[order.length + 1];
        for (int friend : friends) {
            isFriend[friend] = true;
        }

        int[] result = new int[friends.length];
        int idx = 0;

        for (int id : order) {
            if (isFriend[id]) {
                result[idx++] = id;
            }
        }

        return result;
    }
}