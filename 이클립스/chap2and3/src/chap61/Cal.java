package chap61;

public class Cal {
	static double pi = 3.14159;
	public double multi(double num1,double num2) {
		double result=(double)num1*num2;
		return result;
	}
	public double plus(double num1, double num2) {
		double result=(double)num1+num2;
		return result;
	}
	public double minus(double num1, double num2) {
		double result=(double)num1-num2;
		return result;
	}
	public double quot(double num1, double num2) {
		double result=(double)num1/num2;
		return result;
	}
	public double remain(double num1, double num2) {
		double result=(double)num1%num2;
		return result;
	}
	
	public static void main(String[] args) {
		Cal cal=new Cal();
		System.out.println(cal.multi(pi, 265));
		System.out.println(cal.plus(10, 5));
		System.out.println(cal.minus(10, 5));
		System.out.println(cal.quot(pi, 10));
		System.out.println(cal.remain(pi, 10));
		System.out.println(cal.plus(cal.minus(10, 5), cal.quot(pi, 10)));
	}
}
