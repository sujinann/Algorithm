import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String s = br.readLine();
            if (s.equals("0")){
                break;
            };

            boolean flag = true;
            for (int i=0; i<s.length()/2; i++){
                if (s.charAt(i) != s.charAt(s.length()-1-i)){
                    flag = false;
                    break;
                };
            };

            if (flag) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            };
        };
        
    }
}