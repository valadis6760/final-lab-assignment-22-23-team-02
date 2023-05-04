package team2.upm.es;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.microsoft.azure.functions.ExecutionContext;
import com.microsoft.azure.functions.HttpMethod;
import com.microsoft.azure.functions.HttpRequestMessage;
import com.microsoft.azure.functions.HttpResponseMessage;
import com.microsoft.azure.functions.HttpStatus;
import com.microsoft.azure.functions.annotation.AuthorizationLevel;
import com.microsoft.azure.functions.annotation.FunctionName;
import com.microsoft.azure.functions.annotation.HttpTrigger;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.logging.Logger;
import java.util.stream.Collectors;

/**
 * Azure Functions with HTTP Trigger.
 */
public class Function {
    /**
     * This function listens at endpoint "/api/HttpExample". Two ways to invoke it
     * using "curl" command in bash:
     * 1. curl -d "HTTP Body" {your host}/api/HttpExample
     * 2. curl "{your host}/api/HttpExample?name=HTTP%20Query"
     */
    @FunctionName("HttpExample")
    public HttpResponseMessage run(
            @HttpTrigger(name = "req", methods = { HttpMethod.POST }, authLevel = AuthorizationLevel.ANONYMOUS) HttpRequestMessage<Optional<String>> request,
            final ExecutionContext context) {

        Logger log = context.getLogger();
        log.info("Java HTTP trigger processed a request.");

        // Extract the message from the request body
        String message = request.getBody().get();
        log.info("Message: " + message);
    //    String webhookUrl = "https://web-app-monitoring.azurewebsites.net/webhook";
        String webhookUrl = "http://localhost:3000/webhook";

        // Create an HTTP client to send the message to the Azure Web App
        CloseableHttpClient client = HttpClientBuilder.create().build();
        HttpPost httpPost = new HttpPost(webhookUrl);

        Gson gson = new Gson();
        List payload = gson.fromJson(message, List.class);
        List<DeviceDTO> devices = (List<DeviceDTO>) payload.stream().map(device -> gson.fromJson(device.toString(), DeviceDTO.class)).collect(Collectors.toList());
        log.info("Devices found: " + devices.size());
        List<AlertDTO> alerts = getAlerts(devices, log);
        log.info("Alerts found: " + alerts.size());

        try {
            boolean error = false;
            for (AlertDTO alert : alerts) {

                Gson gson2 = new Gson();
                JsonElement je = gson2.toJsonTree(alert);
                JsonObject jo = new JsonObject();
                jo.add("alert", je);


                log.info("Alert: " + jo);
                // Set the message as the request body
                StringEntity entity = new StringEntity(jo.toString(), ContentType.APPLICATION_JSON);
                httpPost.setEntity(entity);

                // Send the HTTP POST request to the Azure Web App
                HttpResponse response = client.execute(httpPost);
                log.info("Response: " + response.toString());
                int statusCode = response.getStatusLine().getStatusCode();
                if (statusCode < 200 || statusCode >= 300) {
                    error = true;
                    break;
                }
            }
            if (!error) {
                return request.createResponseBuilder(HttpStatus.OK).build();
            } else {
                return request.createResponseBuilder(HttpStatus.INTERNAL_SERVER_ERROR).build();
            }
        } catch (IOException e) {
            // An error occurred while sending the HTTP request
            log.severe("An error occurred while sending the webhook: " + e.getMessage());
            return request.createResponseBuilder(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }

    private List<AlertDTO> getAlerts(List<DeviceDTO> devices, Logger log) {
        List<AlertDTO> alerts = new ArrayList<>();
        devices.forEach(device -> {
            if (device.getDevice_battery() > 0 && device.getDevice_battery() < 20) {
                AlertDTO alert = AlertDTO.builder().type("battery").collarId(device.getDevice_id()).build();
                log.info("Alert added for battery type with battery " + device.getDevice_battery());
                alerts.add(alert);
            } else if (device.getCow_temperature() > 35) {
                AlertDTO alert = AlertDTO.builder().type("temperature").collarId(device.getDevice_id()).build();
                log.info("Alert added for temperature type with temperature " + device.getCow_temperature());
                alerts.add(alert);
            }
        });
        return alerts;
    }
}
