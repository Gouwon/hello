package hijava;

public class Student {
	
	private Integer studentId;
	private String name;
	private String telNo;
	private int age;
	private int score;
	
	public Student(int i, String name) {
		this.name = name;
		this.studentId = i;
	}

	public Student(int i, String string, int j) {
		// TODO Auto-generated constructor stub
		setStudentId(i);
		setName(string);
		setScore(j);
	}

	public Integer getStudentId() {
		return studentId;
	}

	public void setStudentId(Integer studentId) {
		this.studentId = studentId;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getTelNo() {
		if (this.telNo == null || this.telNo.length() <= 7)
			return telNo;
		else
			return this.telNo.substring(0, this.telNo.length() - 4) + "****";
	}

	public void setTelNo(String telNo) {
		this.telNo = telNo;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	@Override
	public String toString() {
		return "Student [studentId=" + studentId + ", name=" + name + ", telNo=" + telNo + ", age=" + age + "]";
	}

	public int getScore() {
		return score;
	}

	public void setScore(int score) {
		this.score = score;
	}

	
	
}
