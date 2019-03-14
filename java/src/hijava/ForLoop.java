package hijava;

public class ForLoop {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 함수 생성 단축키는 command+1
//		sumByWhile();
		sumByFor();
	}

	private static void sumByFor() {
		// TODO Auto-generated method stub
		int total = 0;
		for (int i = 0; i <= 100; i++) {
			total += i;
		}
		
		System.out.println("result = " + total);
	}

	private static void sumByWhile() {
		// TODO Auto-generated method stub
		
	}
}
