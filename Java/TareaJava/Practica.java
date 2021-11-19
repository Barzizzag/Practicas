package TareaJava;

import java.util.Scanner;

public class Practica {

	//Primera forma
	/*
	public static void main(String[] args) {
		int [] arr1 = new int [4];
		float acumulador = 0;
		for (int i=0; i<4; i++) {
			arr1[i]= (i+4);
		}
		for (int i=0; i<4; i++) {
			acumulador=acumulador + arr1[i];
			
		}
		float promedio=(acumulador/4);
		System.out.println(promedio);
		
	}*/
	//Segunda forma
	public static void main(String[]args){
		int []arr1= new int [4];
		float acumulador =0;
		for (int i=0; i<4; i++) {
			System.out.print("Ingrese los numeros a promediar: ");
			arr1 [i]= (new Scanner(System.in)).nextInt();
		}
		for (int i=0; i<4; i++) {
			acumulador=acumulador+arr1[i];
		}
		System.out.println("El promedio es: "+(acumulador/4));
	}

}
