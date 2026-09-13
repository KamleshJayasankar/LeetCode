class Solution {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int[] answer = new int[n];

        int balls = 0;
        int operations = 0;
        for (int i = 0; i < n; i++) {
            answer[i] += operations;
            balls += boxes.charAt(i) - '0';
            operations += balls;
        }

        balls = 0;
        operations = 0;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] += operations;
            balls += boxes.charAt(i) - '0';
            operations += balls;
        }

        return answer;
    }
}