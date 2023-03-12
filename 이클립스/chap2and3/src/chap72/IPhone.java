package chap72;

public class IPhone extends Phone {
	public IPhone(String owner) {
		super(owner);
		this.owner=owner;
	}
	public void TakeSelfie() {
		System.out.println("Take a selfie.");
		System.out.println("Click!");
	}
	public void LivePhoto() {
		System.out.println("Take the live-photo.");
		System.out.println("Press the button for 5 sec.");
		System.out.println("Click!");
	}
	public void Battery() {
		System.out.println("Battery: "+Math.random()*101);
	}
}
