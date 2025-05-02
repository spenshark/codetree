import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A_math_score = sc.nextInt();
        int B_math_score = sc.nextInt();
        int A_english_score = sc.nextInt();
        int B_english_score = sc.nextInt();

        if(A_math_score >= B_math_score && A_english_score >= B_english_score){
            System.out.print("1");
        } else{
            System.out.print("0");
        }
    }
}