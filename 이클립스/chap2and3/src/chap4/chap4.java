package chap4;
import java.util.Scanner;

public class chap4 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num1,num2,num3;
		System.out.print("1�� ����");
		num1=scanner.nextInt();
		System.out.print("2�� ����");
		num2=scanner.nextInt();
		System.out.print("3�� ����");
		num3=scanner.nextInt();
		double result=(double)num1*num2/num3;
		System.out.print("���� ���: "+result);
		int result1=(int)result;
		if (result1==result==true) {
			System.out.print("����");
		}else {
			System.out.print("�Ⱦ�");
		}
	}

}
