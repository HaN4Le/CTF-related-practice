using Microsoft.VisualBasic;
using Microsoft.VisualBasic.CompilerServices;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Web.Security;
using System.Windows.Forms;
using 御剑WEB目录扫描优化版;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

       /* private void button1_Click(object sender, EventArgs e)
        {
            if (Operators.CompareString(Module1.AesEncrypt(Encoding.Default.GetBytes(textBox1.Text), new byte[]
			{
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15
			}), textBox2.Text, false) == 0)
            {
            //    File.WriteAllBytes("lisences.dat", Encoding.Default.GetBytes(this.TextBox2.Text));
                Interaction.MsgBox("激活成功", MsgBoxStyle.OkOnly, null);
              //  MyProject.Forms.Form1.CheckJH();
                this.Close();
            }
            else
            {
                Interaction.MsgBox("激活失败", MsgBoxStyle.OkOnly, null);
            }
        }*/

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = FormsAuthentication.HashPasswordForStoringInConfigFile(Module1.GETCPUID() + Module1.GetDiskSerialNumber() + Module1.GetMacAddress(), "SHA1"); ;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (textBox1.Text=="")
            {
                MessageBox.Show("请先获取机器码");
            }

            string data = Module1.AesEncrypt(Encoding.Default.GetBytes(textBox1.Text), new byte[]
			{
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15,
				15
			});
            textBox2.Text = data;
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
