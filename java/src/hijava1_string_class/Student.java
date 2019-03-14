package hijava1_string_class;

public class Student implements Cloneable{
//	학번(id)과 이름(name)을 갖는 학생(Student) 클래스를 만들고,
//	각각의 getter, setter를 만드시오.

	private int id;
	private String name;
	
	public Student() {
		
	}
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public Student(int i, String string) {
		this.setId(i);
		this.setName(string);
	}

	public Student(String name, int id) {
		this.setId(id);
		this.setName(name);
	}

	public void setInfo(String name, int id) {
		this.setId(id);
		this.setName(name);
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return getName() + "(" + getId() + ")";
	}

	@Override
	public boolean equals(Object obj) {
//		if (this == obj)	 // 동일한 메모리 주소면 true(==연산에서)
//			return true;
//		if (obj == null)	 // this는 절대 null이 될 수 없으므로, obj가 null이면 false
//			return false;
//		if (getClass() != obj.getClass())	// 동일한 class가 아니면 false
//			return false;
//		Student other = (Student) obj;		
//		if (id != other.id)
//			return false;
//		if (name == null) {
//			if (other.name != null)
//				return false;
//		} else if (!name.equals(other.name))
//			return false;
//		return true;
		
		Student other = (Student) obj;
		return this.name != null && this.id == other.id && this.name.equals(other.name);
		
		
	}

	@Override
	protected Object clone() throws CloneNotSupportedException {
		Student cloned_object = (Student)super.clone();
		cloned_object.setName(cloned_object.getName() + " 복제본");
		return cloned_object;
	}

}
