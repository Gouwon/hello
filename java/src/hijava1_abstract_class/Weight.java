package hijava1_abstract_class;

/*
 * 
 * 무게(Weight) 클래스를 추상 클래스로 정의하고,
 * 이를 상속한 근(Guen: 600g)과 파운드(Pound: 453g) 클래스를 만들고,
 * 그램수를 반환하는 getGram() 함수를 각각 구현하시오.
 * 
 */


public abstract class Weight {
	public abstract int getGram(int n);

}
