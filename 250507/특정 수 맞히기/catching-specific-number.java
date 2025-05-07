import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num;
        while (true) {
            num = Integer.parseInt(br.readLine());
            if(num > 25) System.out.println("Lower");
            else if (num < 25) {
                System.out.println("Higher");
            } else {
                System.out.println("Good");
                break;
            }
        }
    }
}