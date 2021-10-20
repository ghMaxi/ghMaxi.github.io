using System;
using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace WWW
{
	public static class NetworkProcedures
    {
        public static void SendMessage(Message message, string ip)
        {
            new Thread(() =>
            {
                var client = new TcpClient();
                var ipAddress = IPAddress.Parse(ip);
                try
                {
                    client.Connect(ipAddress, NetworkSettings.port);

                    var networkStream = client.GetStream();
                    var bytes = new NetworkMessage(
                        message.text, message.time).ToBytes();
                    networkStream.Write(bytes);
                    Thread.Sleep(10);
                }
                catch (SocketException e)
                {
                    Debug.WriteLine(e);
				}
            }).Start();
        }

        public static void RunServer(Engine engine)
        {
            new Thread(() =>
            {
                var server = new TcpListener(NetworkSettings.localIPAddress, NetworkSettings.port);
                server.Start();
                while (true)
                {
                    Debug.WriteLine("client...");
                    var client = server.AcceptTcpClient();
                    Debug.WriteLine("data...");
                    var networkStream = client.GetStream();
                    while (client.Available < 3) ;
                    var bytes = new byte[client.Available];
                    networkStream.Read(bytes, 0, bytes.Length);
                    var message = new NetworkMessage(bytes);
                    var address = (
                        (IPEndPoint)client.Client.RemoteEndPoint)
                            .Address;
                    var engine_message = new Message(
                        message, address.ToString());
                    engine.ReceiveMessage(engine_message);
                }
            }).Start();
        }
    }
}
