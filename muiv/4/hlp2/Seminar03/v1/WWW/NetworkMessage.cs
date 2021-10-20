using System;
using System.Text;

namespace WWW
{
    public struct NetworkMessage
    {
        public readonly string message;
        public readonly string time;

        public NetworkMessage(string message, string time)
        {
            (this.message, this.time) = (message, time);
        }

        public NetworkMessage(byte[] source)
        {
            var data = Encoding.UTF8.GetString(source);
            var index = data.IndexOf('\t');
            message = data.Substring(0, index);
            time = data.Substring(index + 1, data.Length - index - 1);
        }

        public byte[] ToBytes()
        {
            var byteMessage = Encoding.UTF8.GetBytes(message + '\t');
            var byteTime = Encoding.UTF8.GetBytes(time);
            var result = new byte[byteMessage.Length + byteTime.Length];
            Array.Copy(byteMessage, 0, result, 0, byteMessage.Length);
            Array.Copy(byteTime, 0, result, byteMessage.Length, byteTime.Length);
            return result;
        }

        public override string ToString()
        {
            return $"{message} -- {time}";
        }
    }
}
