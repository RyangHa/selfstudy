package chap4;
import java.util.Scanner;

public class chap4 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num1,num2,num3;
		System.out.print("1번 숫자");
		num1=scanner.nextInt();
		System.out.print("2번 숫자");
		num2=scanner.nextInt();
		System.out.print("3번 숫자");
		num3=scanner.nextInt();
		double result=(double)num1*num2/num3;
		System.out.print("연산 결과: "+result);
		int result1=(int)result;
		if (result1==result==true) {
			System.out.print("좋아");
		}else {
			System.out.print("싫어");
		}
	}

}
