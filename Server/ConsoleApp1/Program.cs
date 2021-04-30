using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        public static string data;
        public static void start()
        {
           
            string _port = "5900";
            Console.WriteLine("Port: "+_port);
            byte[] buffer = new Byte[1024];
            IPEndPoint localEndPoint = new IPEndPoint(IPAddress.Any, int.Parse(_port));
            Socket listener = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            try
            {
                listener.Bind(localEndPoint);
                listener.Listen(10);

                while (true)
                {
                    Console.WriteLine("Client tarafından cevap bekleniyor.");
                    Socket socket = listener.Accept();
                    data = null;

                    while (true)
                    {
                        int bytesRec = socket.Receive(buffer);
                        data += Encoding.ASCII.GetString(buffer, 0, bytesRec);
                        if (data.IndexOf("") > -1)
                        {
                            break;
                        }
                    }

                    Console.WriteLine("IP:"+ IPAddress.Parse(((IPEndPoint)socket.RemoteEndPoint).Address.ToString()));
                    Console.WriteLine("Alınan Veri : {0}", data);
                    byte[] msg = Encoding.ASCII.GetBytes(data);

                    socket.Send(msg);
                    socket.Shutdown(SocketShutdown.Both);
                    socket.Close();
                }

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }

            Console.WriteLine("\nKapatmak için ENTER tuşuna basın.");
            Console.Read();
        }

        static void Main(string[] args)
        {
            start();
        }
    }
}
