public class Program
{
    public static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Please specify which logic to run.");
            return;
        }

        switch (args[0].ToLower())
        {
            case "lumoria":
                Lumoria.Run();
                break;
            case "algora":
                Algora.Run();
                break;
            default:
                Console.WriteLine($"Unknown option: {args[0]}");
                break;
        }
    }
}