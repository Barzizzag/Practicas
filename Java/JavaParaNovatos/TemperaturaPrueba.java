package JavaParaNovatos;
import java.util.Scanner;

public class TemperaturaPrueba {
    public static void main (String []args){
        
            //Prueba Temperatura
        double temp =0;
        String cualTemp;
        Scanner sc= new Scanner(System.in);
        Temperatura tp = new Temperatura();
        
        System.out.print("Ingrese C para convertir a grados Celsius o F para convertir a grados Farenheit: ");
        cualTemp = sc.nextLine().toUpperCase();
        System.out.print("Ingrese la temperatura: ");
        temp= sc.nextDouble();
        if (cualTemp.equals("C")){
            System.out.println ("La temperatura en grados celsius es: "+tp.aCelsius(temp));
        }else if (cualTemp.equals("F")){
            System.out.println ("La temperatura en grados farenheit es: "+tp.aFarenheit(temp));
        }else {
            System.out.println("No existe ese sistema de medicion de temperatura!");
        }     
        System.out.println(cualTemp);
        
    }
}
