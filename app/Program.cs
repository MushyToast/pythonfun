using System;

namespace GetUserInput
{
    class Program
    {
        private static void Main(string[] args)
        {
            Console.Write("Please enter your name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, " + name + "!");
            Thread.Sleep(5000);
            Console.WriteLine("Hello");
        }
    }
}
