using System;
using System.Diagnostics;

namespace WWW
{
    public class Engine
    {
        public event Action<Message> OnNewMessage;

        public bool SendMesage(Message message, string ip)
        {
            NetworkProcedures.SendMessage(message, ip);
            return true;
        }
        public void ReceiveMessage(Message message)
        {
            try { _mainWindow1.AddNewMessage(message); }
            catch (NullReferenceException) {
                Debug.WriteLine("Engine.OnNewMessage has no subs."); }
        }

        MainWindow _mainWindow1;
		internal void IntroduceMainWindow(MainWindow mainWindow)
		{
            _mainWindow1 = mainWindow;
		}
	}
}
