package UTN.Cine;

public class Pelicula {
    
    private String anioEstreno;
    private Boolean disponible;
    private Double duracion;
    private String fechaIngreso;
    private String nombre;
    private String tituloOriginal;
    private Genero genero;
    private PaisDeOrigen paisDeOrigen;
    private Calificacion calificacion;
//Constructor sin parametros (Por defecto)
    public Pelicula(){
    }
//Constructor con dos parametros definido.
    public Pelicula(String nombre, String anioEstreno){
        this.nombre=nombre;
        this.anioEstreno=anioEstreno;
    }

    public String getAnioEstreno() {
        return anioEstreno;
    }
    public void setAnioEstreno(String anioEstreno) {
        this.anioEstreno = anioEstreno;
    }
    /*
    public Boolean getDisponible() {
        return disponible;
    }
    */
    public void setDisponible(Boolean disponible) {
        this.disponible = disponible;
    }
    public Double getDuracion() {
        return duracion;
    }
    public void setDuracion(Double duracion) {
        this.duracion = duracion;
    }
    public String getFechaIngreso() {
        return fechaIngreso;
    }
    public void setFechaIngreso(String fechaIngreso) {
        this.fechaIngreso = fechaIngreso;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getTituloOriginal() {
        return tituloOriginal;
    }
    public void setTituloOriginal(String tituloOriginal) {
        this.tituloOriginal = tituloOriginal;
    }
    public Boolean estaDisponible(){
        return disponible;
    }
    public Boolean estaEnCartel(){
        //desarrollar la logica para el metodo segun logica del negocio.
        return true;
    }
//Relacion al genero    
    public Genero getGenero() {
        return genero;
    }
    public void setGenero(Genero genero) {
        this.genero = genero;
    }
//Relacion al pais de origen    
    public PaisDeOrigen getPais(){
        return paisDeOrigen;
    }
    public void setPais(PaisDeOrigen paisDeOrigen) {
        this.paisDeOrigen = paisDeOrigen;
    }
//Relacion a la calificacion
    public Calificacion getCalificacion(){
        return calificacion;
    }
    public void setCalificacion(Calificacion calificacion){
        this.calificacion=calificacion;
    }
    @Override
    public String toString(){
        return "Hola mundo";
    }
}
