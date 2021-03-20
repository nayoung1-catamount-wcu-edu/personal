using System;

namespace NumberGuessingGame
{
    class Program
    {
        static void Main(string[] args)
        {
            Random r = new Random();

            int winNum = r.Next(0, 100);

            bool win = false;

            do
            {
                Console.Write("Guess a number in between 0 and 100: ");
                string s = Console.ReadLine();

                int i = int.Parse(s);

                if (i > winNum)
                {
                    Console.WriteLine("Too high!  Guess a lower number...");
                }
                else if (i < winNum)
                {
                    Console.WriteLine("Too low!  Guess a higher number...");
                }
                else if (i == winNum)
                {
                    Console.WriteLine("You win!");
                    win = true;
                }

                Console.WriteLine();

            } while (win == false);

            Console.Write("Press any key to continue...");
            Console.ReadKey(true);
        }
    }
}
