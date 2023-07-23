public class Date {
    //Store date as a character array
    private char[] date = {' ',' ','/',' ',' ','/',' ',' ',' ',' '};

    public Date(){
        //Create curdate object
        long millis=System.currentTimeMillis();  
        java.sql.Date curDate = new java.sql.Date(millis);
        //Split curDate into a char array
        char[] tempArray = curDate.toString().toCharArray();
        int dateIndex = 6;
        //Fix formatting of curDate using for loops
        for(int i = 0; i < 4; i++){
            date[dateIndex] = tempArray[i];
            dateIndex++;
        }
        dateIndex = 0;
        for(int i = 5; i < 7; i++){
            date[dateIndex] = tempArray[i];
            dateIndex++;
        }
        dateIndex = 3;
        for(int i = 8; i < 10; i++){
            date[dateIndex] = tempArray[i];
            dateIndex++;
        }
    }
    public Date(String date){
        this.date = date.toCharArray();
    }


    @Override
    public String toString(){
        String temp = "";
        for(int i = 0; i < date.length; i++){
            temp += date[i];
        }
        return temp;
    }
}
