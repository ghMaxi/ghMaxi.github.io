using System;
using System.Windows.Forms;

namespace WWW
{
    public partial class MainWindow : Form
    {
        private Engine _engine;
        public MainWindow(Engine engine)
        {
            _engine = engine;
            _engine.OnNewMessage += AddNewMessage;
            InitializeComponent();
            var ipBytes = NetworkSettings.localIPAddress.GetAddressBytes();
            var numerics = new NumericUpDown[]
            {
                numericUpDown1, numericUpDown2, numericUpDown3, numericUpDown4
            };
            for (int i = 0; i < 4; i++)
            {
                numerics[i].Value = ipBytes[i];
			}
            label3.Text = NetworkSettings.localIPAddress.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var message = new Message(
                "You",
                richTextBox1.Text,
                DateTime.Now.ToString());
            AddNewMessage(message);
            var ipString = $"{numericUpDown1.Value}.{numericUpDown2.Value}.{numericUpDown3.Value}.{numericUpDown4.Value}";
            _engine.SendMesage(message, ipString);
            richTextBox1.Text = "";
        }

        public void AddNewMessage(Message message)
        {
            Invoke((MethodInvoker)delegate
            {
                richTextBox2.Text += "\n" + message;
            });
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
