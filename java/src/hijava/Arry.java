package hijava;

public class Arry {

	public static void main(String[] args) {
//		ex1();
//		ex2();
//		ex3();
//		ex5();
		ex6();
	}
	
	private static void ex6() {
		char[][] arr = new char[2][26];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				if (i == 0)
					arr[i][j] = (char)(j + 65);
				else
					arr[i][j] = (char)(j + 97);
			}	
		}
		
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println("");
		}	
	}

	private static void ex5() {
		int[] arr1 = {10, 20, 30, 40, 50};
		int[] arr2 = { 1, 2, 3, 4, 5 };
		System.arraycopy(arr1, 0, arr2, 2, 3);
		
		for (int i : arr2) {
			System.out.println(i);
		}
	}

	private static void ex3() {
		Man[] humans = new Man[9];
		int len = humans.length;
		for (int i = 0; i < len; i++) {
			humans[i] = new Man("김" + (i + 1) + "수");
			System.out.println(humans[i].getName());
		}
		
//		for (Man man : humans) {
//			System.out.println(man);
//		}
	}

	private static void ex2() {
		String[] strs = new String[100];
		int len = strs.length;
		for (int i = 0; i < len; i++) {
			strs[i] = "str" + (i + 1);
		}
		
		printArray(strs);
	}

	private static void ex1() {
		int[] nums = new int[100];
		
		for (int i = 0; i < nums.length; i++) {
			nums[i] = i + 1;
		}
		
		printArray(nums);
	}
	

	private static void printArray(int[] nums) {
		for (int i = 0; i < nums.length; i++) {
			System.out.println(nums[i]);
		}
	}
	
	private static void printArray(String[] strs) {
		for (int i = 0; i < strs.length; i++) {
			System.out.println(strs[i]);
		}
	}

}