package chap61;

public class SelfNumber {
	public static void notselfnum() {
		boolean numar[]=new boolean[10000];
		for (int i=0;i<10000;++i){
			int num2=selfnum(i);
			if (num2<10000) {
				numar[num2]=true;
			}
		}
		for (int i=0;i<10000;i++) {
			if (numar[i]==false) {
				System.out.println(i);
			}
		}
	}
	public static int selfnum(int num1) {
		int num2=num1;
		while (num1>0) {
			num2+=num1%10;
			num1/=10;
		}
		return num2;
	}
	public static void main(String[] args) {
		notselfnum();
	}

}

/*
String num2=String.valueOf(num1);
int finalNum=num1;
int numar[];
numar=new int[1000000000];
for (int i=0;i<num2.length();i++) {
	switch(i) {
	case 0:
		int k=num1%10; 
		System.out.println(k);
		finalNum+=k;
		break;
	case 1:
		char k11=num2.charAt(1);
		int k1=(int)k11;
		System.out.println(k1);
		finalNum+=k1;
		break;
	case 2:
		char k22=num2.charAt(2);
		int k2=(int)k22;
		System.out.println(k2);
		finalNum+=k2;
		break;
	case 3:
		char k33=num2.charAt(3);
		int k3=(int)k33;
		System.out.println(k3);
		finalNum+=k3;
		break;
	}
}
if (finalNum<10000) {
	numar[i]=finalNum;
	System.out.println(finalNum);
}
*/