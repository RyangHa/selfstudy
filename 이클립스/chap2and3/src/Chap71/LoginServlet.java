package Chap71;

import java.util.Scanner;

public class LoginServlet extends HttpServlet {
	Scanner sc=new Scanner(System.in);
	
	@Override
	public void service() {
		System.out.println("set the id");
		String id=sc.nextLine();
		System.out.println("set the password");
		String password=sc.nextLine();
		
		System.out.println("input the id");
		String inputid=sc.nextLine();
		System.out.println("input the password");
		String inputpass=sc.nextLine();
		
		if (id.equals(inputid) && password.equals(inputpass)) {
			System.out.println("Login");
		}else if (id.equals(inputid) && !password.equals(inputpass)) {
			System.out.println("Wrong password");
		}else if (!id.equals(inputid) && password.equals(inputpass)) {
			System.out.println("Wrong id");
		}else {
			System.out.println("Both wrong");
		}
	}
	
}
