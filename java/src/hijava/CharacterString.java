package hijava;

public class CharacterString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char c = 'A';		// cf. char c = 65;    or  char c = '\uD55C';
		byte b = 'A';
		System.out.println(c);
		System.out.println( (int)c );    // cf. (char)c  or   (char)b
		System.out.println(b);
		
		String str = "AB";
		System.out.println(str);
		System.out.println("AB".getBytes().length);
		System.out.println("AB한".getBytes().length);
//		윈도우는 문자 인코딩 시, MS-949를 사용하기 때문에 JAVA에서 한글 한 글자를 나타내는 데 2Byte로도 충분하지만, 기본 3Byte의 메모리를 할당하지만, 윈도우에서는 2Byte로 나타낸다.
	}

}
