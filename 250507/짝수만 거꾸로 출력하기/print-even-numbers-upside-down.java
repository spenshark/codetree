import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        ArrayList<Integer> nums = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (num % 2 == 0) {
                nums.add(num);
            }
        }

        for (int i = nums.size() - 1; i >= 0; i--) {
            System.out.print(nums.get(i) + " ");
        }
    }
}