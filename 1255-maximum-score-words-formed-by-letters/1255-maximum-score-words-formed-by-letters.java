class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        int[] letterCount = new int[26];
        for (char ch : letters) {
            letterCount[ch - 'a']++;
        }

        return backtrack(words, 0, letterCount, score);
    }

    private int backtrack(String[] words, int index, int[] letterCount, int[] score) {
        if (index == words.length) {
            return 0;
        }

        int maxScore = backtrack(words, index + 1, letterCount, score);

        String word = words[index];
        boolean canForm = true;
        int wordScore = 0;
        int[] used = new int[26];

        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            used[ch - 'a']++;
            if (used[ch - 'a'] > letterCount[ch - 'a']) {
                canForm = false;
            }
            wordScore += score[ch - 'a'];
        }

        if (canForm) {
            for (int i = 0; i < 26; i++) {
                letterCount[i] -= used[i];
            }

            maxScore = Math.max(maxScore, wordScore + backtrack(words, index + 1, letterCount, score));

            for (int i = 0; i < 26; i++) {
                letterCount[i] += used[i];
            }
        }

        return maxScore;
    }
}