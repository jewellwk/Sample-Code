/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author JewellWright
 */
public class GravityCalculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       results (-9.81, 0, 10, 0, 0);
        
    }
    public static void results (double gravity, double initialVelocity, 
            double fallingTime, double initialPosition, double finalPosition) {
        double result = 
                (0.5 * gravity * Math.pow(fallingTime, 2)) 
                + initialVelocity
                + initialPosition;
        System.out.println("The object's position after " +fallingTime +
                " seconds is " +result + " m.");
        
    }
    
}

// x(t) = 0.5 * at^2 + vit + xi
// a = -9.81 = acceleration (m/s^2)
// t = 10 = time (s)
// vi = 0 = initial velocity (m/s^2)
// xi = 0 = ititial position 
// The correct value is -490.5m 