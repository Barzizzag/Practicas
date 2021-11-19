package UTN.Cine;

import java.util.Scanner;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Pelicula> pelicualasDisponibles = new ArrayList<>();

        // Creamos los generos
        Genero terror = new Genero();
        terror.setDescripcion("Es alta pelicula de terror");
        terror.setNombre("Terror");

        Genero comedia = new Genero();
        comedia.setDescripcion("Alto cago de risa");
        comedia.setNombre("Comedia");

        // Creamos dos peliculas
        Pelicula pelicula1 = new Pelicula("Titanic","1990");//Pelicula creada con el segundo constructor
        pelicula1.setDisponible(true);
        pelicula1.setTituloOriginal("Titanic");
        pelicula1.setDuracion(1.5);
        pelicula1.setFechaIngreso("22/10/1990");
        pelicula1.setGenero(terror);

        Pelicula pelicula2 = new Pelicula();

        pelicula2.setNombre("Shrek");
        pelicula2.setAnioEstreno("1995");
        pelicula2.setDisponible(true);
        pelicula2.setTituloOriginal("Shrek");
        pelicula2.setDuracion(1.75);
        pelicula2.setFechaIngreso("22/10/1995");
        pelicula2.setGenero(comedia);

        // Agrego las peliculas al arraylist
        pelicualasDisponibles.add(pelicula1);
        pelicualasDisponibles.add(pelicula2);

        //Desde aca solo

        PaisDeOrigen pais1 = new PaisDeOrigen();
        pais1.setNombrePais("Argentina");
        pais1.setIdiomaPais("Castellano");
        PaisDeOrigen pais2 = new PaisDeOrigen();
        pais2.setNombrePais("China");
        pais2.setIdiomaPais("Chino Mandarin");
//Asignamos los paises
        pelicula1.setPais(pais1);
        pelicula2.setPais(pais2);
        /*
        System.out.println(pelicula1.getPais().getNombrePais());
        System.out.println(pelicula1.getPais().getIdiomaPais());
        System.out.println(pelicula2.getPais());
        System.out.println(pelicula2.getPais().getNombrePais());
        */
//Calificacion
        Calificacion calificacion1 = new Calificacion();
        Calificacion calificacion2 = new Calificacion();

        calificacion1.setNombre("ATP");
        calificacion1.setDescripcion("Apta todo publico");
        calificacion2.setNombre("R");
        calificacion2.setDescripcion("Restringida, pelicula no apta para menores de edad");

//Asignamos las calificaciones
        pelicula1.setCalificacion(calificacion2);
        pelicula2.setCalificacion(calificacion1);


        System.out.println("Desea ver todas las peliculas 1 para afirmativo, 2 para mostrar el genero, 3 para toda la info, 4 para salir:");
        int entrada = sc.nextInt();

        if (entrada == 1) {
            for (int i = 0; i < pelicualasDisponibles.size(); i++) {
                System.out.println(pelicualasDisponibles.get(i).getNombre());
                pelicula1.toString();
            }
        } else if (entrada == 2) {
            for (int i = 0; i < pelicualasDisponibles.size(); i++) {
                System.out.println(pelicualasDisponibles.get(i).getGenero().getNombre());
            }
        } else if (entrada ==3){
            for (int i =0;i<pelicualasDisponibles.size();i++){
                System.out.println(pelicualasDisponibles.get(i).getNombre());
                System.out.println(pelicualasDisponibles.get(i).getDuracion());
                System.out.println(pelicualasDisponibles.get(i).getAnioEstreno());
                System.out.println(pelicualasDisponibles.get(i).getTituloOriginal());
                System.out.println(pelicualasDisponibles.get(i).getFechaIngreso());
                System.out.println(pelicualasDisponibles.get(i).getGenero().getNombre());
                System.out.println(pelicualasDisponibles.get(i).getGenero().getDescripcion());
                System.out.println(pelicualasDisponibles.get(i).getCalificacion().getNombre());
                System.out.println(pelicualasDisponibles.get(i).getCalificacion().getDescripcion());
                System.out.println(pelicualasDisponibles.get(i).getPais().getNombrePais());
                System.out.println(pelicualasDisponibles.get(i).getPais().getIdiomaPais());
            }

        }else {
            System.out.println("Hasta luego");
        }
        /*
         * System.out.println(pelicula1.getNombre());
         * System.out.println(pelicula1.getGenero().getNombre());
         * System.out.println(pelicula1.getGenero().getDescripcion());
         */
    }
}
