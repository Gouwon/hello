package hijava;

public class WhileLoop {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i = 0;
		
		while (i++ < 10) {
			if (i > 5)
				break;
			
			if ((i % 2 == 0))
				continue;
			
			System.out.println(">>>>>>>>>>>>>>>>>>>>> i = " + i);
			
		}
	}
}
