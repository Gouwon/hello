package hijava1_interface;

public class SubTotal {
	public int sum(int[] nums) {
		int result = 0;
		for (int i : nums)
			result += i;

		return result;
	}
}
