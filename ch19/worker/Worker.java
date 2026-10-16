import com.sun.net.httpserver.HttpServer;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

public class Worker {
    public static void main(String[] args) throws Exception {
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "5000"));
        var server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/", exchange -> {
            var body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            var task = exchange.getRequestHeaders().getFirst("X-Aws-Sqsd-Taskname");
            System.out.println("worker got " + exchange.getRequestMethod() + " " + exchange.getRequestURI()
                    + (task == null ? "" : " task=" + task) + " body=" + body);
            var reply = "ok\n".getBytes(StandardCharsets.UTF_8);
            exchange.sendResponseHeaders(200, reply.length);
            exchange.getResponseBody().write(reply);
            exchange.close();
        });
        server.start();
        System.out.println("worker listening on " + port);
    }
}
