class Solution {

    public String reversePrefix(String s, int k) {
        char[] characters = s.toCharArray();
        for (int leftIndex = 0, rightIndex = k - 1;
             leftIndex < rightIndex;
             leftIndex++, rightIndex--) {
            char temporaryCharacter = characters[leftIndex];
            characters[leftIndex] = characters[rightIndex];
            characters[rightIndex] = temporaryCharacter;
        }

        return new String(characters);
    }
}