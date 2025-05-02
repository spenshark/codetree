import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int value;
        int[] array = new int[N];
        for(int i = 0; i < N; i++){
            value = sc.nextInt();
            array[i] = value * value;       
        }

        for(int i = 0; i < N ; i++){
            System.out.print(array[i] + " ");
        }
    }
}