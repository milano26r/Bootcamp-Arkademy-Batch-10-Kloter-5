using System;

namespace ReplaceString
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine(ganti_kata("purwakarta", 'a', 'o'));
		}
		
		static string ganti_kata(string kata_awal, char pilih_huruf, char ganti_huruf)
  		{      	     
			string kata_akhir = "";			
			int count = kata_awal.Length;
      		for (int i = 0; i < count; i++)
      		{
      			if (kata_awal[i] == pilih_huruf)
      			{
      				kata_akhir += ganti_huruf;
      			}
      			else
      				kata_akhir += kata_awal[i];
      		}
			
	        return kata_akhir;
  		}  
	}
}