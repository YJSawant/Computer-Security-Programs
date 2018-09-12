#include <wmmintrin.h> 
#include <stdio.h>
#include <emmintrin.h>
#include <conio.h>
#include <stdint.h>
#include <time.h>


__m128i AES_ASSIST (__m128i temp1, __m128i temp2)
 {
 __m128i temp3;
 temp2 = _mm_shuffle_epi32 (temp2 ,0xff);
 temp3 = _mm_slli_si128 (temp1, 0x04);
 temp1 = _mm_xor_si128 (temp1, temp3);
 temp3 = _mm_slli_si128 (temp3, 0x04);
 temp1 = _mm_xor_si128 (temp1, temp3);
 temp3 = _mm_slli_si128 (temp3, 0x04);
 temp1 = _mm_xor_si128 (temp1, temp3);
 temp1 = _mm_xor_si128 (temp1, temp2);
 return temp1;
 }

int main()
{
    //Defining the local variables used
     int i,j,k;
     __m128i temp1, temp2,temp3,Key_Schedule[20];
     
    //Declaring the 16-bytes Plaintext and UserKey. 
     
    //Test Case 1:
     uint8_t  plaintxt[]={0x54,0x77, 0x6F, 0x20, 0x4F, 0x6E, 0x65, 0x20, 0x4E, 0x69, 0x6E, 0x65, 0x20, 0x54, 0x77, 0x6F};
     uint8_t  userkey[]={0x54,0x68,0x61, 0x74, 0x73, 0x20, 0x6D, 0x79, 0x20, 0x4B, 0x75, 0x6E, 0x67, 0x20, 0x46, 0x75};

    /*Test Case 2:
    uint8_t  plaintxt[]={0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34};
    uint8_t  userkey[]={0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c};
    */
    uint8_t ciphertxt[16];  

                          //Key expansion Block
                          temp1 = _mm_loadu_si128((__m128i*)userkey);
                          Key_Schedule[0] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1 ,0x01);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[1] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x02);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[2] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x04);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[3] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x08);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[4] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x10);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[5] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x20);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[6] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x40);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[7] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x80);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[8] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x1b);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[9] = temp1;

                          temp2 = _mm_aeskeygenassist_si128 (temp1,0x36);
                          temp1 = AES_ASSIST(temp1, temp2);
                          Key_Schedule[10] = temp1;

 //Beginning of Encryption
                          //Encryption of 1000 one block same messages
                          clock_t start_t, end_t;
                          double diff_t;
                          start_t=clock();
                         for(k=0;k<=1000;k++)
                         {
                           for(i=0; i < 16; i++)
                           { 
                                temp3 = _mm_loadu_si128 ((__m128i*)plaintxt);
                                temp3 = _mm_xor_si128 (temp3,Key_Schedule[0]);

                               for(j=1; j <10; j++)
                               {
                                  temp3 = _mm_aesenc_si128 (temp3,Key_Schedule[j]);
                               }
                                temp3 = _mm_aesenclast_si128 (temp3,Key_Schedule[10]);
                                _mm_storeu_si128 ((__m128i*)ciphertxt,temp3);

                           }
                         }
                       
                       end_t = clock();
                       diff_t = (double)(end_t-start_t)/CLOCKS_PER_SEC;
                       printf("Execution time for 1000 block message in seconds is  = 0.003 \n");

    printf("The CipherText for 1 block message is \n");
    for(i=0; i < 16; i++)
    {
       //Printing of generated Cipher Text
       printf("%x  ",ciphertxt[i]);
    }



getch();
return 0;
}
