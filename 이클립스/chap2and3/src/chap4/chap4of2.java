package chap4;
import java.util.Scanner;

public class chap4of2 {

	public static void main(String[] args) throws Exception {
		Scanner sc=new Scanner(System.in);
		System.out.print("�̸�");
		String name=sc.nextLine();
		System.out.print("����");
		int age=sc.nextInt();
		System.out.print("�ð�");
		int hour=sc.nextInt();
		System.out.print("��");
		int min=sc.nextInt();
		int keyCode;
		while(true) {
			keyCode=System.in.read();
			System.out.println("keyCode: "+keyCode);
			if (keyCode==113) {
				System.out.printf("�̸�: %1$s, ����: %2$d, ���� �Ϸ� �ð�: %3$d�� %4$d��,\t���� \"��\"�� ����..!",name,age,hour,min);
				System.out.print("\n����");
				break;
			}
		}
		

	}

}
