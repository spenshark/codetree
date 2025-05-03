import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next();
        int len = word.length();
        word = word.charAt(0) + "a" + word.substring(2, len-2) + 'a' + word.charAt(len-1);

        System.out.println(word);
    }
}