using System;
using System.IO;                        // For memorystream and file operation
using System.Collections;

namespace Convert
{
	public class Program
	{
		public static void SaveByteArrayToFileWithFileStream(byte[] data)
		{
			String newfile = "implant.png";

			byte[] newArray = new byte[data.Length + 4];
    		
    		data.CopyTo(newArray, 4);
    		
    		newArray[0] = 0x89;
    		newArray[1] = 0x50;
    		newArray[2] = 0x4E;
    		newArray[3] = 0x47;

		    using var stream = File.Create(newfile);
		    stream.Write(newArray, 0, newArray.Length);
		}

		static void Main(string[] args)
		{
			Console.Write("[+] Enter file name: ");
			String filename = Console.ReadLine();

			byte[] fileBytes = File.ReadAllBytes(filename);

			SaveByteArrayToFileWithFileStream(fileBytes);
		}
	}
}