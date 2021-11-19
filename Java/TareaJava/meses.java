package TareaJava;

import java.util.Scanner;

public class meses {
    /*
    public static void main(String args[]) {
      System.out.print ("Ingrese el número del mes: ");
      int numero;
      Scanner numIng = new Scanner (System.in);
      numero =numIng.nextInt();
      
      if (numero==1){
          System.out.println ("El mes ingresado es enero");
      }else if (numero==2){
          System.out.println ("El mes ingresado es febrero");
      }else if (numero==3){
          System.out.println ("El mes ingresado es marzo");
      }else if (numero==4){
          System.out.println ("El mes ingresado es abril");
      }else if (numero==5){
          System.out.println ("El mes ingresado es mayo");
      }else if (numero==6){
          System.out.println ("El mes ingresado es junio");
      }else if (numero==7){
          System.out.println ("El mes ingresado es julio");
      }else if (numero==8){
          System.out.println ("El mes ingresado es agosto");
      }else if (numero==9){
          System.out.println ("El mes ingresado es septiembre");
      }else if (numero==10){
          System.out.println ("El mes ingresado es octubre");
      }else if (numero==11){
          System.out.println ("El mes ingresado es noviembre");
      }else if (numero==12){
          System.out.println ("El mes ingresado es diciembre");
      }else {
          System.out.println ("Ingreso un numero equivocado ");
    	}
}
*/

//Con Case
    public static void main(String args[]) {
      System.out.print ("Ingrese el número del mes: ");
      int numero;
      Scanner numIng = new Scanner (System.in);
      numero =numIng.nextInt();
    
    switch (numero)  {
        case 1:
            System.out.println ("Enero");
            break;
        case 2:
            System.out.println ("Febrero");
            break;
        case 3:
            System.out.println("Marzo");
            break;
        case 4:
            System.out.println("Abril");
            break;
        case 5:
            System.out.println("Mayo");
            break;
        case 6:
            System.out.println("Junio");
            break;
        case 7:
            System.out.println("Julio");
            break;
        case 8:
            System.out.println("Agosto");
            break;
        case 9:
            System.out.println("Septiembre");
            break;
        case 10:
            System.out.println("Octubre");
            break;        
        case 11:
            System.out.println("noviembre");
            break;
        case 12:
            System.out.println("diciembre");
            break;
        default:
            System.out.println("Numero ingresado incorrecto");
        }
    }
}