import java.util.Arrays;

class Solution {
    private int[] prod;
    private int[][] freq;
    private int K;
    
    public int[] resultArray(int[] nums, int k, int[][] queries) {
        int n = nums.length;
        this.K = k;
        
        prod = new int[4 * n];
        freq = new int[4 * n][k];
        
        build(0, 0, n - 1, nums);
        
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int idx = queries[i][0];
            int val = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];
            
            update(0, 0, n - 1, idx, val % k);
            
            Node res = query(0, 0, n - 1, start, n - 1);
            ans[i] = (res != null) ? res.freq[x] : 0;
        }
        
        return ans;
    }
    
    private void build(int node, int start, int end, int[] nums) {
        if (start == end) {
            prod[node] = nums[start] % K;
            freq[node][nums[start] % K] = 1;
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node + 1, start, mid, nums);
        build(2 * node + 2, mid + 1, end, nums);
        mergeNode(node, 2 * node + 1, 2 * node + 2);
    }
    
    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            prod[node] = val;
            Arrays.fill(freq[node], 0); 
            freq[node][val] = 1;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) {
            update(2 * node + 1, start, mid, idx, val);
        } else {
            update(2 * node + 2, mid + 1, end, idx, val);
        }
        mergeNode(node, 2 * node + 1, 2 * node + 2);
    }
    
    private void mergeNode(int parent, int left, int right) {
        prod[parent] = (prod[left] * prod[right]) % K;
        
        for (int i = 0; i < K; i++) {
            freq[parent][i] = freq[left][i];
        }
        
        int leftProd = prod[left];
        for (int i = 0; i < K; i++) {
            freq[parent][(leftProd * i) % K] += freq[right][i];
        }
    }
    
    private class Node {
        int prod;
        int[] freq = new int[K];
    }
    
    private Node query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return null;
        }
        
        if (l <= start && end <= r) {
            Node res = new Node();
            res.prod = prod[node];
            for (int i = 0; i < K; i++) {
                res.freq[i] = freq[node][i];
            }
            return res;
        }
        
        int mid = (start + end) / 2;
        Node left = query(2 * node + 1, start, mid, l, r);
        Node right = query(2 * node + 2, mid + 1, end, l, r);
        
        if (left == null) return right;
        if (right == null) return left;
        
        Node res = new Node();
        res.prod = (left.prod * right.prod) % K;
        
        for (int i = 0; i < K; i++) {
            res.freq[i] = left.freq[i];
        }
        for (int i = 0; i < K; i++) {
            res.freq[(left.prod * i) % K] += right.freq[i];
        }
        
        return res;
    }
}