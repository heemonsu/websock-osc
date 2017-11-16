# websock-osc
Contains Javascript WebSocket server and Python client

npm libraries used for server:
npm install node-osc
npm install ws

python2 libraries for client:
pip install websocket-client
(python2 -m pip install websocket-client)

<h3>Setup:</h3>
<ul>
  <li>Clone this repo on both the Server (Windows Machine connected to the Kinect) and the Client (Any system which wants the Kinect data)</li>
  <li>On the Server, cd into this directory and run </li>


```
      npm install .
``` 
  <li>Install Microsoft Kinect SDK and NI Mate on the Server system, and check your connection to the Kinect using Kinect Studio and NI Mate's viewer.
</ul>
<ul>
<li>The client needs to install the Python2 library listed above.</li>
</ul>

<h3>Usage:</h3>
<ul>
  <li>Start NI Mate on the Server and change the IP to which the data is sent to 127.0.0.1:3333 in the 'Setup' and 'Kinect for Windows --> Skeleton Tracking' (you might have to click the lock to enable editing).</li>
  <li>Go to 'log' and check the 'OSC' checkbox to be check if the OSC data is being sent.</li>
  <li>Open a Command Window and cd into this directory.</li>
  <li>Launch the server.js file</li>
  
```
node server.js
```
  <li>On the client side, launch the pyclient.py file.</li>
  <li>You should see a 'Client connected' message each time a client is connected, and 'Client closed' when it disconnects on the server cmd.</li>
  <li>
</ul>

  
