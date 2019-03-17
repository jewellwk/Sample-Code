/*
 * This program uses the PasswordSpecifications class to create an instance
 * of PasswordSpecifications. The properties of this object are minimum length,
 * maximum length, minimum number of uppercase characters, and minimum number of 
 * digits.
 */

/**
 *
 * @author JewellWright
 */
public class PasswordSpecifications { 
/*  properties of the PasswordSpecification class*/
    private int minlength;
    private int maxlength;
    private int minNumUchars;
    private int minNumDigits;
/*  overridden constructor method*/
    public PasswordSpecifications (int minlength, int maxlength,
    int minNumUchars, int minNumDigits) {
        this.maxlength = maxlength;
        this.minlength = minlength;
        this.minNumDigits = minNumDigits;
        this.minNumUchars = minNumUchars;
        
    }
/*  default constructor method for user input*/
    public PasswordSpecifications () {
        this.maxlength = 0;
        this.minlength = 0;
        this.minNumDigits = 0;
        this.minNumUchars = 0;
    }
/* returns the maximum value for the length*/   
    public int getMaxlength (){
        return this.maxlength;
    }
/*  returns the minimum value for the length*/  
    public int getMinlength (){
        return this.minlength;
    }
/*  returns the minimum number of digits necessary*/   
    public int getMinnumDigits (){
        return this.minNumDigits;
    }
/*  returns the number of chars necessary*/  
    public int getNumUchars (){
        return this.minNumUchars;
    }
/*  sets the maximum length*/
    public void setMaxLenth(int maxLength){
        this.maxlength = maxLength;      
    }
/*  sets the minimum length*/   
    public void setMinLength(int minLength){
        this.minlength = minLength;      
    }
/*  sets the minimum number of digits*/    
    public void setMinNumDigits(int minNumDigits ){
        this.minNumDigits = minNumDigits;
    }
/*  sets the minimum number of uppercase chars*/   
    public void setNumUchars (int numUchars){
        this.minNumUchars = numUchars;
    }
/* overridden toString method that returns the PasswordSpecifications object
 in proper format*/
    @Override
    public String toString () {
        return "PASSWORD SPECIFICATIONS "
                + "\nMaximum password length:  " + maxlength
                + "\nMinimum password length: " + minlength
                + "\nMinimum number of Uppercase letters: " + minNumUchars
                + "\nMinimum number of digits: " + minNumDigits;
    }

}
