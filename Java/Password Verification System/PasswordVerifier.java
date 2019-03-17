
import static java.lang.Character.isDigit;
import static java.lang.Character.isUpperCase;

/*
 * This program uses the PasswordVerifier class to create an instance
 * of a PasswordVerifier. Through the use of the verifyPassword method
 * a String object will be evaluated.
 */
/**
 *
 * @author JewellWright
 */
public class PasswordVerifier {

    private PasswordSpecifications password;
/*  contructor method that builds an object that takes a PasswordSpecifications object*/
    public PasswordVerifier(PasswordSpecifications password) {
        this.password = password;
    }
/*  method that evaluates a String and returns a String*/
    public String verifyPassword(String pw) {
//  count variables
        int countUchars = 0;
        int countNum = 0;
//  conversion of a String to a char array     
        char passw[] = pw.toCharArray();
//  String elements that need to be returned      
        String checkminl, checkmaxl, checkminU, checkminNum;
//  compares the String length to the value of the maximum length      
        if (pw.length() > password.getMaxlength()) {
            checkmaxl = "F";
        } else {
            checkmaxl = "P";
        }
//  compares the String length to the vale of the minimum length      
        if (pw.length() < password.getMinlength()) {
            checkminl = "F";
        } else {
            checkminl = "P";
        }
//  loop that goes through the char away    
        for (int count = 0; count < pw.length(); count++) {
//  if statement that counts the uppercase chars          
            if (isUpperCase(passw[count]) == true) {
                countUchars++;
            }
        }
//  compare the number of uppercase chars to the minimum number of chars value      
        if (countUchars >= password.getNumUchars()) {
            checkminU = "P";
        } else {
            checkminU = "F";
        }
//  loop that goes through the char away 
        for (int count = 0; count < pw.length(); count++) {
//  if statement the counts the amount of digits         
            if (isDigit(passw[count]) == true) {
                countNum++;
            }
        }
//  if statement that compares the number of digits to the minimum value of digits      
        if (countNum >= password.getMinnumDigits()) {
            checkminNum = "P";
        } else {
            checkminNum = "F";
        }
//  output that indicates whether or note each word "P" or "F" each section      
        return checkmaxl + checkminl + checkminU + checkminNum;
    }
    
}
