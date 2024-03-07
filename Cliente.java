import java.io.*;
import java.net.*;

public class Cliente {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java Cliente <Server IP> <Port>");
            return;
        }

        String serverIP = args[0];
        int port = Integer.parseInt(args[1]);

        try {
            Socket socket = new Socket(serverIP, port);
            BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            int number;
            while (true) {
                System.out.print("Ingresa un numero: ");
                number = Integer.parseInt(input.readLine());
                out.println(number);

                if (number == 0) {
                    System.out.println("Saliendo...");
                    break;
                }

                String response = in.readLine();
                System.out.println("Respuesta del servidor: " + response);
            }

            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

