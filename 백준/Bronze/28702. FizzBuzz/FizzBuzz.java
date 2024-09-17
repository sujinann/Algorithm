import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] arr = new String[3];
        for (int i=0; i<3; i++) {
            arr[i] = br.readLine();
        };

        String target;
        String answer = "";
        for (int i=0; i<3; i++) {
            if (arr[i].charAt(0) <= '9') {
                target = arr[i];
                int temp = Integer.parseInt(target);
                temp += 3-i;

                if (temp % 3 == 0) {
                    if (temp % 5 == 0) {
                        answer = "FizzBuzz";
                    } else {
                        answer = "Fizz";
                    };
                } else {
                    if (temp % 5 == 0) {
                        answer = "Buzz";
                    } else {
                        answer = Integer.toString(temp);
                    }
                };                
                break;
            }
        }

        System.out.println(answer);
    }
}
