import java.util.HashMap;
import java.util.Map;

public class Codec {
    // Stores the mapping from the short URL suffix to the original long URL
    private final Map<String, String> urlMap = new HashMap<>();
    // A counter to generate unique IDs for each new URL
    private int id = 0;
    // The base domain required for the short URL structure
    private static final String BASE_URL = "http://tinyurl.com/";

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        id++;
        String shortKey = Integer.toString(id);
        urlMap.put(shortKey, longUrl);
        return BASE_URL + shortKey;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        // Extract the unique key by removing the base URL prefix
        String shortKey = shortUrl.replace(BASE_URL, "");
        return urlMap.get(shortKey);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));