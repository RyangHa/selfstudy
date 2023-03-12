package chap4;
import java.util.Scanner;

public class thirdp {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		double a,b,c;
		a=sc.nextDouble();
		b=sc.nextDouble();
		c=sc.nextDouble();
		if (a>=b) {
			if (b>=c) {
				System.out.println(c);
			}else {
				System.out.println(b);
			}
		}else if (b>a) {
			if (a>=c) {
				System.out.println(c);
			}else {
				System.out.println(a);
			}
		}

	}

}
