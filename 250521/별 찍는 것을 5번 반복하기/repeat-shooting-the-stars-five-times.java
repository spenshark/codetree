
public class Main {
    public static void main (String args[]) {
        for (int i = 0; i < 5; i++) {
            star();
        }
    }

    private static void star() {
        for (int i = 0; i < 10; i++) {
            System.out.print("*");
            if(i== 9) {
                System.out.println();
            }
        }
    }
}

