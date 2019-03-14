package hijava;
/**
 * 첫 번째 자바 실
 * @author gouwon
 * @update say함수 추가(2019-01-12 by gouwon)
 */
public class HelloJava {
	/*
	 * 파일 실행 단축키는 fn+control+F11 
	 * 자동 완성 단축키는 command+space
	 * 코드 indentation는 command+shift+f
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello, Java World!");
		HelloJava.say("This is function call.");
	}

	public static void say(String msg) {
		System.out.println(msg);
	}

}
