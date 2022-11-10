using System;
using System.Text.RegularExpressions;

public partial class Program
{
    public static void Main(string[] args)
    {
        string str = "abekrlf 459-472-21-23 abrljf eprjg 459-472-21-23 abeprog";
        // string pattern = @"ab([a-z]*)";
        string pattern = @"[0-9]{3}-\d{3}-\d{2}-\d{2}"; // поиск телефонного номера
        Regex regex = new Regex(pattern);
        MatchCollection matches = regex.Matches(str);
        foreach(Match match in matches)
        {
            Console.WriteLine(match.Value);
        }
        Console.Write("\n\n");

        string[] emails = new string[]
        {
            "tom@gmail.com",
            "igo123r@gmail.com",
            "sa-m@ay.com",
            "wiejfwpe",
        };

        string pattern2 = @"([a-z\d\-]+)@([a-z]+)\.([a-z]+)"; // проверка email на корректность
        for(int i=0; i<emails.Length; i++)
        {
            if(Regex.IsMatch(emails[i], pattern2, RegexOptions.IgnoreCase))
                Console.WriteLine(emails[i]);
        }
        Console.Write("\n\n");

        string str2 = "abekrlf abrljf eprabjg abeprog";
        string pattern3 = @"\bab";  // замена ab на 11 в начале строки
        Regex regex2 = new Regex(pattern3);
        string result = regex2.Replace(str2, "11");
        Console.WriteLine(result);
        
        // redular expression for checking correct ip
        string ip = Console.ReadLine();
        while (ip != "0")
        {
            string pattern = @"(([0-1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5]|[0-9][0-9]|[0-9])\.){3}([0-1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5]|[0-9][0-9]|[0-9])";
            Regex regex = new Regex(pattern);
            MatchCollection matches = regex.Matches(ip);
            foreach (Match match in matches)
            {
                Console.WriteLine(match.Value);
            }
            Console.Write("\n\n");
            ip = Console.ReadLine();
        }
    }
}
