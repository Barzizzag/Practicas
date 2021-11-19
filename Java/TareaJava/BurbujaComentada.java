package TareaJava;

import java.util.Scanner;

public class BurbujaComentada{
public static void main (String []args){
    Scanner sc =new Scanner(System.in);
    int ordOk=0;
    boolean ordenado=false;
    System.out.print("Ingrese la cantidad de numeros a ordenar: ");
    int n=sc.nextInt();
    int  aOrdenar[]= new int[n];
    //Cargamos los datos
    for (int x=0; x<aOrdenar.length; x++){
        System.out.print("Numero: "); 
        aOrdenar[x]=sc.nextInt();
    }
    while (ordenado==false){
        for (int i=0; i<(aOrdenar.length-1); i++){
            //System.out.println ("Reset al valor de i? "+i);
            if (aOrdenar[i]>aOrdenar[i+1]){
                //System.out.println ("Antes del cambio en: "+i + " anterior "+aOrdenar[i]+" posterior "+aOrdenar[i+1]);
                //ordenado=false;
                int aux=aOrdenar[i];
                //System.out.println (aux);
                aOrdenar[i]=aOrdenar[i+1];
                //System.out.println (aOrdenar[i]);
                aOrdenar[i+1]=aux;
                //System.out.println (aOrdenar[i+1]);
                //System.out.println ("Despues del cambio en: " +i + " anterior "+aOrdenar[i]+" posterior "+aOrdenar[i+1]);
                ordOk-=1;
            }else {
                //System.out.println ("salida por else en: "+i);
                //System.out.println (aOrdenar[i]+", "+aOrdenar[i+1]);
                ordOk+=1;
            }  
        }
        if (ordOk>=aOrdenar.length){
            ordenado=true;
        }
        //System.out.println("Fin del for");
    }
    for (int y=0; y<aOrdenar.length;y++){
        System.out.print(aOrdenar[y]+", ");
    }
//System.out.print("Hola mundo");
}
}