package UTN;

import java.util.Scanner;

public class SubCadena {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la cadena: ");
        String cadena = sc.nextLine();
        System.out.println("Ingrese la subcadena a buscar: ");
        String subCadena = sc.nextLine();
        Integer largoTotal = cadena.length();
        Integer largoSub = subCadena.length();
        Integer diferencia = largoTotal - largoSub;
        for (Integer i = 0; i <= diferencia; i++) {
            String auxiliarCadena = cadena.substring(i, (i + largoSub));
            if (auxiliarCadena.equals(subCadena)) {
                System.out.println("La subcadena " + subCadena + " se encuentra entre: " + i + " y " + (i + largoSub));
                /*Si descomentamos la siguiente linea el ciclo termina al encontrar la primer coincidencia. */
                //i = diferencia;
            } else if (i == diferencia) {
                System.out.println("La subcadena no se encuentra en el texto dado");
            }
        }
    }
}
