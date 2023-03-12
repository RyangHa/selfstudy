package chap4;
import java.util.Scanner;

public class chap4of2 {

	public static void main(String[] args) throws Exception {
		Scanner sc=new Scanner(System.in);
		System.out.print("이름");
		String name=sc.nextLine();
		System.out.print("나이");
		int age=sc.nextInt();
		System.out.print("시간");
		int hour=sc.nextInt();
		System.out.print("분");
		int min=sc.nextInt();
		int keyCode;
		while(true) {
			keyCode=System.in.read();
			System.out.println("keyCode: "+keyCode);
			if (keyCode==113) {
				System.out.printf("이름: %1$s, 나이: %2$d, 과제 완료 시각: %3$d시 %4$d분,\t드디어 \"집\"에 간다..!",name,age,hour,min);
				System.out.print("\n종료");
				break;
			}
		}
		

	}

}
