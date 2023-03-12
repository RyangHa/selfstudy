package chap4;
import java.util.Scanner;

public class problem {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int Celsius;
		Celsius=scanner.nextInt();
		double Fahrenheit=(double)9/5*Celsius+(double)32;
		System.out.print(Fahrenheit);
		scanner.close();

	}

}
