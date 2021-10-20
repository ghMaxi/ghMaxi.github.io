namespace WWW
{
	public class Message
	{
		public readonly string name, text, time;

		public Message(NetworkMessage message, string address)
			: this(address, message.message, message.time) { }

		public Message(string name, string text, string time)
		{
			(this.name, this.text, this.time) = (name, text, time);
		}

		public override string ToString()
		{
			return $"{name}\n{text}\n{time}\n";
		}
	}
}