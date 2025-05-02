import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        
        int[] array = new int[10];
        for(int i = 0; i < 10; i++){
            if(i == 0){
                array[i] = a;
            } else if(i == 1){
                array[i] = b;
            } else {
                array[i] = (array[i-1] + array[i-2]) % 10;
            }
        }

        for(int i = 0; i < 10 ; i++){
            System.out.print(array[i] + " ");
        }
    }
}