public class Purchase {
    //Store the amount of the purchase, the date of the transaction and where the purchase was made
    private int amount;
    private Date date;
    private String vendor;
    
    public Purchase(){
        amount = 0;
        date = new Date();
        vendor = "N/A";       
    }
}
