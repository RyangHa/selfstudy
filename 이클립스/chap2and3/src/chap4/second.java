package chap4;
import java.util.Scanner;

public class second {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int maximum=sc.nextInt();
		for (int i=2;i<=maximum;i++) {
			int j = 2;
            while(i%j != 0) {
               j++;
               }
            if(i==j) {
            	System.out.println(j);
            }
		}
		sc.close();

	}

}
