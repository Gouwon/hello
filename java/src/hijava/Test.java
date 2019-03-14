package hijava;

public class Test {

	public static void main(String[] args) {
		String txt = "Please locate where 'locate' occurs!";
		System.out.println(txt.indexOf("where"));
		
		String x = "10";
		String y = "20";
		int z = 3;
//		System.out.println(y * z);
		System.out.println(x + y);
		
		//Note that if the default statement is used as the last statement in a switch block, it does not need a break.
		int day = 4;
		switch (day) {
		  default:
			System.out.println("Weekend");
//			break;
		  case 6:
		    System.out.println("Saturday");
//		    break;
		    
		  case 7:
		    System.out.println("Sunday");
		    break;
		    
//		  default:
//			System.out.println("Weekend");
		}
	}

}
