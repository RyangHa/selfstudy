package chap2and3;

import java.util.Scanner;

public class chap2 {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		String inputData;
		String password="";
		while(password.length()!=6) {
			System.out.print("숫자를 입력해주세요: ");
			inputData=scanner.nextLine();
			int data=Integer.parseInt(inputData);
			char number=(char)data;
			String so1=String.valueOf(number);
			System.out.println(so1);
			password+=so1;		
			
		}
		System.out.print(password);

	}

}
