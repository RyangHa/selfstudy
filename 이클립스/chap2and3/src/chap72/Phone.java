package chap72;

public abstract class Phone {
	String owner;
	public Phone(String owner) {
		
	}
	public void Ring() {
		System.out.println("");
	}
	public void TurnOn() {
		System.out.println("Turn on the phone.");
	}
	public void PickupPhone() {
		System.out.println("Pick up the phone.");
		System.out.println("Hello!");
	}
	public void Answer() {
		System.out.println("You respond to what the other person is saying.").
		System.out.println("Yes.");
	}
	public void TurndownPhone() {
		System.out.println("Turn down the phone.");
	}
	public void turnOff() {
		System.out.println("Turn off the phone.");
	}
}
