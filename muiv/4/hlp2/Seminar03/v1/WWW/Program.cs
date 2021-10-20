using System;
using System.Windows.Forms;
using System.Threading;


namespace WWW
{
    static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.SetHighDpiMode(HighDpiMode.SystemAware);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
                       
            var engine = new Engine();
            var mainWindow = new MainWindow(engine);
            engine.IntroduceMainWindow(mainWindow);
            NetworkProcedures.RunServer(engine);
                 
            Application.Run(mainWindow);
        }
    }
}
