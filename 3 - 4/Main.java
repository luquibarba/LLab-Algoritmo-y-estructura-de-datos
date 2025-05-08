import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static ArrayList<String> estudiantes = new ArrayList<>();
    static ArrayList<String> fechas = new ArrayList<>();
    static ArrayList<ArrayList<String>> asistencias = new ArrayList<>();

    public static void main(String[] args) {
        int opcion;
        do {
            System.out.println("\n--- Sistema de Asistencia ---");
            System.out.println("1. Registrar estudiante");
            System.out.println("2. Cargar asistencia");
            System.out.println("3. Ver estadísticas");
            System.out.println("4. Salir");
            System.out.print("Opción: ");
            while (!sc.hasNextInt()) {
                System.out.print("Por favor ingrese un número: ");
                sc.next();
            }
            opcion = sc.nextInt();
            sc.nextLine(); 

            switch (opcion) {
                case 1:
                    registrarEstudiante();
                    break;
                case 2:
                    cargarAsistencia();
                    break;
                case 3:
                    mostrarEstadisticas();
                    break;
                case 4:
                    System.out.println("Saliendo del sistema...");
                    break;
                default:
                    System.out.println("Opción inválida, intente de nuevo.");
            }
        } while (opcion != 4);
    }

    public static void registrarEstudiante() {
        System.out.print("Nombre completo: ");
        String nombre = sc.nextLine().trim();

        System.out.print("Año (1-6): ");
        int anio;
        try {
            anio = Integer.parseInt(sc.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Año inválido.");
            return;
        }

        System.out.print("División (A-D): ");
        String division = sc.nextLine().trim().toUpperCase();

        if (nombre.isEmpty() || anio < 1 || anio > 6 || !division.matches("[A-D]")) {
            System.out.println("Datos inválidos.");
            return;
        }

        String estudiante = nombre + " - " + anio + "°" + division;
        if (estudiantes.contains(estudiante)) {
            System.out.println("El estudiante ya está registrado.");
        } else {
            estudiantes.add(estudiante);
            System.out.println("Estudiante registrado exitosamente.");
        }
    }

    public static void cargarAsistencia() {
        if (estudiantes.isEmpty()) {
            System.out.println("No hay estudiantes registrados.");
            return;
        }

        System.out.print("Fecha (DD/MM/AAAA): ");
        String fecha = sc.nextLine().trim();

        if (fecha.isEmpty()) {
            System.out.println("Fecha inválida.");
            return;
        }

        if (fechas.contains(fecha)) {
            System.out.println("Ya hay asistencia cargada para esta fecha.");
            return;
        }

        ArrayList<String> presentes = new ArrayList<>();
        for (String est : estudiantes) {
            System.out.print("¿" + est + " está presente? (s/n): ");
            String r = sc.nextLine().trim().toLowerCase();
            if (r.equals("s")) {
                presentes.add(est);
            }
        }

        fechas.add(fecha);
        asistencias.add(presentes);
        System.out.println("Asistencia registrada para " + fecha + ".");
    }

    public static void mostrarEstadisticas() {
        int totalClases = fechas.size();
        System.out.println("\n--- Estadísticas de Asistencia ---");
        System.out.println("Total de clases cargadas: " + totalClases);

        if (totalClases == 0) {
            System.out.println("No hay asistencias registradas.");
            return;
        }

        for (String est : estudiantes) {
            int presentes = 0;
            for (ArrayList<String> lista : asistencias) {
                if (lista.contains(est)) {
                    presentes++;
                }
            }

            double porcentaje = (presentes * 100.0) / totalClases;
            System.out.printf("%s - Asistencia: %.2f%%\n", est, porcentaje);

            if (porcentaje < 80.0) {
                System.out.println(">> ALERTA: Riesgo de quedar irregular");
            }
        }
    }
}
