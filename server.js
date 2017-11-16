const osc = require('node-osc')
const WebSocket = require('ws');

const wss = new WebSocket.Server({ host:'130.215.206.245', port: 3000});
var oscServer, oscClient;

var obj = {
  server: {
    port: 3333,
    host: '127.0.0.1'
  },
  client: {
    port: 3333,
    host: '127.0.0.1'
  }
}
//
var clients = [];

wss.on('connection', function connection(ws){
  console.log("Opening connection")
  
  ws.onclose = function(){
    console.log("Connection closed by client")
  }

  oscServer = new osc.Server(obj.server.port,obj.server.host);
  oscServer.on('message', function(msg, rinfo){
    if (ws.readyState == ws.OPEN){
      ws.send(JSON.stringify(msg));
    }
    else{
      oscServer.kill()
      // console.log(ws.readyState)
    }
  });
});
