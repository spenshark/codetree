import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ch = br.readLine();

        String[] arr = {"apple", "banana", "grape", "blueberry", "orange"};

        ArrayList<String> fruits = new ArrayList<>(Arrays.asList(arr));

        int count = 0;

        for (String fruit : fruits) {
            if (fruit.charAt(2) == ch.charAt(0) || fruit.charAt(3) == ch.charAt(0)) {
                System.out.println(fruit);
                count++;
            }
        }

        System.out.println(count);
    }
}