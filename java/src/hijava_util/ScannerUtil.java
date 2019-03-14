package hijava_util;

import java.util.Scanner;
import hijava1_interface.CalcOper;

public class ScannerUtil {

	public static void scanner() {
		System.out.print("메시지를 입력하세요>> ");
		Scanner scanner = new Scanner(System.in);
		String msg = scanner.nextLine();
		System.out.println("Input Message is " + msg);

	}

	// 두개의 숫자와 연산자(*,/)를 입력 받아, CalcOper 클래스를 이용하여 연산 결과를 출력하는 코드를 작성하시오.
	public static void scanner1() {

		Scanner scanner = new Scanner(System.in);
		boolean loof = true;
		while (loof) {
			System.out.print("계산할 연산식을 입력하세요>> ");
			String msg = scanner.nextLine();

			System.out.println("Input Message is " + msg);
			String[] msg2 = msg.split(" ");

			if (msg2[0].equals("quit")) {
				System.out.println("Calc End!");
				loof = false;
				break;
			} else {
				int x = Integer.parseInt(msg2[0]);
				int y = Integer.valueOf(msg2[2]);
				String arvg = msg2[1];
			
				
				hijava1_interface.CalcOper co = new hijava1_interface.CalcOper();

				int result = 0;
				if (arvg.equals("*") == true) {
					result = co.mul(x, y);
					System.out.println(msg + " = " + result);
				} else if (arvg.equals("/") == true) {
					result = co.div(x, y);
					System.out.println(msg + " = " + result);
				} else
					System.out.println("InputError");
			}
		}
		scanner.close();
	}
}
