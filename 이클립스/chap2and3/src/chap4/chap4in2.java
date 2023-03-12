package chap4;
import java.util.Scanner;

public class chap4in2 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("메뉴를 선택하세요.:");
		System.out.println("1. 로그인 2. 회원가입 3. 종료");
		int num=sc.nextInt();
		switch(num) {
		case 1: 
			System.out.println("아이디를 입력하세요.");
			String id=sc.next();
			System.out.println("비밀번호를 입력하세요.");
			String pw=sc.next();
			if (id.equals("abc")) {
				if (pw.equals("1234")) {
					System.out.println("로그인이 되었습니다.");
				}else {
					System.out.println("비밀번호를 틀렸습니다.");
				}
			}else {
				System.out.println("아이디가 존재하지 않습니다.");
			}
			sc.close();
			break;
		case 2:
			System.out.println("회원가입 메뉴입니다.");
			break;
		case 3:
			System.out.println("시스템을 종료합니다.");
			break;
		default:
			System.out.println("잘못된 메뉴를 선택했습니다.");
		}
	}

}
