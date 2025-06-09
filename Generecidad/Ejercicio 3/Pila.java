import java.util.ArrayList;

public class Pila<T> {
    private ArrayList<T> elementos;
    
    public Pila() {
        elementos = new ArrayList<T>();
    }
    
    public void apilar(T elemento) {
        elementos.add(elemento);
    }
    
    public T desapilar() {
        if (elementos.isEmpty()) {
            System.out.println("Vacio.");
            return null;
        }
        return elementos.remove(elementos.size() - 1);
    }
    
    public void mostrar() {
        if (elementos.isEmpty()) {
            System.out.println("Vacio.");
            return;
        }
        for (int i = elementos.size() - 1; i >= 0; i--) {
            System.out.println(elementos.get(i));
        }
    }
}