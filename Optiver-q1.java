import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    // This is the class you need to implement! Feel free to add members, private
    // methods etc, but don't change the public
    // method signatures.
    static class RiskLimitProcessor {
        private static class InstrumentState {
            double maxValue; // Maximum value per order
            int maxVolume10Seconds; // Maximum volume within 10 seconds
            double maxValue1Second; // Maximum value within 1 second
            long lastOrderTime; // Timestamp of the last order
            int totalVolume10Seconds; // Total volume within the last 10 seconds
            double totalValue10Seconds; // Total value within the last 10 seconds
            double totalValue1Second; // Total value within the last second
        }

        private Map<String, InstrumentState> instruments = new HashMap<>();
        private long currentTime = 0;

        public void AddLimit(String instrument, double maxValue, int maxVolume10Seconds, double maxValue1Second) {
            InstrumentState state = new InstrumentState();
            state.maxValue = maxValue;
            state.maxVolume10Seconds = maxVolume10Seconds;
            state.maxValue1Second = maxValue1Second;
            instruments.put(instrument, state);
        }

        public void ProcessOrder(String instrument, long timestamp, int volume, double price) {
            // Check if limits are defined for the instrument
            InstrumentState state = instruments.get(instrument);
            if (state == null) {
                System.out.println("NO_LIMITS " + instrument);
                return;
            }
            // Update current time and instrument state
            currentTime = timestamp;
            UpdateState(state, timestamp);
            // Check value limit
            double value = volume * price;
            if (value > state.maxValue) {
                System.out.println("MAX_VAL_LIMIT " + instrument);
                return;
            }
            // Check volume limit
            state.totalVolume10Seconds += volume;
            if (state.totalVolume10Seconds > state.maxVolume10Seconds) {
                System.out.println("MAX_VOL_10S_LIMIT " + instrument);
                return;
            }
            // Check value per second limit
            state.totalValue1Second += value;
            if (state.totalValue1Second > state.maxValue1Second) {
                System.out.println("MAX_VAL_1S_LIMIT " + instrument);
                return;
            }
            // Update state with new order
            state.totalValue10Seconds += value;
            state.lastOrderTime = timestamp;
        }

        private void UpdateState(InstrumentState state, long timestamp) {
            long timeDiff = timestamp - state.lastOrderTime;
            if (timeDiff > 10000) { // Reset state after 10 seconds
                state.totalVolume10Seconds = 0;
                state.totalValue10Seconds = 0;
            } else if (timeDiff > 1000) { // Reset value per second after 1 second
                state.totalValue1Second = 0;
            }
        }
    }

    public static void main(String[] args) {
        RiskLimitProcessor store = new RiskLimitProcessor();

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String inputLine;
        try {
            while ((inputLine = reader.readLine()) != null) {
                StringTokenizer tokenizer = new StringTokenizer(inputLine);
                String action = tokenizer.nextToken();
                String instrument = tokenizer.nextToken();
                if (action.equals("LIMIT")) {
                    double maxValue = Double.parseDouble(tokenizer.nextToken());
                    int maxVolume10Seconds = Integer.parseInt(tokenizer.nextToken());
                    double maxValue1Second = Double.parseDouble(tokenizer.nextToken());
                    store.AddLimit(instrument, maxValue, maxVolume10Seconds, maxValue1Second);
                } else if (action.equals("ORDER")) {
                    long timestamp = Long.parseLong(tokenizer.nextToken());
                    int volume = Integer.parseInt(tokenizer.nextToken());
                    double price = Double.parseDouble(tokenizer.nextToken());
                    store.ProcessOrder(instrument, timestamp, volume, price);
                } else {
                    System.err.println("Malformed input!");
                    System.exit(-1);
                }
            }
        } catch (IOException e) {
            System.err.println("Input reading error!");
            System.exit(-1);
        }
    }

}