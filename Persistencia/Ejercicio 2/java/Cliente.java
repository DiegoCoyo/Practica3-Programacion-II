import java.io.Serializable;

public class Cliente implements Serializable {
    private static final long serialVersionUID = 1L;
    public int id;
    public String nombre;
    public int telefono;
    
    public Cliente(int id, String nombre, int telefono) {
        this.id = id;
        this.nombre = nombre;
        this.telefono = telefono;
    }
}