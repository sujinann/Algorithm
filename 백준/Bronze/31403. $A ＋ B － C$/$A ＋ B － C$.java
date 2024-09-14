import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int A = Integer.parseInt(br.readLine().trim());
        int B = Integer.parseInt(br.readLine().trim());
        int C = Integer.parseInt(br.readLine().trim());

        int t = Integer.toString(B).length();
        
        int powerOfTen = (int) Math.pow(10, t);

        System.out.println(A + B - C);
        System.out.println(A * powerOfTen + B - C);
    }
}