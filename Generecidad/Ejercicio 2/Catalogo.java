import java.util.ArrayList;

public class Catalogo<T> {
    private ArrayList<T> elementos;
    
    public Catalogo() {
        elementos = new ArrayList<T>();
    }
    
    public void agregar(T elemento) {
        elementos.add(elemento);
    }
    
    public T buscar(int indice) {
        if (indice < 0 || indice >= elementos.size()) {
            System.out.println("no permitido");
            return null;
        }
        return elementos.get(indice);
    }
}