import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int sum = 0;
        
        for (int i = 1; i <= 100; i++) {
            sum += i;
            if(sum >= n) {
                sb.append(i).append("\n");
                break;
            }
        }
        
        System.out.println(sb);
    }
}