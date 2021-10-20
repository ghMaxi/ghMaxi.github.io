using System.Net;
using System.Net.Sockets;

namespace WWW
{
	public static class NetworkSettings
    {
        public const int port = 3485;
        public static readonly IPAddress localIPAddress = GetLocalIPAddress();

        private static IPAddress GetLocalIPAddress()
        {
            var host = Dns.GetHostEntry(Dns.GetHostName());
            foreach (var ip in host.AddressList)
            {
                if (ip.AddressFamily == AddressFamily.InterNetwork)
                {
                    return ip;
                }
            }

            var LOCALHOST_IP = "127.0.0.1";
            return IPAddress.Parse(LOCALHOST_IP);
        }
    }
}
