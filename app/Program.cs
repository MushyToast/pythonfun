using System;

namespace GetUserInput
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Please enter your name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, " + name + "!");
        }
    }
}
