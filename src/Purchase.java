public class Purchase {
    //Store the amount of the purchase, the date of the transaction and where the purchase was made
    private double amount;
    private Date date;
    private String vendor;
    
    //Default constructor
    public Purchase(){
        amount = 0;
        date = new Date();
        vendor = "N/A";       
    }
    public Purchase(String date, String vendor, double amount){
        this.date = new Date(date);
        this.vendor = vendor;
        this.amount = amount;
    }
    
    @Override
    public String toString(){
        return date + "," + vendor + "," + amount;
    }
}
