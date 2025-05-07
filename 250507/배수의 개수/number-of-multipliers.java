import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num;
        int count3 = 0;
        int count5 = 0;

        for (int i = 0; i < 10; i++) {
            num = Integer.parseInt(br.readLine());
            if(num % 3 == 0) {
                count3++;
            }
            if (num % 5 == 0) {
                count5++;
            }
        }

        System.out.println(count3 + " " + count5);
    }
}