package chap61;

public class MyDate {
	private int day;
	private int month;
	private int year;
	private boolean isValid;
	public MyDate(int day, int month, int year){
		this.day=day;
		this.month=month;
		this.year=year;
		setYear(year);
		setMonth(month);
		setDay(day);
	}
	public int getDay() {
		return day;
	}
    void setDay(int day) {
    	switch (getMonth()) {
    	case 1: case 3: case 5: case 7: case 8: case 10: case 12:
    		if (day<1||day>31) {
    			isValid=false;
    		}else {
    			isValid=true;
    		}
    		break;
    	case 4: case 6: case 9: case 11:
    		if (day<1||day>30) {
    			isValid=false;
    		}else {
    			isValid=true;
    		}
    		break;
    	case 2:
    		if (year%4==0 && year%100!=0) {
    			if (day<1) {
    				isValid=false;
    			}else if(day>29) {
    				isValid=false;
    			}else {
    				isValid=true;
    			}
    		}else if (year%400==0) {
    			if (day<1||day>29) {
    				isValid=false;
    			}else {
    				isValid=true;
    			}
    		}else {
    			if (day<1||day>28) {
    				isValid=false;
    			}else {
    				isValid=true;
    			}
    		}
    	}
		
	}
    public int getMonth() {
    	return month;
    }
    void setMonth(int month) {
		if (getMonth()>12||getMonth()<1) {
			isValid=false;
		}else {
			isValid=true;
		}
	}
    public int getYear() {
    	return year;
    }
	void setYear(int year) {
		if (getYear()<1) {
			isValid=false;
		}else {
			isValid=true;
		}
	}
	public void isValid() {
		if (isValid==false) {
			System.out.println("유효하지 않은 날짜입니다.");
		}else {
			System.out.println("유효한 날짜입니다.");
		}
	}
	
	public static void main(String[] args) {
		MyDate md=new MyDate(29,2,2019);
		md.isValid();
	}

}
