import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[][] arr1 = new int[3][3];
        for(int i = 0; i < 3; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j <3 ; j++){
                arr1[i][j] = Integer.parseInt(st.nextToken()) ;
            }
        }

        br.readLine();

        int[][] arr2 = new int[3][3];
        for(int i = 0; i < 3; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j <3 ; j++){
                arr2[i][j] = Integer.parseInt(st.nextToken()) ;
            }
        }

        for(int i = 0; i < 3; i++){
            for(int j = 0; j <3 ; j++){
                System.out.print(arr1[i][j] * arr2[i][j] + " ");
            }
            System.out.println();

        }
    }
}