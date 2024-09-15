import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int l = Integer.parseInt(br.readLine());
        String s = br.readLine();

        long answer = 0;
        long p = 1;
        for (int i=0; i<s.length(); i++) {
            answer += (s.charAt(i) - 'a' + 1) * p;
            p = (p * 31) % 1234567891;
        }

        answer %= 1234567891;
        
        System.out.println(answer);
    }
}