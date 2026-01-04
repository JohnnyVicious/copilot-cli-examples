using System;

/*
Starter template for C# 12 (.NET 8.0)
Entrypoint: Run with `dotnet run` (requires a .csproj) or compile with `csc Starter.cs` and run `./Starter`
For simpler testing: `dotnet script Starter.cs` (requires dotnet-script tool)
Sample I/O:
  Input: (via stdin or args)
  Output: (via stdout)
*/

class Starter
{
    static void Main(string[] args)
    {
        // Read input
        Console.Write("Enter your name: ");
        string? input = Console.ReadLine();

        // Process
        string result = $"Hello, {input ?? "World"}!";

        // Write output
        Console.WriteLine(result);
    }
}
