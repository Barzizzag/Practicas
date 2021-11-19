package JavaParaNovatos;

class MiNumero {

private int numero;

    public MiNumero(){
        numero=10;
    }
    public MiNumero(int num){
        this.numero=num;
    }
    public void cambiaNumero (int nuevoNum){
        this.numero=nuevoNum;
    }
    public void suma(int aSumar){
        this.numero=numero+aSumar;
    }
    public void restar(int aRestar){
        this.numero=numero-aRestar;
    }
    public int getValor(){
        int num=this.numero;
        return num;
    }
    public int getDoble(){
        return (numero*2);
    }
    public int getTriple(){
        return (numero*3);
    }
    public int getCuadruple(){
        return (numero*4);
    }
}
