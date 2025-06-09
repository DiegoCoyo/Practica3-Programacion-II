public class Caja<T> {
    private T contenido;
    
    public Caja() {
        contenido = null;
    }
    
    public void guardar(T valor) {
        contenido = valor;
    }
    
    public T obtener() {
        return contenido;
    }
}