package JavaParaNovatos;

import java.util.Scanner;

public class MiNumeroPrueba {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        MiNumero miNumero = new MiNumero();
        int nuevoNum, aSumar, aRestar;
        boolean salida = false;
        do {
            System.out.println("1 Nuevo numero - 2 Nuevo numero con ingreso - 3 Cambiar el numero");
            System.out.println("4 Sumar numero - 5 Restar numero - 6 Averiguar el numero");
            System.out.println("7 Doble del numero - 8 - Triple del numero - 9 Cuadruple del numero");
            System.out.print("Ingrese una opcion:");
            String ingreso = sc.next();
            switch (ingreso) {
                /*
                 * case "1": MiNumero miNumero = new MiNumero(); break; case "2": Integer
                 * numero=sc.nextInt(); MiNumero miNumero = new MiNumero(numero); break;
                 */
                case "3":
                    System.out.println("Que numero quiere ingresar: ");
                    nuevoNum = sc.nextInt();
                    miNumero.cambiaNumero(nuevoNum);
                    break;
                case "4":
                    System.out.println("Que numero quiere sumar: ");
                    aSumar = sc.nextInt();
                    miNumero.suma(aSumar);
                    break;
                case "5":
                    System.out.println("Que numero quiere ingresar: ");
                    aRestar = sc.nextInt();
                    miNumero.restar(aRestar);
                    break;
                case "6":
                    System.out.println("El numero es: " + miNumero.getValor());
                    break;
                case "7":
                    System.out.println("El doble del numero es: " + miNumero.getDoble());
                    break;
                case "8":
                    System.out.println("El triple del numero es: " + miNumero.getTriple());
                    break;
                case "9":
                    System.out.println("El cuadruple del numero es: " + miNumero.getCuadruple());
                    break;
                case "0":
                    salida = true;
                    break;
            }
        } while (salida == false);

    }
}
