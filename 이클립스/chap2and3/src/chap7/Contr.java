package chap7;

public class Contr {

	public static void main(String[] args) {
		Controller controller=new Controller();
		controller.setService(new MemberService());
		controller.service.login();
		
		controller.setService(new AService());
		controller.service.login();

	}

}
