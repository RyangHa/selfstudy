package chap4;
import java.util.Scanner;

public class chap4in2 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("�޴��� �����ϼ���.:");
		System.out.println("1. �α��� 2. ȸ������ 3. ����");
		int num=sc.nextInt();
		switch(num) {
		case 1: 
			System.out.println("���̵� �Է��ϼ���.");
			String id=sc.next();
			System.out.println("��й�ȣ�� �Է��ϼ���.");
			String pw=sc.next();
			if (id.equals("abc")) {
				if (pw.equals("1234")) {
					System.out.println("�α����� �Ǿ����ϴ�.");
				}else {
					System.out.println("��й�ȣ�� Ʋ�Ƚ��ϴ�.");
				}
			}else {
				System.out.println("���̵� �������� �ʽ��ϴ�.");
			}
			sc.close();
			break;
		case 2:
			System.out.println("ȸ������ �޴��Դϴ�.");
			break;
		case 3:
			System.out.println("�ý����� �����մϴ�.");
			break;
		default:
			System.out.println("�߸��� �޴��� �����߽��ϴ�.");
		}
	}

}
