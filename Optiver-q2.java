import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public class TruckPosition {
        public double mX;
        public double mY;
    }

    public class TruckPositionDelta {
        public int mTruckId;
        public int mClientId;
        public double mDeltaX;
        public double mDeltaY;
        public int mTimestamp = 0;
    }

    public interface IServer {
        public TruckPosition SubscribeToTruck(int truckId);
    }

    public interface ISubscriber {
        // Called by server after initial subscription
        public void ProcessUpdate(final TruckPositionDelta positionDelta);

        // Called by clients
        public TruckPosition SubscribeToTruck(int truckId, int clientId);

        public List<TruckPositionDelta> GetUpdates(int clientId);
    }

    class Subscriber implements ISubscriber {
        private IServer mServer;
        private Map<Integer, Map<Integer, List<TruckPositionDelta>>> mUpdates;
        private Map<Integer, Map<Integer, TruckPosition>> mTruckPositions;

        public Subscriber(IServer server) {
            mServer = server;
            mUpdates = new HashMap<>();
            mTruckPositions = new HashMap<>();
        }

        @Override
        public void ProcessUpdate(final TruckPositionDelta positionDelta) {
            int truckId = positionDelta.mTruckId;
            int clientId = positionDelta.mClientId;
            Map<Integer, List<TruckPositionDelta>> updates = mUpdates.getOrDefault(truckId, new HashMap<>());
            List<TruckPositionDelta> clientUpdates = updates.getOrDefault(clientId, new ArrayList<>());
            clientUpdates.add(positionDelta);
            updates.put(clientId, clientUpdates);
            mUpdates.put(truckId, updates);

            Map<Integer, TruckPosition> truckPositions = mTruckPositions.getOrDefault(truckId, new HashMap<>());
            TruckPosition currentPosition = truckPositions.getOrDefault(clientId, mServer.SubscribeToTruck(truckId));
            truckPositions.put(clientId, currentPosition);
            mTruckPositions.put(truckId, truckPositions);

            currentPosition.mX += positionDelta.mDeltaX;
            currentPosition.mY += positionDelta.mDeltaY;
        }

        @Override
        public TruckPosition SubscribeToTruck(int truckId, int clientId) {
            Map<Integer, List<TruckPositionDelta>> updates = mUpdates.getOrDefault(truckId, new HashMap<>());
            List<TruckPositionDelta> clientUpdates = updates.getOrDefault(clientId, new ArrayList<>());
            updates.put(clientId, clientUpdates);
            mUpdates.put(truckId, updates);

            Map<Integer, TruckPosition> truckPositions = mTruckPositions.getOrDefault(truckId, new HashMap<>());
            TruckPosition currentPosition = truckPositions.getOrDefault(clientId, mServer.SubscribeToTruck(truckId));
            truckPositions.put(clientId, currentPosition);
            mTruckPositions.put(truckId, truckPositions);

            return currentPosition;
        }

        @Override
        public List<TruckPositionDelta> GetUpdates(int clientId) {
            List<TruckPositionDelta> clientUpdates = new ArrayList<>();
            for (Map.Entry<Integer, Map<Integer, List<TruckPositionDelta>>> entry : mUpdates.entrySet()) {
                int truckId = entry.getKey();
                Map<Integer, List<TruckPositionDelta>> updates = entry.getValue();
                if (updates.containsKey(clientId)) {
                    List<TruckPositionDelta> truckUpdates = updates.get(clientId);
                    clientUpdates.addAll(truckUpdates);
                }
            }
            Collections.sort(clientUpdates, Comparator.comparingInt(a -> a.mTimestamp));
            return clientUpdates;
        }

    }

    class Server implements IServer {
        private HashSet<Integer> mRegisteredTrucks;
        private HashMap<Integer, TruckPosition> mCurrentPos;

        public Server() {
            mRegisteredTrucks = new HashSet<>();
            mCurrentPos = new HashMap<>();
        }

        @Override
        public TruckPosition SubscribeToTruck(int truckId) {
            mRegisteredTrucks.add(truckId);
            TruckPosition pos = mCurrentPos.get(truckId);
            TruckPosition copy = new TruckPosition();
            copy.mX = pos.mX;
            copy.mY = pos.mY;
            return copy;
        }

        public void AddPosition(int truckId, TruckPosition pos) {
            mCurrentPos.put(truckId, pos);
        }

        public void OnUpdate(Subscriber subscriber, final TruckPositionDelta delta) {
            if (mRegisteredTrucks.contains(delta.mTruckId)) {
                subscriber.ProcessUpdate(delta);
            }
            TruckPosition pos = mCurrentPos.get(delta.mTruckId);
            pos.mX += delta.mDeltaX;
            pos.mY += delta.mDeltaY;
        }
    }

    class Client {
        private final int mClientId;
        private final Subscriber mSubscriber;
        private final DecimalFormat mFormat;

        public Client(int clientId, Subscriber subscriber) {
            mClientId = clientId;
            mSubscriber = subscriber;
            mFormat = new DecimalFormat("0.#");
        }

        public void Subscribe(int truckId) {
            TruckPosition pos = mSubscriber.SubscribeToTruck(truckId, mClientId);
            System.out.println(
                    "S " + mClientId + " " + truckId + " " + mFormat.format(pos.mX) + " " + mFormat.format(pos.mY));
        }

        public void RequestUpdate() {
            List<TruckPositionDelta> updates = mSubscriber.GetUpdates(mClientId);
            for (final TruckPositionDelta delta : updates) {
                System.out.println("U " + mClientId + " " + delta.mTruckId + " " + mFormat.format(delta.mDeltaX) + " "
                        + mFormat.format(delta.mDeltaY));
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Server server = solution.new Server();
        Subscriber subscriber = solution.new Subscriber(server);
        List<Client> clients = new ArrayList<>();

        Scanner scanner = new Scanner(System.in);
        int numTrucks = scanner.nextInt();
        for (int i = 0; i < numTrucks; i++) {
            TruckPosition pos = solution.new TruckPosition();
            pos.mX = scanner.nextDouble();
            pos.mY = scanner.nextDouble();
            server.AddPosition(i, pos);
        }

        while (scanner.hasNext()) {
            char command = scanner.next().charAt(0);
            if (command == 'S') {
                int clientId = scanner.nextInt();
                if (clientId >= clients.size()) {
                    clients.add(solution.new Client(clientId, subscriber));
                }
                clients.get(clientId).Subscribe(scanner.nextInt());
            } else if (command == 'U') {
                TruckPositionDelta delta = solution.new TruckPositionDelta();
                delta.mTruckId = scanner.nextInt();
                delta.mDeltaX = scanner.nextDouble();
                delta.mDeltaY = scanner.nextDouble();
                server.OnUpdate(subscriber, delta);
            } else if (command == 'R') {
                int clientId = scanner.nextInt();
                clients.get(clientId).RequestUpdate();
            } else {
                throw new IllegalArgumentException("Invalid input");
            }
        }
    }
}