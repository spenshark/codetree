import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                System.out.printf("%d * %d = %d", i, j, i * j);
                if(j < n) {
                    System.out.print(", ");
                }
            }
            System.out.println();
        }
    }
}