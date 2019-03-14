package hijava;

public class IfElse {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long ctm = System.currentTimeMillis() % 10;
		System.out.println("ctm=" + ctm);
		
		long sct = ctm % 3;
		
		if (sct == 1) {
			System.out.println("One");
		} 
		else if (sct == 2) {
			System.out.println("Two");
		} 
		else {
			System.out.println("Zero");
		}
	}
}
