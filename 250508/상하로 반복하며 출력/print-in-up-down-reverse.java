import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        int[][] arr2 = new int[n][n];
        int cnt;

        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }

        for (int i = 0; i < n; i++) {
            if(i % 2 == 0) {
                cnt = 0;
                for (int j = 0; j < n; j++) {
                    arr2[j][i] = arr[cnt++];
                }
            } else {
                cnt = n-1;
                for (int j = 0; j < n; j++) {
                    arr2[j][i] = arr[cnt--];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(arr2[i][j]);
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}