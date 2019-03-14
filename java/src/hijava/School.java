package hijava;

public class School {

	public static void main(String[] args) {
		
		Score korean = new Score();
		korean.setSubject("국어");
		korean.setScore(90);
		String k = korean.toString();
		System.out.println(korean);
		System.out.println(korean.toString());	// 다른 타입을 프린트할 때의 정석.
		System.out.println(k);
		
		Score math = new Score("수학", 80);
		System.out.println(math.toString());
		
		Score science = new Score("과학");
		System.out.println(science.toString());
	}

}
