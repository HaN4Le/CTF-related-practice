using Microsoft.VisualBasic.CompilerServices;
using System;
using System.Management;
using System.Security.Cryptography;

namespace 御剑WEB目录扫描优化版
{
    [StandardModule]
    internal sealed class Module1
    {
        public static string GETCPUID()
        {
            string result = "";
            ManagementClass managementClass = new ManagementClass("Win32_Processor");
            try
            {
                ManagementObjectCollection.ManagementObjectEnumerator enumerator = managementClass.GetInstances().GetEnumerator();
                while (enumerator.MoveNext())
                {
                    ManagementBaseObject current = enumerator.Current;
                    ManagementObject managementObject = (ManagementObject)current;
                    result = managementObject.Properties["ProcessorId"].Value.ToString();
                }
            }
            finally
            {
              //  ManagementObjectCollection.ManagementObjectEnumerator enumerator;
             /*   if (enumerator != null)
                {
                    ((IDisposable)enumerator).Dispose();
                }*/
            }
            return result;
        }

        public static string GetDiskSerialNumber()
        {
            string result = "";
            ManagementClass managementClass = new ManagementClass("Win32_DiskDrive");
            try
            {
                ManagementObjectCollection.ManagementObjectEnumerator enumerator = managementClass.GetInstances().GetEnumerator();
                if (enumerator.MoveNext())
                {
                    ManagementBaseObject current = enumerator.Current;
                    ManagementObject managementObject = (ManagementObject)current;
                    result = Conversions.ToString(managementObject.Properties["Model"].Value);
                }
            }
            finally
            {
            /*    ManagementObjectCollection.ManagementObjectEnumerator enumerator;
                if (enumerator != null)
                {
                    ((IDisposable)enumerator).Dispose();
                }*/
            }
            return result;
        }

        public static string GetMacAddress()
        {
            string result = "";
            ManagementClass managementClass = new ManagementClass("Win32_NetworkAdapterConfiguration");
            try
            {
                ManagementObjectCollection.ManagementObjectEnumerator enumerator = managementClass.GetInstances().GetEnumerator();
                while (enumerator.MoveNext())
                {
                    ManagementBaseObject current = enumerator.Current;
                    ManagementObject managementObject = (ManagementObject)current;
                    if (Conversions.ToBoolean(managementObject["IPEnabled"]))
                    {
                        result = managementObject["MacAddress"].ToString();
                        break;
                    }
                }
            }
            finally
            {
             /*   ManagementObjectCollection.ManagementObjectEnumerator enumerator;
                if (enumerator != null)
                {
                    ((IDisposable)enumerator).Dispose();
                }*/
            }
            return result;
        }

        public static string AesEncrypt(byte[] SourceArray, byte[] KeyArray)
        {
            RijndaelManaged rijndaelManaged = new RijndaelManaged();
            RijndaelManaged rijndaelManaged2 = rijndaelManaged;
            rijndaelManaged2.Key = KeyArray;
            rijndaelManaged2.Mode = CipherMode.ECB;
            rijndaelManaged2.Padding = PaddingMode.Zeros;
            byte[] value = rijndaelManaged.CreateEncryptor().TransformFinalBlock(SourceArray, 0, SourceArray.Length);
            return BitConverter.ToString(value).Replace("-", "");
        }
    }
}
