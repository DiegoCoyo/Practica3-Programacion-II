import java.io.*;

public class ArchivoCliente {
    private String nomA;
    
    public ArchivoCliente(String nomA) {
        this.nomA = nomA;
    }
    
    public void crearArchivo() {
        try {
            new FileOutputStream(nomA).close();
        } catch (IOException e) {
            System.out.println("Error, no se creo archivo.");
        }
    }
    
    public void guardaCliente(Cliente c) {
        try {
            FileOutputStream file = new FileOutputStream(nomA, true);
            ObjectOutputStream out;
            if (new File(nomA).length() == 0) {
                out = new ObjectOutputStream(file);
            } else {
                out = new ObjectOutputStream(file) {
                    protected void writeStreamHeader() throws IOException {
                    }
                };
            }
            out.writeObject(c);
            out.close();
            file.close();
        } catch (IOException ex) {
            System.out.println("Error, no se guardo cliente.");
        }
    }
    
    public Cliente buscarCliente(int c) {
        FileInputStream file = null;
        ObjectInputStream in = null;
        try {
            file = new FileInputStream(nomA);
            in = new ObjectInputStream(file);
            while (true) {
                Cliente cl = (Cliente) in.readObject();
                if (cl.id == c) {
                    return cl;
                }
            }
        } catch (EOFException e) {
            return null;
        } catch (IOException | ClassNotFoundException ex) {
            System.out.println("Error, no se busco cliente.");
            return null;
        } finally {
            try {
                if (in != null) in.close();
                if (file != null) file.close();
            } catch (IOException e) {
                System.out.println("Error, no se cerro el archivo.");
            }
        }
    }
    
    public Cliente buscarCelularCliente(int c) {
        FileInputStream file = null;
        ObjectInputStream in = null;
        try {
            file = new FileInputStream(nomA);
            in = new ObjectInputStream(file);
            while (true) {
                Cliente cl = (Cliente) in.readObject();
                if (cl.telefono == c) {
                    return cl;
                }
            }
        } catch (EOFException e) {
            return null;
        } catch (IOException | ClassNotFoundException ex) {
            System.out.println("Error por celular: " + ex.getMessage());
            return null;
        } finally {
            try {
                if (in != null) in.close();
                if (file != null) file.close();
            } catch (IOException e) {
                System.out.println("Error, no se cerro el archivo.");
            }
        }
    }
}